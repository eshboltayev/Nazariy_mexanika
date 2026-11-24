/* Nazariy mexanika — interaktiv simulyatorlar.
   Har bir simulyator HTML’da <div class="sim-box" data-sim="KALIT"></div> ko‘rinishida chaqiriladi.
   Modellar o‘quv maqsadida soddalashtirilgan; birliklar SI (alohida ko‘rsatilmagan bo‘lsa). */
(() => {
  'use strict';
  const g0 = 9.81;
  const A = s => (window.YAF_ALIF ? window.YAF_ALIF.A(s) : String(s));
  const C = { cyan:'#22d3ee', green:'#34d399', amber:'#fbbf24', rose:'#fb7185', violet:'#a78bfa', blue:'#60a5fa', grid:'#1e2c44', axis:'#64748b', text:'#cbd5e1' };
  const SUP = { '-':'⁻', '0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹' };
  const sci = (v, d = 2) => {
    if (!isFinite(v)) return '—';
    if (v === 0) return '0';
    const e = Math.floor(Math.log10(Math.abs(v)));
    if (e >= -2 && e <= 3) return v.toFixed(Math.max(0, d - (e > 0 ? e : 0)));
    const m = v / 10 ** e;
    return `${m.toFixed(d)}·10${String(e).split('').map(ch => SUP[ch]).join('')}`;
  };
  const fx = (v, d = 3) => (isFinite(v) ? Number(v).toFixed(d) : '—');

  function ctx2d(canvas) {
    const r = canvas.getBoundingClientRect();
    const zoom = parseFloat(getComputedStyle(document.documentElement).zoom) || 1;
    const dpr = Math.min((window.devicePixelRatio || 1) * zoom, 4);
    const w = Math.max(1, Math.floor(canvas.clientWidth || r.width)), h = Math.max(1, Math.floor(canvas.clientHeight || r.height));
    if (canvas.width !== w * dpr || canvas.height !== h * dpr) { canvas.width = w * dpr; canvas.height = h * dpr; }
    const c = canvas.getContext('2d'); c.setTransform(dpr, 0, 0, dpr, 0, 0); c.clearRect(0, 0, w, h);
    return { c, w, h };
  }

  function niceTicks(a, b, n = 5) {
    const span = b - a; if (span <= 0) return [a];
    const raw = span / n, mag = 10 ** Math.floor(Math.log10(raw));
    const step = [1, 2, 2.5, 5, 10].map(s => s * mag).find(s => span / s <= n + .5) || mag * 10;
    const out = []; for (let t = Math.ceil(a / step) * step; t <= b + step * 1e-6; t += step) out.push(+t.toPrecision(10));
    return out;
  }

  /* Umumiy grafik chizuvchi */
  function plot(c, box, o) {
    const [X0, Y0, W, H] = box, L = 54, R = 12, T = 22, B = 36;
    const px = X0 + L, py = Y0 + T, pw = W - L - R, ph = H - T - B;
    const tx = v => (o.logx ? Math.log10(v) : v), ty = v => (o.logy ? Math.log10(Math.max(v, 1e-300)) : v);
    const [xa, xb] = o.xr.map(tx), [ya, yb] = o.yr.map(ty);
    const X = v => px + (tx(v) - xa) / (xb - xa) * pw;
    const Y = v => py + ph - (ty(v) - ya) / (yb - ya) * ph;
    c.save(); c.font = '11px JetBrains Mono, monospace'; c.lineWidth = 1;
    const xt = o.logx ? range(Math.ceil(xa), Math.floor(xb)).map(e => 10 ** e) : niceTicks(o.xr[0], o.xr[1], o.nx || 6);
    const yt = o.logy ? range(Math.ceil(ya), Math.floor(yb)).filter((e, i, arr) => arr.length < 9 || i % 2 === 0).map(e => 10 ** e) : niceTicks(o.yr[0], o.yr[1], o.ny || 5);
    c.strokeStyle = C.grid; c.fillStyle = C.axis; c.textAlign = 'center';
    xt.forEach(t => { const x = X(t); c.beginPath(); c.moveTo(x, py); c.lineTo(x, py + ph); c.stroke(); c.fillText(fmtTick(t), x, py + ph + 15); });
    c.textAlign = 'right';
    yt.forEach(t => { const y = Y(t); c.beginPath(); c.moveTo(px, y); c.lineTo(px + pw, y); c.stroke(); c.fillText(fmtTick(t), px - 6, y + 4); });
    c.strokeStyle = C.axis; c.strokeRect(px, py, pw, ph);
    if (!o.logy && o.yr[0] < 0 && o.yr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(px, Y(0)); c.lineTo(px + pw, Y(0)); c.stroke(); }
    if (!o.logx && o.xr[0] < 0 && o.xr[1] > 0) { c.strokeStyle = '#475569'; c.beginPath(); c.moveTo(X(0), py); c.lineTo(X(0), py + ph); c.stroke(); }
    c.fillStyle = C.text; c.textAlign = 'center'; c.fillText(A(o.xl || ''), px + pw / 2, py + ph + 30);
    c.textAlign = 'left'; c.fillText(A(o.yl || ''), px, py - 8);
    c.beginPath(); c.rect(px, py, pw, ph); c.clip();
    (o.fill || []).forEach(f => { c.fillStyle = f.c; c.beginPath(); f.pts.forEach(([x, y], i) => (i ? c.lineTo(X(x), Y(y)) : c.moveTo(X(x), Y(y)))); c.closePath(); c.fill(); });
    (o.series || []).forEach(s => {
      c.strokeStyle = s.c || C.cyan; c.lineWidth = s.w || 2; c.setLineDash(s.dash || []); c.beginPath(); let started = false;
      s.pts.forEach(([x, y]) => { if (!isFinite(y) || !isFinite(x) || (o.logy && y <= 0) || (o.logx && x <= 0)) { started = false; return; } const xx = X(x), yy = Y(y); if (!started) { c.moveTo(xx, yy); started = true; } else c.lineTo(xx, yy); });
      c.stroke(); c.setLineDash([]);
    });
    (o.vl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(X(v.x), py); c.lineTo(X(v.x), py + ph); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), X(v.x) + 4, py + 12); } });
    (o.hl || []).forEach(v => { c.strokeStyle = v.c || C.amber; c.setLineDash([5, 4]); c.beginPath(); c.moveTo(px, Y(v.y)); c.lineTo(px + pw, Y(v.y)); c.stroke(); c.setLineDash([]); if (v.l) { c.fillStyle = v.c || C.amber; c.fillText(A(v.l), px + 6, Y(v.y) - 5); } });
    (o.marks || []).forEach(m => { c.fillStyle = m.c || '#fff'; c.beginPath(); c.arc(X(m.x), Y(m.y), m.r || 5, 0, 7); c.fill(); if (m.l) { c.fillText(A(m.l), X(m.x) + 8, Y(m.y) - 8); } });
    c.restore();
    if ((o.legend || []).length) { c.fillStyle = 'rgba(3,7,18,.82)'; c.fillRect(px + pw - 156, py + 2, 152, o.legend.length * 16 + 8); }
    (o.legend || []).forEach((g, i) => { c.font = '11px Inter, sans-serif'; c.fillStyle = g.c; c.fillRect(px + pw - 150, py + 8 + i * 16, 12, 3); c.fillStyle = C.text; c.textAlign = 'left'; c.fillText(A(g.l), px + pw - 133, py + 13 + i * 16); });
    return { X, Y };
  }
  const fmtTick = t => (Math.abs(t) >= 1000 || (Math.abs(t) < .01 && t !== 0) ? sci(t, 1) : String(+t.toFixed(3)));
  const range = (a, b) => { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; };
  const lin = (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1));
  const label = (c, t, x, y, col = C.text, al = 'left') => { c.fillStyle = col; c.font = '12px Inter, sans-serif'; c.textAlign = al; c.fillText(A(t), x, y); };

  /* ---------- Chizish yordamchilari ---------- */
  const ln = (c, x1, y1, x2, y2, col = C.text, w = 1.5, dash) => { c.strokeStyle = col; c.lineWidth = w; c.setLineDash(dash || []); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2, y2); c.stroke(); c.setLineDash([]); };
  const arrow = (c, x1, y1, x2, y2, col = C.amber, w = 2) => { if (Math.hypot(x2 - x1, y2 - y1) < 1) return; ln(c, x1, y1, x2, y2, col, w); const a = Math.atan2(y2 - y1, x2 - x1), s = 8; c.fillStyle = col; c.beginPath(); c.moveTo(x2, y2); c.lineTo(x2 - s * Math.cos(a - .4), y2 - s * Math.sin(a - .4)); c.lineTo(x2 - s * Math.cos(a + .4), y2 - s * Math.sin(a + .4)); c.closePath(); c.fill(); };
  const circ = (c, x, y, r, col = C.text, fill, w = 1.5) => { c.beginPath(); c.arc(x, y, Math.max(r, .5), 0, 7); if (fill) { c.fillStyle = fill; c.fill(); } if (col) { c.strokeStyle = col; c.lineWidth = w; c.stroke(); } };
  const txt = (c, t, x, y, col = C.text, al = 'center', size = 12) => { c.fillStyle = col; c.font = `${size}px Inter, sans-serif`; c.textAlign = al; c.fillText(A(t), x, y); };
  const poly = (c, pts, col, w = 2, dash) => { c.strokeStyle = col; c.lineWidth = w; c.setLineDash(dash || []); c.beginPath(); pts.forEach(([x, y], i) => (i ? c.lineTo(x, y) : c.moveTo(x, y))); c.stroke(); c.setLineDash([]); };
  const rk4 = (f, s, dt) => { const k1 = f(s), k2 = f(s.map((v, i) => v + dt / 2 * k1[i])), k3 = f(s.map((v, i) => v + dt / 2 * k2[i])), k4 = f(s.map((v, i) => v + dt * k3[i])); return s.map((v, i) => v + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])); };
  const agm = (a, b) => { for (let i = 0; i < 30; i++) { const t = (a + b) / 2; b = Math.sqrt(a * b); a = t; } return a; };
  const deg = Math.PI / 180;
  /* Parametrlar o‘zgarganda keshni yangilash (animatsiyali modellar uchun) */
  const cache = (cv, P, make) => { const key = JSON.stringify(P); if (cv._key !== key) { cv._key = key; cv._d = make(); cv._t = 0; } return cv._d; };
  const tick = (cv, dt) => { cv._t = (cv._t || 0) + Math.max(0, dt || 0); return cv._t; };

  const S = {};

  /* M1 — Fundamental o‘zaro ta’sirlar: Kulon va Yukava */
  S.forces = {
    title: 'Kulon va Yukava potensiallari',
    params: [
      { k: 'a', l: 'Ta’sir radiusi a, fm', min: .2, max: 10, step: .1, v: 1.4 },
      { k: 'r', l: 'Masofa r, fm', min: .2, max: 10, step: .1, v: 3 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), rs = lin(.1, 10, 300);
      plot(c, [0, 0, w * .6, h], {
        xr: [.1, 10], yr: [1e-6, 10], logy: true, xl: 'r, fm', yl: '|U|·(g²) birliklarda',
        series: [{ pts: rs.map(r => [r, 1 / r]), c: C.blue }, { pts: rs.map(r => [r, Math.exp(-r / P.a) / r]), c: C.rose, w: 2.5 }],
        vl: [{ x: P.r, l: 'r', c: C.amber }, { x: P.a, l: 'a', c: C.green }],
        legend: [{ c: C.blue, l: 'Kulon 1/r' }, { c: C.rose, l: 'Yukava e^(−r/a)/r' }]
      });
      const x0 = w * .63, bw = w * .35, items = [['Kuchli', 1, C.rose, '1'], ['Elektromagnit', 1e-2, C.amber, '10⁻²'], ['Kuchsiz', 1e-6, C.green, '10⁻⁶'], ['Gravitatsion', 1e-38, C.violet, '10⁻³⁸']];
      txt(c, 'Nisbiy kuch (log masshtab)', x0 + bw / 2, 18, C.text);
      items.forEach(([n, s, col, lab], i) => {
        const y = 40 + i * (h - 60) / 4, L = (38 + Math.log10(s)) / 38 * (bw - 10);
        c.fillStyle = col + '55'; c.fillRect(x0, y + 16, Math.max(L, 3), 18); c.strokeStyle = col; c.strokeRect(x0, y + 16, Math.max(L, 3), 18);
        txt(c, `${n}: ${lab}`, x0, y + 10, C.text, 'left', 12);
      });
      const mc2 = 197.3 / P.a;
      return { 'Tashuvchi massasi mc², MeV': fx(mc2, 1), 'U_Y / U_C (r da)': sci(Math.exp(-P.r / P.a), 2), 'r/a': fx(P.r / P.a, 2), 'Taqqoslash': mc2 > 120 && mc2 < 160 ? 'pion massasiga yaqin' : mc2 > 1e4 ? 'W/Z bozon tartibi' : '—' };
    }
  };

  /* M2, A1, A2 — Koordinatalar sistemalari */
  S.coords = {
    title: 'Dekart, silindrik va sferik koordinatalar',
    params: [
      { k: 'mode', l: 'Sistema', type: 'sel', opts: ['Sferik', 'Silindrik'], v: 'Sferik' },
      { k: 'r', l: 'r (yoki ρ), m', min: .2, max: 3, step: .05, v: 2 },
      { k: 'th', l: 'θ (sferik), °', min: 0, max: 180, step: 1, v: 45 },
      { k: 'ph', l: 'φ, °', min: 0, max: 360, step: 1, v: 45 },
      { k: 'z', l: 'z (silindrik), m', min: -2.5, max: 2.5, step: .05, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), sph = P.mode === 'Sferik';
      const ph = P.ph * deg, th = P.th * deg;
      const rho = sph ? P.r * Math.sin(th) : P.r, z = sph ? P.r * Math.cos(th) : P.z;
      const x = rho * Math.cos(ph), y = rho * Math.sin(ph), R = Math.hypot(rho, z);
      const s = Math.min(w / 7, h / 4.6), cx = w * .5, cy = h * .56;
      const pr = (X, Y, Z) => [cx + s * (Y - .55 * X), cy - s * (Z - .32 * X)];
      const ax = [[3, 0, 0, 'x'], [0, 3, 0, 'y'], [0, 0, 3, 'z']];
      ax.forEach(([X, Y, Z, n]) => { const [a, b] = pr(-X * .4, -Y * .4, -Z * .4), [e, f] = pr(X, Y, Z); arrow(c, a, b, e, f, C.axis, 1.5); txt(c, n, e + 10, f, C.axis); });
      const O = pr(0, 0, 0), Pp = pr(x, y, z), Q = pr(x, y, 0);
      poly(c, [O, Q], C.green, 1.5, [5, 4]); poly(c, [Q, Pp], C.green, 1.5, [5, 4]);
      poly(c, [pr(x, 0, 0), Q, pr(0, y, 0)], '#475569', 1, [3, 3]);
      const arcP = lin(0, ph, 40).map(a => pr(.6 * Math.cos(a), .6 * Math.sin(a), 0)); poly(c, arcP, C.amber, 2); txt(c, 'φ', ...pr(.8 * Math.cos(ph / 2), .8 * Math.sin(ph / 2), 0), C.amber);
      if (sph) { const arcT = lin(0, th, 40).map(a => pr(.7 * Math.sin(a) * Math.cos(ph), .7 * Math.sin(a) * Math.sin(ph), .7 * Math.cos(a))); poly(c, arcT, C.rose, 2); txt(c, 'θ', ...pr(.95 * Math.sin(th / 2) * Math.cos(ph), .95 * Math.sin(th / 2) * Math.sin(ph), .95 * Math.cos(th / 2)), C.rose); arrow(c, O[0], O[1], Pp[0], Pp[1], C.cyan, 2.5); }
      else { const ring = lin(0, 2 * Math.PI, 80).map(a => pr(rho * Math.cos(a), rho * Math.sin(a), z)); poly(c, ring, '#334155', 1); arrow(c, O[0], O[1], Pp[0], Pp[1], C.cyan, 2); }
      circ(c, Pp[0], Pp[1], 6, '#fff', C.cyan);
      txt(c, `P(${fx(x, 2)}; ${fx(y, 2)}; ${fx(z, 2)})`, Pp[0] + 10, Pp[1] - 10, '#fff', 'left');
      const thS = R > 0 ? Math.acos(z / R) / deg : 0;
      return { 'x, y, z, m': `${fx(x, 3)}; ${fx(y, 3)}; ${fx(z, 3)}`, 'ρ, φ, z (silindrik)': `${fx(rho, 3)}; ${fx(P.ph, 0)}°; ${fx(z, 3)}`, 'r, θ, φ (sferik)': `${fx(R, 3)}; ${fx(thS, 1)}°; ${fx(P.ph, 0)}°`, 'Lame koeff.': sph ? '1, r, r·sinθ' : '1, ρ, 1' };
    }
  };

  /* M3, A12 — Eng kichik ta’sir prinsipi */
  S.action = {
    title: 'Ta’sir funksionali: haqiqiy va variatsiyalangan yo‘l',
    params: [
      { k: 'eps', l: 'Variatsiya amplitudasi ε, m', min: -.3, max: .3, step: .01, v: .1 },
      { k: 'n', l: 'Garmonika tartibi n', min: 1, max: 4, step: 1, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), m = 1, T = 1, g = g0, N = 400, ts = lin(0, T, N);
      const yTrue = t => -g * t * t / 2, eta = t => P.eps * Math.sin(P.n * Math.PI * t / T);
      const Sof = e => { let s = 0; for (let i = 0; i < N - 1; i++) { const t = (ts[i] + ts[i + 1]) / 2, dt = ts[i + 1] - ts[i]; const yd = -g * t + e * P.n * Math.PI / T * Math.cos(P.n * Math.PI * t / T), y = yTrue(t) + e * Math.sin(P.n * Math.PI * t / T); s += (m * yd * yd / 2 - m * g * y) * dt; } return s; };
      const S0 = Sof(0), S1 = Sof(P.eps);
      plot(c, [0, 0, w * .5, h], { xr: [0, T], yr: [-5.5, .6], xl: 't, s', yl: 'y(t), m', series: [{ pts: ts.map(t => [t, yTrue(t)]), c: C.cyan, w: 2.5 }, { pts: ts.map(t => [t, yTrue(t) + eta(t)]), c: C.rose, dash: [6, 4] }], legend: [{ c: C.cyan, l: 'haqiqiy yo‘l' }, { c: C.rose, l: 'variatsiyalangan' }] });
      const es = lin(-.3, .3, 121), dS = e => m * e * e * P.n * P.n * Math.PI * Math.PI / (4 * T);
      plot(c, [w * .5, 0, w * .5, h], { xr: [-.3, .3], yr: [0, dS(.3) * 1.1], xl: 'ε, m', yl: 'ΔS = S − S₀, J·s', series: [{ pts: es.map(e => [e, dS(e)]), c: C.amber, w: 2.5 }], marks: [{ x: P.eps, y: S1 - S0, c: C.rose }] });
      return { 'S₀ (haqiqiy), J·s': fx(S0, 4), 'S (variatsiya), J·s': fx(S1, 4), 'ΔS (sonli), J·s': fx(S1 - S0, 4), 'ΔS = mε²n²π²/4T': fx(dS(P.eps), 4) };
    }
  };

  /* M4 — Matematik mayatnik (katta amplitudalar, so‘nish) */
  S.pendulum = {
    title: 'Matematik mayatnik: θ(t) va davr',
    anim: true,
    params: [
      { k: 'th0', l: 'Boshlang‘ich burchak θ₀, °', min: 5, max: 175, step: 1, v: 60 },
      { k: 'l', l: 'Uzunlik l, m', min: .2, max: 3, step: .05, v: 1 },
      { k: 'gam', l: 'So‘nish koeffitsiyenti β, s⁻¹', min: 0, max: 1, step: .02, v: 0 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), Tmax = 12;
      const d = cache(cv, P, () => { const pts = [], lin2 = []; let s = [P.th0 * deg, 0]; const w0 = Math.sqrt(g0 / P.l), f = ([a, b]) => [b, -w0 * w0 * Math.sin(a) - 2 * P.gam * b], dt2 = .002; for (let i = 0; i <= Tmax / dt2; i++) { const t = i * dt2; if (i % 5 === 0) { pts.push([t, s[0] / deg]); lin2.push([t, P.th0 * Math.exp(-P.gam * t) * Math.cos(Math.sqrt(Math.max(w0 * w0 - P.gam * P.gam, 0)) * t)]); } s = rk4(f, s, dt2); } return { pts, lin2 }; });
      const t = tick(cv, dt) % Tmax, i = Math.min(d.pts.length - 1, Math.round(t / .01)), th = d.pts[i][1] * deg;
      const px = w * .2, py = 30, L = Math.min(w * .18, h * .7) * (0.55 + .45 * P.l / 3);
      ln(c, px - 40, py, px + 40, py, C.axis, 3);
      const bx = px + L * Math.sin(th), by = py + L * Math.cos(th);
      ln(c, px, py, bx, by, C.text, 2); circ(c, bx, by, 12, '#fff', C.cyan);
      ln(c, px, py, px, py + L + 20, '#334155', 1, [4, 4]);
      txt(c, `θ = ${fx(th / deg, 1)}°`, px, h - 14, C.cyan);
      plot(c, [w * .4, 0, w * .6, h], { xr: [0, Tmax], yr: [-P.th0 * 1.15, P.th0 * 1.15], xl: 't, s', yl: 'θ, °', series: [{ pts: d.lin2, c: '#64748b', dash: [5, 4], w: 1.5 }, { pts: d.pts, c: C.cyan, w: 2.2 }], vl: [{ x: t, c: C.amber }], legend: [{ c: C.cyan, l: 'aniq (RK4)' }, { c: '#64748b', l: 'kichik burchak taqribi' }] });
      const T0 = 2 * Math.PI * Math.sqrt(P.l / g0), Tex = T0 / agm(1, Math.cos(P.th0 * deg / 2));
      return { 'T₀ = 2π√(l/g), s': fx(T0, 3), 'T (aniq, β=0), s': fx(Tex, 3), 'T/T₀': fx(Tex / T0, 4), 'Asllik Q': P.gam > 0 ? fx(Math.sqrt(g0 / P.l) / (2 * P.gam), 1) : '∞' };
    }
  };

  /* M5, A14 — Simmetriya va saqlanish qonunlari (Nyoter) */
  S.noether = {
    title: 'Simmetriya va saqlanuvchi kattaliklar',
    params: [
      { k: 'pot', l: 'Potensial maydon', type: 'sel', opts: ['Markaziy (−1/r)', 'Bir jinsli maydon (U = y)', 'Anizotrop ossilyator', 'Erkin zarra'], v: 'Markaziy (−1/r)' },
      { k: 'v0', l: 'Boshlang‘ich tezlik v₀', min: .3, max: 1.4, step: .02, v: 1.1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), kind = P.pot[0];
      const U = { M: (x, y) => -1 / Math.hypot(x, y), B: (x, y) => y, A: (x, y) => (x * x + 2.25 * y * y) / 2, E: () => 0 }[kind];
      const F = { M: (x, y) => { const r3 = Math.hypot(x, y) ** 3; return [-x / r3, -y / r3]; }, B: () => [0, -1], A: (x, y) => [-x, -2.25 * y], E: () => [0, 0] }[kind];
      let [x, y, vx, vy] = { M: [1, 0, 0, P.v0], B: [-2, 0, P.v0 * .8, P.v0 * 1.6], A: [1, 0, .3 * P.v0, P.v0], E: [-2, -1, P.v0, .5 * P.v0] }[kind];
      const dt = .002, Tm = { M: 30, B: 3.2 * P.v0, A: 25, E: 4 / P.v0 }[kind], tr = [], qs = [];
      let [fx0, fy0] = F(x, y); vx += dt / 2 * fx0; vy += dt / 2 * fy0;
      for (let i = 0; i * dt < Tm; i++) {
        x += dt * vx; y += dt * vy; const [ax, ay] = F(x, y); vx += dt * ax; vy += dt * ay;
        if (i % 20 === 0) { const ux = vx - dt / 2 * ax, uy = vy - dt / 2 * ay; tr.push([x, y]); qs.push([i * dt, (ux * ux + uy * uy) / 2 + U(x, y), ux, uy, x * uy - y * ux]); }
        if (Math.hypot(x, y) > 40) break;
      }
      const ext = Math.max(2, ...tr.map(p => Math.max(Math.abs(p[0]), Math.abs(p[1])))) * 1.1;
      plot(c, [0, 0, w * .45, h], { xr: [-ext, ext], yr: [-ext, ext], xl: 'x', yl: 'y — trayektoriya', series: [{ pts: tr, c: C.cyan, w: 2 }], marks: kind === 'M' ? [{ x: 0, y: 0, c: C.amber, r: 6 }] : [] });
      const names = ['E', 'p_x', 'p_y', 'L_z'], cols = [C.amber, C.rose, C.green, C.violet];
      const series = names.map((n, j) => ({ pts: qs.map(q => [q[0], q[j + 1]]), c: cols[j], w: 2 }));
      const all = qs.flatMap(q => q.slice(1)); const lo = Math.min(...all), hi = Math.max(...all), pad = (hi - lo) * .1 + .1;
      plot(c, [w * .46, 0, w * .54, h], { xr: [0, qs[qs.length - 1][0]], yr: [lo - pad, hi + pad], xl: 't', yl: 'kattaliklar', series, legend: names.map((n, j) => ({ c: cols[j], l: n })) });
      const cons = names.filter((n, j) => { const v = qs.map(q => q[j + 1]); return Math.max(...v) - Math.min(...v) < 1e-3 * (1 + Math.abs(v[0])); });
      const sym = { M: 'burilish (izotropiya), vaqt', B: 'x bo‘ylab siljish, vaqt', A: 'faqat vaqt', E: 'barcha siljishlar, burilish, vaqt' }[kind];
      return { 'Simmetriya': sym, 'Saqlanadi': cons.join(', ') || '—', 'Saqlanmaydi': names.filter(n => !cons.includes(n)).join(', ') || '—' };
    }
  };

  /* M6, A15 — Erkin, so‘nuvchi va majburiy tebranishlar */
  S.oscill = {
    title: 'Majburiy tebranishlar va rezonans',
    params: [
      { k: 'm', l: 'Massa m, kg', min: .1, max: 2, step: .05, v: .5 },
      { k: 'k', l: 'Bikrlik k, N/m', min: 10, max: 500, step: 5, v: 200 },
      { k: 'b', l: 'So‘nish β, s⁻¹', min: .1, max: 6, step: .1, v: 1 },
      { k: 'F', l: 'Kuch amplitudasi F₀, N', min: .5, max: 5, step: .1, v: 2 },
      { k: 'g', l: 'Majburlovchi chastota γ, rad/s', min: 1, max: 40, step: .1, v: 20 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), w0 = Math.sqrt(P.k / P.m);
      const amp = g => P.F / P.m / Math.sqrt((w0 * w0 - g * g) ** 2 + 4 * P.b * P.b * g * g);
      const gs = lin(0, 40, 400), bmax = Math.max(...gs.map(amp));
      plot(c, [0, 0, w * .5, h], { xr: [0, 40], yr: [0, bmax * 1.15], xl: 'γ, rad/s', yl: 'Amplituda b, m', series: [{ pts: gs.map(g => [g, amp(g)]), c: C.cyan, w: 2.5 }], vl: [{ x: w0, l: 'ω₀', c: C.green }], marks: [{ x: P.g, y: amp(P.g), c: C.amber }] });
      let s = [0, 0]; const f = (t) => ([x, v]) => [v, P.F / P.m * Math.cos(P.g * t) - 2 * P.b * v - w0 * w0 * x], pts = [], dt = .002;
      for (let i = 0; i <= 5000; i++) { const t = i * dt; if (i % 4 === 0) pts.push([t, s[0]]); s = rk4(f(t + dt / 2), s, dt); }
      const ya = Math.max(...pts.map(p => Math.abs(p[1]))) * 1.15 || 1;
      plot(c, [w * .5, 0, w * .5, h], { xr: [0, 10], yr: [-ya, ya], xl: 't, s', yl: 'x(t), m (tinchlikdan boshlanadi)', series: [{ pts, c: C.rose, w: 1.6 }], hl: [{ y: amp(P.g), c: '#64748b' }, { y: -amp(P.g), c: '#64748b' }] });
      const del = Math.atan2(2 * P.b * P.g, w0 * w0 - P.g * P.g) / deg, gr = w0 * w0 > 2 * P.b * P.b ? Math.sqrt(w0 * w0 - 2 * P.b * P.b) : NaN;
      return { 'ω₀, rad/s': fx(w0, 2), 'γ_rez, rad/s': fx(gr, 2), 'b(γ), m': sci(amp(P.g), 3), 'Faza δ, °': fx(del, 1), 'Asllik Q': fx(w0 / (2 * P.b), 1), 'Statik siljish F₀/k, m': sci(P.F / P.k, 3) };
    }
  };

  /* M7, A3, A6 — Kepler masalasi va effektiv potensial */
  S.orbit = {
    title: 'Markaziy maydonda orbita (GM = 1, r₀ = 1)',
    params: [
      { k: 'k', l: 'Tezlik / aylana tezligi', min: .3, max: 1.6, step: .01, v: 1.2 },
      { k: 'a', l: 'Tezlik yo‘nalishi (urinmadan), °', min: -60, max: 60, step: 1, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), vr = P.k * Math.sin(P.a * deg), vt = P.k * Math.cos(P.a * deg);
      const E = P.k * P.k / 2 - 1, L = vt, p = L * L, e = Math.sqrt(Math.max(0, 1 + 2 * E * L * L));
      const ph0 = e < 1e-6 ? 0 : -Math.sign(vr || 0) * Math.acos(Math.max(-1, Math.min(1, (p - 1) / e)));
      const pts = []; for (let f = -Math.PI; f <= Math.PI + 1e-9; f += Math.PI / 360) { const den = 1 + e * Math.cos(f - ph0); if (den > .02) { const r = p / den; if (r < 12) pts.push([r * Math.cos(f), r * Math.sin(f)]); else pts.push([NaN, NaN]); } else pts.push([NaN, NaN]); }
      const ext = E < 0 ? Math.min(Math.max(1.3, p / (1 - e) * 1.1), 12) : 4;
      const s = Math.min(w * .5, h) / (2.2 * ext), cx = w * .27, cy = h / 2;
      c.save(); c.beginPath(); c.rect(0, 0, w * .54, h); c.clip();
      poly(c, lin(0, 2 * Math.PI, 90).map(a => [cx + s * Math.cos(a), cy - s * Math.sin(a)]), '#334155', 1, [3, 4]);
      let seg = []; pts.forEach(([x, y]) => { if (isNaN(x)) { if (seg.length) poly(c, seg, C.cyan, 2.2); seg = []; } else seg.push([cx + s * x, cy - s * y]); }); if (seg.length) poly(c, seg, C.cyan, 2.2);
      circ(c, cx, cy, 9, null, C.amber); circ(c, cx + s, cy, 5, null, '#fff');
      arrow(c, cx + s, cy, cx + s + 40 * vr, cy - 40 * vt, C.rose, 2);
      c.restore(); txt(c, 'orbita', 12, 18, C.text, 'left');
      const rs = lin(.2, 6, 300), Ueff = r => -1 / r + L * L / (2 * r * r);
      plot(c, [w * .54, 0, w * .46, h], { xr: [0, 6], yr: [-Math.max(1.2, 1.3 / (L * L || 1)), .8], xl: 'r', yl: 'U_eff(r) va E', series: [{ pts: rs.map(r => [r, Ueff(r)]), c: C.violet, w: 2.5 }, { pts: rs.map(r => [r, -1 / r]), c: '#64748b', dash: [4, 4], w: 1.4 }], hl: [{ y: E, l: 'E', c: C.amber }], marks: [{ x: 1, y: Ueff(1), c: '#fff', r: 4 }] });
      const type = e < 1e-3 ? 'aylana' : e < 1 ? 'ellips' : Math.abs(e - 1) < 2e-3 ? 'parabola' : 'giperbola';
      const a = E < 0 ? -1 / (2 * E) : NaN;
      return { 'Energiya E': fx(E, 3), 'Impuls momenti M': fx(L, 3), 'Eksentrisitet e': fx(e, 3), 'Orbita turi': type, 'Katta yarim o‘q a': fx(a, 3), 'Davr T = 2πa^{3/2}': E < 0 ? fx(2 * Math.PI * a ** 1.5, 3) : '—' };
    }
  };

  /* M8, A7, A9 — Rezerford sochilishi */
  S.scatter = {
    title: 'Kulon maydonida sochilish (Rezerford)',
    params: [
      { k: 'E', l: 'Kinetik energiya E, MeV', min: 1, max: 20, step: .1, v: 5 },
      { k: 'Z', l: 'Yadro zaryadi Z (α-zarra)', min: 6, max: 92, step: 1, v: 79 },
      { k: 'b', l: 'Nishon parametri b, fm', min: 2, max: 120, step: .25, v: 22.75 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), al = 2 * P.Z * 1.44, d0 = al / P.E, Hs = Math.max(2.2 * d0, 1.3 * P.b, 60);
      const traj = b => { let x = -3 * Hs, y = b; const v0 = Math.sqrt(2 * P.E); let vx = v0, vy = 0; const out = []; for (let i = 0; i < 20000; i++) { const r = Math.hypot(x, y), dt = .004 * Math.max(r, d0 * .3) / v0; const a = al / (r * r * r); vx += a * x * dt; vy += a * y * dt; x += vx * dt; y += vy * dt; if (i % 3 === 0) out.push([x, y]); if (r > 3.2 * Hs && x > -Hs) break; } return out; };
      const W2 = w * .55, s = Math.min(W2, h) / (2.2 * Hs), cx = W2 * .55, cy = h / 2;
      c.save(); c.beginPath(); c.rect(0, 0, W2, h); c.clip();
      for (let i = 1; i <= 6; i++) { const b = i * Hs / 6.5; poly(c, traj(b).map(([x, y]) => [cx + s * x, cy - s * y]), '#33415599', 1.2); poly(c, traj(-b).map(([x, y]) => [cx + s * x, cy - s * y]), '#33415599', 1.2); }
      poly(c, traj(P.b).map(([x, y]) => [cx + s * x, cy - s * y]), C.cyan, 2.5);
      circ(c, cx, cy, Math.max(3, s * 7), null, C.amber); circ(c, cx, cy, s * d0, '#fbbf2455', null, 1);
      ln(c, 0, cy - s * P.b, cx, cy - s * P.b, C.rose, 1, [4, 4]); txt(c, 'b', 14, cy - s * P.b - 5, C.rose);
      c.restore(); txt(c, `masshtab: ${fx(Hs, 0)} fm`, 10, h - 10, C.axis, 'left', 11);
      const chi = 2 * Math.atan(al / (2 * P.E * P.b)), ds = th => (al / (4 * P.E)) ** 2 / Math.sin(th / 2) ** 4;
      const ths = lin(5 * deg, Math.PI, 300);
      plot(c, [W2, 0, w - W2, h], { xr: [5, 180], yr: [1, 1e6], logy: true, xl: 'χ, °', yl: 'dσ/dΩ, fm²/sr', series: [{ pts: ths.map(t => [t / deg, ds(t)]), c: C.violet, w: 2.5 }], marks: [{ x: chi / deg, y: ds(chi), c: C.cyan }] });
      return { 'α = Z₁Z₂e²/4πε₀, MeV·fm': fx(al, 1), 'd₀ = α/E, fm': fx(d0, 2), 'Sochilish burchagi χ, °': fx(chi / deg, 2), 'dσ/dΩ, fm²/sr': sci(ds(chi), 3), 'dσ/dΩ, b/sr': sci(ds(chi) / 100, 3), 'r_min, fm': fx(al / (2 * P.E) * (1 + 1 / Math.sin(chi / 2)), 2) };
    }
  };

  /* M9 — Inersiya momenti, Shteyner teoremasi, dumalash */
  S.inertia = {
    title: 'Inersiya momenti va qiya tekislikda dumalash',
    params: [
      { k: 'sh', l: 'Jism shakli', type: 'sel', opts: ['Yaxlit shar', 'Disk / silindr', 'Halqa', 'Kovak shar', 'Sterjen (uzunligi 2R)'], v: 'Yaxlit shar' },
      { k: 'M', l: 'Massa M, kg', min: .5, max: 10, step: .5, v: 2 },
      { k: 'R', l: 'Radius R, m', min: .05, max: 1, step: .01, v: .2 },
      { k: 'd', l: 'O‘qning siljishi d, m', min: 0, max: 1, step: .01, v: 0 },
      { k: 'al', l: 'Qiyalik α, °', min: 5, max: 60, step: 1, v: 30 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), K = { 'Yaxlit shar': .4, 'Disk / silindr': .5, 'Halqa': 1, 'Kovak shar': 2 / 3, 'Sterjen (uzunligi 2R)': 1 / 3 };
      const k = K[P.sh], Ic = k * P.M * P.R * P.R, I = Ic + P.M * P.d * P.d, rod = P.sh.startsWith('Sterjen');
      const cx = w * .22, cy = h * .45, s = Math.min(w * .15, h * .3) / Math.max(P.R, P.d + .05, .3) * .9;
      if (rod) { c.fillStyle = '#22d3ee44'; c.fillRect(cx - s * P.R, cy - 6, 2 * s * P.R, 12); c.strokeStyle = C.cyan; c.strokeRect(cx - s * P.R, cy - 6, 2 * s * P.R, 12); }
      else { circ(c, cx, cy, s * P.R, C.cyan, P.sh === 'Halqa' || P.sh === 'Kovak shar' ? null : '#22d3ee33', P.sh === 'Halqa' || P.sh === 'Kovak shar' ? 4 : 2); }
      circ(c, cx, cy, 3, null, '#fff');
      ln(c, cx + s * P.d, cy - h * .35, cx + s * P.d, cy + h * .35, C.amber, 2, [7, 4]); txt(c, 'aylanish o‘qi', cx + s * P.d + 6, cy - h * .3, C.amber, 'left', 11);
      if (P.d > 0) { arrow(c, cx, cy + h * .3, cx + s * P.d, cy + h * .3, C.rose, 1.5); txt(c, 'd', cx + s * P.d / 2, cy + h * .3 - 6, C.rose); }
      txt(c, `I_c = ${fx(k, 3)}·MR²`, cx, h - 12, C.text);
      const sa = g0 * Math.sin(P.al * deg), shapes = [['Shar', .4], ['Disk', .5], ['Kovak shar', 2 / 3], ['Halqa', 1], ['Sirpanish', 0]];
      const x0 = w * .48, bw = w * .48, amax = sa;
      txt(c, `a = g·sinα/(1 + I_c/MR²), α = ${P.al}°`, x0, 20, C.text, 'left', 12);
      shapes.forEach(([n, kk], i) => { const a = sa / (1 + kk), y = 40 + i * (h - 60) / 5, L = a / amax * (bw - 170), cur = !rod && Math.abs(kk - k) < 1e-6; c.fillStyle = cur ? '#22d3ee88' : '#64748b55'; c.fillRect(x0 + 90, y, L, 20); txt(c, n, x0 + 84, y + 15, cur ? C.cyan : C.text, 'right', 12); txt(c, `${fx(a, 2)} m/s²`, x0 + 96 + L, y + 15, C.text, 'left', 11); });
      const a = rod ? NaN : sa / (1 + k);
      return { 'I_c, kg·m²': sci(Ic, 3), 'I (Shteyner), kg·m²': sci(I, 3), 'I_c/MR²': fx(k, 3), 'a (dumalash), m/s²': rod ? '—' : fx(a, 3), '1 m yo‘l vaqti, s': rod ? '—' : fx(Math.sqrt(2 / a), 3) };
    }
  };

  /* M10, A11 — Fazaviy portret */
  S.phase = {
    title: 'Fazaviy fazo: ossilyator va mayatnik',
    params: [
      { k: 'mode', l: 'Sistema', type: 'sel', opts: ['Garmonik ossilyator', 'Matematik mayatnik'], v: 'Garmonik ossilyator' },
      { k: 'E', l: 'Energiya E, J (m = 1 kg)', min: .5, max: 30, step: .1, v: 8 },
      { k: 'w', l: 'Ossilyator chastotasi ω, rad/s', min: .5, max: 4, step: .1, v: 2 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), osc = P.mode[0] === 'G';
      if (osc) {
        const qm = Math.sqrt(2 * P.E) / P.w, pm = Math.sqrt(2 * P.E), Q = Math.max(qm, 3) * 1.15, Pm = Math.max(pm, 6) * 1.15;
        const ell = (E) => lin(0, 2 * Math.PI, 160).map(a => [Math.sqrt(2 * E) / P.w * Math.cos(a), Math.sqrt(2 * E) * Math.sin(a)]);
        plot(c, [0, 0, w, h], { xr: [-Q, Q], yr: [-Pm, Pm], xl: 'q, m', yl: 'p, kg·m/s', series: [2, 6, 12, 20, 28].map(E => ({ pts: ell(E), c: '#334155', w: 1 })).concat([{ pts: ell(P.E), c: C.cyan, w: 2.8 }]) });
        return { 'q_max, m': fx(qm, 3), 'p_max, kg·m/s': fx(pm, 3), 'Fazaviy yuza J = 2πE/ω, J·s': fx(2 * Math.PI * P.E / P.w, 3), 'Davr T, s': fx(2 * Math.PI / P.w, 3), 'Holat': 'tebranish (davr E ga bog‘liq emas)' };
      }
      const g = g0, Es = 2 * g, U = q => g * (1 - Math.cos(q)), qs = lin(-1.5 * Math.PI, 1.5 * Math.PI, 600);
      const br = (E, sg) => qs.map(q => [q, E - U(q) >= 0 ? sg * Math.sqrt(2 * (E - U(q))) : NaN]);
      const fam = [3, 8, 14, Es, 24, 30].flatMap(E => [{ pts: br(E, 1), c: Math.abs(E - Es) < 1e-9 ? C.rose : '#334155', w: Math.abs(E - Es) < 1e-9 ? 1.6 : 1, dash: Math.abs(E - Es) < 1e-9 ? [6, 4] : [] }, { pts: br(E, -1), c: Math.abs(E - Es) < 1e-9 ? C.rose : '#334155', w: Math.abs(E - Es) < 1e-9 ? 1.6 : 1, dash: Math.abs(E - Es) < 1e-9 ? [6, 4] : [] }]);
      plot(c, [0, 0, w, h], { xr: [-1.5 * Math.PI, 1.5 * Math.PI], yr: [-9.5, 9.5], xl: 'θ, rad', yl: 'p_θ (ml² = 1)', series: fam.concat([{ pts: br(P.E, 1), c: C.cyan, w: 2.8 }, { pts: br(P.E, -1), c: C.cyan, w: 2.8 }]), vl: [{ x: Math.PI, c: '#475569' }, { x: -Math.PI, c: '#475569' }] });
      let T; const w0 = Math.sqrt(g);
      if (P.E < Es) { const qm = Math.acos(1 - P.E / g); T = 2 * Math.PI / w0 / agm(1, Math.cos(qm / 2)); }
      else { let sum = 0; const N = 2000; for (let i = 0; i < N; i++) { const q = (i + .5) * 2 * Math.PI / N; sum += 2 * Math.PI / N / Math.sqrt(Math.max(2 * (P.E - U(q)), 1e-9)); } T = sum; }
      return { 'Separatrisa energiyasi 2mgl, J': fx(Es, 2), 'Holat': P.E < Es ? 'tebranish (librasiya)' : Math.abs(P.E - Es) < .05 ? 'separatrisa yaqinida' : 'aylanish (rotatsiya)', 'θ_max, °': P.E < Es ? fx(Math.acos(1 - P.E / g) / deg, 1) : '—', 'Davr T, s': fx(T, 3) };
    }
  };

  /* M11, A8 — Elastik to‘qnashuv: impulslar diagrammasi */
  S.collision = {
    title: 'Elastik to‘qnashuv: impulslar diagrammasi',
    params: [
      { k: 'mr', l: 'Massalar nisbati m₂/m₁', min: .1, max: 12, step: .05, v: 3 },
      { k: 'chi', l: 'MM sistemadagi burchak χ, °', min: 0, max: 180, step: 1, v: 90 },
      { k: 'v', l: 'Tezlik v, m/s (m₁ = 1 kg)', min: 1, max: 10, step: .1, v: 4 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), m1 = 1, m2 = P.mr, M = m1 + m2, p = m1 * P.v, mu = m1 * m2 / M, p0 = mu * P.v, ch = P.chi * deg;
      const W2 = w * .55, s = Math.min((W2 - 40) / (p * 1.1 + p0 * .2), (h - 60) / (2.2 * p0)), Ax = 20, Ay = h * .62;
      const Ox = Ax + s * p * m1 / M, Bx = Ax + s * p, Cx = Ox + s * p0 * Math.cos(ch), Cy = Ay - s * p0 * Math.sin(ch);
      circ(c, Ox, Ay, s * p0, '#475569', null, 1.2);
      arrow(c, Ax, Ay, Bx, Ay, C.text, 2); txt(c, 'p₁ = m₁v', (Ax + Bx) / 2, Ay + 18, C.text);
      arrow(c, Ax, Ay, Cx, Cy, C.cyan, 2.5); arrow(c, Cx, Cy, Bx, Ay, C.rose, 2.5); ln(c, Ox, Ay, Cx, Cy, C.amber, 1.2, [4, 3]);
      txt(c, 'p₁′', (Ax + Cx) / 2 - 10, (Ay + Cy) / 2 - 6, C.cyan); txt(c, 'p₂′', (Bx + Cx) / 2 + 12, (Ay + Cy) / 2 - 6, C.rose); txt(c, 'χ', Ox + 18, Ay - 6, C.amber);
      circ(c, Ax, Ay, 3, null, '#fff'); circ(c, Ox, Ay, 3, null, C.amber); circ(c, Bx, Ay, 3, null, '#fff'); txt(c, 'A', Ax - 2, Ay + 32, C.axis); txt(c, 'O', Ox, Ay + 32, C.amber); txt(c, 'B', Bx, Ay + 32, C.axis);
      const t1 = ch2 => Math.atan2(m2 * Math.sin(ch2), m1 + m2 * Math.cos(ch2)) / deg, t2 = ch2 => (Math.PI - ch2) / 2 / deg;
      const xs = lin(0, Math.PI, 181);
      plot(c, [W2, 0, w - W2, h], { xr: [0, 180], yr: [0, 180], xl: 'χ, °', yl: 'θ₁, θ₂ (L sistema), °', series: [{ pts: xs.map(x => [x / deg, t1(x)]), c: C.cyan, w: 2.3 }, { pts: xs.map(x => [x / deg, t2(x)]), c: C.rose, w: 2.3 }], marks: [{ x: P.chi, y: t1(ch), c: C.cyan }, { x: P.chi, y: t2(ch), c: C.rose }], legend: [{ c: C.cyan, l: 'θ₁ (uchib keluvchi)' }, { c: C.rose, l: 'θ₂ (tepki)' }] });
      const frac = 4 * m1 * m2 / (M * M) * Math.sin(ch / 2) ** 2, p1 = Math.hypot(Cx - Ax, Cy - Ay) / s;
      return { 'θ₁, °': fx(t1(ch), 2), 'θ₂, °': fx(t2(ch), 2), 'θ₁ + θ₂, °': fx(t1(ch) + t2(ch), 2), 'v₁′, m/s': fx(p1 / m1, 3), 'Uzatilgan energiya ulushi': fx(frac, 4), 'θ₁ max': m1 > m2 ? fx(Math.asin(m2 / m1) / deg, 2) + '°' : '180° (cheklanmagan)' };
    }
  };

  /* M12 — Minkovskiy diagrammasi */
  S.lorentz = {
    title: 'Lorens almashtirishi: Minkovskiy diagrammasi',
    params: [
      { k: 'b', l: 'β = V/c', min: -.95, max: .95, step: .01, v: .6 },
      { k: 'x', l: 'Voqea x, (yorug‘lik-birlik)', min: -3, max: 3, step: .05, v: 1 },
      { k: 't', l: 'Voqea ct', min: -3, max: 3, step: .05, v: 2 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), W2 = Math.min(w * .58, h * 1.05), s = Math.min(W2, h) / 8, cx = W2 / 2 + 4, cy = h / 2;
      const T = (x, t) => [cx + s * x, cy - s * t], b = P.b, g = 1 / Math.sqrt(1 - b * b);
      c.save(); c.beginPath(); c.rect(0, 0, W2 + 8, h); c.clip();
      for (let i = -4; i <= 4; i++) { ln(c, ...T(i, -4), ...T(i, 4), '#1e2c44', 1); ln(c, ...T(-4, i), ...T(4, i), '#1e2c44', 1); }
      for (let i = -6; i <= 6; i++) { if (!i) continue; const p1 = [(-8) , 0], A1 = [g * (i * 1 + b * -8), g * (-8 + b * i)], A2 = [g * (i + b * 8), g * (8 + b * i)]; ln(c, ...T(...A1), ...T(...A2), '#a78bfa22', 1); const B1 = [g * (-8 + b * i), g * (i + b * -8)], B2 = [g * (8 + b * i), g * (i + b * 8)]; ln(c, ...T(...B1), ...T(...B2), '#a78bfa22', 1); }
      ln(c, ...T(-4, -4), ...T(4, 4), C.amber, 1.5, [6, 4]); ln(c, ...T(-4, 4), ...T(4, -4), C.amber, 1.5, [6, 4]);
      arrow(c, ...T(-3.9, 0), ...T(3.9, 0), C.axis, 1.5); arrow(c, ...T(0, -3.9), ...T(0, 3.9), C.axis, 1.5); txt(c, 'x', ...T(3.75, -.3), C.axis); txt(c, 'ct', ...T(.3, 3.75), C.axis);
      const L = 3.6; arrow(c, ...T(-L, -L * b), ...T(L, L * b), C.violet, 2); arrow(c, ...T(-L * b, -L), ...T(L * b, L), C.violet, 2); txt(c, 'x′', ...T(L + .15, L * b + .25), C.violet); txt(c, 'ct′', ...T(L * b + .3, L + .1), C.violet);
      const xp = g * (P.x - b * P.t), tp = g * (P.t - b * P.x);
      const Px = [g * (xp + b * 0), g * (0 + b * xp)], Pt = [g * (0 + b * tp), g * (tp + b * 0)];
      ln(c, ...T(P.x, P.t), ...T(...Px), C.green, 1.2, [3, 3]); ln(c, ...T(P.x, P.t), ...T(...Pt), C.green, 1.2, [3, 3]);
      circ(c, ...T(P.x, P.t), 6, '#fff', C.green); c.restore();
      const bs = lin(0, .99, 200);
      plot(c, [W2 + 10, 0, w - W2 - 10, h], { xr: [0, 1], yr: [1, 8], xl: 'β', yl: 'γ = 1/√(1−β²)', series: [{ pts: bs.map(x => [x, 1 / Math.sqrt(1 - x * x)]), c: C.cyan, w: 2.3 }], marks: [{ x: Math.abs(b), y: g, c: C.amber }] });
      const s2 = P.t * P.t - P.x * P.x;
      return { 'γ': fx(g, 4), 'x′': fx(xp, 3), 'ct′': fx(tp, 3), 's² = c²t² − x²': fx(s2, 3), 's′² (tekshiruv)': fx(tp * tp - xp * xp, 3), 'Interval turi': Math.abs(s2) < 1e-6 ? 'yorug‘liksimon' : s2 > 0 ? 'vaqtsimon' : 'fazosimon' };
    }
  };

  /* M13 — Parametrik rezonans (Matye tenglamasi) */
  S.param = {
    title: 'Parametrik rezonans: q̈ + ω₀²(1 + h·cos γt)q = 0',
    params: [
      { k: 'h', l: 'Modulyatsiya chuqurligi h', min: 0, max: .5, step: .005, v: .1 },
      { k: 'r', l: 'γ/ω₀ (ω₀ = 10 rad/s)', min: 1.5, max: 2.5, step: .005, v: 2 },
      { k: 'b', l: 'So‘nish β, s⁻¹', min: 0, max: .6, step: .01, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), w0 = 10, gm = P.r * w0, T = 20, dt = .002;
      let s = [.01, 0]; const pts = [], f = t => ([q, v]) => [v, -w0 * w0 * (1 + P.h * Math.cos(gm * t)) * q - 2 * P.b * v];
      let a1 = 0, a2 = 0;
      for (let i = 0; i <= T / dt; i++) { const t = i * dt; if (i % 5 === 0) pts.push([t, s[0]]); if (t < 4) a1 = Math.max(a1, Math.hypot(s[0], s[1] / w0)); if (t > T - 4) a2 = Math.max(a2, Math.hypot(s[0], s[1] / w0)); s = rk4(f(t + dt / 2), s, dt); }
      const mx = Math.max(...pts.map(p => Math.abs(p[1]))) * 1.1;
      plot(c, [0, 0, w * .55, h], { xr: [0, T], yr: [-mx, mx], xl: 't, s', yl: 'q(t)', series: [{ pts, c: C.cyan, w: 1.3 }] });
      const hs = lin(0, .5, 60);
      plot(c, [w * .55, 0, w * .45, h], { xr: [1.5, 2.5], yr: [0, .5], xl: 'γ/ω₀', yl: 'h — beqarorlik sohasi', fill: [{ c: '#fb718533', pts: [[2, 0], ...hs.map(x => [2 + x / 2, x]), ...hs.slice().reverse().map(x => [2 - x / 2, x])] }], series: [{ pts: hs.map(x => [2 + x / 2, x]), c: C.rose }, { pts: hs.map(x => [2 - x / 2, x]), c: C.rose }], hl: P.b > 0 ? [{ y: 4 * P.b / w0, l: 'h_kr = 4β/ω₀', c: C.amber }] : [], marks: [{ x: P.r, y: P.h, c: '#fff' }] });
      const eps = gm - 2 * w0, sth = .5 * Math.sqrt(Math.max(0, (P.h * w0 / 2) ** 2 - eps * eps));
      const meas = Math.log(a2 / a1) / (T - 4);
      return { 'Soha: γ ∈': `${fx(2 * w0 - P.h * w0 / 2, 2)} … ${fx(2 * w0 + P.h * w0 / 2, 2)} rad/s`, 's (nazariya), s⁻¹': fx(sth, 3), 's − β, s⁻¹': fx(sth - P.b, 3), 'O‘sish (model), s⁻¹': fx(meas, 3), 'h_kr = 4β/ω₀': fx(4 * P.b / w0, 3), 'Holat': sth > P.b + 1e-9 ? 'REZONANS (beqaror)' : 'turg‘un' };
    }
  };

  /* M14 — Bernulli tenglamasi: Venturi naychasi */
  S.bernoulli = {
    title: 'Bernulli tenglamasi: Venturi naychasi (suv)',
    params: [
      { k: 'd1', l: 'Keng qism diametri d₁, sm', min: 2, max: 10, step: .1, v: 4 },
      { k: 'd2', l: 'Tor qism diametri d₂, sm', min: .5, max: 10, step: .1, v: 2 },
      { k: 'v1', l: 'Keng qismdagi tezlik v₁, m/s', min: .1, max: 3, step: .05, v: 1 },
      { k: 'h', l: 'Tor qism balandligi Δh, m', min: 0, max: 2, step: .05, v: 0 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), rho = 1000, eta = 1e-3, d2 = Math.min(P.d2, P.d1);
      const v2 = P.v1 * (P.d1 / d2) ** 2, dp = rho * (v2 * v2 - P.v1 * P.v1) / 2 + rho * g0 * P.h, p1 = 200e3, p2 = p1 - dp;
      const W2 = w * .6, y0 = h * .72, sc = h * .16 / Math.max(P.d1, 4), xs = lin(20, W2 - 20, 200);
      const dia = x => { const u = (x - 20) / (W2 - 40); const k = u < .3 ? 0 : u < .45 ? (u - .3) / .15 : u < .55 ? 1 : u < .7 ? 1 - (u - .55) / .15 : 0; const sm = .5 - .5 * Math.cos(Math.PI * k); return P.d1 + (d2 - P.d1) * sm; };
      const lift = x => { const u = (x - 20) / (W2 - 40); const k = u < .3 ? 0 : u < .45 ? (u - .3) / .15 : u < .55 ? 1 : u < .7 ? 1 - (u - .55) / .15 : 0; return (.5 - .5 * Math.cos(Math.PI * k)) * P.h * 18; };
      c.fillStyle = '#22d3ee22'; c.beginPath(); xs.forEach((x, i) => { const y = y0 - lift(x) - dia(x) * sc / 2; i ? c.lineTo(x, y) : c.moveTo(x, y); }); xs.slice().reverse().forEach(x => c.lineTo(x, y0 - lift(x) + dia(x) * sc / 2)); c.closePath(); c.fill();
      poly(c, xs.map(x => [x, y0 - lift(x) - dia(x) * sc / 2]), C.cyan, 2); poly(c, xs.map(x => [x, y0 - lift(x) + dia(x) * sc / 2]), C.cyan, 2);
      const ph = 34 / Math.max(p1, 1) * 1000 * .0045;
      [[20 + (W2 - 40) * .15, p1, P.v1], [20 + (W2 - 40) * .5, p2, v2]].forEach(([x, p, v], i) => { const top = y0 - lift(x) - dia(x) * sc / 2, col = Math.max(4, Math.min(top - 40, (p / 1000 - 150) * (top - 60) / 55)); c.fillStyle = '#60a5fa66'; c.fillRect(x - 5, top - col, 10, col); c.strokeStyle = C.blue; c.strokeRect(x - 7, 34, 14, top - 34); txt(c, `p${i ? '₂' : '₁'} = ${fx(p / 1000, 1)} kPa`, x, 26, C.blue); for (let k = -1; k <= 1; k++) arrow(c, x - 20, y0 - lift(x) + k * dia(x) * sc / 4, x - 20 + Math.min(60, v * 9), y0 - lift(x) + k * dia(x) * sc / 4, C.amber, 1.5); txt(c, `v = ${fx(v, 2)} m/s`, x, y0 - lift(x) + dia(x) * sc / 2 + 18, C.amber); });
      const prof = xs.map(x => { const v = P.v1 * (P.d1 / dia(x)) ** 2; return [(x - 20) / (W2 - 40), (p1 - rho * (v * v - P.v1 * P.v1) / 2 - rho * g0 * lift(x) / 18) / 1000]; });
      const lo = Math.min(...prof.map(p => p[1]));
      plot(c, [W2, 0, w - W2, h], { xr: [0, 1], yr: [Math.min(lo - 5, 190), 205], xl: 'naycha bo‘ylab (nisbiy)', yl: 'p, kPa', series: [{ pts: prof, c: C.blue, w: 2.3 }] });
      const Re1 = rho * P.v1 * P.d1 / 100 / eta;
      return { 'v₂ = v₁(d₁/d₂)², m/s': fx(v2, 3), 'Δp = p₁ − p₂, Pa': fx(dp, 0), 'Hajmiy sarf Q, l/s': fx(Math.PI * (P.d1 / 100) ** 2 / 4 * P.v1 * 1000, 3), 'Re (keng qism)': sci(Re1, 2), 'Oqim rejimi': Re1 < 2000 ? 'laminar' : Re1 < 4000 ? 'o‘tish' : 'turbulent (ideal suyuqlik — taqribiy)' };
    }
  };

  /* M15 — Krivoship-shatunli mexanizm */
  S.crank = {
    title: 'Krivoship-shatunli mexanizm kinematikasi',
    anim: true,
    params: [
      { k: 'r', l: 'Krivoship radiusi r, sm', min: 2, max: 15, step: .5, v: 5 },
      { k: 'l', l: 'Shatun uzunligi l, sm', min: 10, max: 60, step: 1, v: 20 },
      { k: 'n', l: 'Aylanish chastotasi, ayl/min', min: 500, max: 6000, step: 100, v: 3000 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), r = P.r / 100, l = Math.max(P.l, P.r * 1.2) / 100, om = P.n * 2 * Math.PI / 60, lam = r / l;
      const t = tick(cv, dt), ph = (t * 2.2) % (2 * Math.PI);
      const X = p => r * Math.cos(p) + Math.sqrt(l * l - (r * Math.sin(p)) ** 2);
      const V = p => { const e = 1e-5; return (X(p + e) - X(p - e)) / (2 * e) * om; }, Ac = p => { const e = 1e-4; return (X(p + e) - 2 * X(p) + X(p - e)) / (e * e) * om * om; };
      const W2 = w * .52, sc = (W2 - 60) / (2 * r + l) * .95, ox = 30 + sc * r, oy = h * .5;
      circ(c, ox, oy, sc * r, '#334155', null, 1); circ(c, ox, oy, 5, null, C.text);
      const ax = ox + sc * r * Math.cos(ph), ay = oy - sc * r * Math.sin(ph), bx = ox + sc * X(ph);
      c.fillStyle = '#1e293b'; c.fillRect(ox + sc * (l - r) - 20, oy - 26, sc * 2 * r + 60, 52); c.strokeStyle = '#475569'; c.strokeRect(ox + sc * (l - r) - 20, oy - 26, sc * 2 * r + 60, 52);
      ln(c, ox, oy, ax, ay, C.amber, 5); ln(c, ax, ay, bx, oy, C.cyan, 4);
      c.fillStyle = '#fb718566'; c.fillRect(bx - 4, oy - 22, 34, 44); c.strokeStyle = C.rose; c.lineWidth = 2; c.strokeRect(bx - 4, oy - 22, 34, 44);
      circ(c, ax, ay, 5, null, '#fff'); circ(c, bx, oy, 5, null, '#fff');
      txt(c, `φ = ${fx(ph / deg, 0)}°`, ox, h - 14, C.amber); txt(c, 'krivoship', ox, oy + sc * r + 18, C.amber, 'center', 11); txt(c, 'porshen', bx + 13, oy - 30, C.rose, 'center', 11);
      const ps = lin(0, 2 * Math.PI, 361), Vs = ps.map(p => [p / deg, V(p)]), As = ps.map(p => [p / deg, Ac(p)]);
      const vm = Math.max(...Vs.map(p => Math.abs(p[1]))), am = Math.max(...As.map(p => Math.abs(p[1])));
      plot(c, [W2, 0, w - W2, h / 2], { xr: [0, 360], yr: [-vm * 1.15, vm * 1.15], xl: '', yl: 'v, m/s', series: [{ pts: Vs, c: C.green, w: 2 }], vl: [{ x: ph / deg, c: C.amber }] });
      plot(c, [W2, h / 2, w - W2, h / 2], { xr: [0, 360], yr: [-am * 1.15, am * 1.15], xl: 'φ, °', yl: 'a, m/s²', series: [{ pts: As, c: C.rose, w: 2 }, { pts: ps.map(p => [p / deg, -r * om * om * (Math.cos(p) + lam * Math.cos(2 * p))]), c: '#64748b', dash: [4, 4], w: 1.3 }], vl: [{ x: ph / deg, c: C.amber }] });
      const iv = Vs.reduce((b, p) => (Math.abs(p[1]) > Math.abs(b[1]) ? p : b), [0, 0]);
      return { 'λ = r/l': fx(lam, 3), 'ω, rad/s': fx(om, 1), 'Porshen yo‘li 2r, sm': fx(2 * P.r, 1), 'O‘rtacha tezlik, m/s': fx(2 * r * 2 * P.n / 60, 2), 'a (YuChN) = rω²(1+λ), m/s²': fx(r * om * om * (1 + lam), 0), 'v_max, m/s (φ)': `${fx(Math.abs(iv[1]), 2)} (${fx(iv[0] > 180 ? 360 - iv[0] : iv[0], 0)}°)`, 'Erkinlik darajasi W': '3·3 − 2·4 = 1' };
    }
  };

  /* A4, A5 — Kinematika: trayektoriya, tezlik, tezlanish, egrilik */
  S.traj = {
    title: 'Trayektoriya, tezlik va tezlanish vektorlari',
    params: [
      { k: 'mode', l: 'Harakat qonuni', type: 'sel', opts: ['x = 2t, y = 4t − t²', 'x = 3cos t, y = 2sin t', 'Sikloida: R = 1, ω = 1', 'Qiya otish: v₀ = 20 m/s, 45°', 'Qiya otish + havo qarshiligi'], v: 'x = 2t, y = 4t − t²' },
      { k: 't', l: 'Vaqt t, s', min: 0, max: 6.28, step: .01, v: 1 }
    ],
    draw(cv, P) {
      const { c, w, h } = ctx2d(cv), m = P.mode;
      let R, tmax;
      if (m.startsWith('x = 2t')) { R = t => [2 * t, 4 * t - t * t]; tmax = 4; }
      else if (m.startsWith('x = 3cos')) { R = t => [3 * Math.cos(t), 2 * Math.sin(t)]; tmax = 6.28; }
      else if (m.startsWith('Sikloida')) { R = t => [t - Math.sin(t), 1 - Math.cos(t)]; tmax = 6.28; }
      else if (m.includes('havo')) { const k = .02, v0 = 20 / Math.SQRT2, pts = []; let s = [0, 0, v0, v0]; const f = ([x, y, vx, vy]) => { const v = Math.hypot(vx, vy); return [vx, vy, -k * v * vx, -g0 - k * v * vy]; }; for (let i = 0; i <= 3000; i++) { pts.push(s); s = rk4(f, s, .001); } R = t => { const i = Math.min(pts.length - 1, Math.round(t / .001)); return [pts[i][0], pts[i][1]]; }; tmax = 2.6; }
      else { const v0 = 20 / Math.SQRT2; R = t => [v0 * t, v0 * t - g0 * t * t / 2]; tmax = 2.88; }
      const t = Math.min(P.t, tmax), e = 1e-3;
      const r0 = R(t), rp = R(Math.min(t + e, tmax)), rm = R(Math.max(t - e, 0)), hh = (Math.min(t + e, tmax) - Math.max(t - e, 0)) / 2;
      const v = [(rp[0] - rm[0]) / (2 * hh), (rp[1] - rm[1]) / (2 * hh)], a = [(rp[0] - 2 * r0[0] + rm[0]) / (hh * hh), (rp[1] - 2 * r0[1] + rm[1]) / (hh * hh)];
      const vv = Math.hypot(...v), cr = v[0] * a[1] - v[1] * a[0], at = (a[0] * v[0] + a[1] * v[1]) / (vv || 1), an = Math.abs(cr) / (vv || 1), Rc = vv ** 3 / Math.max(Math.abs(cr), 1e-9);
      const path = lin(0, tmax, 400).map(R), xs = path.map(p => p[0]), ys = path.map(p => p[1]);
      let x0 = Math.min(...xs), x1 = Math.max(...xs), y0 = Math.min(...ys), y1 = Math.max(...ys); const pad = .15 * Math.max(x1 - x0, y1 - y0) + .5;
      const W2 = w * .7, s = Math.min((W2 - 40) / (x1 - x0 + 2 * pad), (h - 40) / (y1 - y0 + 2 * pad)), T = ([x, y]) => [20 + s * (x - x0 + pad), h - 20 - s * (y - y0 + pad)];
      ln(c, ...T([x0 - pad, 0]), ...T([x1 + pad, 0]), '#334155', 1); ln(c, ...T([0, y0 - pad]), ...T([0, y1 + pad]), '#334155', 1);
      poly(c, path.map(T), C.cyan, 2.2);
      const P0 = T(r0), dv = (u) => { const a1 = R(Math.min(u + e, tmax)), a0 = R(Math.max(u - e, 0)); return Math.hypot(a1[0] - a0[0], a1[1] - a0[1]) / (Math.min(u + e, tmax) - Math.max(u - e, 0)); };
      const vmax = Math.max(...lin(0, tmax, 120).map(dv), 1e-9), am = Math.hypot(...a);
      if (Rc < 1e3 && Rc * s < 2000) { const nx = -v[1] / vv * Math.sign(cr), ny = v[0] / vv * Math.sign(cr); const cc = T([r0[0] + nx * Rc, r0[1] + ny * Rc]); circ(c, cc[0], cc[1], Rc * s, '#a78bfa66', null, 1); }
      const Lv = 80 * vv / vmax; if (vv > 1e-9) arrow(c, P0[0], P0[1], P0[0] + v[0] / vv * Lv, P0[1] - v[1] / vv * Lv, C.green, 2.5);
      if (am > 1e-9) arrow(c, P0[0], P0[1], P0[0] + a[0] / am * 55, P0[1] - a[1] / am * 55, C.rose, 2.5);
      circ(c, P0[0], P0[1], 6, '#fff', C.amber);
      const lx = W2 + 10; txt(c, 'Belgilar:', lx, 24, C.text, 'left'); [[C.cyan, 'trayektoriya'], [C.green, 'tezlik v'], [C.rose, 'tezlanish a'], [C.violet, 'egrilik aylanasi']].forEach(([col, n], i) => { c.fillStyle = col; c.fillRect(lx, 38 + i * 20, 14, 4); txt(c, n, lx + 20, 44 + i * 20, C.text, 'left', 12); });
      return { 't, s': fx(t, 2), 'x, y, m': `${fx(r0[0], 2)}; ${fx(r0[1], 2)}`, 'v, m/s': fx(vv, 3), 'a, m/s²': fx(Math.hypot(...a), 3), 'a_τ, m/s²': fx(at, 3), 'a_n, m/s²': fx(an, 3), 'Egrilik radiusi R, m': Rc > 1e4 ? '∞' : fx(Rc, 3) };
    }
  };

  /* A10 — Qo‘sh mayatnik */
  S.dpend = {
    title: 'Qo‘sh mayatnik (l₁ = l₂ = 1 m): Lagranj tenglamalari',
    anim: true,
    params: [
      { k: 'a', l: 'φ₁(0), °', min: -180, max: 180, step: 1, v: 120 },
      { k: 'b', l: 'φ₂(0), °', min: -180, max: 180, step: 1, v: -10 },
      { k: 'mr', l: 'm₂/m₁', min: .2, max: 3, step: .05, v: 1 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), m1 = 1, m2 = P.mr, Tm = 20, d2 = .002;
      const f = ([a, b, wa, wb]) => { const d = a - b, M11 = (m1 + m2), M12 = m2 * Math.cos(d), M21 = Math.cos(d), M22 = 1; const r1 = -m2 * wb * wb * Math.sin(d) - (m1 + m2) * g0 * Math.sin(a), r2 = wa * wa * Math.sin(d) - g0 * Math.sin(b); const det = M11 * M22 - M12 * M21; return [wa, wb, (r1 * M22 - M12 * r2) / det, (M11 * r2 - M21 * r1) / det]; };
      const En = ([a, b, wa, wb]) => (m1 + m2) / 2 * wa * wa + m2 / 2 * wb * wb + m2 * wa * wb * Math.cos(a - b) - (m1 + m2) * g0 * Math.cos(a) - m2 * g0 * Math.cos(b);
      const d = cache(cv, P, () => { const run = da => { let s = [P.a * deg + da, P.b * deg, 0, 0]; const out = []; for (let i = 0; i <= Tm / d2; i++) { if (i % 10 === 0) out.push(s); s = rk4(f, s, d2); } return out; }; const A1 = run(0), B1 = run(1e-3 * deg); return { A1, B1, E0: En(A1[0]), E1: En(A1[A1.length - 1]) }; });
      const t = tick(cv, dt) % Tm, i = Math.min(d.A1.length - 1, Math.floor(t / (10 * d2)));
      const W2 = w * .55, s = Math.min(W2, h) / 4.6, ox = W2 / 2, oy = h / 2 - s * .2;
      const pos = st => { const x1 = ox + s * Math.sin(st[0]), y1 = oy + s * Math.cos(st[0]); return [x1, y1, x1 + s * Math.sin(st[1]), y1 + s * Math.cos(st[1])]; };
      const trail = []; for (let j = Math.max(0, i - 150); j <= i; j++) { const p = pos(d.A1[j]); trail.push([p[2], p[3]]); } poly(c, trail, '#22d3ee66', 1.5);
      const [x1, y1, x2, y2] = pos(d.A1[i]), [u1, v1, u2, v2] = pos(d.B1[i]);
      ln(c, ox, oy, u1, v1, '#fb718566', 2); ln(c, u1, v1, u2, v2, '#fb718566', 2); circ(c, u2, v2, 6, null, '#fb718588');
      ln(c, ox, oy, x1, y1, C.text, 2.5); ln(c, x1, y1, x2, y2, C.text, 2.5); circ(c, ox, oy, 4, null, C.axis); circ(c, x1, y1, 8, '#fff', C.amber); circ(c, x2, y2, 6 + 3 * Math.min(P.mr, 2), '#fff', C.cyan);
      txt(c, 'pushti — φ₁(0) ga 0,001° qo‘shilgan nusxa', 10, h - 10, C.rose, 'left', 11);
      const sl = d.A1.slice(0, i + 1).map((st, j) => [j * 10 * d2, st[0] / deg]), sl2 = d.A1.slice(0, i + 1).map((st, j) => [j * 10 * d2, st[1] / deg]);
      plot(c, [W2, 0, w - W2, h], { xr: [0, Tm], yr: [-400, 400], xl: 't, s', yl: 'φ₁, φ₂, °', series: [{ pts: sl, c: C.amber, w: 1.6 }, { pts: sl2, c: C.cyan, w: 1.6 }], legend: [{ c: C.amber, l: 'φ₁' }, { c: C.cyan, l: 'φ₂' }] });
      const mu = m2 / m1, wA = Math.sqrt(g0 * ((1 + mu) - Math.sqrt((1 + mu) * mu))), wB = Math.sqrt(g0 * ((1 + mu) + Math.sqrt((1 + mu) * mu)));
      const div = Math.hypot(d.A1[i][0] - d.B1[i][0], d.A1[i][1] - d.B1[i][1]) / deg;
      return { 't, s': fx(t, 1), 'Normal chastotalar ω₁, ω₂, rad/s': `${fx(wA, 3)}; ${fx(wB, 3)}`, 'Energiya xatosi (20 s)': sci(Math.abs(d.E1 - d.E0), 1), 'Nusxalar farqi, °': fx(div, 3) };
    }
  };

  /* A13 — Braxistoxrona */
  S.brach = {
    title: 'Braxistoxrona: eng tez tushish chizig‘i',
    anim: true,
    params: [
      { k: 'X', l: 'Oxirgi nuqta X, m', min: .5, max: 5, step: .05, v: 3.14 },
      { k: 'Y', l: 'Pastga balandlik Y, m', min: .3, max: 3, step: .05, v: 2 }
    ],
    draw(cv, P, dt) {
      const { c, w, h } = ctx2d(cv), N = 1500;
      const d = cache(cv, P, () => {
        const ratio = P.X / P.Y; let lo = 1e-4, hi = 2 * Math.PI - 1e-4; for (let k = 0; k < 80; k++) { const m = (lo + hi) / 2; ((m - Math.sin(m)) / (1 - Math.cos(m)) < ratio) ? lo = m : hi = m; }
        const te = (lo + hi) / 2, a = P.Y / (1 - Math.cos(te));
        const Rr = (P.X * P.X + P.Y * P.Y) / (2 * P.X), pe = Math.atan2(P.Y, Rr - P.X);
        const curves = [
          ['To‘g‘ri chiziq', C.green, lin(0, 1, N).map(u => [P.X * u * u, P.Y * u * u])],
          ['Aylana yoyi', C.amber, lin(0, pe, N).map(f => [Rr * (1 - Math.cos(f)), Rr * Math.sin(f)])],
          ['Sikloida', C.cyan, lin(0, te, N).map(th => [a * (th - Math.sin(th)), a * (1 - Math.cos(th))])]];
        return curves.map(([n, col, pts]) => { const ts = [0]; for (let i = 1; i < pts.length; i++) { const ds = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]), ym = (pts[i][1] + pts[i - 1][1]) / 2; ts.push(ts[i - 1] + ds / Math.sqrt(2 * g0 * Math.max(ym, 1e-9))); } return { n, col, pts, ts, T: ts[ts.length - 1] }; });
      });
      const ymax = Math.max(...d.flatMap(cu => cu.pts.map(p => p[1])));
      const s = Math.min((w - 60) / P.X, (h - 70) / ymax) * .95, ox = 30, oy = 30, T = ([x, y]) => [ox + s * x, oy + s * y];
      const Tm = Math.max(...d.map(cu => cu.T)), t = tick(cv, dt) % (Tm + 1.2);
      d.forEach(cu => { poly(c, cu.pts.map(T), cu.col, 2.2); let j = cu.ts.findIndex(x => x >= t); if (j < 0) j = cu.ts.length - 1; const p = T(cu.pts[j]); circ(c, p[0], p[1], 7, '#fff', cu.col); });
      circ(c, ...T([0, 0]), 4, null, '#fff'); circ(c, ...T([P.X, P.Y]), 5, null, C.rose);
      d.forEach((cu, i) => txt(c, `${cu.n}: ${fx(cu.T, 3)} s`, w - 14, h - 14 - (2 - i) * 18, cu.col, 'right', 12));
      txt(c, `t = ${fx(Math.min(t, Tm), 2)} s`, 14, h - 14, C.text, 'left', 12);
      return Object.fromEntries(d.map(cu => [`${cu.n}, s`, fx(cu.T, 4)]).concat([['Sikloida ustunligi', `${fx((1 - d[2].T / d[0].T) * 100, 1)} % (to‘g‘ri chiziqqa nisbatan)`]]));
    }
  };

  /* ---------- Simulyator konteynerini qurish ---------- */
  function build(box) {
    const key = box.dataset.sim, sim = S[key]; if (!sim) return;
    const id = `${key}-${Math.random().toString(36).slice(2, 7)}`;
    const ctrls = sim.params.map(p => {
      if (p.type === 'sel') return `<label class="control">${A(p.l)}<select data-k="${p.k}">${p.opts.map(o => `<option value="${o}"${o === p.v ? ' selected' : ''}>${A(o)}</option>`).join('')}</select></label>`;
      return `<label class="control">${A(p.l)} <output data-o="${p.k}"></output><input type="range" data-k="${p.k}" min="${p.min}" max="${p.max}" step="${p.step}" value="${p.v}"></label>`;
    }).join('');
    box.innerHTML = `<div class="sim-layout"><div class="card controls"><h3>${A(sim.title)}</h3>${ctrls}<div class="actions"><button class="secondary" type="button" data-reset>${A('Boshlang‘ich qiymatlar')}</button></div><div class="readout" aria-live="polite"></div></div><div class="card canvas-card"><div class="toolbar"><span>${A(sim.title)}</span><span class="stat notranslate">model · SI birliklar</span></div><canvas id="${id}" role="img" aria-label="${A(sim.title)}"></canvas></div></div>`;
    const cv = box.querySelector('canvas'), ro = box.querySelector('.readout');
    const read = () => { const P = {}; box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); P[p.k] = p.type === 'sel' ? el.value : (p.log ? 10 ** +el.value : +el.value); const o = box.querySelector(`[data-o="${p.k}"]`); if (o) o.textContent = p.log ? sci(10 ** +el.value, 1) : (+el.value).toString(); }); return P; };
    const render = (dt) => { const r = sim.draw(cv, read(), dt || 0); ro.innerHTML = Object.entries(r || {}).map(([k, v]) => `<span>${A(k)}</span><b>${A(v)}</b>`).join(''); };
    box.addEventListener('input', () => render()); box.addEventListener('change', () => render());
    box.querySelector('[data-reset]').addEventListener('click', () => { box.querySelectorAll('[data-k]').forEach(el => { const p = sim.params.find(x => x.k === el.dataset.k); el.value = p.v; }); render(); });
    window.addEventListener('resize', () => render());
    render();
    if (sim.anim) { let last = performance.now(), vis = true; new IntersectionObserver(e => { vis = e[0].isIntersecting; }).observe(box); const loop = now => { if (vis) render(Math.min((now - last) / 1000, .1)); last = now; requestAnimationFrame(loop); }; requestAnimationFrame(loop); }
  }
  window.YAF_SIMS = S;
  const init = () => document.querySelectorAll('.sim-box[data-sim]').forEach(build);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
