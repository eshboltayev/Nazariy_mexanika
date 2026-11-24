"""A1–A15 amaliy mashg'ulotlar va S1–S6 seminarlar mazmuni (Nazariy mexanika, NM1406)."""

A = []

A.append(dict(n=1, lec=2, sim="coords", tn=["TN2", "TN3", "TN14", "TN15"],
 title=r"Dekart va silindrik koordinatalar sistemasi",
 goal=r"Dekart va silindrik (qutb) koordinatalarida nuqta holati, tezligi va tezlanishini ifodalash, koordinatalar orasida o‘tish hamda erkin zarra Lagranj funksiyasini silindrik koordinatalarda yozishni o‘rganish.",
 theory=r"""<p>Silindrik koordinatalar: \(x=\rho\cos\varphi,\ y=\rho\sin\varphi,\ z=z\); teskari: \(\rho=\sqrt{x^2+y^2}\), \(\operatorname{tg}\varphi=y/x\). Birlik vektorlar \(\vec e_\rho,\vec e_\varphi\) vaqt bo‘yicha o‘zgaradi: \(\dot{\vec e}_\rho=\dot\varphi\vec e_\varphi\), \(\dot{\vec e}_\varphi=-\dot\varphi\vec e_\rho\). Natijada:</p>
$$\vec v=\dot\rho\,\vec e_\rho+\rho\dot\varphi\,\vec e_\varphi+\dot z\,\vec e_z,\qquad v^2=\dot\rho^2+\rho^2\dot\varphi^2+\dot z^2,$$
$$a_\rho=\ddot\rho-\rho\dot\varphi^2,\qquad a_\varphi=\rho\ddot\varphi+2\dot\rho\dot\varphi=\frac1\rho\frac{d}{dt}(\rho^2\dot\varphi),\qquad a_z=\ddot z.$$
<p>Erkin zarra: \(L=\frac m2(\dot\rho^2+\rho^2\dot\varphi^2+\dot z^2)\). Bunda \(\varphi\) va \(z\) siklik koordinatalar.</p>""",
 solved=[("Vint chiziq bo‘ylab harakat", r"Nuqta \(x=R\cos\omega t,\ y=R\sin\omega t,\ z=ut\) qonun bo‘yicha harakatlanadi; \(R=0{,}5\) m, \(\omega=4\) rad/s, \(u=1\) m/s. Silindrik koordinatalarda harakat qonuni, tezlik va tezlanishni toping.",
          r"\(\rho=R\), \(\varphi=\omega t\), \(z=ut\). \(v^2=R^2\omega^2+u^2=4+1\) ⇒ \(v=2{,}24\) m/s (o‘zgarmas). \(a_\rho=-R\omega^2=-8\) m/s², \(a_\varphi=a_z=0\) — tezlanish o‘qqa tik yo‘nalgan."),
         ("Aylanayotgan sterjendagi munchoq", r"Munchoq sterjen bo‘ylab \(\rho=bt\) qonun bilan siljiydi, sterjen esa \(\varphi=\omega t\) bilan aylanadi; \(b=0{,}2\) m/s, \(\omega=3\) rad/s. \(t=2\) s dagi tezlik va tezlanishni toping.",
          r"\(\dot\rho=b\), \(\rho\dot\varphi=bt\omega=1{,}2\) m/s ⇒ \(v=\sqrt{0{,}04+1{,}44}=1{,}22\) m/s. \(a_\rho=-\rho\omega^2=-0{,}4\cdot9=-3{,}6\) m/s², \(a_\varphi=2\dot\rho\dot\varphi=1{,}2\) m/s² ⇒ \(a=3{,}79\) m/s². \(a_\varphi\) — Koriolis tezlanishi."),
         ("Koordinatalarni almashtirish", r"\((x,y,z)=(3;\,4;\,5)\) nuqtani silindrik koordinatalarda yozing va hajm elementini ko‘rsating.",
          r"\(\rho=5\), \(\varphi=\operatorname{arctg}(4/3)=53{,}13^\circ\), \(z=5\). \(dV=\rho\,d\rho\,d\varphi\,dz\) (Lame koeffitsiyentlari \(1,\rho,1\)).")],
 tasks=[(r"\((\rho,\varphi,z)=(2;\,120^\circ;\,-1)\) nuqtaning Dekart koordinatalari?", r"\((-1;\ 1{,}732;\ -1)\)"),
        (r"\(\rho=2\) m, \(\dot\rho=0{,}5\) m/s, \(\dot\varphi=1\) rad/s, \(\dot z=0\). \(v\) = ?", r"\(\sqrt{0{,}25+4}=2{,}06\) m/s"),
        (r"Tekislikda \(\rho=a e^{k\varphi}\) logarifmik spiral bo‘ylab \(\dot\varphi=\omega\) bilan harakatda \(v\) ni toping.", r"\(v=\rho\omega\sqrt{1+k^2}\)"),
        (r"Silindrik koordinatalarda erkin zarra uchun Lagranj tenglamalarini yozing; qaysi kattaliklar saqlanadi?", r"\(m(\ddot\rho-\rho\dot\varphi^2)=0\); \(p_\varphi=m\rho^2\dot\varphi\) va \(p_z=m\dot z\) saqlanadi")],
 model=("python", r"""import numpy as np
# Silindrik formulani sonli differensiallash bilan tekshirish
b, w = 0.2, 3.0
t = np.linspace(0, 4, 40001); dt = t[1] - t[0]
rho, phi = b*t, w*t
x, y = rho*np.cos(phi), rho*np.sin(phi)
vx, vy = np.gradient(x, dt), np.gradient(y, dt)
ax, ay = np.gradient(vx, dt), np.gradient(vy, dt)
i = np.searchsorted(t, 2.0)
print("v (sonli)   =", np.hypot(vx[i], vy[i]))
print("v (formula) =", np.hypot(b, b*t[i]*w))
print("a (sonli)   =", np.hypot(ax[i], ay[i]))
print("a (formula) =", np.hypot(-b*t[i]*w**2, 2*b*w))"""),
 questions=["Silindrik birlik vektorlar nima uchun vaqtga bog‘liq?", "Koriolis tezlanishi qaysi had bilan ifodalanadi?", "Qachon silindrik koordinatalar qulay?", "Lame koeffitsiyentlari nimani bildiradi?"]))

A.append(dict(n=2, lec=2, sim="coords", tn=["TN2", "TN3", "TN15"],
 title=r"Sferik koordinatalar sistemasi",
 goal=r"Sferik koordinatalarda holat, tezlik va kinetik energiyani ifodalash, sfera sirtidagi harakat va sferik mayatnik masalalarini Lagranj funksiyasi orqali tahlil qilish.",
 theory=r"""<p>\(x=r\sin\theta\cos\varphi\), \(y=r\sin\theta\sin\varphi\), \(z=r\cos\theta\); \(0\le\theta\le\pi\), \(0\le\varphi\lt2\pi\). Lame koeffitsiyentlari \((1,\,r,\,r\sin\theta)\):</p>
$$v^2=\dot r^2+r^2\dot\theta^2+r^2\sin^2\theta\,\dot\varphi^2,\qquad dV=r^2\sin\theta\,dr\,d\theta\,d\varphi.$$
<p><b>Sferik mayatnik</b> (\(\theta\) pastga yo‘nalgan vertikaldan): \(L=\frac{ml^2}{2}(\dot\theta^2+\sin^2\theta\,\dot\varphi^2)+mgl\cos\theta\). \(\varphi\) siklik, shuning uchun \(p_\varphi=ml^2\sin^2\theta\,\dot\varphi=\text{const}\). Konus mayatnik (\(\theta=\text{const}\)) uchun \(\dot\varphi^2=g/(l\cos\theta)\).</p>""",
 solved=[("Sfera sirtida harakat", r"Zarra radiusi \(R=2\) m sfera sirtida harakatlanmoqda; biror paytda \(\theta=60^\circ\), \(\dot\theta=1\) rad/s, \(\dot\varphi=2\) rad/s. Tezlikni toping.",
          r"\(\dot r=0\): \(v^2=R^2(\dot\theta^2+\sin^2\theta\,\dot\varphi^2)=4(1+0{,}75\cdot4)=16\) ⇒ \(v=4\) m/s."),
         ("Koordinatalarni aniqlash", r"\((x,y,z)=(-2;\,2;\,2\sqrt2)\) nuqtaning sferik koordinatalarini toping.",
          r"\(r=\sqrt{4+4+8}=4\); \(\cos\theta=2\sqrt2/4=0{,}707\) ⇒ \(\theta=45^\circ\); \(x\lt0,\ y\gt0\) ⇒ \(\varphi=135^\circ\)."),
         ("Konus mayatnik", r"\(l=1\) m ip bilan mayatnik vertikaldan \(\theta=30^\circ\) og‘ib, aylana bo‘ylab harakatlanadi. Burchak tezlik va davrni toping.",
          r"\(\theta\) bo‘yicha Lagranj tenglamasi: \(ml^2\sin\theta\cos\theta\,\dot\varphi^2-mgl\sin\theta=0\) ⇒ \(\dot\varphi=\sqrt{g/(l\cos\theta)}=\sqrt{9{,}81/0{,}866}=3{,}37\) rad/s, \(T=2\pi/\dot\varphi=1{,}87\) s.")],
 tasks=[(r"\((r,\theta,\varphi)=(3;\,90^\circ;\,270^\circ)\) — Dekart koordinatalari?", r"\((0;\,-3;\,0)\)"),
        (r"Sferik koordinatalarda integrallab, shar hajmini toping.", r"\(\int_0^R r^2dr\int_0^\pi\sin\theta\,d\theta\int_0^{2\pi}d\varphi=\frac43\pi R^3\)"),
        (r"\(l=0{,}5\) m, \(\theta=60^\circ\) konus mayatnik burchak tezligi?", r"\(\sqrt{9{,}81/0{,}25}=6{,}26\) rad/s"),
        (r"Sferik koordinatalarda erkin zarra Lagranj funksiyasini yozing va siklik koordinatani ko‘rsating.", r"\(L=\frac m2(\dot r^2+r^2\dot\theta^2+r^2\sin^2\theta\dot\varphi^2)\); \(\varphi\) siklik, \(p_\varphi=mr^2\sin^2\theta\,\dot\varphi\)")],
 model=("python", r"""import numpy as np
# Sferik mayatnik: RK4 bilan integrallash va p_phi saqlanishini tekshirish
g, l = 9.81, 1.0
def f(s):
    th, w, ph, om = s
    return np.array([w, np.sin(th)*np.cos(th)*om**2 - g/l*np.sin(th), om,
                     -2*w*om*np.cos(th)/np.sin(th)])
th0 = np.radians(30); s = np.array([th0, 0.0, 0.0, np.sqrt(g/(l*np.cos(th0)))*1.1])
dt = 1e-3
for k in range(5001):
    if k % 1000 == 0:
        th, w, ph, om = s
        E = 0.5*l**2*(w**2 + np.sin(th)**2*om**2) - g*l*np.cos(th)
        print(f"t={k*dt:4.1f} s  theta={np.degrees(th):6.2f}°  p_phi={l**2*np.sin(th)**2*om:.5f}  E={E:.5f}")
    k1 = f(s); k2 = f(s + dt/2*k1); k3 = f(s + dt/2*k2); k4 = f(s + dt*k3)
    s = s + dt/6*(k1 + 2*k2 + 2*k3 + k4)"""),
 questions=["\\(\\theta\\) burchak qanday oraliqda o‘zgaradi va nima uchun?", "Sferik mayatnikda qaysi kattaliklar saqlanadi?", "Qutblarda (\\(\\theta=0\\)) sferik koordinatalarning qanday xususiyati bor?", "Sferik koordinatalar qaysi masalalarda qulay?"]))

