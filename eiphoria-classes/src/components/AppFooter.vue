<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-grid">
        <!-- Brand Section -->
        <div class="brand-section">
          <router-link to="/" class="footer-logo">
            <span class="logo-text">Euphoria</span>
            <span class="logo-accent">Classes</span>
          </router-link>
          <p class="brand-description">
            Inspiring learners worldwide with cutting-edge education and innovative learning experiences. Join us and unleash your potential!
          </p>
        </div>

        <!-- Quick Links -->
        <div class="links-section">
          <h3 class="section-title">Quick Links</h3>
          <nav class="footer-nav">
            <ul class="footer-links">
              <li v-for="item in menuItems" :key="item.path">
                <router-link :to="item.path" class="footer-link">
                  {{ item.name }}
                </router-link>
              </li>
            </ul>
          </nav>
        </div>

        <!-- Contact Info -->
        <div class="contact-section">
          <h3 class="section-title">Get in Touch</h3>
          <ul class="contact-list">
            <li>
              <a href="mailto:hello@euphoriaclasses.com" class="contact-link">
                hello@euphoriaclasses.com
              </a>
            </li>
            <li>
              <a href="tel:+1234567890" class="contact-link">
                +1 (234) 567-890
              </a>
            </li>
          </ul>
        </div>

        <!-- Social Links -->
        <div class="social-section">
          <h3 class="section-title">Stay Connected</h3>
          <div class="social-links">
            <a href="#" class="social-link" aria-label="Twitter">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="LinkedIn">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                <rect x="2" y="9" width="4" height="12"></rect>
                <circle cx="4" cy="4" r="2"></circle>
              </svg>
            </a>
            <a href="#" class="social-link" aria-label="Instagram">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.5" y2="6.5"></line>
              </svg>
            </a>
          </div>
        </div>
      </div>

      <!-- Copyright -->
      <div class="copyright-section">
        <p class="copyright-text">
          © {{ currentYear }} Euphoria Classes. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter',
  data() {
    return {
      menuItems: [
        { name: 'About Us', path: '/about' },
        { name: 'Courses', path: '/courses' },
        { name: 'Contact', path: '/contact' },
        { name: 'Get Started', path: '/get-started' }
      ],
      currentYear: new Date().getFullYear()
    }
  }
}
</script>

<style scoped>
.footer-container {
  background-color: #0f172a;
  border-top: 2px solid #fbbf24;
  padding: 4rem 1.5rem 2rem;
  color: #e5e7eb;
}

.footer-content {
  max-width: 1280px;
  margin: 0 auto;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 4rem;
  margin-bottom: 3rem;
}

.brand-section {
  grid-column: span 1;
}

.footer-logo {
  display: flex;
  gap: 0.25rem;
  text-decoration: none;
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 1rem;
  color: #fbbf24;
}

.brand-description {
  color: #94a3b8;
  font-size: 1rem;
  line-height: 1.6;
}

.section-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #fbbf24;
  margin-bottom: 1.5rem;
}

.footer-links,
.contact-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-link,
.contact-link {
  color: #94a3b8;
  text-decoration: none;
  font-size: 1rem;
  display: block;
  padding: 0.375rem 0;
  transition: color 0.3s ease;
}

.footer-link:hover,
.contact-link:hover {
  color: #fbbf24;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-link {
  color: #94a3b8;
  transition: color 0.3s ease;
}

.social-link:hover {
  color: #fbbf24;
}

.social-icon {
  width: 1.5rem;
  height: 1.5rem;
  stroke-width: 2;
}

.copyright-section {
  border-top: 1px solid #1e293b;
  padding-top: 2rem;
  text-align: center;
}

@media (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 3rem;
  }
}

@media (max-width: 640px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .footer-container {
    padding: 3rem 1.5rem 2rem;
  }

  .brand-section {
    text-align: center;
  }

  .footer-logo {
    justify-content: center;
  }

  .section-title {
    text-align: center;
  }

  .footer-links,
  .contact-list {
    text-align: center;
  }

  .social-links {
    justify-content: center;
  }
}
</style>
