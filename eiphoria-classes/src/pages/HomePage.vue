<template>
  <section class="hero">
    <!-- Animated Background -->
    <div class="animated-bg">
      <div v-for="n in 5" :key="n" class="floating-circle"></div>
    </div>

    <!-- Main Content -->
    <div class="content-wrapper">
      <div class="hero-content" v-motion :initial="{ opacity: 0, y: 100 }" :enter="{ opacity: 1, y: 0 }">
        <div class="badge" v-motion :initial="{ scale: 0 }" :enter="{ scale: 1 }">
          <span>🚀 Elevate Your Learning</span>
        </div>

        <h1 class="title">
          Step into the Future with  
          <span class="gradient-text">Limitless Possibilities</span>
        </h1>

        <p class="description">
          Unlock the full potential of your skills with interactive courses, AI-driven insights, and personalized guidance.
        </p>

        <div class="cta-group">
          <button class="primary-btn" @click="$router.push('/Login')">
            <span class="btn-icon">✨</span>
            Get Started
          </button>
        </div>
      </div>

      <!-- Feature Cards -->
      <div class="features-grid">
        <div v-for="(feature, index) in features" 
             :key="feature.title"
             class="feature-card"
             v-motion
             :initial="{ opacity: 0, x: 100 }"
             :enter="{ opacity: 1, x: 0 }"
             :delay="index * 200">
          <div class="feature-icon" :style="{ background: feature.bgColor }">
            {{ feature.icon }}
          </div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const features = [
  {
    icon: '🎯',
    title: 'AI-Powered Learning',
    description: 'Smart technology to personalize your education journey.',
    bgColor: 'linear-gradient(135deg, #ff9a8b, #ff6a88, #ff99ac)'
  },
  {
    icon: '⚡',
    title: 'Ultra Fast Performance',
    description: 'Seamless access to courses, tools, and insights anytime.',
    bgColor: 'linear-gradient(135deg, #38ef7d, #11998e)'
  },
  {
    icon: '🌎',
    title: 'Global Community',
    description: 'Connect with learners and experts around the world.',
    bgColor: 'linear-gradient(135deg, #56ccf2, #2f80ed)'
  }
]
</script>

<style scoped>
.hero {
  min-height: 100vh;
  background: linear-gradient(135deg, #ffdde1, #ee9ca7);
  position: relative;
  overflow: hidden;
  padding: 3rem;
  color: #2c3e50;
}

/* Animated Background */
.animated-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.floating-circle {
  position: absolute;
  background: linear-gradient(45deg, rgba(255, 87, 87, 0.1), rgba(255, 195, 113, 0.1));
  border-radius: 50%;
  animation: float 20s infinite linear;
}

.floating-circle:nth-child(1) { width: 250px; height: 250px; top: 10%; left: 15%; animation-delay: 0s; }
.floating-circle:nth-child(2) { width: 180px; height: 180px; top: 60%; left: 80%; animation-delay: -4s; }
.floating-circle:nth-child(3) { width: 320px; height: 320px; top: 40%; left: 50%; animation-delay: -8s; }
.floating-circle:nth-child(4) { width: 120px; height: 120px; top: 80%; left: 20%; animation-delay: -12s; }
.floating-circle:nth-child(5) { width: 220px; height: 220px; top: 25%; left: 70%; animation-delay: -16s; }

@keyframes float {
  0% { transform: translateY(0px); }
  100% { transform: translateY(-20px); }
}

/* Main Content */
.content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}

.hero-content {
  max-width: 650px;
  margin-bottom: 2rem;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 20px;
  backdrop-filter: blur(10px);
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1rem;
}

.gradient-text {
  background: linear-gradient(45deg, #ff758c, #ff7eb3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.description {
  font-size: 1.2rem;
  color: #374151;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.cta-group {
  margin-bottom: 2rem;
}

.primary-btn {
  padding: 1rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: transform 0.3s ease;
  background: linear-gradient(45deg, #ff758c, #ff7eb3);
  color: white;
  box-shadow: 0 4px 15px rgba(255, 120, 180, 0.4);
}

.primary-btn:hover {
  transform: translateY(-2px);
}

/* Feature Cards */
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 1.5rem;
  transition: transform 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  margin-bottom: 0.8rem;
}

.feature-card h3 {
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.feature-card p {
  font-size: 1rem;
  color: #374151;
  line-height: 1.5;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero {
    padding: 2rem;
  }

  .title {
    font-size: 2.8rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