A.append(dict(n=3, lec=5, sim="orbit", tn=["TN8", "TN14", "TN21"],
 title=r"Impuls momenti",
 goal=r"Moddiy nuqta va sistemaning impuls momentini hisoblash, momentlar tenglamasini qo‘llash va impuls momentining saqlanish qonuni bilan masalalar yechish.",
 theory=r"""<p>Impuls momenti \(\vec M=\vec r\times\vec p\). Momentlar tenglamasi \(\dfrac{d\vec M}{dt}=\vec r\times\vec F=\vec N\). Markaziy kuchda \(\vec N=0\), shuning uchun \(\vec M=\text{const}\). Qattiq jism qo‘zg‘almas o‘q atrofida aylanganda \(M_z=I\omega\), \(T=\frac12I\omega^2=M_z^2/2I\).</p>
$$\vec M=\begin{vmatrix}\vec i&\vec j&\vec k\\x&y&z\\p_x&p_y&p_z\end{vmatrix},\qquad M_z=m(xv_y-yv_x)=mr^2\dot\varphi.$$
<p>Sistemaning impuls momenti \(\vec M=\vec R\times\vec P+\vec M_{MM}\) — massa markazi harakati va uning atrofidagi harakat hissalari.</p>""",
 solved=[("Vektor ko‘paytma", r"\(\vec r=(1;\,2;\,0)\) m, \(\vec p=(3;\,-1;\,2)\) kg·m/s. \(\vec M\) va \(|\vec M|\) ni toping.",
          r"\(M_x=yp_z-zp_y=4\), \(M_y=zp_x-xp_z=-2\), \(M_z=xp_y-yp_x=-1-6=-7\). \(|\vec M|=\sqrt{69}=8{,}31\) kg·m²/s."),
         ("Figurachi", r"Figurachi qo‘llarini yoyganda \(I_1=4\) kg·m², 1 ayl/s tezlik bilan aylanadi. Qo‘llarini yig‘ganda \(I_2=1{,}6\) kg·m². Yangi chastota va kinetik energiya o‘zgarishi?",
          r"\(I_1\omega_1=I_2\omega_2\) ⇒ \(\nu_2=2{,}5\) ayl/s. \(T=M^2/2I\) ⇒ \(T_2/T_1=I_1/I_2=2{,}5\). Energiya mushaklar bajargan ish hisobiga ortadi."),
         ("To‘g‘ri chiziqli harakatning momenti", r"\(m=2\) kg jism \(v=3\) m/s tezlik bilan koordinata boshidan \(b=0{,}5\) m masofadan o‘tuvchi to‘g‘ri chiziq bo‘ylab harakatlanmoqda. \(M\) = ?",
          r"\(M=mvb=3\) kg·m²/s — kuch yo‘q, shuning uchun moment o‘zgarmas (sektorial tezlik doimiy).")],
 tasks=[(r"Yerning Quyosh atrofidagi orbital impuls momenti (\(m=5{,}97\cdot10^{24}\) kg, \(r=1{,}496\cdot10^{11}\) m, \(v=29{,}78\) km/s)?", r"\(2{,}66\cdot10^{40}\) kg·m²/s"),
        (r"\(I=0{,}5\) kg·m² disk 10 rad/s bilan aylanmoqda; ustiga xuddi shunday tinch disk tushirildi. Umumiy burchak tezlik va energiya yo‘qotilishi?", r"5 rad/s; energiyaning 50 % i"),
        (r"Koordinata boshidan \(\vec v_0\) bilan otilgan jism uchun og‘irlik kuchining momentini va \(dM_z/dt\) ni toping.", r"\(N_z=-mgx\); \(M_z=-\frac12mgv_{0x}t^2\)"),
        (r"Markaziy maydonda \(M=mr^2\dot\varphi\). \(r\) 2 marta kamaysa, \(\dot\varphi\) qanday o‘zgaradi?", "4 marta ortadi")],
 model=("python", r"""import numpy as np
# Markaziy maydonda impuls momenti saqlanishini tekshirish (leapfrog)
GM = 1.0
r = np.array([1.0, 0.0]); v = np.array([0.0, 1.2]); dt = 1e-3
acc = lambda r: -GM*r/np.linalg.norm(r)**3
v = v + 0.5*dt*acc(r)
for k in range(1, 20001):
    r = r + dt*v; a = acc(r); v = v + dt*a
    if k % 4000 == 0:
        vh = v - 0.5*dt*a
        print(f"t={k*dt:5.1f}  r={np.linalg.norm(r):.4f}  Mz={r[0]*vh[1]-r[1]*vh[0]:.6f}")"""),
 questions=["Impuls momenti qaysi nuqtaga nisbatan aniqlanadi? Natija nuqtaga bog‘liqmi?", "Momentlar tenglamasini Nyuton qonunidan keltirib chiqaring.", "Markaziy maydonda nima uchun harakat tekis?", "Sektorial tezlik bilan \\(M\\) qanday bog‘langan?"]))

A.append(dict(n=4, lec=2, sim="traj", tn=["TN1", "TN2", "TN15"],
 title=r"Harakat qonunlari va trayektoriya (1): kinematik tahlil",
 goal=r"Berilgan harakat qonunidan trayektoriya tenglamasini, tezlik va tezlanish vektorlarini, tangensial va normal tezlanishlarni hamda egrilik radiusini aniqlashni o‘rganish.",
 theory=r"""<p>Harakat qonuni \(\vec r(t)\) berilsa, \(\vec v=\dot{\vec r}\), \(\vec a=\ddot{\vec r}\). Parametr \(t\) ni yo‘qotish trayektoriya tenglamasini beradi. Tabiiy o‘qlarda:</p>
$$a_\tau=\frac{dv}{dt}=\frac{\vec a\cdot\vec v}{v},\qquad a_n=\frac{v^2}{R}=\frac{|\vec v\times\vec a|}{v},\qquad R=\frac{v^3}{|\vec v\times\vec a|}.$$
<p>Gorizontga \(\alpha\) burchak ostida otilgan jism: uchish uzoqligi \(L=v_0^2\sin2\alpha/g\), maksimal balandlik \(H=v_0^2\sin^2\alpha/2g\), trayektoriya parabola.</p>""",
 solved=[("Parabolik harakat", r"\(x=2t\), \(y=4t-t^2\) (m, s). Trayektoriya, \(t=1\) s dagi \(v\), \(a_\tau\), \(a_n\) va egrilik radiusini toping.",
          r"\(t=x/2\) ⇒ \(y=2x-x^2/4\) — parabola. \(\vec v=(2;\,4-2t)=(2;\,2)\), \(v=2{,}83\) m/s; \(\vec a=(0;\,-2)\). \(a_\tau=\vec a\cdot\vec v/v=-4/2{,}83=-1{,}41\) m/s², \(a_n=\sqrt{4-2}=1{,}41\) m/s², \(R=v^2/a_n=8/1{,}41=5{,}66\) m."),
         ("Ellips bo‘ylab harakat", r"\(x=3\cos t\), \(y=2\sin t\). Tezlanish markazga yo‘nalganini ko‘rsating va \(t=0\) dagi egrilik radiusini toping.",
          r"\(\vec a=-\vec r\) — markazga yo‘nalgan (izotrop ossilyator). \(t=0\): \(\vec v=(0;\,2)\), \(\vec a=(-3;\,0)\), \(a_n=3\) ⇒ \(R=4/3=1{,}33\) m \(=b^2/a\) ✓."),
         ("Qiya otish", r"Jism \(v_0=20\) m/s tezlik bilan \(45^\circ\) burchak ostida otildi. Uchish uzoqligi va maksimal balandlik?",
          r"\(L=400/9{,}81=40{,}8\) m, \(H=400\cdot0{,}5/19{,}62=10{,}2\) m. Eng yuqori nuqtada \(R=v_0^2\cos^2\alpha/g=20{,}4\) m.")],
 tasks=[(r"\(x=3\cos2t\), \(y=3\sin2t\): trayektoriya, \(v\), \(a\)?", r"aylana \(R=3\) m; \(v=6\) m/s; \(a=12\) m/s²"),
        (r"\(x=t\), \(y=t^3\): \(t=1\) s dagi egrilik radiusi?", r"\(R=10^{3/2}/6=5{,}27\) m"),
        (r"Sikloida \(x=R(\omega t-\sin\omega t)\), \(y=R(1-\cos\omega t)\); \(R=0{,}3\) m, \(\omega=10\) rad/s. Maksimal tezlik?", r"\(v=2R\omega|\sin(\omega t/2)|\), \(v_{max}=6\) m/s"),
        (r"Qiya otishda qaysi burchakda uchish uzoqligi maksimal (havo qarshiligisiz)?", r"\(45^\circ\)")],
 model=("python", r"""import numpy as np
# Trayektoriya, tezlik, tezlanish va egrilik radiusini hisoblash
t = np.linspace(0, 4, 4001); dt = t[1] - t[0]
x, y = 2*t, 4*t - t**2
vx, vy = np.gradient(x, dt), np.gradient(y, dt)
ax, ay = np.gradient(vx, dt), np.gradient(vy, dt)
v = np.hypot(vx, vy); cross = np.abs(vx*ay - vy*ax)
R = v**3/np.maximum(cross, 1e-12)
for tt in (0, 1, 2, 3):
    i = np.searchsorted(t, tt)
    print(f"t={tt}  v={v[i]:.3f}  a_tau={(ax[i]*vx[i]+ay[i]*vy[i])/v[i]:+.3f}  a_n={cross[i]/v[i]:.3f}  R={R[i]:.3f}")"""),
 questions=["Trayektoriya va harakat qonunining farqi nima?", "Tangensial va normal tezlanishlar nima uchun javob beradi?", "Tekis aylanma harakatda \\(a_\\tau\\) nimaga teng?", "Egrilik radiusi qayerda eng kichik?"]))

