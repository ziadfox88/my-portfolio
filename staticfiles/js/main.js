//Activating Mobile Menu

const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId);
    const nav = document.getElementById(navId);

    if(toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show');
        })
    }
}

showMenu('nav-toggle', 'nav-menu');

//Toggling Menu by clicking in mobile menu links

const navLink = document.querySelectorAll('.nav-link');

function linkAction() {
    navLink.forEach(n => n.classList.remove('active'));
    this.classList.add('active');

    const navMenu = document.getElementById('nav-menu');
    navMenu.classList.remove('show');
}

navLink.forEach(n => n.addEventListener('click', linkAction));

// Changing Active Menu section while scrolling

const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', scrollActive);

function scrollActive() {
    const scrollY = window.pageYOffset;

    sections.forEach(current => {
        const sectionHeight = current.offsetHeight;
        const sectionTop = current.offsetTop - 50;
        const sectionId = current.getAttribute('id');

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.add('active');
        } else {
            document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.remove('active');
        }
    })
}

// Scroll Reveal Settings

const sr = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 2000,
    reset: true
})

sr.reveal('.home-title', {});
sr.reveal('.home-scroll', {delay: 200});
sr.reveal('.home-img', {origin: 'right', delay: 400 });

sr.reveal('.about-img', {delay: 500});
sr.reveal('.about-subtitle', {delay: 300});
sr.reveal('.about-profession', {delay: 400});
sr.reveal('.about-text', {delay: 500});
sr.reveal('.about-social-icon', {delay: 600, interval: 200});

sr.reveal('.skills-subtitle', {});
sr.reveal('.skills-name', {distance: '20px', delay: 50, interval: 100});
sr.reveal('.skills-img', {delay: 400});

sr.reveal('.portfolio-img', {interval: 200});

// sr.reveal('.contact-subtitle', {});
// sr.reveal('.contact-text', {interval: 300});
// sr.reveal('.contact-input', {delay: 400});
// sr.reveal('.contact-button', {delay: 600});


const toggle = document.getElementById('dark-mode-toggle');
const darkModePreference = localStorage.getItem('dark-mode');

// Set initial state based on localStorage or system preference
if (darkModePreference === 'enabled') {
    document.body.classList.add('dark-mode');
    toggle.checked = true;
} else if (darkModePreference === 'disabled') {
    document.body.classList.remove('dark-mode');
    toggle.checked = false;
} else {
    // No preference saved, check system preference
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark-mode');
        toggle.checked = true;
    }
}

// Toggle dark mode on checkbox change
toggle.addEventListener('change', function() {
    if (this.checked) {
        document.body.classList.add('dark-mode');
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('dark-mode', 'disabled');
    }
});



// Automatically hide alert messages after 10 seconds
setTimeout(function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.classList.remove('show'); // Hide the alert visually
        alert.classList.add('fade'); // Add fade effect for smooth transition
        setTimeout(() => alert.remove(), 500); // Remove alert element after transition
    });
}, 6000); // 6 seconds