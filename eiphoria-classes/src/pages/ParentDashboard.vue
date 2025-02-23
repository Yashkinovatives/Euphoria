# ParentDashboard.vue
<template>
  <div class="dashboard">
    <!-- Animated Background -->
    <div class="animated-bg">
      <div v-for="n in 8" :key="n" class="floating-element"></div>
    </div>

    <!-- Main Content -->
    <div class="dashboard-container">
      <!-- Header Section -->
      <header class="header">
        <div class="header-content">
          <h1>Parent Dashboard</h1>
          <div class="header-date">{{ new Date().toLocaleDateString() }}</div>
        </div>
      </header>

      <div v-if="loading" class="loader">
        <div class="loader-spinner"></div>
        <p>Loading your dashboard...</p>
      </div>

      <div v-else>
        <!-- Enrollment Form -->
        <div v-if="enrollmentRequired" class="enrollment-section">
          <EnrollmentForm 
            :classSections="classSections"
            @enroll="handleEnrollment"
            @enrollmentSuccess="refreshDashboard"
          />
        </div>

        <div v-else class="dashboard-content">
          <!-- Quick Stats -->
          <QuickStats :students="students" :testResults="testResults" />
          
          <!-- Student Overview -->
          <StudentOverview :students="students" />
          
          <!-- Academic Performance -->
          <AcademicPerformance :testResults="testResults" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import EnrollmentForm from '@/components/ParentDashboradComponents/EnrollmentForm.vue';
import QuickStats from '@/components/ParentDashboradComponents/QuickStats.vue';
import StudentOverview from '@/components/ParentDashboradComponents/StudentOverview.vue';
import AcademicPerformance from '@/components/ParentDashboradComponents/AcademicPerformance.vue';

const students = ref([]);
const enrollmentRequired = ref(false);
const loading = ref(true);
const classSections = ref([]);
const testResults = ref([]);

const fetchStudentResults = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/parent/test-results/", {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });
    testResults.value = response.data.results || [];
  } catch (error) {
    console.error("Error fetching test results:", error);
    testResults.value = [];
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

const fetchParentDashboard = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/api/parent-dashboard/", {
      headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` },
    });

    if (response.data.enrollment_required) {
      enrollmentRequired.value = true;
    } else {
      enrollmentRequired.value = false;
      students.value = response.data.students;
    }
  } catch (error) {
    console.error("Error fetching dashboard:", error);
  }
};

const handleEnrollment = async (enrollmentData) => {
  try {
    loading.value = true;
    // Log the enrollment data for confirmation
    console.log('Enrollment successful:', enrollmentData);
    // Refresh dashboard to show newly enrolled student
    await refreshDashboard();
    // You could also show a success message here
    alert('Student enrolled successfully!');
  } catch (error) {
    console.error("Error handling enrollment:", error);
  } finally {
    loading.value = false;
  }
};

const refreshDashboard = async () => {
  try {
    loading.value = true;
    await Promise.all([
      fetchParentDashboard(),
      fetchStudentResults()
    ]);
  } catch (error) {
    console.error("Error refreshing dashboard:", error);
  } finally {
    loading.value = false;
  }
};

onMounted(async () => {
  try {
    await Promise.all([
      fetchParentDashboard(),
      fetchClassSections(),
      fetchStudentResults()
    ]);
  } catch (err) {
    console.error("Error loading dashboard:", err);
  } finally {
    loading.value = false;
  }
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

.dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f3ff, #ede9fe);
  position: relative;
  overflow: hidden;
  font-family: 'Outfit', sans-serif;
}

.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 0;
}

.floating-element {
  position: absolute;
  background: linear-gradient(45deg, rgba(139, 92, 246, 0.1), rgba(192, 132, 252, 0.1));
  border-radius: 50%;
  filter: blur(1px);
  animation: float 25s infinite ease-in-out alternate;
}

.floating-element:nth-child(1) { width: 300px; height: 300px; top: 5%; left: 10%; animation-delay: 0s; }
.floating-element:nth-child(2) { width: 200px; height: 200px; top: 65%; left: 85%; animation-delay: -4s; }
.floating-element:nth-child(3) { width: 350px; height: 350px; top: 35%; left: 55%; animation-delay: -8s; }
.floating-element:nth-child(4) { width: 150px; height: 150px; top: 75%; left: 15%; animation-delay: -12s; }
.floating-element:nth-child(5) { width: 250px; height: 250px; top: 20%; left: 75%; animation-delay: -16s; }
.floating-element:nth-child(6) { width: 180px; height: 180px; top: 80%; left: 45%; animation-delay: -5s; }
.floating-element:nth-child(7) { width: 220px; height: 220px; top: 15%; left: 35%; animation-delay: -9s; }
.floating-element:nth-child(8) { width: 270px; height: 270px; top: 60%; left: 70%; animation-delay: -13s; }

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(3deg); }
  100% { transform: translateY(-40px) rotate(-3deg); }
}

.dashboard-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  position: relative;
  z-index: 1;
}

.header {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 20px rgba(139, 92, 246, 0.1);
  border: 1px solid rgba(139, 92, 246, 0.1);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
}

.header-date {
  font-size: 1.1rem;
  color: #64748b;
}

.loader {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 400px;
}

.loader-spinner {
  width: 50px;
  height: 50px;
  border: 3px solid #e9d5ff;
  border-top-color: #7c3aed;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.dashboard-content {
  display: grid;
  gap: 2rem;
}

.enrollment-section {
  animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .dashboard-container {
    padding: 1rem;
  }

  .header {
    padding: 1rem;
  }

  .header h1 {
    font-size: 1.5rem;
  }
}
</style>