A.append(dict(n=5, lec=4, sim="traj", tn=["TN1", "TN6", "TN25"],
 title=r"Harakat qonunlari va trayektoriya (2): dinamikaning asosiy masalasi",
 goal=r"Kuch va boshlang‘ich shartlar berilganda harakat tenglamalarini integrallab, harakat qonuni va trayektoriyani topish; muhit qarshiligi va magnit maydondagi harakatni tahlil qilish.",
 theory=r"""<p>Dinamikaning asosiy (teskari) masalasi: \(m\ddot{\vec r}=\vec F(\vec r,\dot{\vec r},t)\), \(\vec r(0)=\vec r_0\), \(\dot{\vec r}(0)=\vec v_0\). Muhim hollar:</p>
<ul><li><b>Chiziqli qarshilik</b> \(\vec F=m\vec g-b\vec v\): \(v(t)=v_t(1-e^{-t/\tau})\), \(\tau=m/b\), \(v_t=mg/b\).</li><li><b>Kvadratik qarshilik</b> \(F=cv^2\): \(v_t=\sqrt{mg/c}\).</li><li><b>Bir jinsli magnit maydon</b> \(m\dot{\vec v}=q\vec v\times\vec B\): aylana, \(\omega_c=qB/m\), \(r=mv_\perp/qB\); \(B\) bo‘ylab tekis — vint chiziq.</li><li><b>Elastik kuch</b> \(F=-kx\): \(x=A\cos(\omega t+\alpha)\), \(A=\sqrt{x_0^2+v_0^2/\omega^2}\).</li></ul>""",
 solved=[("Chiziqli qarshilik bilan tushish", r"\(m=10\) g sharcha \(b=0{,}002\) kg/s qarshilik koeffitsiyentli muhitda tinch holatdan tushmoqda. \(\tau\), \(v_t\) va \(t=5\) s dagi tezlik?",
          r"\(\tau=m/b=5\) s, \(v_t=mg/b=49{,}05\) m/s. \(v(5)=49{,}05(1-e^{-1})=31{,}0\) m/s."),
         ("Proton magnit maydonda", r"Proton \(v=10^6\) m/s tezlik bilan \(B=0{,}5\) T maydonga tik uchib kirdi. Siklotron chastotasi va orbita radiusi?",
          r"\(\omega_c=eB/m_p=1{,}602\cdot10^{-19}\cdot0{,}5/1{,}673\cdot10^{-27}=4{,}79\cdot10^7\) rad/s; \(r=v/\omega_c=2{,}09\) sm."),
         ("Ossilyator boshlang‘ich shartlari", r"\(\omega=2\) rad/s, \(x_0=0{,}1\) m, \(v_0=0{,}4\) m/s. Amplituda va boshlang‘ich faza?",
          r"\(A=\sqrt{0{,}01+0{,}04}=0{,}224\) m; \(\operatorname{tg}\alpha=-v_0/(\omega x_0)=-2\) ⇒ \(\alpha=-63{,}4^\circ\).")],
 tasks=[(r"Parashyutchi: \(m=80\) kg, \(c=0{,}25\) kg/m. Oxirgi tezlik?", r"\(\sqrt{80\cdot9{,}81/0{,}25}=56\) m/s"),
        (r"Elektronning \(B=1\) mT maydondagi siklotron chastotasi \(f\)?", "≈ 28 MGs"),
        (r"\(k=8\) N/m, \(m=2\) kg ossilyator davri?", r"\(T=2\pi\sqrt{m/k}=\pi\approx3{,}14\) s"),
        (r"Kvadratik qarshilikda qiya otish trayektoriyasi parabolaga nisbatan qanday o‘zgaradi?", "uzoqlik va balandlik kamayadi, tushish qismi tikroq (asimmetrik)")],
 model=("python", r"""import numpy as np
# Kvadratik havo qarshiligi bilan qiya otish (RK4)
g, m, c = 9.81, 0.145, 0.0013   # beysbol to'pi
def f(s):
    x, y, vx, vy = s; v = np.hypot(vx, vy)
    return np.array([vx, vy, -c/m*v*vx, -g - c/m*v*vy])
for cc in (0.0, c):
    c = cc; v0, a = 40.0, np.radians(45)
    s = np.array([0, 0, v0*np.cos(a), v0*np.sin(a)]); dt = 1e-3; H = 0
    while s[1] >= 0:
        k1=f(s); k2=f(s+dt/2*k1); k3=f(s+dt/2*k2); k4=f(s+dt*k3)
        s = s + dt/6*(k1+2*k2+2*k3+k4); H = max(H, s[1])
    print(f"c={cc}:  uzoqlik={s[0]:.1f} m  balandlik={H:.1f} m")"""),
 questions=["Dinamikaning to‘g‘ri va teskari masalalari nimasi bilan farq qiladi?", "Yechim yagona bo‘lishi uchun nechta boshlang‘ich shart kerak?", "Magnit maydon zarra energiyasini o‘zgartiradimi?", "Oxirgi tezlik qanday shartdan topiladi?"]))

A.append(dict(n=6, lec=7, sim="orbit", tn=["TN5", "TN8", "TN21"],
 title=r"Markaziy kuch maydoni",
 goal=r"Markaziy maydonda harakat integrallari va effektiv potensialdan foydalanib, orbita parametrlari, burilish nuqtalari, Kepler qonunlari va kosmik manyovrlar bilan bog‘liq masalalarni yechish.",
 theory=r"""<p>Integrallar: \(M=\mu r^2\dot\varphi\), \(E=\frac{\mu\dot r^2}{2}+U_{eff}(r)\), \(U_{eff}=U+\frac{M^2}{2\mu r^2}\). Trayektoriya:</p>
$$\varphi=\int\frac{M\,dr/r^2}{\sqrt{2\mu(E-U)-M^2/r^2}}+\text{const}.$$
<p>Aylana orbita \(U_{eff}\) minimumida: \(U'(r_0)=M^2/\mu r_0^3\). \(U=kr^n\) uchun aylana orbita turg‘un bo‘lishi sharti \(n\gt-2\). Kepler masalasi: \(a=\alpha/2|E|\), \(T^2=4\pi^2a^3/GM\), vis-viva formulasi \(v^2=GM\left(\frac2r-\frac1a\right)\).</p>""",
 solved=[("Gomann o‘tishi", r"Kosmik apparat 300 km balandlikdagi aylana orbitadan (\(r_1=6671\) km) geostatsionar orbitaga (\(r_2=42\,164\) km) Gomann ellipsi bo‘ylab o‘tadi. \(\Delta v_1\), \(\Delta v_2\) va o‘tish vaqtini toping.",
          r"\(v_1=\sqrt{GM/r_1}=7{,}73\) km/s; \(\Delta v_1=v_1\left(\sqrt{2r_2/(r_1+r_2)}-1\right)=2{,}43\) km/s. \(v_2=3{,}07\) km/s; \(\Delta v_2=v_2\left(1-\sqrt{2r_1/(r_1+r_2)}\right)=1{,}47\) km/s. Jami 3,90 km/s. O‘tish vaqti — ellips davrining yarmi: 5,27 soat."),
         ("Oy davri", r"Oy orbitasi radiusi \(a=384\,400\) km. Kepler III qonuni bo‘yicha davrni toping (\(GM_\oplus=3{,}986\cdot10^{14}\) m³/s²).",
          r"\(T=2\pi\sqrt{a^3/GM}=2{,}37\cdot10^6\) s \(=27{,}45\) sutka (siderik davr 27,32 sutka; farq — Oy massasi \(m_1+m_2\) da hisobga olinmagan)."),
         ("Burilish nuqtalari", r"\(\mu=1\), \(\alpha=1\), \(M=1\), \(E=-0{,}375\) birliklarda Kepler masalasida \(r_{min}\), \(r_{max}\) va eksentrisitetni toping.",
          r"\(E=-1/r+1/2r^2\) ⇒ \(0{,}375r^2-r+0{,}5=0\) ⇒ \(r=\frac{1\pm0{,}5}{0{,}75}\): \(r_{min}=0{,}667\), \(r_{max}=2\). \(e=\sqrt{1+2EM^2}=0{,}5\), \(a=1{,}333\) ✓.")],
 tasks=[(r"Mars orbitasi \(a=1{,}524\) a.b. Davri necha yil?", r"\(1{,}524^{3/2}=1{,}88\) yil"),
        (r"\(U=kr^n\) maydonida aylana orbita turg‘unligi shartini \(U_{eff}''>0\) dan keltirib chiqaring.", r"\(n>-2\)"),
        (r"Geostatsionar orbita radiusi (\(T=86\,164\) s)?", r"\(r=\sqrt[3]{GMT^2/4\pi^2}=42\,164\) km"),
        (r"Yo‘ldosh perigeyda \(r_p=7000\) km, apogeyda \(r_a=14\,000\) km. Perigeydagi tezlik (vis-viva)?", r"\(a=10\,500\) km, \(v_p=\sqrt{GM(2/r_p-1/a)}=8{,}72\) km/s")],
 model=("python", r"""import numpy as np
from math import pi, sqrt
GM = 3.986e14
def hohmann(r1, r2):
    v1, v2 = sqrt(GM/r1), sqrt(GM/r2); a = (r1 + r2)/2
    dv1 = v1*(sqrt(2*r2/(r1 + r2)) - 1); dv2 = v2*(1 - sqrt(2*r1/(r1 + r2)))
    return dv1, dv2, pi*sqrt(a**3/GM)
dv1, dv2, t = hohmann(6671e3, 42164e3)
print(f"dv1={dv1/1e3:.3f} km/s  dv2={dv2/1e3:.3f} km/s  jami={(dv1+dv2)/1e3:.3f} km/s  t={t/3600:.2f} soat")
# Effektiv potensial (birliksiz): burilish nuqtalari
E, M = -0.375, 1.0
r = np.linspace(0.3, 3, 100000); Ueff = -1/r + M**2/(2*r**2)
idx = np.where(np.diff(np.sign(E - Ueff)))[0]
print("burilish nuqtalari:", r[idx].round(3))"""),
 questions=["Effektiv potensialning ikkinchi hadi qanday fizik ma’noga ega?", "Qachon markaziy maydondagi orbita yopiq bo‘ladi (Bertran teoremasi)?", "Gomann o‘tishi nima uchun energetik jihatdan tejamli?", "Vis-viva formulasini energiya saqlanishidan keltirib chiqaring."]))

