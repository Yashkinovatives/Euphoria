<template>
  <section class="hero">
    <div class="hero-content" v-motion-slide-left>
      <h1 class="hero-title">
        <span class="gradient-text">Online</span> Education
      </h1>
      <p class="hero-description">
        Unlock your potential with personalized online learning. Join thousands of students worldwide achieving their dreams.
      </p>
      <button class="cta-button primary-button" @click="$router.push('/Login')" v-motion-pop>
        Get Started Now
      </button>
    </div>
    <div class="hero-image" v-motion-slide-right>
      <img src="@/assets/images/img.jpg" alt="Online Education Illustration" />
    </div>
  </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* Hero Section */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: #f8fafc;
  min-height: 100vh;
  padding: 4rem 8rem;
  gap: 3rem;
}

/* Adjust Hero Content to Prevent Overlap with Sidebar */
.hero-content {
  flex: 1;
  max-width: 550px;
  margin-left: 100px; /* Shift to avoid overlapping sidebar */
}

.hero-title {
  font-size: 3.8rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

.hero-description {
  font-size: 1.2rem;
  color: #64748b;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.gradient-text {
  background: linear-gradient(45deg, #fbbf24, #f59e0b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Hero Image */
.hero-image {
  flex: 1;
  max-width: 500px;
  display: flex;
  justify-content: center;
}

.hero-image img {
  width: 100%;
  height: auto;
  border-radius: 25px;
  box-shadow: 0 20px 30px rgba(0, 0, 0, 0.1);
}

/* CTA Button */
.cta-button {
  padding: 1rem 2rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  border: none;
}

.primary-button {
  background: linear-gradient(45deg, #fbbf24, #f59e0b);
  color: white;
  box-shadow: 0 4px 15px rgba(251, 191, 36, 0.4);
}

.primary-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(251, 191, 36, 0.6);
}

/* Responsive Design */
@media (max-width: 1024px) {
  .hero {
    flex-direction: column;
    text-align: center;
    padding: 3rem 4rem;
  }

  .hero-content {
    margin-left: 0;
  }

  .hero-title {
    font-size: 3rem;
  }
}

@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    text-align: center;
    padding: 2rem 3rem;
  }

  .hero-title {
    font-size: 2.5rem;
  }
}
</style>
