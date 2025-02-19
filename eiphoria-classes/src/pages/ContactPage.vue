<template>
  <div class="contact-container">
    <div class="contact-wrapper">
      <!-- Left Information Section -->
      <div class="contact-info">
        <div class="info-content">
          <h1 class="title">
            Let's Start a <span class="highlight">Conversation</span>
          </h1>
          <p class="subtitle">We'd love to hear from you! Let's create something amazing together.</p>

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
            <label for="name" class="form-label">Name</label>
            <input
              id="name"
              type="text"
              v-model="form.name"
              placeholder="Enter your full name"
              required
              class="input-field"
            />
          </div>
          
          <div class="form-group">
            <label for="email" class="form-label">Email</label>
            <input
              id="email"
              type="email"
              v-model="form.email"
              placeholder="Enter your email address"
              required
              class="input-field"
            />
          </div>

          <div class="form-group">
            <label for="message" class="form-label">Message</label>
            <textarea
              id="message"
              v-model="form.message"
              placeholder="Write your message here..."
              required
              rows="2"
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
          title: 'Address',
          description: '123 Learning Lane, Tech City',
          icon: 'LocationIcon'
        },
        {
          title: 'Email',
          description: 'support@euphoriaclasses.com',
          icon: 'MailIcon'
        },
        {
          title: 'Phone',
          description: '+1 (555) 123-4567',
          icon: 'PhoneIcon'
        }
      ],
      socialLinks: [
        { 
          link: '#', 
          icon: 'TwitterIcon',
          label: 'Twitter'
        },
        { 
          link: '#', 
          icon: 'LinkedinIcon',
          label: 'LinkedIn'
        },
        { 
          link: '#', 
          icon: 'InstagramIcon',
          label: 'Instagram'
        }
      ]
    };
  },
  methods: {
    submitForm() {
      alert('Message sent successfully!');
      this.form = { name: '', email: '', message: '' };
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
  max-width: 1000px;
  width: 100%;
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.contact-info {
  padding: 2rem;
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  color: white;
}

.info-content {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.title {
  font-size: 2.25rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  line-height: 1.2;
}

.highlight {
  color: #fff5e6;
}

.subtitle {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1rem;
  margin-bottom: 2rem;
}

.contact-details {
  margin-bottom: 2rem;
}

.contact-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.25rem;
}

.icon-wrapper {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.75rem;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.contact-icon {
  width: 20px;
  height: 20px;
  color: white;
}

.detail-text h3 {
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.detail-text p {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.9);
}

.social-links {
  margin-top: auto;
  display: flex;
  gap: 0.75rem;
}

.social-icon {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.social-icon:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.icon {
  width: 18px;
  height: 18px;
  color: white;
}

.contact-form-section {
  padding: 2rem;
  background: white;
}

.form-group {
  margin-bottom: 1.25rem;
}

.form-label {
  display: block;
  font-weight: 500;
  margin-bottom: 0.375rem;
  color: #1f2937;
  font-size: 0.9rem;
}

.input-field,
.textarea-field {
  width: 100%;
  padding: 0.75rem;
  background: #f9fafb;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.input-field:focus,
.textarea-field:focus {
  border-color: #fbbf24;
  background: white;
  outline: none;
  box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.1);
}

.textarea-field {
  resize: vertical;
  min-height: 60px;
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background: linear-gradient(135deg, #f59e0b, #fbbf24);
  border: none;
  color: white;
  font-weight: 600;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-size: 0.9rem;
}

.submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(251, 191, 36, 0.3);
}

.send-icon {
  width: 18px;
  height: 18px;
}

@media (max-width: 768px) {
  .contact-wrapper {
    grid-template-columns: 1fr;
  }

  .contact-container {
    padding: 0.75rem;
  }

  .contact-info,
  .contact-form-section {
    padding: 1.5rem;
  }

  .title {
    font-size: 1.75rem;
  }
}
</style>