A.append(dict(n=7, lec=8, sim="scatter", tn=["TN1", "TN5", "TN11"],
 title=r"Kulon maydoni",
 goal=r"Tortuvchi va itaruvchi Kulon maydonlarida zarra harakatini tahlil qilish: klassik atom modeli, giperbolik trayektoriyalar, eng yaqin kelish masofasi va ikki zaryad tizimining energiyasi.",
 theory=r"""<p>\(U=\pm\alpha/r\), \(\alpha=k|q_1q_2|\), \(k=1/4\pi\varepsilon_0=8{,}988\cdot10^9\) N·m²/C². Tortishishda Kepler masalasining barcha natijalari o‘rinli. Itarishda faqat \(E>0\) bo‘lishi mumkin va trayektoriya giperbolaning tashqi tarmog‘i bo‘ladi:</p>
$$\frac pr=-1+e\cos\varphi,\qquad r_{min}=\frac{\alpha}{2E}\left(1+\sqrt{1+\left(\frac{2Eb}{\alpha}\right)^2}\right).$$
<p>Yadro fizikasida qulay: \(e^2/4\pi\varepsilon_0=1{,}44\) MeV·fm. Laboratoriya energiyasi \(E_L\) bo‘lsa, MM sistemadagi energiya \(E=E_L\,m_2/(m_1+m_2)\).</p>""",
 solved=[("Klassik vodorod atomi", r"Elektron protonning atrofida \(r=0{,}529\cdot10^{-10}\) m radiusli aylana bo‘ylab harakatlanadi deb hisoblab, uning tezligi va to‘liq energiyasini (eV da) toping.",
          r"\(mv^2/r=ke^2/r^2\) ⇒ \(v=\sqrt{ke^2/mr}=2{,}19\cdot10^6\) m/s (\(\approx c/137\)). \(E=-ke^2/2r=-13{,}6\) eV — Bor modeli natijasi."),
         ("Ikki zaryadning itarishi", r"Massasi 1 g, zaryadi 1 mkC bo‘lgan ikki sharcha 10 sm masofada tinch holatdan qo‘yib yuborildi. Ularning oxirgi tezliklari?",
          r"Boshlang‘ich energiya \(kq^2/r=8{,}99\cdot10^9\cdot10^{-12}/0{,}1=0{,}0899\) J; impuls saqlanishidan teng bo‘linadi: \(mv^2/2=0{,}0449\) J ⇒ \(v=9{,}48\) m/s."),
         ("Yadroga yaqinlashish", r"Laboratoriyada 1 MeV energiyali proton tinch protonga markaziy yo‘nalishda uchmoqda. Eng yaqin kelish masofasi?",
          r"MM sistemada \(E=0{,}5\) MeV ⇒ \(d_0=\alpha/E=1{,}44/0{,}5=2{,}88\) fm — yadro kuchlari radiusiga yaqin.")],
 tasks=[(r"7,7 MeV alfa-zarraning oltin yadrosiga (\(Z=79\)) eng yaqin kelish masofasi (yadro tepkisi hisobga olinmasin)?", r"\(227{,}5/7{,}7=29{,}5\) fm"),
        (r"Klassik vodorod atomida elektronning aylanish davri?", r"\(T=2\pi r/v=1{,}52\cdot10^{-16}\) s"),
        (r"Tortuvchi Kulon maydonida \(E=0\) bo‘lsa, trayektoriya turi?", "parabola"),
        (r"Itaruvchi maydonda \(b\to\infty\) da sochilish burchagi nimaga intiladi?", "0 ga")],
 model=("python", r"""import numpy as np
# Itaruvchi Kulon maydonida trayektoriyalar va r_min (birliklar: MeV, fm)
alpha, E, m = 227.5, 5.0, 1.0           # alfa + Au, 5 MeV (birlik massa — burchaklar massaga bog'liq emas)
acc = lambda r: alpha/m*r/np.linalg.norm(r)**3
for b in (10, 22.75, 50):
    r = np.array([-3000.0, b]); dt = 0.02; rmin = 1e9
    v = np.array([np.sqrt(2*(E - alpha/np.linalg.norm(r))/m), 0.0])   # energiya saqlanishi
    v = v + 0.5*dt*acc(r)
    while np.linalg.norm(r) < 3100:
        r = r + dt*v; v = v + dt*acc(r); rmin = min(rmin, np.linalg.norm(r))
    chi = np.degrees(np.arctan2(v[1], v[0]))
    teor = alpha/(2*E)*(1 + np.sqrt(1 + (2*E*b/alpha)**2))
    print(f"b={b:6.2f} fm  chi={chi:6.1f}°  (nazariya {np.degrees(2*np.arctan(alpha/(2*E*b))):.1f}°)  rmin={rmin:.2f} fm  (nazariya {teor:.2f})")"""),
 questions=["Tortuvchi va itaruvchi Kulon maydonida trayektoriyalar qanday farqlanadi?", "Nima uchun klassik atom modeli beqaror (nurlanish)?", "MM sistemaga o‘tish energiyani qanday o‘zgartiradi?", "\\(r_{min}\\) formulasini energiya va impuls momenti saqlanishidan keltirib chiqaring."]))

A.append(dict(n=8, lec=11, sim="collision", tn=["TN6", "TN8", "TN21"],
 title=r"Ikki jism masalasi. To‘qnashuv diagrammalari",
 goal=r"Ikki jism masalasida massa markazi va keltirilgan massani topish, elastik va noelastik to‘qnashuvlarni impulslar diagrammasi yordamida MM va L sistemalarida tahlil qilish.",
 theory=r"""<p>MM: \(\vec R=\frac{m_1\vec r_1+m_2\vec r_2}{m_1+m_2}\); jismlar MM dan \(r_1=\frac{m_2}{m_1+m_2}r\), \(r_2=\frac{m_1}{m_1+m_2}r\) masofada. To‘qnashuvda (2-zarra tinch): MM tezligi \(V=\frac{m_1v}{m_1+m_2}\), MM sistemada tezliklar \(u_1=\frac{m_2v}{m_1+m_2}\), \(u_2=\frac{m_1v}{m_1+m_2}\).</p>
$$\vec v_1'=\vec V+u_1\vec n_0,\qquad\vec v_2'=\vec V-u_2\vec n_0,\qquad\operatorname{tg}\theta_1=\frac{m_2\sin\chi}{m_1+m_2\cos\chi}.$$
<p>Mutlaq noelastik to‘qnashuvda \(V=\frac{m_1v}{m_1+m_2}\), yo‘qolgan energiya \(\Delta E=\frac{\mu v^2}{2}\).</p>""",
 solved=[("Yer–Oy sistemasi", r"Yer–Oy massa markazi Yer markazidan qancha masofada (\(m_\oplus=5{,}97\cdot10^{24}\), \(m_☾=7{,}35\cdot10^{22}\) kg, \(r=384\,400\) km)? Keltirilgan massa?",
          r"\(r_1=r\,m_☾/(m_\oplus+m_☾)=4675\) km — Yer ichida (\(R=6371\) km). \(\mu=m_\oplus m_☾/(m_\oplus+m_☾)=7{,}26\cdot10^{22}\) kg."),
         ("Diagramma bo‘yicha elastik to‘qnashuv", r"\(m_1=1\) kg, \(v=4\) m/s, \(m_2=3\) kg tinch; MM sistemada \(\chi=90^\circ\). L sistemadagi tezliklar va burchaklar?",
          r"\(V=1\), \(u_1=3\), \(u_2=1\) m/s. \(\vec v_1'=(1;\,3)\): \(v_1'=3{,}16\) m/s, \(\theta_1=71{,}6^\circ\). \(\vec v_2'=(1;\,-1)\): \(v_2'=1{,}41\) m/s, \(\theta_2=45^\circ\). Tekshiruv: \(5+3=8\) J ✓."),
         ("Ballistik mayatnik", r"10 g o‘q 500 m/s tezlik bilan 2 kg yog‘och brusokka kirib qoldi. Brusok tezligi, energiya yo‘qotish ulushi va ko‘tarilish balandligi?",
          r"\(V=0{,}01\cdot500/2{,}01=2{,}49\) m/s. Yo‘qotish ulushi \(m_2/(m_1+m_2)=99{,}5\) %. \(h=V^2/2g=0{,}315\) m.")],
 tasks=[(r"Teng massalar, \(\chi=60^\circ\): \(\theta_1\), \(\theta_2\)?", r"\(30^\circ\), \(60^\circ\)"),
        (r"\(m_1=4m_2\): maksimal sochilish burchagi?", r"\(\arcsin0{,}25=14{,}5^\circ\)"),
        (r"Elastik markaziy to‘qnashuvda \(m_1=1\), \(m_2=3\) kg, \(v=4\) m/s: tezliklar?", r"\(v_1'=-2\) m/s, \(v_2'=2\) m/s"),
        (r"Quyosh–Yupiter MM Quyosh markazidan qancha masofada (\(m_J/m_\odot=9{,}55\cdot10^{-4}\), \(a=7{,}78\cdot10^8\) km)?", r"≈ \(7{,}4\cdot10^5\) km — Quyosh sirtidan tashqarida")],
 model=("python", r"""import numpy as np
# Impulslar diagrammasi: chi bo'yicha L sistemadagi burchaklar va energiyalar
m1, m2, v = 1.0, 3.0, 4.0
V, u1, u2 = m1*v/(m1+m2), m2*v/(m1+m2), m1*v/(m1+m2)
for chi in np.radians([0, 30, 60, 90, 120, 150, 180]):
    v1 = np.array([V + u1*np.cos(chi),  u1*np.sin(chi)])
    v2 = np.array([V - u2*np.cos(chi), -u2*np.sin(chi)])
    E1, E2 = m1*v1@v1/2, m2*v2@v2/2
    print(f"chi={np.degrees(chi):5.0f}°  th1={np.degrees(np.arctan2(v1[1], v1[0])):6.1f}°  "
          f"th2={np.degrees(np.arctan2(-v2[1], v2[0])):5.1f}°  E1={E1:.3f}  E2={E2:.3f}  sum={E1+E2:.3f}")"""),
 questions=["Ikki jism masalasini bir jism masalasiga qanday keltiramiz?", "Impulslar diagrammasini qanday quramiz?", "Qachon to‘qnashuvdan keyin birinchi zarra orqaga qaytishi mumkin?", "Noelastik to‘qnashuvda qaysi energiya “yo‘qolmaydi”?"]))

