/* JLC Service — interactions */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header + barre de progression */
  const top = $('.top'), prog = $('#prog');
  const onScroll = () => {
    if (top) top.classList.toggle('scrolled', scrollY > 12);
    if (prog) {
      const h = document.documentElement;
      const p = h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight);
      prog.style.transform = `scaleX(${p})`;
    }
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* menu mobile */
  const burger = $('.burger'), menu = $('.menu');
  if (burger && menu) {
    const close = () => { menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; };
    burger.onclick = () => { menu.classList.add('open'); burger.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; };
    $('.x', menu).onclick = close;
    $$('a', menu).forEach(a => a.onclick = close);
    addEventListener('keydown', e => e.key === 'Escape' && close());
  }

  /* lien courant */
  const here = location.pathname.split('/').pop() || 'index.html';
  $$('.nav nav a, .menu a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === here || (here.startsWith('realisation') && href === 'realisations.html')) a.setAttribute('aria-current', 'page');
  });

  /* reveals */
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); if (e.target.classList.contains('steps')) e.target.style.setProperty('--fill', 1), e.target.classList.add('go'); io.unobserve(e.target); }
  }), { threshold: .15, rootMargin: '0px 0px -8% 0px' });
  $$('[data-reveal], .words, .steps').forEach(el => io.observe(el));

  /* hero : changer d'exemple (au clic seulement) */
  const hf = $('#hero-fr');
  if (hf) $$('.scene.one .tag button').forEach(b => b.onclick = () => {
    $$('.scene.one .tag button').forEach(x => x.setAttribute('aria-pressed', x === b));
    hf.classList.add('fade');
    setTimeout(() => { hf.src = b.dataset.src; }, 300);
    hf.onload = () => hf.classList.remove('fade');
  });

  /* avant / après */
  $$('.ba').forEach(ba => {
    const inp = $('input', ba);
    const upd = () => ba.style.setProperty('--p', inp.value + '%');
    inp.addEventListener('input', upd); upd();
    const fit = () => { const w = ba.clientWidth; ba.style.setProperty('--bs', w / 1280); };
    fit(); addEventListener('resize', fit);
  });

  /* mise à l'échelle des iframes dans les écrans d'ordinateur et les cartes */
  const fitScr = () => {
    $$('.laptop .lid .scr').forEach(s => s.closest('.laptop').style.setProperty('--ls', s.clientWidth / 1280));
    $$('.work .prev').forEach(p => p.closest('.work').style.setProperty('--ws', p.clientWidth / (p.closest('.work.big') && innerWidth > 620 ? 1280 : 390)));
  };
  fitScr(); addEventListener('resize', fitScr); addEventListener('load', fitScr);

  /* démo « plat du jour » : panneau → téléphone */
  const live = $('#live');
  if (live) {
    const fr = $('iframe', live), name = $('#l-name'), price = $('#l-price'), saved = $('#l-saved');
    let t;
    const push = () => {
      try { fr.contentWindow.postMessage({ type: 'dish', name: name.value, price: price.value }, '*'); } catch (e) { }
      saved.textContent = 'Modifié sur le site · à l’instant';
      clearTimeout(t); t = setTimeout(() => saved.textContent = '', 2500);
    };
    [name, price].forEach(i => i.addEventListener('input', push));
    fr.addEventListener('load', push);
    if (!reduce) {
      const n = 'Risotto aux coques';
      new IntersectionObserver((e, o) => {
        if (!e[0].isIntersecting) return; o.disconnect();
        setTimeout(() => {
          if (document.activeElement === name || document.activeElement === price) return;
          let i = 0; name.value = ''; price.value = '21';
          const t = setInterval(() => { name.value = n.slice(0, ++i); push(); if (i >= n.length) clearInterval(t); }, 60);
          name.addEventListener('focus', () => clearInterval(t), { once: true });
        }, 900);
      }, { threshold: .6 }).observe(live);
    }
  }

  /* compteurs */
  $$('[data-count]').forEach(el => {
    const end = +el.dataset.count, suf = el.dataset.suffix || '';
    new IntersectionObserver((e, o) => {
      if (!e[0].isIntersecting) return; o.disconnect();
      if (reduce) { el.textContent = end + suf; return; }
      const t0 = performance.now(), dur = 1400;
      const step = now => { const p = Math.min(1, (now - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - p, 3))); el.textContent = v + suf; if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    }, { threshold: .5 }).observe(el);
  });
})();

