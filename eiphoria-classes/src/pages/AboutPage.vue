<template>
  <div class="about-hero-container">
    <section class="about-hero">
      <!-- Animated Hero Header -->
      <div
        class="hero-header"
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0 }"
      >
        <h1 class="hero-title">
          Why <span class="gradient-text">Choose</span> Us
          <span
            class="arrow-icon"
            v-motion
            :initial="{ x: 0 }"
            :enter="{ 
              x: 10,
              transition: {
                repeat: Infinity,
                duration: 1,
                repeatType: 'reverse'
              }
            }"
          >
            →
          </span>
        </h1>
      </div>

      <!-- Animated Stats Grid -->
      <div class="stats-grid">
        <div
          v-for="(stat, index) in stats"
          :key="stat.id"
          class="stat-card"
          :class="{ 'featured': stat.featured }"
          v-motion
          :initial="{ opacity: 0, y: 50 }"
          :enter="{ 
            opacity: 1, 
            y: 0,
            transition: {
              delay: index * 0.1
            }
          }"
        >
          <div class="stat-content">
            <h2 class="stat-value">{{ stat.value }}</h2>
            <p class="stat-label">{{ stat.label }}</p>
          </div>
          <div class="card-background"></div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";

const stats = ref([
  {
    id: 1,
    value: "3+",
    label: "Years of Industry Experience",
    featured: false,
  },
  {
    id: 2,
    value: "42+",
    label: "Happy Clients",
    featured: false,
  },
  {
    id: 3,
    value: "113+",
    label: "Projects Done",
    featured: false,
  },
  {
    id: 4,
    value: "12",
    label: "Recent Clients",
    featured: true,
  },
]);
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap");

.about-hero-container {
  min-height: 100vh;
  background-color: #f8fafc;
  padding: 4rem 2rem;
}

.about-hero {
  max-width: 1200px;
  margin: 0 auto;
}

.hero-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 3rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: 800;
  color: #0f172a;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-align: center;
}

.gradient-text {
  background: linear-gradient(45deg, #fbbf24, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.arrow-icon {
  font-size: 2rem;
  color: #fbbf24;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.stat-card {
  position: relative;
  background-color: white;
  padding: 1.5rem;
  border-radius: 1rem;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-in-out;
}

.stat-card.featured {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  color: white;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.stat-content {
  z-index: 1;
  position: relative;
}

.stat-value {
  font-size: 2rem;
  font-weight: 800;
  color: #0f172a;
}

.stat-card.featured .stat-value {
  color: white;
}

.stat-label {
  font-size: 1rem;
  color: #475569;
}

.stat-card.featured .stat-label {
  color: #ffeedd;
}

.card-background {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at top right, rgba(251, 191, 36, 0.1), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 0;
}

.stat-card:hover .card-background {
  opacity: 1;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style>