A.append(dict(n=9, lec=8, sim="scatter", tn=["TN1", "TN11", "TN24"],
 title=r"Elastik sochilish. Effektiv kesim",
 goal=r"Differensial va to‘liq effektiv kesimlarni hisoblash, Rezerford formulasini tajriba sharoitlariga (folga qalinligi, detektor burchagi) qo‘llash va qattiq shar modelida kesimni topish.",
 theory=r"""<p>\(d\sigma=2\pi b\,db\), \(\dfrac{d\sigma}{d\Omega}=\dfrac{b}{\sin\chi}\left|\dfrac{db}{d\chi}\right|\). Yupqa nishonda (konsentratsiya \(n\), qalinlik \(t\)) \(\chi\) dan katta burchakka sochilgan zarralar ulushi:</p>
$$f(\gt\chi)=n\,t\,\pi b^2(\chi).$$
<p>Rezerford: \(b=\frac{\alpha}{2E}\operatorname{ctg}\frac\chi2\), \(\frac{d\sigma}{d\Omega}=\left(\frac{\alpha}{4E}\right)^2\sin^{-4}\frac\chi2\). Qattiq shar: \(b=R\cos\frac\chi2\), \(\frac{d\sigma}{d\Omega}=\frac{R^2}{4}\), \(\sigma=\pi R^2\). 1 barn \(=10^{-28}\) m² \(=100\) fm².</p>""",
 solved=[("Geyger–Marsden tajribasi", r"5 MeV alfa-zarralar qalinligi 1 mkm oltin folgaga tushmoqda (\(n=5{,}9\cdot10^{28}\) m⁻³). \(90^\circ\) dan katta burchakka sochilganlar ulushi?",
          r"\(b(90^\circ)=22{,}75\) fm. \(f=nt\pi b^2=5{,}9\cdot10^{28}\cdot10^{-6}\cdot\pi\cdot(22{,}75\cdot10^{-15})^2=9{,}6\cdot10^{-5}\) — taxminan 10 000 tadan bittasi."),
         ("Burchaklar bo‘yicha nisbat", r"Rezerford sochilishida \(30^\circ\) va \(90^\circ\) dagi differensial kesimlar nisbati?",
          r"\(\sin^4 45^\circ/\sin^4 15^\circ=0{,}25/0{,}00449=55{,}7\)."),
         ("Qattiq shar", r"Qattiq shar uchun \(b=R\cos(\chi/2)\) dan \(d\sigma/d\Omega\) ni keltirib chiqaring.",
          r"\(|db/d\chi|=\frac R2\sin\frac\chi2\); \(\frac{d\sigma}{d\Omega}=\frac{R\cos(\chi/2)\cdot\frac R2\sin(\chi/2)}{\sin\chi}=\frac{R^2}{4}\) — izotrop; \(\sigma=4\pi\cdot R^2/4=\pi R^2\).")],
 tasks=[(r"5 MeV, \(Z=79\): \(\chi=60^\circ\) uchun nishon parametri?", r"\(22{,}75\cdot\sqrt3=39{,}4\) fm"),
        (r"Shu sharoitda \(\chi=180^\circ\) dagi \(d\sigma/d\Omega\)?", r"\(11{,}38^2=129\) fm² = 1,29 b/sr"),
        (r"Energiya 2 marta oshsa, \(b(90^\circ)\) va \(f(\gt90^\circ)\) qanday o‘zgaradi?", r"\(b\) 2 marta, \(f\) 4 marta kamayadi"),
        (r"Kesimni \(\chi\) bo‘yicha \(\chi_0\) dan \(\pi\) gacha integrallab, \(\sigma(\gt\chi_0)=\pi b^2(\chi_0)\) ekanini ko‘rsating.", r"\(\int(d\sigma/d\Omega)2\pi\sin\chi\,d\chi=\pi\left(\frac{\alpha}{2E}\right)^2\operatorname{ctg}^2\frac{\chi_0}2\)")],
 model=("python", r"""import numpy as np
# Rezerford kesimini Monte-Karlo bilan tekshirish
alpha, E = 227.5, 5.0                 # MeV*fm, MeV
bmax = 200.0                          # fm
rng = np.random.default_rng(1)
b = bmax*np.sqrt(rng.random(2_000_000))   # nishon yuzasi bo'yicha bir tekis
chi = 2*np.arctan(alpha/(2*E*b))
for c0 in (30, 60, 90, 150):
    frac = np.mean(chi > np.radians(c0))
    sigma_mc = frac*np.pi*bmax**2
    sigma_th = np.pi*(alpha/(2*E))**2/np.tan(np.radians(c0)/2)**2
    print(f"chi>{c0:3d}°  sigma_MC={sigma_mc:8.1f} fm^2   nazariya={sigma_th:8.1f} fm^2")"""),
 questions=["Effektiv kesim qaysi o‘lchovli kattalik va nima uchun?", "Qattiq shar sochilishi nima uchun izotrop?", "Folga qalinligi qanday tanlanadi (bir martalik sochilish sharti)?", "Kesim \\(1/E^2\\) ga proporsionalligining fizik ma’nosi?"]))

A.append(dict(n=10, lec=4, sim="dpend", tn=["TN4", "TN5", "TN16", "TN17"],
 title=r"Lagranj funksiyasi va Lagranj tenglamalari",
 goal=r"Turli mexanik sistemalar (Atvud mashinasi, aylanayotgan halqadagi munchoq, qo‘sh mayatnik) uchun Lagranj funksiyasini tuzish, ikkinchi tur Lagranj tenglamalarini yozish va yechish.",
 theory=r"""<p>Algoritm: umumlashgan koordinatalar → \(T(q,\dot q)\) → \(U(q)\) → \(L=T-U\) → \(\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}=\frac{\partial L}{\partial q_i}\). Qo‘sh mayatnik (\(m_1,m_2,l_1,l_2\)):</p>
$$L=\frac{m_1+m_2}{2}l_1^2\dot\varphi_1^2+\frac{m_2}{2}l_2^2\dot\varphi_2^2+m_2l_1l_2\dot\varphi_1\dot\varphi_2\cos(\varphi_1-\varphi_2)+(m_1+m_2)gl_1\cos\varphi_1+m_2gl_2\cos\varphi_2.$$
<p>Kichik tebranishlarda (\(m_1=m_2\), \(l_1=l_2=l\)) xos chastotalar \(\omega^2=(2\mp\sqrt2)g/l\). Katta amplitudalarda harakat xaotik bo‘ladi.</p>""",
 solved=[("Atvud mashinasi", r"\(m_1=3\) kg va \(m_2=2\) kg yuklar vaznsiz blok orqali osilgan. Lagranj tenglamasidan tezlanishni toping. Blok \(I/R^2=1\) kg bo‘lsa-chi?",
          r"\(q=x\): \(L=\frac12(m_1+m_2+I/R^2)\dot x^2+(m_1-m_2)gx\) ⇒ \(a=\frac{(m_1-m_2)g}{m_1+m_2+I/R^2}\). Vaznsiz blokda \(a=1{,}96\) m/s², \(I/R^2=1\) kg da \(a=1{,}64\) m/s²."),
         ("Aylanayotgan halqadagi munchoq", r"Radiusi \(R=0{,}2\) m halqa vertikal o‘q atrofida \(\Omega=10\) rad/s bilan aylanmoqda. Munchoqning harakat tenglamasi va muvozanat holatlari?",
          r"\(L=\frac m2R^2(\dot\theta^2+\Omega^2\sin^2\theta)+mgR\cos\theta\) ⇒ \(\ddot\theta=\sin\theta\,(\Omega^2\cos\theta-g/R)\). Muvozanatlar: \(\theta=0\) (\(\Omega^2\gt g/R\) bo‘lgani uchun beqaror), \(\cos\theta_0=g/(R\Omega^2)=0{,}49\) ⇒ \(\theta_0=60{,}6^\circ\) (turg‘un)."),
         ("Qo‘sh mayatnik normal modalari", r"\(m_1=m_2\), \(l_1=l_2=1\) m qo‘sh mayatnikning kichik tebranishlar chastotalarini toping.",
          r"\(\omega_{1,2}=\sqrt{(2\mp\sqrt2)g/l}\): \(\omega_1=2{,}40\) rad/s (\(A_2/A_1=\sqrt2\), bir fazada), \(\omega_2=5{,}79\) rad/s (\(A_2/A_1=-\sqrt2\), qarama-qarshi fazada).")],
 tasks=[(r"Qo‘zg‘almas qiya tekislikda (\(\alpha\)) ishqalanishsiz sirpanayotgan jism uchun \(L\) va tezlanish?", r"\(L=\frac m2\dot s^2+mgs\sin\alpha\), \(a=g\sin\alpha\)"),
        (r"Prujinali mayatnik (\(k\), \(l_0\), tekislikda) uchun Lagranj funksiyasi?", r"\(L=\frac m2(\dot r^2+r^2\dot\varphi^2)-\frac k2(r-l_0)^2+mgr\cos\varphi\)"),
        (r"Munchoq masalasida \(\Omega\) ning qaysi qiymatidan boshlab yon muvozanat paydo bo‘ladi (\(R=0{,}2\) m)?", r"\(\Omega_{kr}=\sqrt{g/R}=7{,}0\) rad/s"),
        (r"Osilish nuqtasi gorizontal \(x_0=a\cos\gamma t\) bo‘yicha tebranayotgan mayatnik tenglamasi?", r"\(l\ddot\varphi+g\sin\varphi=a\gamma^2\cos\gamma t\cos\varphi\)")],
 model=("python", r"""import numpy as np
# Qo'sh mayatnik: Lagranj tenglamalarini RK4 bilan yechish, energiya nazorati
g, m1, m2, l1, l2 = 9.81, 1, 1, 1, 1
def f(s):
    a, b, wa, wb = s; d = a - b
    M = np.array([[(m1+m2)*l1, m2*l2*np.cos(d)], [l1*np.cos(d), l2]])
    rhs = np.array([-m2*l2*wb**2*np.sin(d) - (m1+m2)*g*np.sin(a),
                     l1*wa**2*np.sin(d) - g*np.sin(b)])
    return np.array([wa, wb, *np.linalg.solve(M, rhs)])
def energy(s):
    a, b, wa, wb = s
    T = (m1+m2)/2*l1**2*wa**2 + m2/2*l2**2*wb**2 + m2*l1*l2*wa*wb*np.cos(a-b)
    return T - (m1+m2)*g*l1*np.cos(a) - m2*g*l2*np.cos(b)
s = np.array([np.radians(120), np.radians(-10), 0, 0]); dt = 1e-3; E0 = energy(s)
for k in range(10001):
    if k % 2000 == 0: print(f"t={k*dt:4.1f}  phi1={np.degrees(s[0]):8.1f}  phi2={np.degrees(s[1]):8.1f}  dE={energy(s)-E0:.2e}")
    k1=f(s); k2=f(s+dt/2*k1); k3=f(s+dt/2*k2); k4=f(s+dt*k3); s = s + dt/6*(k1+2*k2+2*k3+k4)"""),
 questions=["Qo‘sh mayatnikning erkinlik darajasi nechta?", "Nima uchun katta amplitudalarda harakat xaotik?", "Aylanayotgan halqada \\(h\\) saqlanadimi, \\(E\\) saqlanadimi?", "Lagranj usuli Nyuton usulidan qaysi masalalarda afzal?"]))

