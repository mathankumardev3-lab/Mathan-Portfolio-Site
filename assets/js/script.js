/**
 * Mathan Kumar | Trillion Game Portfolio Script
 * Vanilla JavaScript (ES6+)
 * 
 * - Lucide Icons setup
 * - Mobile Navigation Toggle & Auto-Close
 * - Navbar Scroll Shadow Reaction
 * - GSAP ScrollTrigger Animations
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Lucide Icons
    if (window.lucide) {
        window.lucide.createIcons();
    }

    // 2. Navbar scroll listener
    initNavbarScroll();

    // 3. Mobile Menu Toggle
    initMobileNav();

    // 4. GSAP Entrance Animations
    initGsap();
});

/* =========================================================
   NAVBAR SCROLL
   ========================================================= */
function initNavbarScroll() {
    const nav = document.querySelector('.navbar');
    if (!nav) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 30) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
}

/* =========================================================
   MOBILE MENU TOGGLE
   ========================================================= */
function initMobileNav() {
    const btn = document.getElementById('nav-toggle');
    const menu = document.getElementById('mobile-menu');
    if (!btn || !menu) return;

    btn.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });

    const links = menu.querySelectorAll('.nav-link');
    links.forEach(l => {
        l.addEventListener('click', () => {
            menu.classList.add('hidden');
        });
    });
}

/* =========================================================
   GSAP ENTRANCE ANIMATIONS
   ========================================================= */
function initGsap() {
    if (typeof gsap === 'undefined') return;

    // Hero entrance animations
    gsap.from('.hero-badge, .hero-greeting', {
        y: 20,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        ease: 'power2.out'
    });

    gsap.from('.hero-title', {
        y: 30,
        opacity: 0,
        duration: 0.7,
        delay: 0.15,
        ease: 'power2.out'
    });

    gsap.from('.hero-description, .hero-section .btn-primary-custom, .hero-section .btn-outline-custom', {
        y: 20,
        opacity: 0,
        duration: 0.6,
        stagger: 0.1,
        delay: 0.3,
        ease: 'power2.out'
    });

    gsap.from('.hero-card', {
        y: 30,
        opacity: 0,
        duration: 0.8,
        delay: 0.35,
        ease: 'power2.out'
    });

    // Scroll reveal on project cards
    if (typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        gsap.utils.toArray('.project-card').forEach((card, i) => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: 'top 88%',
                    toggleActions: 'play none none none'
                },
                y: 30,
                opacity: 0,
                duration: 0.6,
                delay: (i % 3) * 0.1,
                ease: 'power2.out'
            });
        });

        gsap.utils.toArray('.service-card, .skill-card').forEach((card, i) => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: 'top 88%',
                    toggleActions: 'play none none none'
                },
                y: 25,
                opacity: 0,
                duration: 0.5,
                delay: (i % 4) * 0.05,
                ease: 'power2.out'
            });
        });
    }
}
