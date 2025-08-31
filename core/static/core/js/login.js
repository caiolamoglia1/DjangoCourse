// Enhanced Login Page JavaScript
document.addEventListener('DOMContentLoaded', function () {

    // Form validation and enhancements
    const loginForm = document.querySelector('#loginForm');
    const usernameInput = document.querySelector('#username');
    const passwordInput = document.querySelector('#password');
    const submitButton = document.querySelector('.btn-login');
    const rememberCheckbox = document.querySelector('#remember');

    // Real-time form validation
    function validateForm() {
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        if (username && password) {
            submitButton.disabled = false;
            submitButton.style.opacity = '1';
        } else {
            submitButton.disabled = true;
            submitButton.style.opacity = '0.7';
        }
    }

    // Add event listeners for real-time validation
    if (usernameInput && passwordInput) {
        usernameInput.addEventListener('input', validateForm);
        passwordInput.addEventListener('input', validateForm);

        // Initial validation
        validateForm();
    }

    // Enhanced form submission with loading state
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            const submitBtn = this.querySelector('.btn-login');
            const btnText = submitBtn.querySelector('.btn-text') || submitBtn;
            const btnLoader = submitBtn.querySelector('.button-loader');

            // Show loading state
            if (btnText) btnText.textContent = 'Conectando...';
            if (btnLoader) btnLoader.style.display = 'block';
            submitBtn.disabled = true;

            // Add a slight delay for visual feedback
            setTimeout(() => {
                // Form will submit naturally after this
            }, 500);
        });
    }

    // Enhanced floating elements animation
    function createFloatingAnimation() {
        const floatingElements = document.querySelectorAll('.floating-element');

        floatingElements.forEach((element, index) => {
            // Add random animation delays
            const delay = Math.random() * 2;
            element.style.animationDelay = `${delay}s`;

            // Add mouse interaction
            element.addEventListener('mouseenter', function () {
                this.style.transform = 'scale(1.2) rotate(10deg)';
                this.style.transition = 'transform 0.3s ease';
            });

            element.addEventListener('mouseleave', function () {
                this.style.transform = '';
            });
        });
    }

    // Enhanced card decorations animation
    function enhanceCardDecorations() {
        const decorations = document.querySelectorAll('.card-decoration');

        decorations.forEach((decoration, index) => {
            // Add pulsing effect
            const delay = index * 0.5;
            decoration.style.animationDelay = `${delay}s`;

            // Add hover interaction
            decoration.addEventListener('mouseenter', function () {
                this.style.transform = 'scale(1.1) rotate(45deg)';
                this.style.boxShadow = '0 0 30px rgba(255, 215, 0, 0.6)';
            });

            decoration.addEventListener('mouseleave', function () {
                this.style.transform = '';
                this.style.boxShadow = '';
            });
        });
    }

    // Dashboard preview chart animation
    function animateChartBars() {
        const bars = document.querySelectorAll('.bar');

        bars.forEach((bar, index) => {
            const height = ['60%', '40%', '80%', '30%', '70%', '50%'][index];
            bar.style.height = '0%';

            setTimeout(() => {
                bar.style.transition = 'height 1s ease-out';
                bar.style.height = height;
            }, 1500 + (index * 200));
        });
    }

    // Intersection Observer for animations
    function setupIntersectionObserver() {
        const observerOptions = {
            threshold: 0.3,
            rootMargin: '-50px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');

                    // Special handling for chart
                    if (entry.target.classList.contains('dashboard-preview')) {
                        setTimeout(animateChartBars, 500);
                    }
                }
            });
        }, observerOptions);

        // Observe elements
        const elementsToObserve = document.querySelectorAll('.feature-item, .dashboard-preview, .login-card');
        elementsToObserve.forEach(el => observer.observe(el));
    }

    // Form input enhancements
    function enhanceFormInputs() {
        const formGroups = document.querySelectorAll('.form-group');

        formGroups.forEach(group => {
            const input = group.querySelector('input');
            const label = group.querySelector('label');

            if (input && label) {
                // Add floating label effect
                input.addEventListener('focus', () => {
                    group.classList.add('focused');
                });

                input.addEventListener('blur', () => {
                    if (!input.value.trim()) {
                        group.classList.remove('focused');
                    }
                });

                // Check if input has value on load
                if (input.value.trim()) {
                    group.classList.add('focused');
                }
            }
        });
    }

    // Social login buttons enhancement
    function enhanceSocialButtons() {
        const socialButtons = document.querySelectorAll('.btn-social');

        socialButtons.forEach(button => {
            button.addEventListener('click', function (e) {
                e.preventDefault();

                // Add loading state
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Conectando...';
                this.disabled = true;

                // Simulate connection (replace with actual social login)
                setTimeout(() => {
                    this.innerHTML = originalText;
                    this.disabled = false;

                    // Show message
                    showNotification('Funcionalidade em desenvolvimento!', 'info');
                }, 2000);
            });
        });
    }

    // Notification system
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close">&times;</button>
        `;

        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            z-index: 10000;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            animation: slideInRight 0.3s ease-out;
            max-width: 350px;
        `;

        document.body.appendChild(notification);

        // Auto remove
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        }, 5000);

        // Close button
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        });
    }

    // Password visibility toggle
    function addPasswordToggle() {
        const passwordGroup = passwordInput?.closest('.form-group');
        if (passwordGroup && !passwordGroup.querySelector('.password-toggle')) {
            const toggleButton = document.createElement('button');
            toggleButton.type = 'button';
            toggleButton.className = 'password-toggle';
            toggleButton.innerHTML = '<i class="fas fa-eye"></i>';
            toggleButton.style.cssText = `
                position: absolute;
                right: 15px;
                top: 50%;
                transform: translateY(-50%);
                background: none;
                border: none;
                color: #888;
                cursor: pointer;
                transition: color 0.3s;
            `;

            passwordGroup.style.position = 'relative';
            passwordGroup.appendChild(toggleButton);

            toggleButton.addEventListener('click', () => {
                const isPassword = passwordInput.type === 'password';
                passwordInput.type = isPassword ? 'text' : 'password';
                toggleButton.innerHTML = isPassword ? '<i class="fas fa-eye-slash"></i>' : '<i class="fas fa-eye"></i>';
            });
        }
    }

    // Initialize all enhancements
    createFloatingAnimation();
    enhanceCardDecorations();
    setupIntersectionObserver();
    enhanceFormInputs();
    enhanceSocialButtons();
    addPasswordToggle();

    // Add CSS animations for intersection observer
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes slideOutRight {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
        
        .animate-in {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
        
        .feature-item, .dashboard-preview {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.6s ease-out;
        }
        
        .form-group.focused label {
            color: #ffd700;
            transform: translateY(-8px);
            font-size: 0.85rem;
        }
        
        .password-toggle:hover {
            color: #ffd700 !important;
        }
    `;
    document.head.appendChild(style);

    // Console message for developers
    console.log('%c🚀 Enhanced Login Page Loaded!', 'color: #ffd700; font-size: 16px; font-weight: bold;');
});