A.append(dict(n=11, lec=10, sim="phase", tn=["TN4", "TN5", "TN16", "TN17"],
 title=r"Gamilton funksiyasi va kanonik tenglamalar",
 goal=r"Turli sistemalar uchun Gamilton funksiyasini tuzish, kanonik tenglamalarni yozish va yechish, fazaviy trayektoriyalarni qurish.",
 theory=r"""<p>Tartib: \(L\) → \(p_i=\partial L/\partial\dot q_i\) → \(\dot q_i\) ni \(p\) orqali ifodalash → \(H=\sum p_i\dot q_i-L\). Muhim misollar:</p>
<ul><li>Markaziy maydon: \(H=\frac{p_r^2}{2m}+\frac{p_\varphi^2}{2mr^2}+U(r)\).</li><li>Mayatnik: \(H=\frac{p_\theta^2}{2ml^2}-mgl\cos\theta\).</li><li>Elektromagnit maydondagi zaryad: \(H=\frac{(\vec p-q\vec A)^2}{2m}+q\varphi\).</li></ul>
$$\dot q_i=\frac{\partial H}{\partial p_i},\qquad\dot p_i=-\frac{\partial H}{\partial q_i}.$$""",
 solved=[("Markaziy maydon", r"Qutb koordinatalarida markaziy maydondagi zarra uchun \(H\) va kanonik tenglamalarni yozing.",
          r"\(p_r=m\dot r\), \(p_\varphi=mr^2\dot\varphi\); \(H=\frac{p_r^2}{2m}+\frac{p_\varphi^2}{2mr^2}+U\). \(\dot p_\varphi=-\partial H/\partial\varphi=0\) (moment saqlanadi), \(\dot p_r=\frac{p_\varphi^2}{mr^3}-U'(r)\)."),
         ("Ossilyator", r"\(m=0{,}5\) kg, \(k=2\) N/m, \(q_0=0{,}1\) m, \(p_0=0\). Kanonik tenglamalarni yeching, energiya va fazaviy trayektoriya?",
          r"\(\omega=2\) rad/s. \(q=0{,}1\cos2t\), \(p=-0{,}1\sin2t\) kg·m/s. \(E=kq_0^2/2=0{,}01\) J. Trayektoriya: \(q^2/0{,}01+p^2/0{,}01=1\) — bu holda aylana."),
         ("Puasson qavsi", r"\(\{p_x,L_z\}\) ni hisoblang (\(L_z=xp_y-yp_x\)).",
          r"\(\{p_x,L_z\}=\sum\left(\frac{\partial p_x}{\partial q}\frac{\partial L_z}{\partial p}-\frac{\partial p_x}{\partial p}\frac{\partial L_z}{\partial q}\right)=-\frac{\partial L_z}{\partial x}=-p_y\).")],
 tasks=[(r"Bir jinsli og‘irlik maydonida vertikal otilgan jism uchun \(H\) va kanonik tenglamalar?", r"\(H=p^2/2m+mgz\); \(\dot z=p/m\), \(\dot p=-mg\)"),
        (r"\(L=\frac m2(\dot x^2+\dot y^2)+\frac{qB}{2}(x\dot y-y\dot x)\) uchun \(p_x\), \(p_y\)?", r"\(p_x=m\dot x-qBy/2\), \(p_y=m\dot y+qBx/2\)"),
        (r"Mayatnik uchun separatrisa energiyasi?", r"\(E=mgl\) (\(H\) da \(U=-mgl\cos\theta\) bilan)"),
        (r"\(\{L_x,L_y\}\) = ?", r"\(L_z\)")],
 model=("python", r"""import numpy as np
# Mayatnik fazaviy portreti: simplektik (leapfrog) integrallash
g, l, m = 9.81, 1.0, 1.0
H = lambda q, p: p**2/(2*m*l**2) - m*g*l*np.cos(q)
dt = 1e-3
for E in (-5, 0, 9.81, 15):
    q = 0.0; p = np.sqrt(2*m*l**2*(E + m*g*l)); qmax = 0
    for k in range(20000):
        p -= dt/2*m*g*l*np.sin(q); q += dt*p/(m*l**2); p -= dt/2*m*g*l*np.sin(q)
        qmax = max(qmax, abs(q))
    turi = "tebranish" if qmax < np.pi else "aylanish/separatrisa"
    print(f"E={E:6.2f} J  q_max={np.degrees(qmax):8.1f}°  H oxirida={H(q, p):.4f}  -> {turi}")"""),
 questions=["Lejandr almashtirishining geometrik ma’nosi nima?", "Kanonik tenglamalarning afzalligi nimada?", "Elektromagnit maydonda kanonik va kinetik impuls farqi?", "Fazaviy trayektoriyalar nima uchun kesishmaydi?"]))

A.append(dict(n=12, lec=10, sim="action", tn=["TN5", "TN19", "TN20"],
 title=r"Gamilton–Yakobi tenglamasi",
 goal=r"Gamilton–Yakobi tenglamasini tuzish, o‘zgaruvchilarni ajratish usuli bilan to‘liq integralni topish va undan harakat qonunini olish.",
 theory=r"""<p>Ta’sir yuqori chegaraning funksiyasi sifatida: \(\partial S/\partial q_i=p_i\), \(\partial S/\partial t=-H\). Shundan <b>Gamilton–Yakobi tenglamasi</b> kelib chiqadi:</p>
$$\frac{\partial S}{\partial t}+H\left(q,\frac{\partial S}{\partial q},t\right)=0.$$
<p>\(H\) vaqtga bog‘liq bo‘lmasa, \(S=-Et+W(q)\). To‘liq integral \(S(q,\alpha,t)\) (\(\alpha_i\) — \(s\) ta doimiy) topilsa, harakat qonuni \(\partial S/\partial\alpha_i=\beta_i\) dan olinadi. Siklik koordinata uchun \(W=p_\varphi\varphi+\ldots\). Ta’sir o‘zgaruvchisi \(J=\oint p\,dq\).</p>""",
 solved=[("Erkin zarra", r"Bir o‘lchovli erkin zarra uchun Gamilton–Yakobi tenglamasini yeching.",
          r"\(\frac{\partial S}{\partial t}+\frac1{2m}\left(\frac{\partial S}{\partial x}\right)^2=0\); \(S=-Et+\sqrt{2mE}\,x\). \(\partial S/\partial E=-t+x\sqrt{m/2E}=\beta\) ⇒ \(x=\sqrt{2E/m}\,(t+\beta)\) — tekis harakat."),
         ("Garmonik ossilyator", r"\(H=\frac{p^2}{2m}+\frac{m\omega^2q^2}{2}\) uchun harakat qonunini Gamilton–Yakobi usulida toping.",
          r"\(S=-Et+\int\sqrt{2mE-m^2\omega^2q^2}\,dq\). \(\frac{\partial S}{\partial E}=-t+\frac1\omega\arcsin\left(q\sqrt{\frac{m\omega^2}{2E}}\right)=\beta\) ⇒ \(q=\sqrt{\frac{2E}{m\omega^2}}\sin\omega(t+\beta)\)."),
         ("Ta’sir o‘zgaruvchisi", r"Ossilyator uchun \(J=\oint p\,dq\) ni hisoblang; \(m=1\), \(\omega=2\), \(E=8\) J.",
          r"Fazaviy ellips yuzasi: \(J=\pi\sqrt{2mE}\sqrt{2E/m\omega^2}=2\pi E/\omega=8\pi\approx25{,}1\) J·s. \(E=\omega J/2\pi\) ⇒ \(\partial E/\partial J=\omega/2\pi=\nu\).")],
 tasks=[(r"Bir jinsli og‘irlik maydonidagi (\(U=mgz\)) jism uchun \(W(z)\)?", r"\(W=\int\sqrt{2m(E-mgz)}\,dz=-\frac{2\sqrt{2m}}{3mg}(E-mgz)^{3/2}\)"),
        (r"Markaziy maydon uchun o‘zgaruvchilarni ajrating.", r"\(S=-Et+M\varphi+\int\sqrt{2m(E-U)-M^2/r^2}\,dr\)"),
        (r"Bor–Zommerfeld sharti \(J=nh\) ossilyator uchun qanday energiya beradi?", r"\(E_n=n\hbar\omega\)"),
        (r"Gamilton–Yakobi tenglamasi qaysi optik tenglamaga o‘xshash?", "eykonal tenglamasi (geometrik optika)")],
 model=("python", r"""import numpy as np
# Ta'sir o'zgaruvchisi J = ∮p dq ni sonli hisoblash va davr T = dJ/dE
m, w = 1.0, 2.0
def J(E, U=lambda q: 0.5*m*w**2*q**2):
    qmax = np.sqrt(2*E/(m*w**2))
    q = np.linspace(-qmax, qmax, 200001)
    p = np.sqrt(np.maximum(2*m*(E - U(q)), 0))
    trap = getattr(np, "trapezoid", None) or np.trapz
    return 2*trap(p, q)
for E in (2, 8, 18):
    dE = 1e-4; T = (J(E+dE) - J(E-dE))/(2*dE)
    print(f"E={E:3d}  J={J(E):8.4f}  (2piE/w={2*np.pi*E/w:8.4f})  T=dJ/dE={T:.4f}  (2pi/w={2*np.pi/w:.4f})")"""),
 questions=["Gamilton–Yakobi tenglamasidagi \\(S\\) ning fizik ma’nosi?", "To‘liq integral nechta doimiyni o‘z ichiga oladi?", "Qachon o‘zgaruvchilarni ajratish mumkin?", "Gamilton–Yakobi tenglamasi kvant mexanikasiga qanday o‘tadi?"]))

