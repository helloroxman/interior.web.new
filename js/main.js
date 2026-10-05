/* Oksana Ivanova — site scripts (vanilla, no dependencies) */
(function () {
  'use strict';

  var body = document.body;
  // Tint the mobile browser toolbar to match whatever covers the screen (iOS Safari reads theme-color live)
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var themeDefault = themeMeta ? themeMeta.getAttribute('content') : '#f6f3ee';
  function setTheme(color) { if (themeMeta) themeMeta.setAttribute('content', color || themeDefault); }
  if (/[?&]static\b/.test(location.search)) {
    document.documentElement.classList.add('no-fx');
    window.addEventListener('load', function () { var h = location.hash && document.querySelector(location.hash); if (h) h.scrollIntoView({ behavior: 'instant', block: 'start' }); });
  }

  /* ---------- Header state ---------- */
  var header = document.querySelector('.header');
  function onScroll() {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile menu ---------- */
  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = body.classList.toggle('menu-open');
      body.classList.toggle('is-locked', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      setTheme(open ? '#17171a' : null);
    });
    document.querySelectorAll('.menu a').forEach(function (a) {
      a.addEventListener('click', function () {
        body.classList.remove('menu-open', 'is-locked');
        burger.setAttribute('aria-expanded', 'false');
        setTheme(null);
      });
    });
  }

  /* ---------- Language dropdown ---------- */
  var langs = document.querySelectorAll('.lang');
  langs.forEach(function (l) {
    var btn = l.querySelector('.lang__btn');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = l.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  function closeLangs() { langs.forEach(function (l) { l.classList.remove('is-open'); var b = l.querySelector('.lang__btn'); if (b) b.setAttribute('aria-expanded', 'false'); }); }
  document.addEventListener('click', closeLangs);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeLangs(); });

  /* ---------- Gallery masonry (keeps every photo uncropped) ---------- */
  var gallery = document.querySelector('.gallery');
  function layoutGallery() {
    if (!gallery) return;
    gallery.classList.add('gallery--masonry');
    var cs = getComputedStyle(gallery);
    var row = parseFloat(cs.gridAutoRows) || 8;
    var gap = parseFloat(cs.rowGap) || 0;
    gallery.querySelectorAll('.gallery__item').forEach(function (it) {
      var im = it.querySelector('img');
      var w = parseFloat(im.getAttribute('width')), h = parseFloat(im.getAttribute('height'));
      if (!w || !h) return;
      var height = it.getBoundingClientRect().width * h / w;
      it.style.gridRowEnd = 'span ' + Math.max(1, Math.round((height + gap) / (row + gap)));
    });
  }
  if (gallery) {
    layoutGallery();
    var rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(layoutGallery, 120); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(layoutGallery);
    window.addEventListener('load', layoutGallery);
  }

  /* ---------- Reveal on scroll ---------- */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- Counters ---------- */
  var counters = document.querySelectorAll('[data-count]');
  function animateCount(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var suffix = el.getAttribute('data-suffix') || '';
    var start = null, dur = 1400;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = String(Math.round(target * eased)).replace(/\B(?=(\d{3})+(?!\d))/g, '\u202f') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (counters.length) {
    if ('IntersectionObserver' in window) {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { animateCount(e.target); cio.unobserve(e.target); } });
      }, { threshold: 0.4 });
      counters.forEach(function (c) { cio.observe(c); });
    } else {
      counters.forEach(animateCount);
    }
  }

  /* ---------- Portfolio filters ---------- */
  var filters = document.querySelectorAll('.filter');
  var cards = document.querySelectorAll('.card[data-type]');
  var empty = document.querySelector('.grid-empty');
  function applyFilter(type) {
    var shown = 0;
    cards.forEach(function (c) {
      var show = type === 'all' || c.getAttribute('data-type') === type;
      c.classList.toggle('is-hidden', !show);
      if (show) shown++;
    });
    if (empty) empty.classList.toggle('is-visible', shown === 0);
    filters.forEach(function (f) {
      var active = f.getAttribute('data-filter') === type;
      f.classList.toggle('is-active', active);
      f.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    // re-flow wide cards: every 5th visible card becomes wide for an editorial rhythm
    var i = 0;
    cards.forEach(function (c) {
      if (c.classList.contains('is-hidden')) return;
      c.classList.toggle('card--wide', i % 5 === 0);
      i++;
    });
  }
  if (filters.length) {
    filters.forEach(function (f) {
      f.addEventListener('click', function () {
        var t = f.getAttribute('data-filter');
        applyFilter(t);
        if (history.replaceState) history.replaceState(null, '', t === 'all' ? location.pathname : '#projects-' + t);
      });
    });
    var m = location.hash.match(/^#projects-(\w+)$/);
    applyFilter(m ? m[1] : 'all');
  }

  /* ---------- Lightbox ---------- */
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery__item'));
  var lb = document.querySelector('.lightbox');
  if (items.length && lb) {
    var img = lb.querySelector('img');
    var counter = lb.querySelector('.lightbox__counter');
    var idx = 0, lastFocus = null;
    var srcs = items.map(function (it) { return it.getAttribute('data-full'); });

    function preload(i) { var n = srcs[(i + srcs.length) % srcs.length]; if (n) { var p = new Image(); p.src = n; } }
    function show(i, dir) {
      idx = (i + srcs.length) % srcs.length;
      if (dir) {
        img.classList.remove('is-from-next', 'is-from-prev');
        void img.offsetWidth; // restart the animation
        img.classList.add(dir > 0 ? 'is-from-next' : 'is-from-prev');
      }
      img.src = srcs[idx];
      img.alt = items[idx].querySelector('img').alt;
      counter.textContent = (idx + 1) + ' / ' + srcs.length;
      preload(idx + 1); preload(idx - 1);
    }
    // Mouse wheel / trackpad: scroll down = next photo, scroll up = previous
    var wheelAcc = 0, wheelLock = 0;
    lb.addEventListener('wheel', function (e) {
      e.preventDefault();
      var now = Date.now();
      if (now < wheelLock) return;
      var delta = Math.abs(e.deltaY) >= Math.abs(e.deltaX) ? e.deltaY : e.deltaX;
      wheelAcc += delta;
      if (Math.abs(wheelAcc) < 60) return;
      show(idx + (wheelAcc > 0 ? 1 : -1), wheelAcc > 0 ? 1 : -1);
      wheelAcc = 0;
      wheelLock = now + 450;
    }, { passive: false });
    function open(i) {
      lastFocus = document.activeElement;
      lb.classList.add('is-open');
      body.classList.add('is-locked');
      setTheme('#0c0c0e');
      show(i);
      lb.querySelector('.lightbox__close').focus();
    }
    function close() {
      lb.classList.remove('is-open');
      body.classList.remove('is-locked');
      setTheme(null);
      img.src = '';
      if (lastFocus) lastFocus.focus();
    }
    items.forEach(function (it, i) { it.addEventListener('click', function (e) { e.preventDefault(); open(i); }); });
    lb.querySelector('.lightbox__close').addEventListener('click', close);
    lb.querySelector('.lightbox__prev').addEventListener('click', function () { show(idx - 1, -1); });
    lb.querySelector('.lightbox__next').addEventListener('click', function () { show(idx + 1, 1); });
    lb.querySelector('.lightbox__stage').addEventListener('click', function (e) { if (e.target === e.currentTarget) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') { e.preventDefault(); show(idx + 1, 1); }
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); show(idx - 1, -1); }
    });
    var tx = null;
    lb.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (tx === null) return;
      var dx = e.changedTouches[0].clientX - tx; tx = null;
      if (Math.abs(dx) > 50) show(dx < 0 ? idx + 1 : idx - 1, dx < 0 ? 1 : -1);
    });
  }

  /* ---------- Current year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