/* v2.2 : écrans à activer au clic + formulaire en étapes */
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  $$('.tapzone').forEach(z => {
    const t = $('.tap', z);
    t.addEventListener('click', () => z.classList.add('on'));
    z.addEventListener('pointerleave', e => { if (e.pointerType === 'mouse') z.classList.remove('on'); });
  });

  const f = $('#funnel'); if (!f) return;
  const steps = $$('.fn-step', f), bar = $('.fn-bar i', f), count = $('.fn-count b', f), back = $('.fn-back', f);
  let cur = 1;
  const store = { get() { try { return JSON.parse(sessionStorage.getItem('jlc-fn') || '{}'); } catch (e) { return {}; } },
                  set(v) { try { sessionStorage.setItem('jlc-fn', JSON.stringify(v)); } catch (e) {} } };
  const data = () => {
    const d = {};
    ['secteur', 'site_actuel', 'delai'].forEach(n => { const i = $(`input[name=${n}]:checked`, f); d[n] = i ? i.value : ''; d[n + '_l'] = i ? i.dataset.label : ''; });
    const pr = $$('input[name=priorites]:checked', f); d.priorites = pr.map(i => i.dataset.label).join(', ');
    d.commerce = $('input[name=commerce]', f).value.trim(); d.ville = $('input[name=ville]', f).value.trim();
    return d;
  };
  const go = n => {
    cur = n;
    steps.forEach(s => s.hidden = +s.dataset.step !== n);
    bar.style.width = (n / 5 * 100) + '%'; count.textContent = n; back.hidden = n === 1;
    if (n === 5) finish();
    const top = f.getBoundingClientRect().top + scrollY - 90;
    if (scrollY > top) scrollTo({ top, behavior: 'smooth' });
    const first = $(`.fn-step[data-step="${n}"] input`, f); if (first && n !== 5) first.focus({ preventScroll: true });
  };
  const save = () => { const d = data(); store.set(d); return d; };
  // étapes 1 et 2 : un clic = étape suivante
  ['secteur', 'site_actuel'].forEach((n, k) => $$(`input[name=${n}]`, f).forEach(i => i.addEventListener('change', () => { save(); setTimeout(() => go(k + 2), 220); })));
  // étape 3
  const n3 = $('[data-step="3"] .fn-next', f);
  $$('input[name=priorites]', f).forEach(i => i.addEventListener('change', () => { n3.disabled = !$('input[name=priorites]:checked', f); save(); }));
  n3.onclick = () => go(4);
  // étape 4
  const n4 = $('[data-step="4"] .fn-next', f), ok4 = () => n4.disabled = !(data().commerce && data().ville);
  $$('[data-step="4"] input', f).forEach(i => i.addEventListener('input', () => { ok4(); save(); }));
  $$('[data-step="4"] input[type=radio]', f).forEach(i => i.addEventListener('change', save));
  $$('[data-step="4"] input[type=text], [data-step="4"] input:not([type])', f).forEach(i => i.addEventListener('keydown', e => { if (e.key === 'Enter' && !n4.disabled) go(5); }));
  n4.onclick = () => go(5);
  back.onclick = () => go(Math.max(1, cur - 1));

  function finish() {
    const d = save();
    const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
    const parts = [['Activité', d.secteur_l], ['Site actuel', d.site_actuel_l], ['Commerce', d.commerce + (d.ville ? ' · ' + d.ville : '')], ['Priorités', d.priorites], ['Délai', d.delai_l]].filter(p => p[1]);
    $('#fn-recap').innerHTML = parts.map(([k, v]) => `<span>${k} : <b>${esc(v)}</b></span>`).join('');
    const q = new URLSearchParams({ secteur: d.secteur_l, site_actuel: d.site_actuel_l, priorites: d.priorites, commerce: d.commerce, ville: d.ville, delai: d.delai_l }).toString();
    const fr = $('#fn-tally'), src = window.TALLY_MAQ_EMBED + '&' + q;
    if (fr.getAttribute('src') !== src) fr.setAttribute('src', src);
    $('#fn-tally-link').href = window.TALLY_MAQ + '?' + q;
  }
  // hauteur dynamique du formulaire Tally
  addEventListener('message', e => {
    if (typeof e.data !== 'string' || !e.data.includes('Tally.FormPageView') && !e.data.includes('Tally.FormHeight')) {
      try { const m = typeof e.data === 'string' ? JSON.parse(e.data) : e.data; if (m && m.event === 'Tally.FormSubmitted') store.set({}); } catch (x) {}
    }
    try { const m = typeof e.data === 'string' ? JSON.parse(e.data) : e.data; if (m && m.event === 'Tally.FormHeight' && m.payload) $('#fn-tally').style.height = (m.payload.height || m.payload) + 'px'; } catch (x) {}
  });

  // reprise : réponses gardées + départ depuis l'accueil (?s=secteur)
  const saved = store.get();
  const setR = (n, v) => { const i = v && $(`input[name=${n}][value="${v}"]`, f); if (i) i.checked = true; };
  setR('secteur', saved.secteur); setR('site_actuel', saved.site_actuel); setR('delai', saved.delai);
  if (saved.priorites) $$('input[name=priorites]', f).forEach(i => { if (saved.priorites.split(', ').includes(i.dataset.label)) i.checked = true; });
  if (saved.commerce) $('input[name=commerce]', f).value = saved.commerce;
  if (saved.ville) $('input[name=ville]', f).value = saved.ville;
  n3.disabled = !$('input[name=priorites]:checked', f); ok4();
  const s = new URLSearchParams(location.search).get('s');
  if (s && $(`input[name=secteur][value="${s}"]`, f)) { setR('secteur', s); save(); go(2); }
})();
