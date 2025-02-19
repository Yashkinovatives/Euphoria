<template>
    <div class="dashboard-container">
      <h1>Parent Dashboard</h1>

      <div v-if="loading" class="loading">Loading...</div>

      <!-- Show Enrollment Form if Parent has No Students -->
      <div v-if="enrollmentRequired">
        <h2>Enroll Your Child</h2>
        <form @submit.prevent="enrollStudent">
          <div class="form-group">
            <label>Full Name</label>
            <input type="text" v-model="studentData.name" required />
          </div>

          <div class="form-group">
            <label>Class</label>
            <select v-model="studentData.class_section" required>
              <option v-for="cls in classSections" :key="cls.id" :value="cls.id">{{ cls.name }}</option>
            </select>
          </div>

          <button type="submit" class="btn">Enroll</button>
        </form>
      </div>

      <!-- Show Enrolled Students If Parent Already Has Children -->
      <div v-else>
        <h2>Your Child</h2>
        <ul v-if="students.length">
          <li v-for="student in students" :key="student.id">
            <strong>{{ student.name }}</strong> - {{ student.class_section }}
          </li>
        </ul>

        <div v-if="testResults && testResults.length > 0">  <!-- ✅ Fix: Ensure testResults is always defined -->
          <h2>Your Child's Test Results</h2>
          <div v-for="student in testResults" :key="student.student_name">
            <h3>{{ student.student_name }} - {{ student.class_section }}</h3>
            <ul v-if="student.results && student.results.length > 0">  <!-- ✅ Fix: Ensure student.results is always defined -->
              <li v-for="result in student.results" :key="result.subject">
                <strong>{{ result.subject }}</strong>: {{ result.marks_obtained }} / {{ result.total_marks }}
              </li>
            </ul>
            <p v-else>No test results available.</p>
          </div>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const students = ref([]);
const enrollmentRequired = ref(false);
const loading = ref(true);
const classSections = ref([]);
const studentData = ref({ name: "", class_section: "" });
const testResults = ref([]); // ✅ Fix: Ensure testResults is initialized as an empty array

onMounted(async () => {
  await fetchParentDashboard();
  await fetchClassSections();
  await fetchStudentResults();
});

const fetchStudentResults = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/parent/test-results/", {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });

    testResults.value = response.data.results || []; // ✅ Ensure it's an array
  } catch (error) {
    console.error("Error fetching test results:", error);
    testResults.value = []; // ✅ Set as empty array if API fails
  }
};

const fetchParentDashboard = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/parent-dashboard/", {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });

    if (response.data.enrollment_required) {
      enrollmentRequired.value = true;
    } else {
      students.value = response.data.students;
    }
  } catch (error) {
    console.error("Error fetching student results:", error);
  } finally {
    loading.value = false;
  }
};

const fetchClassSections = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/class-sections/");
    classSections.value = response.data;
  } catch (error) {
    console.error("Error fetching class sections:", error);
  }
};

const enrollStudent = async () => {
  try {
    await axios.post(
      "http://127.0.0.1:8000/api/parent/enroll-student/",
      studentData.value,
      { headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } }
    );

    enrollmentRequired.value = false;
    await fetchParentDashboard(); // Refresh dashboard

  } catch (error) {
    alert("Error enrolling student: " + error.response?.data?.error);
  }
};
</script>


  
  <style scoped>
  .dashboard-container {
    padding: 20px;
    max-width: 600px;
    margin: auto;
  }
  
  h1, h2 {
    text-align: center;
  }
  
  .loading {
    text-align: center;
    font-size: 18px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
  }
  
  .form-group label {
    font-weight: bold;
  }
  
  input, select {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  
  .btn {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .btn:hover {
    background-color: #45a049;
  }
  </style>
  