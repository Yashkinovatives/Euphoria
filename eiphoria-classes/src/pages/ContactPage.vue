<template>
  <div class="contact-container">
    <div class="contact-wrapper">
      <!-- Left Information Section -->
      <div class="contact-info">
        <div class="info-content">
          <h1 class="title">
            Connect <span class="highlight">With Us</span>
          </h1>
          <p class="subtitle">Have a project in mind? We're excited to hear about it! Let's bring your ideas to life.</p>

          <div class="contact-details">
            <div
              v-for="(detail, index) in contactDetails"
              :key="index"
              class="contact-item"
            >
              <div class="icon-wrapper">
                <component
                  :is="detail.icon"
                  class="contact-icon"
                />
              </div>
              <div class="detail-text">
                <h3>{{ detail.title }}</h3>
                <p>{{ detail.description }}</p>
              </div>
            </div>
          </div>

          <div class="social-links">
            <a
              v-for="(social, index) in socialLinks"
              :key="index"
              :href="social.link"
              class="social-icon"
              :aria-label="social.label"
              target="_blank"
              rel="noopener noreferrer"
            >
              <component
                :is="social.icon"
                class="icon"
              />
            </a>
          </div>
        </div>
      </div>

      <!-- Right Form Section -->
      <div class="contact-form-section">
        <form @submit.prevent="submitForm" class="contact-form">
          <div class="form-group">
            <label for="name" class="form-label">Full Name</label>
            <input
              id="name"
              type="text"
              v-model="form.name"
              placeholder="Your full name"
              required
              class="input-field"
              autocomplete="name"
            />
          </div>
          
          <div class="form-group">
            <label for="email" class="form-label">Email Address</label>
            <input
              id="email"
              type="email"
              v-model="form.email"
              placeholder="you@example.com"
              required
              class="input-field"
              autocomplete="email"
            />
          </div>

          <div class="form-group">
            <label for="message" class="form-label">Your Message</label>
            <textarea
              id="message"
              v-model="form.message"
              placeholder="Share your thoughts or project details..."
              required
              rows="4"
              class="textarea-field"
            ></textarea>
          </div>

          <button type="submit" class="submit-btn">
            <span>Send Message</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="send-icon" viewBox="0 0 24 24">
              <path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        email: '',
        message: ''
      },
      contactDetails: [
        {
          title: 'Company Headquarters',
          description: '123 Innovation Drive, Tech Hub 94123',
          icon: 'LocationIcon'
        },
        {
          title: 'Customer Support',
          description: 'support@creativesolutions.com',
          icon: 'MailIcon'
        },
        {
          title: 'Contact Number',
          description: '+1 (888) creative-help',
          icon: 'PhoneIcon'
        }
      ],
      socialLinks: [
        { 
          link: 'https://twitter.com/creativesolutions', 
          icon: 'TwitterIcon',
          label: 'Twitter Profile'
        },
        { 
          link: 'https://linkedin.com/company/creativesolutions', 
          icon: 'LinkedinIcon',
          label: 'LinkedIn Page'
        },
        { 
          link: 'https://instagram.com/creative.solutions', 
          icon: 'InstagramIcon',
          label: 'Instagram Account'
        }
      ]
    };
  },
  methods: {
    submitForm() {
      // Improved form submission with basic validation
      if (this.form.name.trim() && this.form.email.trim() && this.form.message.trim()) {
        // Here you would typically add actual form submission logic
        // For now, we'll use a simple alert
        alert('Thank you for your message! We will get back to you soon.');
        
        // Reset form
        this.form = { name: '', email: '', message: '' };
      } else {
        alert('Please fill out all fields completely.');
      }
    }
  }
};
</script>

<style scoped>
.contact-container {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #fff5e6, #fbbf24);
  padding: 1rem;
  min-height: 90vh;
}

.contact-wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr;
  max-width: 1200px;
  width: 100%;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.contact-info {
  padding: 2.5rem;
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  color: white;
}

.info-content {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 2.5rem;
  font-weight: 800;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.highlight {
  color: #fff5e6;
}

.subtitle {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.1rem;
  margin-bottom: 2.5rem;
}

.contact-details {
  margin-bottom: 2.5rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}

.icon-wrapper {
  background: rgba(255, 255, 255, 0.2);
  padding: 1rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.contact-icon {
  width: 24px;
  height: 24px;
  color: white;
}

.detail-text h3 {
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 0.35rem;
}

.detail-text p {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
}

.social-links {
  margin-top: auto;
  display: flex;
  gap: 1rem;
}

.social-icon {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.75rem;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-3px);
}

.icon {
  width: 22px;
  height: 22px;
  color: white;
}

.contact-form-section {
  padding: 2.5rem;
  background: white;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #1f2937;
  font-size: 1rem;
}

.input-field,
.textarea-field {
  width: 100%;
  padding: 0.875rem;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  transition: all 0.3s ease;
  font-size: 1rem;
}

.input-field:focus,
.textarea-field:focus {
  border-color: #fbbf24;
  background: white;
  outline: none;
  box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.2);
}

.textarea-field {
  resize: vertical;
  min-height: 120px;
}

.submit-btn {
  width: 100%;
  padding: 0.875rem;
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  border: none;
  color: white;
  font-weight: 700;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  font-size: 1rem;
}

.submit-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 15px rgba(251, 191, 36, 0.4);
}

.send-icon {
  width: 20px;
  height: 20px;
}

@media (max-width: 768px) {
  .contact-wrapper {
    grid-template-columns: 1fr;
  }

  .contact-container {
    padding: 0.5rem;
  }

  .contact-info,
  .contact-form-section {
    padding: 2rem;
  }

  .title {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }
}
</style>