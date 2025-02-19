<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="brand">
        <h1>Welcome Back</h1>
        <p>Sign in to continue</p>
      </div>

      <div class="auth-tabs">
        <button :class="{ active: isLogin }" @click="currentTab = 'login'">
          Sign In
        </button>
        <button :class="{ active: !isLogin }" @click="currentTab = 'signup'">
          Sign Up
        </button>
      </div>

      <form @submit.prevent="handleSubmit" class="auth-form">
        <!-- Name Field (Only for Signup) -->
        <div class="form-group" v-if="!isLogin">
          <label>Full Name</label>
          <input type="text" v-model="form.name" placeholder="Enter your full name" required />
        </div>

        <!-- Email Field -->
        <div class="form-group">
          <label>Email Address</label>
          <input type="email" v-model="form.email" placeholder="Enter your email" required />
        </div>

        <!-- Password Field -->
        <div class="form-group">
          <label>Password</label>
          <div class="password-input">
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="form.password"
              placeholder="Enter your password"
              required
            />
            <button type="button" class="toggle-password" @click="showPassword = !showPassword">
              <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
            </button>
          </div>
        </div>

        <!-- Role Selection (Available for Both Signup & Login) -->
        <div class="form-group">
          <label>Select Role</label>
          <div class="role-buttons">
            <button
              type="button"
              v-for="role in roles"
              :key="role.value"
              :class="{ selected: form.user_type === role.value }"
              class="role-btn"
              @click="form.user_type = role.value"
            >
              {{ role.label }}
            </button>
          </div>
        </div>

        <button type="submit" class="submit-btn" :disabled="loading">
          <span v-if="!loading">{{ isLogin ? 'Sign In' : 'Create Account' }}</span>
          <span v-else class="loader"></span>
        </button>

        <p class="auth-switch">
          {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
          <a href="#" @click.prevent="currentTab = isLogin ? 'signup' : 'login'">
            {{ isLogin ? 'Sign up' : 'Sign in' }}
          </a>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, reactive } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const router = useRouter();
const loading = ref(false);
const showPassword = ref(false);
const currentTab = ref("login");

const isLogin = computed(() => currentTab.value === "login");

const form = reactive({
  name: "",
  email: "",
  password: "",
  user_type: "teacher", // Default role
});

const roles = [
  { label: "Teacher", value: "teacher" },
  { label: "Parent", value: "parent" },
];

const handleSubmit = async () => {
  loading.value = true;
  try {
    const endpoint = isLogin.value
      ? "http://127.0.0.1:8000/api/login/"
      : "http://127.0.0.1:8000/api/signup/";

    const response = await axios.post(endpoint, form);

    if (isLogin.value) {
      // Save tokens & role in localStorage
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
      localStorage.setItem("user_type", response.data.user_type);

      // Redirect based on user type
      if (response.data.user_type === "teacher") {
        router.push("/teacher-dashboard");
      } else {
        router.push("/parent-dashboard");
      }
    } else {
      // Switch to login mode after successful signup
      currentTab.value = "login";
    }
  } catch (error) {
    alert(error.response?.data?.error || "Something went wrong.");
  } finally {
    loading.value = false;
  }
};
</script>

  
<style scoped>
  .auth-container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 20px;
    background: #f5f7ff;
  }
  
  .auth-card {
    background: white;
    width: 100%;
    max-width: 400px;
    padding: 32px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .brand {
    text-align: center;
    margin-bottom: 24px;
  }
  
  .brand h1 {
    font-size: 24px;
    font-weight: 600;
    color: #333;
    margin-bottom: 8px;
  }
  
  .brand p {
    color: #666;
    font-size: 14px;
  }
  
  .auth-tabs {
    display: flex;
    margin-bottom: 24px;
    border-radius: 8px;
    background: #f5f5f5;
    padding: 4px;
  }
  
  .auth-tabs button {
    flex: 1;
    padding: 8px;
    border: none;
    background: none;
    color: #666;
    font-size: 14px;
    cursor: pointer;
    border-radius: 6px;
    transition: all 0.2s;
  }
  
  .auth-tabs button.active {
    background: #6366f1;
    color: white;
  }
  
  .auth-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }
  
  .form-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  
  .form-group label {
    font-size: 14px;
    color: #444;
    font-weight: 500;
  }
  
  .form-group input {
    padding: 10px 12px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 14px;
    transition: border-color 0.2s;
  }
  
  .form-group input:focus {
    outline: none;
    border-color: #6366f1;
  }
  
  .form-group input.error {
    border-color: #ef4444;
  }
  
  .password-input {
    position: relative;
  }
  
  .password-input input {
    width: 100%;
    padding-right: 40px;
  }
  
  .toggle-password {
    position: absolute;
    right: 12px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: #666;
    cursor: pointer;
    padding: 0;
  }
  
  .role-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }
  
  .role-btn {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background: white;
    color: #444;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s;
  }
  
  .role-btn.selected {
    border-color: #6366f1;
    background: #eef2ff;
    color: #6366f1;
  }
  
  .submit-btn {
    width: 100%;
    padding: 12px;
    background: #6366f1;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .submit-btn:hover {
    background: #4f46e5;
  }
  
  .submit-btn:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
  
  .error-text {
    color: #ef4444;
    font-size: 12px;
  }
  
  .auth-switch {
    text-align: center;
    font-size: 14px;
    color: #666;
  }
  
  .auth-switch a {
    color: #6366f1;
    text-decoration: none;
    font-weight: 500;
  }
  
  .loader {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 2px solid #fff;
    border-radius: 50%;
    border-top-color: transparent;
    animation: spin 0.6s linear infinite;
  }
  
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  
  @media (max-width: 480px) {
    .auth-card {
      padding: 24px;
    }
    
    .role-buttons {
      grid-template-columns: 1fr;
    }
  }
  </style>