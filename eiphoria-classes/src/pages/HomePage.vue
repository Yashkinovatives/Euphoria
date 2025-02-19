<template>
  <div class="page-container">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content" v-motion-slide-left>
        <h1 class="hero-title">
          <span class="gradient-text">Online</span> Education
        </h1>
        <p class="hero-description">
          Unlock your potential with personalized online learning. Join thousands of students worldwide achieving their dreams.
        </p>
        <button class="cta-button primary-button" @click="$router.push('/Login')"
                v-motion-pop>
          Get Started Now
        </button>
      </div>
      <div class="hero-image" v-motion-slide-right>
        <img src="@/assets/images/img.jpg" alt="Online Education Illustration" />
      </div>
    </section>

    <!-- Popular Courses Section -->
    <section class="popular-courses" v-motion-fade>
      <h2 class="section-title">Popular Courses</h2>
      <div class="courses-grid">
        <div v-for="course in courses" 
             :key="course.id" 
             class="course-card"
             v-motion-slide-up
             :custom-delay="course.id * 100">
          <div class="course-icon">{{ course.icon }}</div>
          <h3 class="course-title">{{ course.title }}</h3>
          <p class="course-description">{{ course.description }}</p>
          <button class="course-button">Learn More</button>
        </div>
      </div>
    </section>

    <!-- Steps to Career Section -->
    <section class="steps-to-career" v-motion-fade>
      <h2 class="section-title">Three Steps to Your Career</h2>
      <div class="steps-list">
        <div class="step" 
             v-for="(step, index) in steps" 
             :key="index"
             v-motion-slide-visible
             :custom-delay="index * 200">
          <div class="step-content">
            <h3 class="step-number">0{{ index + 1 }}</h3>
            <p class="step-description">{{ step }}</p>
          </div>
          <div class="step-line" v-if="index < steps.length - 1"></div>
        </div>
      </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials" v-motion-fade>
      <h2 class="section-title">What People Think About Our Educational Platform</h2>
      <div class="testimonials-grid">
        <div v-for="testimonial in testimonials" 
             :key="testimonial.id" 
             class="testimonial-card"
             v-motion-pop
             :custom-delay="testimonial.id * 200">
          <div class="testimonial-content">
            <div class="quote-icon">❝</div>
            <p class="testimonial-text">{{ testimonial.text }}</p>
            <div class="testimonial-author">
              <div class="author-avatar"></div>
              <div class="author-info">
                <h3 class="author-name">{{ testimonial.author }}</h3>
                <p class="author-role">{{ testimonial.role }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref} from 'vue';

// Custom directive for scroll animations
const createScrollAnimation = (el, binding) => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            el.classList.add('animate');
          }, binding.value?.delay || 0);
          observer.unobserve(el);
        }
      });
    },
    {
      threshold: 0.1
    }
  );
  observer.observe(el);
};

