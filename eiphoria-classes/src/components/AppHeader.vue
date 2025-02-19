<template>
  <div class="header-container">
    <header class="site-header">
      <div class="header-content">
        <!-- Logo Section -->
        <div class="logo-section">
          <router-link to="/" class="logo-link">
            <h1 class="logo">
              <span class="gradient-text-primary">Online</span>
              <span class="gradient-text-secondary">Education</span>
            </h1>
          </router-link>
        </div>

        <!-- Mobile Menu Button -->
        <button 
          class="mobile-menu-btn"
          @click="toggleMobileMenu"
          :aria-expanded="isMobileMenuOpen"
          aria-label="Toggle menu"
        >
          <span class="sr-only">Menu</span>
          <svg 
            v-if="!isMobileMenuOpen" 
            class="menu-icon" 
            xmlns="http://www.w3.org/2000/svg" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg 
            v-else 
            class="menu-icon" 
            xmlns="http://www.w3.org/2000/svg" 
            fill="none" 
            viewBox="0 0 24 24" 
            stroke="currentColor"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <!-- Navigation and CTA -->
        <div 
          class="nav-cta-wrapper"
          :class="{ 'nav-open': isMobileMenuOpen }"
        >
          <nav class="navigation">
            <ul class="nav-list">
              <li v-for="item in menuItems" :key="item.path" class="nav-item">
                <router-link 
                  :to="item.path" 
                  class="nav-link"
                  @click="isMobileMenuOpen = false"
                >
                  {{ item.name }}
                </router-link>
              </li>
            </ul>
          </nav>
          <div class="cta-section">
            <router-link to="/Login" class="cta-button">
              Login
            </router-link>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      isMobileMenuOpen: false,
      menuItems: [
        { name: 'About us', path: '/about' },
        { name: 'Reviews', path: '/reviews' },
        { name: 'Contact us', path: '/contact' }
      ]
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    }
  },
  watch: {
    '$route'() {
      this.isMobileMenuOpen = false;
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');

.header-container {
  background: linear-gradient(to right, #0f172a, #1e293b);
  border-bottom: 1px solid rgba(251, 191, 36, 0.2);
  position: sticky;
  top: 0;
  z-index: 50;
  backdrop-filter: blur(8px);
}

.site-header {
  max-width: 1280px;
  margin: 0 auto;
  padding: 1rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.logo-section {
  flex-shrink: 0;
}

.logo-link {
  text-decoration: none;
}

.logo {
  font-family: 'Inter', sans-serif;
  font-size: 2.5rem;
  font-weight: 900;
  margin: 0;
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.gradient-text-primary {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.gradient-text-secondary {
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.mobile-menu-btn {
  display: none;
  padding: 0.5rem;
  color: #fbbf24;
  background: transparent;
  border: none;
  cursor: pointer;
}

.menu-icon {
  width: 1.75rem;
  height: 1.75rem;
}

.nav-cta-wrapper {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.nav-list {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: rgba(251, 191, 36, 0.9);
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  transition: all 0.3s ease;
  padding: 0.5rem 0;
  position: relative;
}

.nav-link:after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 0;
  background-color: #fbbf24;
  transition: width 0.3s ease;
}

.nav-link:hover:after {
  width: 100%;
}

.cta-button {
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  color: #000000;
  padding: 0.85rem 1.8rem;
  border-radius: 10px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
  border: 2px solid transparent;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(251, 191, 36, 0.2);
  border-color: rgba(251, 191, 36, 0.5);
}

@media (max-width: 768px) {
  .mobile-menu-btn {
    display: block;
  }

  .nav-cta-wrapper {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: linear-gradient(to right, #0f172a, #1e293b);
    padding: 1rem;
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-1rem);
    transition: all 0.3s ease;
  }

  .nav-cta-wrapper.nav-open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .nav-list {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-link {
    display: block;
    padding: 0.5rem;
  }

  .cta-button {
    text-align: center;
  }
}
</style>
