/* ── SCROLL REVEAL ─────────────────────────────── */
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('[data-reveal]').forEach(el => revealObserver.observe(el));

/* ── ACTIVE NAV LINK ───────────────────────────── */
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

const sectionObserver = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      const id = e.target.id;
      navLinks.forEach(a => {
        a.style.color = a.getAttribute('href') === `#${id}` ? 'var(--text)' : '';
      });
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => sectionObserver.observe(s));

/* ── NAV SCROLL SHADOW ─────────────────────────── */
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
  nav.style.borderBottomColor = window.scrollY > 10
    ? 'rgba(255,255,255,0.1)'
    : 'rgba(255,255,255,0.07)';
}, { passive: true });

/* ── TYPING EFFECT ─────────────────────────────── */
const phrases = ['uv add ragbucket', 'pip install ragbucket'];
let pi = 0, ci = 0, deleting = false;
const typer = document.getElementById('typing-text');

function tick() {
  const phrase = phrases[pi];
  if (!deleting) {
    typer.textContent = phrase.slice(0, ++ci);
    if (ci === phrase.length) { deleting = true; setTimeout(tick, 2400); return; }
  } else {
    typer.textContent = phrase.slice(0, --ci);
    if (ci === 0) { deleting = false; pi = (pi + 1) % phrases.length; setTimeout(tick, 500); return; }
  }
  setTimeout(tick, deleting ? 42 : 72);
}
setTimeout(tick, 1800);

/* ── COPY INSTALL ──────────────────────────────── */
window.copyInstall = function(btn) {
  navigator.clipboard.writeText(typer.textContent.trim() || 'uv add ragbucket');
  btn.textContent = 'Copied!';
  btn.classList.add('copied');
  setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
};

/* ── CODE TABS ─────────────────────────────────── */
window.switchTab = function(btn, id) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('tab-' + id).classList.add('active');
};

/* ── COPY CODE ─────────────────────────────────── */
window.copyCode = function(btn, id) {
  const pre = document.getElementById(id);
  navigator.clipboard.writeText(pre.innerText);
  btn.textContent = 'Copied!';
  btn.classList.add('copied');
  setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
};