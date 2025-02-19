from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Student, TestResult, ClassSection , FeePayment , FeeRecord,Attendance
from rest_framework import status
from datetime import datetime



User = get_user_model()

# Generate JWT Tokens
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "user_type": user.user_type
    }

# Signup API (Only for Teachers & Parents)
@api_view(['POST'])
def signup(request):
    data = request.data

    if User.objects.filter(email=data['email']).exists():
        return Response({"error": "User already exists"}, status=400)

    user = User.objects.create_user(
        username=data['email'], 
        email=data['email'], 
        password=data['password'],
        first_name=data['name'],  
        user_type=data['user_type']
    )
    user.save()

    return Response({"message": f"{data['user_type']} registered successfully"}, status=201)

# Login API
@api_view(['POST'])
def login(request):
    data = request.data
    user = authenticate(username=data['email'], password=data['password'])

    if user:
        if user.user_type != data.get("user_type"):
            return Response({"error": f"You must log in as a {user.user_type}, not {data.get('user_type')}"}, status=400)

        tokens = get_tokens_for_user(user)
        return Response(tokens)
    else:
        return Response({"error": "Invalid credentials"}, status=400)

# Teacher Dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacher_dashboard(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.select_related("class_section", "parent").values(
        "id", "name", "class_section__id", "class_section__name", "parent__email"
    )

    return Response({"students": list(students)})

# Parent Dashboard
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def parent_dashboard(request):
    """Parent Dashboard: Check if child exists, otherwise force enrollment."""
    if request.user.user_type != "parent":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.filter(parent=request.user).values("id", "name", "class_section__name")

    if not students:
        return Response({"enrollment_required": True}, status=200)  # 👈 Tell frontend to show student enrollment form

    return Response({"students": list(students)}, status=200)  # 👈 Show enrolled students

# Parent Enrolls a Student
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_student(request):
    if request.user.user_type != "parent":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    
    try:
        class_section = ClassSection.objects.get(id=data["class_section"])
    except ClassSection.DoesNotExist:
        return Response({"error": "Invalid class_section ID"}, status=400)

    student = Student.objects.create(
        name=data["name"],
        class_section=class_section,
        parent=request.user
    )
    student.save()
    
    return Response({"message": "Student enrolled successfully"}, status=201)

# Teacher Adds a Test Result
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_test_result(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    student = Student.objects.filter(id=data["student_id"]).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    test_result = TestResult.objects.create(
        student=student,
        subject=data["subject"],
        marks_obtained=data["marks_obtained"],
        total_marks=data["total_marks"],
        teacher=request.user
    )
    test_result.save()
    return Response({"message": "Test result added successfully"}, status=201)

# Parent Views Their Child’s Test Results (Now Takes `student_id` as a Parameter)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_results(request):
    """Parent views their child's test results"""
    if request.user.user_type != "parent":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.filter(parent=request.user)
    if not students.exists():
        return Response({"results": []})  # ✅ Always return an array, never None

    results = []
    for student in students:
        student_results = TestResult.objects.filter(student=student).values(
            "subject", "marks_obtained", "total_marks", "teacher__first_name"
        )
        results.append({
            "student_name": student.name,
            "class_section": student.class_section.name,  # ✅ Added class section
            "results": list(student_results)
        })

    return Response({"results": results})  # ✅ Always return an array


# Get All Students (Only for Teachers)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.all().values("id", "name", "class_section__name", "parent__email")
    
    if not students:
        return Response({"message": "No students found"}, status=200)

    return Response({"students": list(students)})


@api_view(['GET'])
def get_class_sections(request):
    """Returns available class sections."""
    sections = ClassSection.objects.all().values("id", "name")
    return Response(list(sections))

# Teachers Set Total Fees for a Student
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_total_fees(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    student = Student.objects.filter(id=data["student_id"]).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    fee_record, created = FeeRecord.objects.get_or_create(student=student)
    fee_record.total_fees = data["total_fees"]
    fee_record.remaining_fees = data["total_fees"]
    fee_record.save()

    return Response({"message": "Total fees set successfully"}, status=201)

# Teachers Add Monthly Fee Payments
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_monthly_fee(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    student = Student.objects.filter(id=data["student_id"]).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    fee_record, created = FeeRecord.objects.get_or_create(student=student)

    existing_payment = FeePayment.objects.filter(student=student, month=data["month"]).first()
    if existing_payment:
        return Response({"error": "Fee for this month is already recorded"}, status=400)

    FeePayment.objects.create(
        student=student,
        month=data["month"],
        amount_paid=data["amount_paid"]
    )

    fee_record.remaining_fees -= data["amount_paid"]
    fee_record.save()

    return Response({"message": "Monthly fee recorded successfully"}, status=201)

# Parents View Fee Status
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_monthly_fee_status(request):
    if request.user.user_type != "parent":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.filter(parent=request.user)
    fee_status = []

    for student in students:
        fee_record = FeeRecord.objects.filter(student=student).first()
        payments = FeePayment.objects.filter(student=student).values("month", "amount_paid", "payment_date")

        fee_status.append({
            "student_name": student.name,
            "class_section": student.class_section.name,
            "total_fees": fee_record.total_fees if fee_record else 0,
            "remaining_fees": fee_record.remaining_fees if fee_record else 0,
            "monthly_payments": list(payments)
        })

    return Response({"fee_status": fee_status})


# ✅ Teacher Marks Attendance
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    student = Student.objects.filter(id=data["student_id"]).first()
    if not student:
        return Response({"error": "Student not found"}, status=404)

    # Ensure no duplicate attendance for the same day
    attendance, created = Attendance.objects.get_or_create(
        student=student,
        date=datetime.strptime(data["date"], "%Y-%m-%d"),
        defaults={"status": data["status"]}
    )

    if not created:
        return Response({"error": "Attendance already marked for this date"}, status=400)

    return Response({"message": "Attendance recorded successfully"}, status=201)

# ✅ Teacher Updates Attendance
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_attendance(request):
    if request.user.user_type != "teacher":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    attendance = Attendance.objects.filter(student_id=data["student_id"], date=data["date"]).first()
    
    if not attendance:
        return Response({"error": "Attendance record not found"}, status=404)

    attendance.status = data["status"]
    attendance.save()

    return Response({"message": "Attendance updated successfully"}, status=200)

# ✅ Parent Views Attendance
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_attendance(request):
    if request.user.user_type != "parent":
        return Response({"error": "Unauthorized"}, status=403)

    students = Student.objects.filter(parent=request.user)
    attendance_data = []

    for student in students:
        attendance_records = Attendance.objects.filter(student=student).values("date", "status")
        attendance_data.append({
            "student_name": student.name,
            "class_section": student.class_section.name,
            "attendance": list(attendance_records)
        })

    return Response({"attendance_records": attendance_data})