A.append(dict(n=13, lec=3, sim="brach", tn=["TN7", "TN20", "TN25"],
 title=r"Eyler–Lagranj tenglamasi. Variatsion masalalar",
 goal=r"Funksional ekstremumi masalalarini Eyler–Lagranj tenglamasi bilan yechish: eng qisqa yo‘l, braxistoxrona, Ferma prinsipi va minimal sirt.",
 theory=r"""<p>\(J[y]=\int_{x_1}^{x_2}F(y,y',x)\,dx\) funksional ekstremal bo‘lishi uchun Eyler–Lagranj tenglamasi bajarilishi kerak:</p>
$$\frac{d}{dx}\frac{\partial F}{\partial y'}-\frac{\partial F}{\partial y}=0.$$
<p>\(F\) oshkor \(x\) ga bog‘liq bo‘lmasa, birinchi integral mavjud: \(F-y'\frac{\partial F}{\partial y'}=C\) (Beltrami ayniyati). <b>Braxistoxrona</b>: \(F=\sqrt{\frac{1+y'^2}{2gy}}\) (\(y\) pastga) ⇒ sikloida \(x=a(\theta-\sin\theta)\), \(y=a(1-\cos\theta)\).</p>""",
 solved=[("Tekislikda eng qisqa yo‘l", r"Ikki nuqta orasidagi eng qisqa chiziq to‘g‘ri chiziq ekanini isbotlang.",
          r"\(F=\sqrt{1+y'^2}\); \(\partial F/\partial y=0\) ⇒ \(\frac{y'}{\sqrt{1+y'^2}}=C\) ⇒ \(y'=\text{const}\) ⇒ \(y=kx+b\)."),
         ("Braxistoxrona va to‘g‘ri chiziq", r"Jism \((0;0)\) dan \((\pi a;\,2a)\) nuqtaga (\(a=1\) m, \(y\) pastga) sikloida va to‘g‘ri chiziq bo‘ylab ishqalanishsiz sirpanadi. Vaqtlarni solishtiring.",
          r"Sikloida (\(\theta=\pi\)): \(t=\pi\sqrt{a/g}=1{,}003\) s. To‘g‘ri chiziq: \(L=\sqrt{\pi^2+4}=3{,}72\) m, \(\sin\alpha=2/3{,}72=0{,}537\); \(t=\sqrt{2L/(g\sin\alpha)}=1{,}19\) s. Sikloida 16 % tez."),
         ("Ferma prinsipidan Snellius qonuni", r"Yorug‘lik \(n_1\) muhitdagi \(A\) nuqtadan \(n_2\) muhitdagi \(B\) nuqtaga boradi. Optik yo‘l minimumidan sinish qonunini keltirib chiqaring.",
          r"\(\Phi(x)=n_1\sqrt{h_1^2+x^2}+n_2\sqrt{h_2^2+(d-x)^2}\); \(\Phi'(x)=0\) ⇒ \(n_1\sin\alpha_1=n_2\sin\alpha_2\).")],
 tasks=[(r"Braxistoxrona: \(a=0{,}5\) m, eng past nuqtagacha tushish vaqti?", r"\(\pi\sqrt{0{,}5/9{,}81}=0{,}709\) s"),
        (r"Aylanish sirti yuzasini minimallashtiruvchi egri chiziq (\(F=y\sqrt{1+y'^2}\))?", r"zanjir chizig‘i \(y=a\operatorname{ch}\frac{x-x_0}{a}\)"),
        (r"Silindr sirtidagi geodezik chiziq?", "vint chiziq (yoyilganda to‘g‘ri chiziq)"),
        (r"Sikloidaning tautoxronlik xossasi nimadan iborat?", r"pastki nuqtaga tushish vaqti boshlang‘ich balandlikka bog‘liq emas: \(\pi\sqrt{a/g}\)")],
 model=("python", r"""import numpy as np
# Braxistoxrona: to'g'ri chiziq, aylana yoyi va sikloida bo'ylab tushish vaqti
g, a = 9.81, 1.0
X, Y = np.pi*a, 2*a                    # oxirgi nuqta (y pastga)
def T(x, y):                           # t = ∫ ds / sqrt(2 g y)
    ds = np.hypot(np.diff(x), np.diff(y)); ym = (y[1:] + y[:-1])/2
    return np.sum(ds/np.sqrt(2*g*np.maximum(ym, 1e-12)))
th = np.linspace(0, np.pi, 400001)
print("sikloida :", T(a*(th - np.sin(th)), a*(1 - np.cos(th))), " nazariya:", np.pi*np.sqrt(a/g))
s = np.linspace(0, 1, 400001)**2
print("to'g'ri  :", T(X*s, Y*s))
R = (X**2 + Y**2)/(2*X)                # (0,0) da vertikal urinmali aylana yoyi
phi = np.linspace(0, np.arctan2(Y, R - X), 400001)
print("aylana   :", T(R*(1 - np.cos(phi)), R*np.sin(phi)))"""),
 questions=["Funksional va funksiyaning farqi nima?", "Beltrami ayniyati qachon qo‘llaniladi?", "Nima uchun sikloida to‘g‘ri chiziqdan tez?", "Mexanikadagi Gamilton prinsipi bilan bu masalalar qanday bog‘langan?"]))

A.append(dict(n=14, lec=10, sim="noether", tn=["TN8", "TN18", "TN21"],
 title=r"Umumlashgan energiya. Puasson qavslari",
 goal=r"Umumlashgan energiya va mexanik energiyani farqlash, Puasson qavslarini hisoblash va ular yordamida harakat integrallarini topish.",
 theory=r"""<p>Umumlashgan energiya \(h=\sum p_i\dot q_i-L\); \(\partial L/\partial t=0\) bo‘lsa saqlanadi. Nostasionar bog‘lanishlarda \(T=T_2+T_1+T_0\) va \(h=T_2-T_0+U\ne E\).</p>
$$\{f,g\}=\sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right),\qquad\frac{df}{dt}=\frac{\partial f}{\partial t}+\{f,H\}.$$
<p>Foydali qavslar: \(\{q_i,p_k\}=\delta_{ik}\), \(\{L_i,L_j\}=\varepsilon_{ijk}L_k\), \(\{L_i,L^2\}=0\), \(\{f,p_i\}=\partial f/\partial q_i\), \(\{f,q_i\}=-\partial f/\partial p_i\).</p>""",
 solved=[("Aylanayotgan sterjendagi munchoq", r"Munchoq gorizontal tekislikda \(\Omega=5\) rad/s bilan aylanayotgan sterjen bo‘ylab ishqalanishsiz siljiydi; \(r_0=0{,}1\) m, \(\dot r_0=0\). \(h\) va \(E\) saqlanadimi? \(t=0{,}5\) s da \(r\)?",
          r"\(L=\frac m2(\dot r^2+\Omega^2r^2)\), \(\partial L/\partial t=0\) ⇒ \(h=\frac m2(\dot r^2-\Omega^2r^2)\) saqlanadi; \(E=\frac m2(\dot r^2+\Omega^2r^2)\) ortadi (sterjen ish bajaradi). \(\ddot r=\Omega^2r\) ⇒ \(r=r_0\operatorname{ch}\Omega t=0{,}1\operatorname{ch}2{,}5=0{,}613\) m."),
         ("Moment algebrasi", r"\(\{L_x,L_y\}=L_z\) ekanini tekshiring.",
          r"\(L_x=yp_z-zp_y\), \(L_y=zp_x-xp_z\). Nolga teng bo‘lmagan hadlar: \(\frac{\partial L_x}{\partial z}\frac{\partial L_y}{\partial p_z}-\frac{\partial L_x}{\partial p_z}\frac{\partial L_y}{\partial z}=(-p_y)(-x)-y\,p_x=xp_y-yp_x=L_z\)."),
         ("Harakat integralini tekshirish", r"\(H=\frac{p^2}{2m}+U(r)\) uchun \(\{L^2,H\}=0\) ekanini ko‘rsating.",
          r"\(\{L_i,p^2\}=0\) (burilishga invariant), \(\{L_i,U(r)\}=0\) ⇒ \(\{L_i,H\}=0\) ⇒ \(\{L^2,H\}=2\sum L_i\{L_i,H\}=0\).")],
 tasks=[(r"\(\{q,p^2/2\}\) = ?", r"\(p\)"),
        (r"\(\{p,q^2\}\) = ?", r"\(-2q\)"),
        (r"Markaziy maydonda \(p_x^2+p_y^2\) saqlanadimi?", r"yo‘q; \(L_z\) va \(H\) saqlanadi"),
        (r"\(H=p_1p_2+q_1q_2\) uchun \(\{q_1p_1-q_2p_2,H\}\) ni hisoblang.", r"0 — harakat integrali")],
 model=("python", r"""import sympy as sp
# Puasson qavslarini ramziy hisoblash (sympy)
x, y, z, px, py, pz = sp.symbols('x y z p_x p_y p_z')
Q, P = (x, y, z), (px, py, pz)
def PB(f, g):
    return sp.simplify(sum(sp.diff(f, q)*sp.diff(g, p) - sp.diff(f, p)*sp.diff(g, q) for q, p in zip(Q, P)))
Lx, Ly, Lz = y*pz - z*py, z*px - x*pz, x*py - y*px
print("{Lx,Ly} =", PB(Lx, Ly))
print("{px,Lz} =", PB(px, Lz))
r = sp.sqrt(x**2 + y**2 + z**2); m, k = sp.symbols('m k', positive=True)
H = (px**2 + py**2 + pz**2)/(2*m) - k/r
print("{Lx**2+Ly**2+Lz**2, H} =", PB(Lx**2 + Ly**2 + Lz**2, H))"""),
 questions=["Umumlashgan energiya qachon mexanik energiyaga teng?", "Puasson teoremasi nimani ta’kidlaydi?", "\\(\\{L_x,L_y\\}=L_z\\) dan \\(L_x\\) va \\(L_y\\) bir vaqtda saqlansa, nima kelib chiqadi?", "Puasson qavslari va kanonik almashtirishlar qanday bog‘langan?"]))

A.append(dict(n=15, lec=6, sim="oscill", tn=["TN9", "TN22", "TN25"],
 title=r"Bir erkinlik darajali sistemaning majburiy tebranishlari",
 goal=r"Majburiy tebranishlar amplitudasi, fazasi, yutilgan quvvat va rezonans egri chizig‘ining kengligini hisoblash; tepkilar va kinematik qo‘zg‘atish masalalarini yechish.",
 theory=r"""<p>Barqaror rejim: \(b=\dfrac{F_0/m}{\sqrt{(\omega_0^2-\gamma^2)^2+4\beta^2\gamma^2}}\), \(\operatorname{tg}\delta=\dfrac{2\beta\gamma}{\omega_0^2-\gamma^2}\). O‘rtacha yutilgan quvvat:</p>
$$\langle P\rangle=\frac{F_0^2}{m}\frac{\beta\gamma^2}{(\omega_0^2-\gamma^2)^2+4\beta^2\gamma^2},\qquad\langle P\rangle_{max}=\frac{F_0^2}{4m\beta}.$$
<p>Yarim quvvat bo‘yicha kenglik \(\Delta\gamma=2\beta\), asllik \(Q=\omega_0/\Delta\gamma\). So‘nish bo‘lmaganda, \(\gamma\approx\omega_0\) da tepkilar kuzatiladi: \(x\propto\sin\frac{\varepsilon t}{2}\), \(\varepsilon=\gamma-\omega_0\).</p>""",
 solved=[("Rezonansdan tashqarida", r"\(m=0{,}5\) kg, \(\omega_0=20\) rad/s, \(\beta=1\) s⁻¹, \(F_0=2\) N, \(\gamma=15\) rad/s. Amplituda va faza siljishi?",
          r"\(b=4/\sqrt{175^2+900}=4/177{,}6=0{,}0225\) m; \(\operatorname{tg}\delta=30/175\) ⇒ \(\delta=9{,}7^\circ\) (siljish kuchdan orqada)."),
         ("Rezonansda yutilgan quvvat", r"Shu sistema uchun \(\langle P\rangle_{max}\) va yarim quvvat kengligi?",
          r"\(\langle P\rangle_{max}=F_0^2/(4m\beta)=4/2=2\) Vt. \(\Delta\gamma=2\beta=2\) rad/s, \(Q=20/2=10\)."),
         ("Kinematik qo‘zg‘atish", r"Avtomobil osmasining xos chastotasi \(f_0=1{,}5\) Gs. Yo‘l notekisliklari orasidagi masofa 5 m bo‘lsa, qaysi tezlikda rezonans bo‘ladi?",
          r"Qo‘zg‘atish chastotasi \(f=v/\lambda\) ⇒ \(v=f_0\lambda=7{,}5\) m/s = 27 km/soat.")],
 tasks=[(r"\(\gamma=25\) rad/s da (shu sistema) amplituda?", r"\(4/\sqrt{225^2+2500}=0{,}0173\) m"),
        (r"\(\beta=0\), \(\omega_0=20\), \(\gamma=19\) rad/s: tepkilar davri?", r"\(2\pi/|\gamma-\omega_0|=6{,}28\) s"),
        (r"Asllik \(Q=50\) bo‘lsa, rezonansdagi amplituda statik siljishdan necha marta katta?", "≈ 50"),
        (r"So‘nmaydigan ossilyatorga \(\gamma=\omega_0\) kuch ta’sir qilsa, \(x(t)\) qanday o‘sadi?", r"\(x=\frac{F_0}{2m\omega_0}t\sin\omega_0t\) — chiziqli")],
 model=("python", r"""import numpy as np
# Rezonans egri chizig'i va yarim quvvat kengligi; RK4 bilan barqaror amplituda
m, w0, beta, F0 = 0.5, 20.0, 1.0, 2.0
g = np.linspace(10, 30, 2001)
b = F0/m/np.sqrt((w0**2 - g**2)**2 + 4*beta**2*g**2)
P = F0**2/m*beta*g**2/((w0**2 - g**2)**2 + 4*beta**2*g**2)
i = P.argmax(); half = g[P >= P[i]/2]
print(f"b_max={b.max():.4f} m at {g[b.argmax()]:.2f} rad/s;  P_max={P[i]:.3f} W;  kenglik={half[-1]-half[0]:.2f} rad/s")
def steady(gam, T=20.0, dt=1e-3):
    x = v = 0.0; amp = 0
    for k in range(int(T/dt)):
        t = k*dt; a = F0/m*np.cos(gam*t) - 2*beta*v - w0**2*x
        v += a*dt; x += v*dt
        if t > T - 2: amp = max(amp, abs(x))
    return amp
for gam in (15, 20, 25): print(f"gamma={gam}: sonli b={steady(gam):.4f}")"""),
 questions=["Majburiy tebranish qaysi chastotada sodir bo‘ladi: xos yoki tashqi?", "Rezonansda faza siljishi nima uchun \\(\\pi/2\\)?", "Yarim quvvat kengligi va asllik qanday bog‘langan?", "Tepkilar qanday sharoitda kuzatiladi?"]))


