<template>
  <div class="side-nav-container" :class="{ 'hide-nav': hideSidebar }">
    <div class="glow-effect"></div>
    <nav class="side-nav">
      <ul class="nav-list">
        <li v-for="item in menuItems" 
            :key="item.path" 
            class="nav-item"
            @click="activeItem = item.path">
          <router-link 
            :to="item.path" 
            class="nav-link"
            :class="{ 'active': activeItem === item.path }">
            <span class="icon-wrapper">
              <component :is="item.icon" 
                        class="icon"
                        :class="{ 'icon-active': activeItem === item.path }" />
            </span>
            <span class="tooltip">{{ item.name }}</span>
          </router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
// Script remains the same as your original code
export default {
  name: "SideNav",
  // components: {
  //   HomeIcon,
  //   GraduationCapIcon,
  //   BookOpenIcon,
  //   MessageCircleIcon,
  //   LogInIcon
  // },
  data() {
    return {
      activeItem: '/',
      menuItems: [
        { name: "Home", path: "/" },
        { name: "Courses", path: "/about" },
        { name: "Resources", path: "/reviews"},
        { name: "Community", path: "/contact"},
        { name: "Login", path: "/login" },
      ],
      hideSidebar: false,
      lastScrollY: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    handleScroll() {
      const currentScrollY = window.scrollY;
      if (currentScrollY > this.lastScrollY) {
        this.hideSidebar = true;
      } else {
        this.hideSidebar = false;
      }
      this.lastScrollY = currentScrollY;
    },
  },
};
</script>

<style scoped>
.side-nav-container {
  position: fixed;
  left: 40px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 50;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.glow-effect {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
  filter: blur(30px);
  opacity: 0.15;
  border-radius: 40px;
  z-index: -1;
}

.hide-nav {
  transform: translateY(-50%) translateX(-100px);
  opacity: 0;
}

.side-nav {
  width: 80px;
  height: 420px;
  background: linear-gradient(145deg, 
    rgba(29, 38, 113, 0.95),
    rgba(19, 15, 64, 0.98));
  backdrop-filter: blur(10px);
  border-radius: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 
    0 20px 40px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(255, 255, 255, 0.1),
    inset 0 0 30px rgba(255, 255, 255, 0.03);
  position: relative;
  overflow: hidden;
}

.nav-list {
  list-style: none;
  padding: 1.5rem 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  width: 100%;
  position: relative;
  z-index: 1;
}

.nav-item {
  width: 100%;
  display: flex;
  justify-content: center;
}

.nav-link {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.nav-link:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateX(4px) scale(1.05);
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.1),
    inset 0 0 0 1px rgba(255, 255, 255, 0.1);
}

.nav-link.active {
  background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
  border-color: transparent;
  box-shadow: 
    0 4px 15px rgba(78, 205, 196, 0.3),
    0 0 0 1px rgba(255, 255, 255, 0.1) inset;
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
}

.icon {
  color: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
}

.icon-active {
  color: #ffffff;
  filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.3));
}

.tooltip {
  position: absolute;
  left: calc(100% + 16px);
  background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
  color: white;
  font-size: 0.9rem;
  font-weight: 500;
  padding: 0.7rem 1.2rem;
  border-radius: 12px;
  opacity: 0;
  visibility: hidden;
  transform: translateX(-8px);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  box-shadow: 
    0 4px 15px rgba(0, 0, 0, 0.1),
    0 0 0 1px rgba(255, 255, 255, 0.1) inset;
}

.nav-link:hover .tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(0);
}

@media (max-width: 768px) {
  .side-nav-container {
    left: 20px;
  }

  .side-nav {
    width: 64px;
    height: 360px;
    border-radius: 32px;
  }

  .nav-link {
    width: 48px;
    height: 48px;
  }

  .icon-wrapper {
    width: 24px;
    height: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .side-nav-container,
  .nav-link,
  .tooltip {
    transition: none;
  }
}
</style>