export default {
  name: "LandingPage",
  setup() {
    const courses = ref([
      { 
        id: 1, 
        icon: "📐", 
        title: "Mathematics",
        description: "Master mathematical concepts from basic to advanced levels."
      },
      { 
        id: 2, 
        icon: "📘", 
        title: "English",
        description: "Improve your language skills with native speakers."
      },
      { 
        id: 3, 
        icon: "🌐", 
        title: "Web Development",
        description: "Build modern websites and web applications."
      },
      { 
        id: 4, 
        icon: "⚗️", 
        title: "Chemistry",
        description: "Explore the fascinating world of chemical sciences."
      },
    ]);

    const steps = ref([
      "Join our educational program and get access to premium content",
      "Study theory and complete practical assignments with guidance from expert teachers",
      "Get a recognized certificate and valuable knowledge for your career",
    ]);

    const testimonials = ref([
      { 
        id: 1, 
        text: "The course content was comprehensive and the instructors were incredibly knowledgeable. I've learned more than I expected!", 
        author: "Den White",
        role: "Software Developer"
      },
      { 
        id: 2, 
        text: "This platform offers an amazing opportunity to learn new skills at your own pace. The community support is outstanding!", 
        author: "Tom Brighton",
        role: "Student"
      },
      { 
        id: 3, 
        text: "I've tried many online learning platforms, but this one stands out for its quality content and excellent teaching methods.", 
        author: "Angela Light",
        role: "Business Analyst"
      },
    ]);

    return {
      courses,
      steps,
      testimonials,
    };
  },
  directives: {
    'motion-slide-left': {
      mounted(el, binding) {
        el.classList.add('slide-left');
        createScrollAnimation(el, binding);
      }
    },
    'motion-slide-right': {
      mounted(el, binding) {
        el.classList.add('slide-right');
        createScrollAnimation(el, binding);
      }
    },
    'motion-slide-up': {
      mounted(el, binding) {
        el.classList.add('slide-up');
        createScrollAnimation(el, binding);
      }
    },
    'motion-fade': {
      mounted(el, binding) {
        el.classList.add('fade');
        createScrollAnimation(el, binding);
      }
    },
    'motion-pop': {
      mounted(el, binding) {
        el.classList.add('pop');
        createScrollAnimation(el, binding);
      }
    },
    'motion-slide-visible': {
      mounted(el, binding) {
        el.classList.add('slide-visible');
        createScrollAnimation(el, binding);
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

.page-container {
  font-family: 'Poppins', sans-serif;
  background-color: #f8fafc;
}

/* Hero Section */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 4rem 6rem;
  background: linear-gradient(135deg, #f8fafc, #f1f5f9);
  min-height: 80vh;
  gap: 4rem;
}

.hero-content {
  flex: 1;
  max-width: 600px;
}

.hero-title {
  font-size: 4rem;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

.hero-description {
  font-size: 1.25rem;
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

.hero-image {
  flex: 1;
  max-width: 600px;
}

.hero-image img {
  width: 100%;
  height: auto;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
}

/* Buttons */
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

.secondary-button {
  background: #475569;
  color: white;
  box-shadow: 0 4px 15px rgba(71, 85, 105, 0.4);
}

.secondary-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(71, 85, 105, 0.6);
}

/* Sections */
section {
  padding: 6rem 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  text-align: center;
  margin-bottom: 3rem;
  color: #1e293b;
}

/* Popular Courses */
.courses-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.course-card {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  text-align: center;
}

.course-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.course-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.course-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.course-description {
  color: #64748b;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.course-button {
  background: transparent;
  color: #f59e0b;
  border: 2px solid #f59e0b;
  padding: 0.5rem 1.5rem;
  border-radius: 9999px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.course-button:hover {
  background: #f59e0b;
  color: white;
}

/* Steps to Career */
.steps-list {
  max-width: 800px;
  margin: 0 auto;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-bottom: 2rem;
}

.step-content {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  width: 100%;
}

.step-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #f59e0b;
  margin-bottom: 1rem;
}

.step-description {
  color: #64748b;
  line-height: 1.6;
}

.step-line {
  height: 50px;
  width: 2px;
  background: #f59e0b;
  margin: 1rem 0;
}

/* Free Trial Section */
.free-trial {
  background: linear-gradient(135deg, #1e293b, #0f172a);
  color: white;
  text-align: center;
}

.free-trial .section-title {
  color: white;
}

.trial-description {
  font-size: 1.25rem;
  color: #cbd5e1;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.trial-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* Testimonials */
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.testimonial-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.quote-icon {
  font-size: 3rem;
  color: #f59e0b;
  line-height: 1;
  margin-bottom: 1rem;
}

.testimonial-text {
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(45deg, #fbbf24, #f59e0b);
}

.author-name {
  font-weight: 600;
  color: #1e293b;
}

.author-role {
  color: #64748b;
  font-size: 0.9rem;
}
/* Animation Classes */
.slide-left {
  opacity: 0;
  transform: translateX(-50px);
  transition: all 0.8s ease-out;
}

.slide-right {
  opacity: 0;
  transform: translateX(50px);
  transition: all 0.8s ease-out;
}

.slide-up {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.6s ease-out;
}

.fade {
  opacity: 0;
  transition: opacity 1s ease-out;
}

.pop {
  opacity: 0;
  transform: scale(0.9);
  transition: all 0.6s cubic-bezier(0.17, 0.67, 0.83, 0.67);
}

.slide-visible {
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.6s ease-out;
}

/* Animation States */
.animate {
  opacity: 1;
  transform: translate(0) scale(1);
}

/* Smooth Scrolling */
html {
  scroll-behavior: smooth;
}

/* Enhanced Hover Effects */
.course-card {
  transition: all 0.4s cubic-bezier(0.17, 0.67, 0.83, 0.67);
}

.course-card:hover {
  transform: translateY(-10px) scale(1.02);
}

.testimonial-card {
  transition: all 0.4s cubic-bezier(0.17, 0.67, 0.83, 0.67);
}

.testimonial-card:hover {
  transform: translateY(-10px) scale(1.02);
}

/* Enhanced Gradient Effects */
.gradient-text {
  background: linear-gradient(45deg, #fbbf24, #f59e0b, #d97706);
  background-size: 200% 200%;
  animation: gradient 5s ease infinite;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

@keyframes gradient {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
/* Responsive Design */
@media (max-width: 1024px) {
  .hero {
    flex-direction: column;
    padding: 3rem 2rem;
    text-align: center;
  }

  .hero-title {
    font-size: 3rem;
  }

  .trial-buttons {
    flex-direction: column;
    align-items: center;
  }

  section {
    padding: 4rem 2rem;
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .courses-grid,
  .testimonials-grid {
    grid-template-columns: 1fr;
  }
}
</style>