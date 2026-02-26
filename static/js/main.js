// ============================================
// MONARK MEHTA PORTFOLIO — MAIN JS
// ============================================

// ── Role cycling animation ──────────────────
const roleEl = document.getElementById('role-text');
if (roleEl) {
    const roles = ["Software Engineer", "Data Scientist", "Python Developer", "Industrial Analytics", "Real-Time Systems"];
    let roleIndex = 0;
    setInterval(() => {
        roleEl.style.opacity = '0';
        roleEl.style.transform = 'translateY(-10px)';
        setTimeout(() => {
            roleIndex = (roleIndex + 1) % roles.length;
            roleEl.textContent = roles[roleIndex];
            roleEl.style.opacity = '1';
            roleEl.style.transform = 'translateY(0)';
        }, 300);
    }, 2500);
}

// ── NAV scroll effect ───────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 50);
});

// ── Mobile nav toggle ───────────────────────
const navToggle = document.getElementById('navToggle');
const navLinks  = document.querySelector('.nav-links');
navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    navToggle.textContent = navLinks.classList.contains('open') ? '✕' : '☰';
});
navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.textContent = '☰';
    });
});

// ── Active nav highlighting ─────────────────
const sections = document.querySelectorAll('section[id]');
const navItems  = document.querySelectorAll('.nav-links a');
const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navItems.forEach(a => a.style.color = '');
            const active = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
            if (active) active.style.color = 'var(--accent)';
        }
    });
}, { rootMargin: '-40% 0px -40% 0px' });
sections.forEach(s => sectionObserver.observe(s));

// ── Reveal on scroll ────────────────────────
// Use threshold:0 so even large elements trigger as soon as 1px is visible
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const delay = parseInt(entry.target.dataset.delay) || 0;
            setTimeout(() => entry.target.classList.add('visible'), delay);
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0, rootMargin: '0px 0px -60px 0px' });

document.querySelectorAll('.reveal').forEach((el, i) => {
    el.dataset.delay = (i % 5) * 80;
    revealObserver.observe(el);
});

// Fallback: make everything visible after 2s in case observer never fires
setTimeout(() => {
    document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
        el.classList.add('visible');
    });
}, 2000);

// ── Typing effect on hero subtitle ─────────
const subtitleEl = document.querySelector('.hero-subtitle');
if (subtitleEl) {
    const original = subtitleEl.textContent.trim();
    subtitleEl.textContent = '';
    let i = 0;
    const type = () => {
        if (i < original.length) {
            subtitleEl.textContent += original[i++];
            setTimeout(type, 35);
        }
    };
    setTimeout(type, 1400);
}

// ── Skill pill hover scale ──────────────────
document.querySelectorAll('.skill-pill, .tech-tag').forEach(pill => {
    pill.addEventListener('mouseover', function() { this.style.transform = 'scale(1.07)'; });
    pill.addEventListener('mouseout',  function() { this.style.transform = ''; });
});

// ── Cursor glow (desktop only) ──────────────
if (window.matchMedia('(pointer:fine)').matches) {
    const cursor = document.createElement('div');
    cursor.style.cssText = `
        position:fixed;width:320px;height:320px;border-radius:50%;
        background:radial-gradient(circle,rgba(0,200,255,0.05),transparent 70%);
        pointer-events:none;z-index:0;
        transform:translate(-50%,-50%);transition:left .08s,top .08s;
    `;
    document.body.appendChild(cursor);
    document.addEventListener('mousemove', e => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top  = e.clientY + 'px';
    });
}