# ---------------- Seminarlar (S1–S6, fan dasturi bo‘yicha 12 soat) ----------------
SEM = [
 dict(n=1, title=r"Koordinatalar sistemasi", am=[1, 2], lec=[2], tn=["TN2", "TN3", "TN14"],
      questions=[r"Dekart, silindrik va sferik koordinatalar orasidagi o‘tish formulalarini yozing.", r"Nima uchun egri chiziqli koordinatalarda birlik vektorlar vaqt bo‘yicha o‘zgaradi?", r"Lame koeffitsiyentlari va hajm elementi qanday topiladi?", r"Masala simmetriyasiga qarab koordinatalarni qanday tanlaymiz? Uchta misol keltiring.", r"Erkinlik darajasi va umumlashgan koordinatalar sonini qanday aniqlaymiz?"],
      tasks=[(r"Parabolik koordinatalar \(x=\xi\eta\cos\varphi\), \(y=\xi\eta\sin\varphi\), \(z=(\xi^2-\eta^2)/2\) da \(v^2\) ni toping.", r"\(v^2=(\xi^2+\eta^2)(\dot\xi^2+\dot\eta^2)+\xi^2\eta^2\dot\varphi^2\)"),
             (r"Konus sirti (\(\theta=\alpha\)) bo‘ylab harakatlanuvchi zarra uchun \(L\) ni yozing.", r"\(L=\frac m2(\dot r^2+r^2\sin^2\alpha\,\dot\varphi^2)-mgr\cos\alpha\)"),
             (r"Sferik koordinatalarda tezlanishning radial tashkil etuvchisini toping.", r"\(a_r=\ddot r-r\dot\theta^2-r\sin^2\theta\,\dot\varphi^2\)")],
      method=r"Guruh ishi: har bir guruh bitta koordinatalar sistemasi uchun formulalar kartochkasini tayyorlaydi va boshqalarga tushuntiradi (“zigzag” usuli)."),
 dict(n=2, title=r"Impuls momenti va harakat qonunlari", am=[3, 4, 5], lec=[2, 5], tn=["TN1", "TN8", "TN21"],
      questions=[r"Impuls momentining saqlanish qonuni qaysi simmetriyadan kelib chiqadi?", r"Kinematik va dinamik masalalarning farqi nimada?", r"Tangensial va normal tezlanishlarni harakat qonunidan qanday topamiz?", r"Muhit qarshiligi bo‘lganda harakat tenglamalari qanday yoziladi?", r"Kepler ikkinchi qonunini isbotlang."],
      tasks=[(r"Ip teshik orqali tortilib, aylanayotgan sharcha radiusi \(r_0\) dan \(r_0/2\) ga kamaytirildi. Tezlik va bajarilgan ish?", r"\(v=2v_0\); \(A=\frac32mv_0^2\)"),
             (r"\(\vec r=(a\cos\omega t,\ b\sin\omega t)\) uchun \(M_z\) ni hisoblang.", r"\(M_z=mab\omega\) — o‘zgarmas"),
             (r"Gorizontal otilgan jismning trayektoriyasi va \(t\) paytdagi egrilik radiusini toping.", r"\(y=gx^2/2v_0^2\); \(R=v^3/(gv_0)\)")],
      method=r"Blits-so‘rov + doskada masala yechish (har bir masalani tasodifiy tanlangan talaba boshlaydi, boshqalar davom ettiradi)."),
 dict(n=3, title=r"Markaziy kuch maydoni va Kulon maydoni", am=[6, 7], lec=[7, 8], tn=["TN5", "TN8", "TN11"],
      questions=[r"Effektiv potensial yordamida orbita turlarini tasniflang.", r"Kepler masalasida \(p\) va \(e\) ni \(E\) va \(M\) orqali ifodalang.", r"Tortuvchi va itaruvchi Kulon maydonidagi harakatning farqlari?", r"Bertran teoremasi nimani ta’kidlaydi?", r"Gomann o‘tishi qanday amalga oshiriladi?"],
      tasks=[(r"\(U=-\alpha/r+\beta/r^2\) maydonida orbita tenglamasini toping.", r"\(p/r=1+e\cos\gamma\varphi\), \(\gamma=\sqrt{1+2\mu\beta/M^2}\) — pretsessiyalanuvchi ellips"),
             (r"Yerdan Marsga Gomann o‘tishi necha kun davom etadi?", "≈ 259 kun"),
             (r"Vodorod atomining klassik modelida elektron orbitasi radiusi \(n^2\) marta oshsa, davri qanday o‘zgaradi?", r"\(n^3\) marta oshadi")],
      method=r"Keys-stadi: “Kosmik missiyani rejalashtirish” — guruhlar orbita parametrlari va \(\Delta v\) byudjetini hisoblab, taqdim etadi."),
 dict(n=4, title=r"Ikki jism masalasi, to‘qnashuv va elastik sochilish", am=[8, 9], lec=[7, 8, 11], tn=["TN6", "TN11", "TN21"],
      questions=[r"Keltirilgan massa qanday kiritiladi va uning fizik ma’nosi?", r"MM va L sistemalaridagi sochilish burchaklari qanday bog‘langan?", r"Effektiv kesimning ta’rifi va o‘lchami?", r"Rezerford formulasini keltirib chiqarish bosqichlari?", r"Nima uchun Kulon to‘liq kesimi cheksiz?"],
      tasks=[(r"\(m_1=m_2\) bo‘lganda L sistemadagi differensial kesimni MM dagi orqali ifodalang.", r"\(\frac{d\sigma}{d\Omega_L}=4\cos\theta_1\frac{d\sigma}{d\Omega}\Big|_{\chi=2\theta_1}\)"),
             (r"Itaruvchi \(U=\beta/r^2\) maydonda \(\chi(b)\) ni toping.", r"\(\chi=\pi\left(1-\frac{b}{\sqrt{b^2+\beta/E}}\right)\)"),
             (r"Deytronning (\(m_d=2m_n\)) neytrondan markaziy elastik sochilishida energiya uzatilishi ulushi?", r"\(8/9\approx0{,}89\)")],
      method=r"Juftlikda ishlash: bir talaba MM sistemada, ikkinchisi L sistemada hisoblaydi; natijalarni diagramma bilan solishtiradi."),
 dict(n=5, title=r"Lagranj funksiyasi va Lagranj tenglamalari", am=[10, 13], lec=[3, 4, 5], tn=["TN4", "TN5", "TN7", "TN17"],
      questions=[r"Eng kichik ta’sir prinsipini ta’riflang va undan Lagranj tenglamalarini keltirib chiqaring.", r"Ikkinchi tur Lagranj tenglamalarini tuzish algoritmi?", r"Umumlashgan kuch qanday hisoblanadi?", r"Dissipativ kuchlar Lagranj formalizmiga qanday kiritiladi?", r"Siklik koordinatalar va saqlanish qonunlari qanday bog‘langan?"],
      tasks=[(r"Osilish nuqtasi gorizontal yo‘nalishda erkin siljiy oladigan (massa \(M\)) mayatnik uchun \(L\) ni yozing.", r"\(L=\frac{M+m}{2}\dot x^2+ml\dot x\dot\varphi\cos\varphi+\frac m2l^2\dot\varphi^2+mgl\cos\varphi\)"),
             (r"Shu sistema kichik tebranishlar chastotasi?", r"\(\omega^2=\frac{g}{l}\left(1+\frac mM\right)\)"),
             (r"Qiya tekislikda sirpanmasdan dumalayotgan silindr (\(I=mR^2/2\)) tezlanishini Lagranj usulida toping.", r"\(a=\frac23g\sin\alpha\)")],
      method=r"Muammoli ma’ruza-seminar: o‘qituvchi sistemani ko‘rsatadi, guruhlar 10 daqiqada \(L\) ni tuzib, tenglamalarni taqqoslaydi."),
 dict(n=6, title=r"Gamilton funksiyasi va Gamilton–Yakobi tenglamasi", am=[11, 12, 14], lec=[10], tn=["TN5", "TN18", "TN19"],
      questions=[r"Lejandr almashtirishi orqali Gamilton funksiyasi qanday kiritiladi?", r"Kanonik tenglamalar va Lagranj tenglamalari ekvivalentligini ko‘rsating.", r"Puasson qavslari va ularning xossalari?", r"Kanonik almashtirishlar va hosil qiluvchi funksiya?", r"Gamilton–Yakobi tenglamasini o‘zgaruvchilarni ajratish usulida yechish?"],
      tasks=[(r"\(Q=\ln\left(\frac{\sin p}{q}\right)\), \(P=q\operatorname{ctg}p\) almashtirishi kanonikligini tekshiring.", r"\(\{Q,P\}=1\) — kanonik"),
             (r"Kepler masalasi uchun Gamilton–Yakobi tenglamasini qutb koordinatalarida ajrating.", r"\(S=-Et+M\varphi+\int\sqrt{2m(E+\alpha/r)-M^2/r^2}\,dr\)"),
             (r"\(H=\frac{p^2}{2m}+\frac{m\omega^2q^2}{2}\) uchun \(\{H,qp\}\) ni hisoblang.", r"\(m\omega^2q^2-p^2/m\)")],
      method=r"Davra suhbati va mini-test: Lagranj, Gamilton va Gamilton–Yakobi usullarining qiyosiy jadvalini birgalikda to‘ldirish."),
]
