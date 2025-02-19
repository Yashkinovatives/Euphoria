<template>
    <div class="dashboard-container">
      <h1>Teacher Dashboard</h1>
      <button @click="logout" class="logout-btn">Logout</button>
  
      <h2>Students List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Class</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="student in students" :key="student.id">
            <td>{{ student.id }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.class_section__name }}</td>
            <td><button @click="openTestModal(student)">Add Test Result</button></td>
          </tr>
        </tbody>
      </table>
  
      <!-- Test Result Modal -->
      <div v-if="showModal" class="modal">
        <div class="modal-content">
          <h2>Add Test Result</h2>
          <label>Subject</label>
          <input type="text" v-model="test.subject" />
          
          <label>Marks Obtained</label>
          <input type="number" v-model="test.marks_obtained" />
  
          <label>Total Marks</label>
          <input type="number" v-model="test.total_marks" />
  
          <button @click="submitTestResult">Submit</button>
          <button @click="showModal = false">Close</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const students = ref([]);
  const showModal = ref(false);
  const selectedStudent = ref(null);
  const test = ref({ subject: '', marks_obtained: '', total_marks: '' });
  
  onMounted(async () => {
    try {
        const token = localStorage.getItem('access_token');
        const response = await axios.get('http://127.0.0.1:8000/api/teacher-dashboard/', {
            headers: { Authorization: `Bearer ${token}` }
        });
        
        console.log("Students Data:", response.data.students);  // Debugging
        students.value = response.data.students;
    } catch (error) {
        console.error("Error fetching students:", error.response?.data || error);
    }
});
  
  const openTestModal = (student) => {
    selectedStudent.value = student;
    showModal.value = true;
  };
  
  const submitTestResult = async () => {
    const token = localStorage.getItem('access_token');
    await axios.post('http://127.0.0.1:8000/api/test-results/add/', {
      student_id: selectedStudent.value.id,
      subject: test.value.subject,
      marks_obtained: test.value.marks_obtained,
      total_marks: test.value.total_marks
    }, {
      headers: { Authorization: `Bearer ${token}` }
    });
    
    showModal.value = false;
    alert('Test Result Added Successfully');
  };
  
  const logout = () => {
    localStorage.clear();
    router.push('/');
  };
  </script>
  
  <style scoped>
  .dashboard-container {
    padding: 20px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
  }
  .logout-btn {
    float: right;
    background: red;
    color: white;
    padding: 8px 12px;
    border: none;
    cursor: pointer;
  }
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
  }
  </style>
  