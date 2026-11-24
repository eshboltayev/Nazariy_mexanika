"""M9–M15 ma'ruzalar mazmuni (Nazariy mexanika, fan dasturi NM1406)."""

L = []

L.append(dict(
 n=9, short=r"Qattiq jism mexanikasi", sim="inertia", refs=[1, 2, 4], intl=["landau", "goldstein", "morin"], tn=["TN1", "TN4", "TN15"],
 title=r"Qattiq jism mexanikasi. Inersiya momenti tenzori",
 goal=r"Qattiq jism harakatini massa markazining ilgarilanma va uning atrofidagi aylanma harakatlariga ajratish, inersiya tenzorini kiritish, to‘g‘ri geometrik shakldagi jismlarning inersiya momentlarini nazariy hisoblash va Shteyner teoremasini qo‘llash.",
 outcomes=[r"qattiq jism kinetik energiyasini \(T=\frac12MV^2+\frac12I_{ik}\Omega_i\Omega_k\) ko‘rinishida yozadi;",
           r"inersiya tenzori komponentlari va bosh o‘qlarni aniqlaydi;",
           r"sterjen, disk, shar, halqa uchun inersiya momentlarini integrallab topadi;",
           r"dumalab tushayotgan jismlarning tezlanishini inersiya momenti orqali taqqoslaydi."],
 plan=["Uzluksiz muhit taqribi va massa markazi", "Qattiq jismning murakkab harakati, qutb", "Kinetik energiya va inersiya tenzori", "Bosh inersiya o‘qlari, Shteyner teoremasi", "Inersiya momentlarini hisoblash"],
 terms=["massa markazi", "burchak tezlik", "inersiya tenzori", "bosh o‘qlar", "Shteyner teoremasi", "dumalash"],
 theory=[
  ("Massa markazi va murakkab harakat", r"""<p>Uzluksiz jismda yig‘indilar integrallarga almashadi: \(M=\int\rho\,dV\), massa markazi \(\vec R=\frac1M\int\rho\vec r\,dV\). Qattiq jism ixtiyoriy nuqtasining tezligi \(\vec v=\vec V+\vec\Omega\times\vec r\), bunda \(\vec V\) — tanlangan <b>qutb</b> (odatda massa markazi) tezligi, \(\vec\Omega\) — burchak tezlik. \(\vec\Omega\) qutb tanlanishiga bog‘liq emas.</p>"""),
  ("Inersiya tenzori", r"""<p>Kinetik energiya massa markazining ilgarilanma va aylanma qismlariga ajraladi:</p>
$$T=\frac{MV^2}{2}+\frac12\sum_{i,k}I_{ik}\Omega_i\Omega_k,\qquad I_{ik}=\int\rho\left(r^2\delta_{ik}-x_ix_k\right)dV.$$
<p>\(I_{ik}\) — simmetrik tenzor. Uni har doim diagonal ko‘rinishga keltirish mumkin. Mos o‘qlar <b>bosh inersiya o‘qlari</b>, diagonal elementlar \(I_1,I_2,I_3\) esa bosh inersiya momentlari deyiladi. Impuls momenti \(M_i=I_{ik}\Omega_k\), ya’ni umumiy holda \(\vec M\nparallel\vec\Omega\).</p>"""),
  ("Shteyner teoremasi va standart natijalar", r"""<p>Massa markazidan \(d\) masofada unga parallel o‘q uchun: \(I=I_c+Md^2\).</p>
<table class="t"><thead><tr><th>Jism (massa markazi orqali o‘q)</th><th>\(I_c\)</th></tr></thead><tbody><tr><td>Ingichka sterjen \(l\), o‘qqa perpendikulyar</td><td>\(Ml^2/12\)</td></tr><tr><td>Yupqa halqa \(R\), simmetriya o‘qi</td><td>\(MR^2\)</td></tr><tr><td>Yaxlit disk/silindr \(R\)</td><td>\(MR^2/2\)</td></tr><tr><td>Yaxlit shar</td><td>\(2MR^2/5\)</td></tr><tr><td>Yupqa sferik qobiq</td><td>\(2MR^2/3\)</td></tr><tr><td>To‘g‘ri burchakli plastina \(a\times b\), tekislikka perpendikulyar</td><td>\(M(a^2+b^2)/12\)</td></tr></tbody></table>
<p>Masalan, sterjen uchiga nisbatan \(I=Ml^2/12+M(l/2)^2=Ml^2/3\).</p>"""),
  ("Qiya tekislikda dumalash", r"""<p>Sirpanmasdan dumalashda \(v=\Omega R\) va energiya saqlanadi. Natijada tezlanish quyidagicha bo‘ladi:</p>
$$a=\frac{g\sin\alpha}{1+I_c/MR^2}.$$
<p>Tezlanish massa va radiusga bog‘liq emas, faqat \(k=I_c/MR^2\) “shakl koeffitsiyenti”ga bog‘liq. Shuning uchun yaxlit shar diskdan, disk esa halqadan tez dumalaydi.</p>""")],
 example=(r"Dumalash poygasi",
  r"Yaxlit shar, disk va yupqa halqa \(\alpha=30^\circ\) qiyalikdan sirpanmasdan dumalaydi. Tezlanishlarni va 1 m yo‘lni bosib o‘tish vaqtini toping.",
  r"\(g\sin\alpha=4{,}905\) m/s². Shar (\(k=0{,}4\)): \(a=3{,}50\) m/s², \(t=\sqrt{2/a}=0{,}76\) s. Disk (\(k=0{,}5\)): \(a=3{,}27\) m/s², \(t=0{,}78\) s. Halqa (\(k=1\)): \(a=2{,}45\) m/s², \(t=0{,}90\) s. Shar birinchi keladi."),
 simtask=[r"Shakllarni almashtirib, misoldagi tezlanishlarni tekshiring.",
          r"Sterjenni tanlab, o‘qni markazdan uchiga siljiting: \(I\) qanday o‘zgaradi? \(Ml^2/3\) bilan solishtiring.",
          r"Massani 2 marta oshiring: dumalash tezlanishi o‘zgaradimi? Nima uchun?"],
 mistakes=[(r"“Og‘ir jism qiya tekislikdan tezroq dumalaydi.”", r"Tezlanish faqat \(I_c/MR^2\) ga bog‘liq; massa qisqarib ketadi."),
           (r"“Impuls momenti har doim burchak tezlikka parallel.”", r"\(\vec M=\hat I\vec\Omega\) — faqat bosh o‘q atrofida aylanishda parallel."),
           (r"“Inersiya momenti jismning o‘ziga xos yagona son.”", r"U o‘qqa bog‘liq; to‘liq tavsif — tenzor.")],
 ai=r"""Sen qattiq jism mexanikasi bo‘yicha repetitorsan. Mavzu: inersiya tenzori.
Menga to‘g‘ri burchakli parallelepiped uchun \(I_{ik}\) ni integrallab topishni bosqichma-bosqich savollar bilan o‘rgat. Keyin bosh o‘qlarni topish uchun xos qiymatlar masalasini Python (numpy.linalg.eigh) bilan yechish algoritmini menga tuzdir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Yaxlit shar inersiya momenti:", [r"\(2MR^2/5\)", r"\(MR^2/2\)", r"\(2MR^2/3\)", r"\(MR^2\)"], 0, "Integrallash natijasi."),
  (r"Sterjenning uchiga nisbatan inersiya momenti:", [r"\(Ml^2/3\)", r"\(Ml^2/12\)", r"\(Ml^2/2\)", r"\(Ml^2\)"], 0, "Shteyner teoremasi."),
  (r"Shteyner teoremasi:", [r"\(I=I_c+Md^2\)", r"\(I=I_c-Md^2\)", r"\(I=I_cMd^2\)", r"\(I=I_c+Md\)"], 0, "Parallel o‘qlar."),
  (r"Qattiq jismning kinetik energiyasi:", [r"\(\frac12MV^2+\frac12I_{ik}\Omega_i\Omega_k\)", r"\(\frac12MV^2\)", r"\(\frac12I\Omega\)", r"\(MV^2+I\Omega^2\)"], 0, "Ilgarilanma + aylanma."),
  (r"Qaysi jism qiya tekislikdan eng tez dumalaydi?", ["yaxlit shar", "disk", "halqa", "kovak shar"], 0, r"\(k\) eng kichik (0,4)."),
  (r"Dumalash tezlanishi massaga:", ["bog‘liq emas", "to‘g‘ri proporsional", "teskari proporsional", "kvadratik bog‘liq"], 0, "Massa qisqaradi."),
  (r"Inersiya tenzori:", ["simmetrik", "antisimmetrik", "skalyar", "diagonal har doim"], 0, r"\(I_{ik}=I_{ki}\)."),
  (r"Yupqa halqa (simmetriya o‘qi):", [r"\(MR^2\)", r"\(MR^2/2\)", r"\(2MR^2/5\)", r"\(MR^2/4\)"], 0, r"Barcha massa \(R\) masofada."),
  (r"Disk uchun \(\alpha=30^\circ\) da dumalash tezlanishi:", ["3,27 m/s²", "4,9 m/s²", "2,45 m/s²", "3,50 m/s²"], 0, r"\(4{,}905/1{,}5\)."),
  (r"Bosh o‘q atrofida aylanishda:", [r"\(\vec M\parallel\vec\Omega\)", r"\(\vec M\perp\vec\Omega\)", r"\(\vec M=0\)", r"\(\vec\Omega=0\)"], 0, r"\(M_i=I_i\Omega_i\).")],
 blits=["Figurachi qo‘llarini yig‘ganda nima uchun tez aylanadi?", "Xom va qaynatilgan tuxumni aylantirib qanday ajratish mumkin?", "Velosiped g‘ildiragi nima uchun yengil bo‘lishi kerak?", "Inersiya momenti va massaning fizik farqi nimada?"]))

L.append(dict(
 n=10, short=r"Kanonik tenglamalar. Puasson qavslari", sim="phase", refs=[1, 2, "Q1"], intl=["goldstein", "landau", "arnold"], tn=["TN4", "TN5", "TN16", "TN17", "TN18"],
 title=r"Gamilton funksiyasi va kanonik tenglamalar. Puasson qavslari",
 goal=r"Lejandr almashtirishi orqali Gamilton funksiyasini kiritish, kanonik tenglamalarni keltirib chiqarish, Puasson qavslari yordamida harakat integrallarini tekshirish va fazaviy fazoda harakatni tahlil qilish.",
 outcomes=[r"\(H=\sum p_i\dot q_i-L\) ni tuzib, uni \(q,p\) orqali ifodalaydi;",
           r"kanonik tenglamalarni yozadi va oddiy sistemalar uchun yechadi;",
           r"Puasson qavslarini hisoblaydi, kattalikning harakat integrali ekanini \(\{f,H\}=0\) bilan tekshiradi;",
           r"fazaviy portret va Liuvill teoremasining ma’nosini izohlaydi."],
 plan=["Lejandr almashtirishi va Gamilton funksiyasi", "Kanonik tenglamalar", "Fazaviy fazo va Liuvill teoremasi", "Puasson qavslari va ularning xossalari", "Kanonik almashtirishlar"],
 terms=["Gamilton funksiyasi", "kanonik tenglamalar", "fazaviy fazo", "Puasson qavsi", "Liuvill teoremasi", "kanonik almashtirish"],
 theory=[
  ("Gamilton funksiyasi", r"""<p>\(L(q,\dot q,t)\) dan umumlashgan tezliklarni impulslarga almashtiramiz (Lejandr almashtirishi):</p>
$$p_i=\frac{\partial L}{\partial\dot q_i},\qquad H(q,p,t)=\sum_ip_i\dot q_i-L.$$
<p>Stasionar bog‘lanishlarda \(H=T+U\) — energiya. Masalan, ossilyator uchun \(H=\frac{p^2}{2m}+\frac{m\omega^2q^2}{2}\).</p>"""),
  ("Kanonik tenglamalar", r"""<p>\(dH\) ni ikki usulda yozib solishtirsak, \(2s\) ta birinchi tartibli tenglama hosil bo‘ladi:</p>
$$\dot q_i=\frac{\partial H}{\partial p_i},\qquad\dot p_i=-\frac{\partial H}{\partial q_i},\qquad\frac{dH}{dt}=\frac{\partial H}{\partial t}.$$
<p>Sistema holati \(2s\) o‘lchamli <b>fazaviy fazo</b>dagi nuqta bilan tasvirlanadi. Bir erkinlik darajasida \(H(q,p)=E\) chiziqlari fazaviy trayektoriyalardir: ossilyatorda ellipslar, mayatnikda esa tebranish va aylanish sohalarini ajratuvchi separatrisa.</p>"""),
  ("Puasson qavslari", r"""<p>Ixtiyoriy \(f(q,p,t)\) uchun \(\dfrac{df}{dt}=\dfrac{\partial f}{\partial t}+\{f,H\}\), bunda</p>
$$\{f,g\}=\sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right).$$
<p>Xossalari: antisimmetriya, chiziqlilik, Leybnis qoidasi, Yakobi ayniyati. Fundamental qavslar: \(\{q_i,p_k\}=\delta_{ik}\). Impuls momenti uchun \(\{M_x,M_y\}=M_z\). <b>Puasson teoremasi</b>: \(f\) va \(g\) harakat integrallari bo‘lsa, \(\{f,g\}\) ham harakat integrali bo‘ladi. Kvant mexanikasida Puasson qavsi kommutatorga o‘tadi: \(\{f,g\}\to\frac{1}{i\hbar}[\hat f,\hat g]\).</p>"""),
  ("Liuvill teoremasi va kanonik almashtirishlar", r"""<p>Fazaviy fazodagi nuqtalar to‘plami harakatlanganda uning hajmi saqlanadi (<b>Liuvill teoremasi</b>) — statistik mexanikaning asosi. <b>Kanonik almashtirishlar</b> \((q,p)\to(Q,P)\) kanonik tenglamalar ko‘rinishini saqlaydi va \(\{Q,P\}=1\) shartni qanoatlantiradi. Ular hosil qiluvchi funksiya orqali beriladi. Gamilton–Yakobi usuli aynan shunday almashtirishga asoslangan.</p>""")],
 example=(r"Garmonik ossilyatorning fazaviy portreti",
  r"\(m=1\) kg, \(\omega=2\) rad/s, \(E=8\) J. Kanonik tenglamalarni yozing, \(q_{max}\), \(p_{max}\) ni va fazaviy ellips yuzasini toping. \(\{q,H\}\) ni hisoblang.",
  r"\(\dot q=p/m\), \(\dot p=-m\omega^2q\). \(q_{max}=\sqrt{2E/m\omega^2}=2\) m, \(p_{max}=\sqrt{2mE}=4\) kg·m/s. Ellips yuzasi \(\pi q_{max}p_{max}=8\pi\approx25{,}1\) J·s \(=2\pi E/\omega\) (ta’sir o‘zgaruvchisi \(J=E/\omega=4\) J·s). \(\{q,H\}=\partial H/\partial p=p/m=\dot q\) ✓."),
 simtask=[r"Ossilyator rejimida energiyani oshiring: ellips kattalashadi, lekin davr o‘zgarmaydi — tekshiring.",
          r"Mayatnik rejimida energiyani separatrisaga (\(E=2mgl\)) yaqinlashtiring: davr qanday o‘zgaradi?",
          r"Separatrisadan yuqori energiyada trayektoriya qanday ko‘rinadi? Fizik ma’nosini ayting."],
 mistakes=[(r"“\(H\) har doim energiya.”", r"Faqat stasionar bog‘lanishlarda va \(L\) vaqtga oshkor bog‘liq bo‘lmaganda."),
           (r"“Kanonik tenglamalar Lagranj tenglamalaridan ko‘p ma’lumot beradi.”", r"Ular ekvivalent: \(s\) ta ikkinchi tartibli o‘rniga \(2s\) ta birinchi tartibli tenglama."),
           (r"“\(\{f,g\}=\{g,f\}\).”", r"Puasson qavsi antisimmetrik: \(\{f,g\}=-\{g,f\}\).")],
 ai=r"""Sen Gamilton mexanikasi bo‘yicha repetitorsan. Mavzu: Puasson qavslari.
Menga \(\{M_x,M_y\}=M_z\) ni o‘zim hisoblashim uchun savollar bilan yo‘l ko‘rsat. Keyin markaziy maydonda \(\{M^2,H\}=0\) ekanini tekshirish topshirig‘ini ber. Oxirida Python’da kanonik tenglamalarni simplektik (leapfrog) usulda integrallash va energiya saqlanishini tekshirishni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Gamilton funksiyasi:", [r"\(\sum p\dot q-L\)", r"\(L-\sum p\dot q\)", r"\(T-U\)", r"\(\partial L/\partial t\)"], 0, "Lejandr almashtirishi."),
  (r"Kanonik tenglama:", [r"\(\dot p=-\partial H/\partial q\)", r"\(\dot p=\partial H/\partial q\)", r"\(\dot q=-\partial H/\partial p\)", r"\(\dot q=\partial H/\partial q\)"], 0, "Ta’rif."),
  (r"\(\{q,p\}\) =", ["1", "0", "−1", r"\(\hbar\)"], 0, "Fundamental qavs."),
  (r"\(f\) harakat integrali bo‘lishi sharti (\(\partial f/\partial t=0\)):", [r"\(\{f,H\}=0\)", r"\(\{f,H\}=1\)", r"\(f=H\)", r"\(\{f,q\}=0\)"], 0, r"\(df/dt=\{f,H\}\)."),
  (r"\(\{M_x,M_y\}\) =", [r"\(M_z\)", "0", r"\(-M_z\)", r"\(M^2\)"], 0, "Impuls momenti algebrasi."),
  (r"Liuvill teoremasi:", ["fazaviy hajm saqlanadi", "energiya saqlanadi", "impuls saqlanadi", "entropiya o‘sadi"], 0, "Gamilton oqimi."),
  (r"Ossilyatorning fazaviy trayektoriyasi:", ["ellips", "giperbola", "to‘g‘ri chiziq", "spiral"], 0, r"\(p^2/2m+m\omega^2q^2/2=E\)."),
  (r"Mayatnikda tebranish va aylanishni ajratuvchi chiziq:", ["separatrisa", "izoklina", "asimptota", "attraktor"], 0, r"\(E=2mgl\)."),
  (r"Kanonik almashtirishda:", [r"\(\{Q,P\}=1\)", r"\(\{Q,P\}=0\)", r"\(Q=P\)", r"\(H=0\)"], 0, "Ta’rif."),
  (r"Kvant mexanikasida Puasson qavsiga mos:", [r"\([\hat f,\hat g]/i\hbar\)", r"\(\hat f\hat g\)", r"\(\langle f\rangle\)", r"\(\hbar f\)"], 0, "Dirak mosligi.")],
 blits=["Nima uchun fazaviy fazo \\(2s\\) o‘lchamli?", "Fazaviy trayektoriyalar kesishishi mumkinmi?", "Puasson qavsi va kvant kommutatori qanday bog‘langan?", "Liuvill teoremasi statistik fizikada nima uchun muhim?"]))

L.append(dict(
 n=11, short=r"Zarralar to‘qnashuvi nazariyasi", sim="collision", refs=[1, 2, 4], intl=["landau", "goldstein", "taylor"], tn=["TN1", "TN6", "TN8", "TN21"],
 title=r"Zarralar to‘qnashuvi nazariyasi: elastik va noelastik to‘qnashuvlar",
 goal=r"Saqlanish qonunlari asosida to‘qnashuvlarni massa markazi (MM) va laboratoriya (L) sistemalarida tahlil qilish, impulslar diagrammasini qurish, energiya uzatilishi va sochilish burchaklari orasidagi bog‘lanishlarni topish.",
 outcomes=[r"MM sistemasida elastik to‘qnashuvni tavsiflaydi va L sistemaga o‘tkazadi;",
           r"impulslar (to‘qnashuv) diagrammasini quradi;",
           r"\(\operatorname{tg}\theta_1=\frac{m_2\sin\chi}{m_1+m_2\cos\chi}\), \(\theta_2=(\pi-\chi)/2\) munosabatlarini qo‘llaydi;",
           r"neytronlarni sekinlashtirish masalasida energiya uzatilishini hisoblaydi."],
 plan=["Zarralarning parchalanishi va to‘qnashuvi", "Massa markazi sistemasi", "Elastik to‘qnashuv: impulslar diagrammasi", "L sistemadagi burchaklar va energiyalar", "Noelastik to‘qnashuvlar"],
 terms=["elastik to‘qnashuv", "massa markazi sistemasi", "impulslar diagrammasi", "laboratoriya sistemasi", "energiya uzatilishi", "noelastik to‘qnashuv"],
 theory=[
  ("Massa markazi sistemasi", r"""<p>Ikki zarra to‘qnashuvida impuls va energiya saqlanadi. MM sistemasida to‘liq impuls nol: zarralar impulslari teng va qarama-qarshi, \(\vec p_0=\mu\vec v\), bunda \(\vec v=\vec v_1-\vec v_2\) — nisbiy tezlik. Elastik to‘qnashuvda \(|\vec p_0|\) o‘zgarmaydi, faqat yo‘nalishi \(\chi\) burchakka buriladi. \(\chi\) saqlanish qonunlaridan aniqlanmaydi — u o‘zaro ta’sir qonuniga bog‘liq (M8 ga qarang).</p>"""),
  ("Impulslar diagrammasi", r"""<p>L sistemada ikkinchi zarra tinch tursa, birinchi zarraning to‘qnashuvdan keyingi impulsi \(\vec p_1'=\mu v\vec n_0+\frac{m_1}{m_1+m_2}\vec p_1\) bo‘ladi. Diagrammada radiusi \(\mu v\) bo‘lgan aylana chiziladi. \(m_1\lt m_2\) bo‘lsa, impulsning boshlang‘ich nuqtasi aylana ichida yotadi va har qanday burchakka sochilish mumkin. \(m_1\gt m_2\) bo‘lsa, nuqta aylanadan tashqarida bo‘ladi va maksimal burchak \(\sin\theta_{1,max}=m_2/m_1\) ga teng.</p>"""),
  ("Laboratoriya sistemasidagi kattaliklar", r"""$$\operatorname{tg}\theta_1=\frac{m_2\sin\chi}{m_1+m_2\cos\chi},\qquad\theta_2=\frac{\pi-\chi}{2},$$
$$\frac{\Delta E}{E_1}=\frac{4m_1m_2}{(m_1+m_2)^2}\sin^2\frac\chi2.$$
<p>Teng massalarda \(\theta_1+\theta_2=\pi/2\) — zarralar to‘g‘ri burchak ostida tarqaladi (bilyard). Markaziy to‘qnashuvda (\(\chi=\pi\)) uzatiladigan energiya maksimal: \(4m_1m_2/(m_1+m_2)^2\). Bu \(m_1=m_2\) bo‘lsa 100 % ga teng.</p>"""),
  ("Noelastik to‘qnashuvlar va parchalanish", r"""<p>Noelastik to‘qnashuvda kinetik energiyaning bir qismi \(Q\) ichki energiyaga aylanadi. Mutlaq noelastik to‘qnashuvda zarralar birlashib, MM tezligi bilan harakatlanadi. Yo‘qolgan energiya \(\frac{\mu v^2}{2}\) ga teng — bu MM sistemadagi to‘liq kinetik energiya. Zarra parchalanganda MM sistemada bo‘laklar teng va qarama-qarshi impulslar bilan uchadi.</p>""")],
 example=(r"Neytronlarni uglerodda sekinlashtirish",
  r"Neytron (\(m\)) uglerod-12 yadrosida (\(12m\)) elastik sochilmoqda. Bitta to‘qnashuvda maksimal energiya yo‘qotish ulushini toping. 2 MeV dan 0,025 eV gacha sekinlashish uchun o‘rtacha nechta to‘qnashuv kerak (logarifmik dekrement \(\xi=1+\frac{(A-1)^2}{2A}\ln\frac{A-1}{A+1}\))?",
  r"Maksimal uzatish \(4A/(A+1)^2=48/169=0{,}284\); markaziy to‘qnashuvdan keyin neytronda \(((A-1)/(A+1))^2=0{,}716\) energiya qoladi. \(\xi=1+\frac{121}{24}\ln\frac{11}{13}=0{,}158\). To‘qnashuvlar soni \(n=\ln(2\cdot10^6/0{,}025)/\xi=18{,}2/0{,}158\approx115\). (Vodorodda \(\xi=1\), atigi ≈ 18 ta.)"),
 simtask=[r"\(m_1=m_2\) qiling va \(\chi\) ni o‘zgartiring: \(\theta_1+\theta_2=90^\circ\) ekanini tekshiring.",
          r"\(m_1=3m_2\) da \(\chi\) ni 0° dan 180° gacha o‘zgartirib, \(\theta_1\) ning maksimumini toping va \(\arcsin(m_2/m_1)\) bilan solishtiring.",
          r"Neytron–uglerod (\(m_2=12m_1\)) uchun \(\chi=180^\circ\) da uzatilgan energiya ulushi 28,4 % ekanini tekshiring."],
 mistakes=[(r"“Sochilish burchagi saqlanish qonunlaridan topiladi.”", r"Saqlanish qonunlari faqat bog‘lanishlarni beradi; \(\chi\) o‘zaro ta’sir qonuni va nishon parametriga bog‘liq."),
           (r"“Og‘ir zarra yengilidan istalgan burchakka sochilishi mumkin.”", r"\(m_1>m_2\) da \(\theta_1\le\arcsin(m_2/m_1)\)."),
           (r"“Noelastik to‘qnashuvda impuls saqlanmaydi.”", r"Impuls har doim saqlanadi; faqat kinetik energiya saqlanmaydi.")],
 ai=r"""Sen to‘qnashuvlar nazariyasi bo‘yicha repetitorsan. Mavzu: impulslar diagrammasi.
Menga diagrammani qanday chizishni qadamma-qadam o‘rgat va 3 ta holat (\(m_1<m_2\), \(m_1=m_2\), \(m_1>m_2\)) uchun burchaklarni diagrammadan topishni so‘ra. Javoblarimni formulalar bilan tekshir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Teng massali elastik to‘qnashuvda (biri tinch) \(\theta_1+\theta_2\) =", ["90°", "180°", "45°", "60°"], 0, "Bilyard qoidasi."),
  (r"Tinch zarraning tepki burchagi:", [r"\((\pi-\chi)/2\)", r"\(\chi/2\)", r"\(\chi\)", r"\(\pi-\chi\)"], 0, "Diagrammadan."),
  (r"\(m_1>m_2\) da maksimal sochilish burchagi:", [r"\(\arcsin(m_2/m_1)\)", "90°", "180°", r"\(\arccos(m_2/m_1)\)"], 0, "Impulslar diagrammasi."),
  (r"Markaziy to‘qnashuvda uzatiladigan energiya ulushi:", [r"\(4m_1m_2/(m_1+m_2)^2\)", r"\(m_2/m_1\)", r"\(m_1/(m_1+m_2)\)", "1"], 0, r"\(\chi=\pi\)."),
  (r"MM sistemada elastik to‘qnashuvda o‘zgaradi:", ["faqat impulslar yo‘nalishi", "impulslar moduli", "energiya", "massalar"], 0, r"\(|\vec p_0|\) saqlanadi."),
  (r"Mutlaq noelastik to‘qnashuvda yo‘qolgan energiya:", [r"\(\mu v^2/2\)", r"\(mv^2/2\)", "0", r"\(Mv^2/2\)"], 0, "MM sistemadagi kinetik energiya."),
  (r"Neytronni sekinlashtirish uchun eng samarali modda:", ["vodorod (suv)", "qo‘rg‘oshin", "temir", "oltin"], 0, "Teng massa — maksimal uzatish."),
  (r"Noelastik to‘qnashuvda:", ["impuls saqlanadi, kinetik energiya saqlanmaydi", "ikkalasi saqlanmaydi", "faqat energiya saqlanadi", "hech narsa saqlanmaydi"], 0, "Yopiq sistema."),
  (r"Neytron va C-12 markaziy to‘qnashuvidan keyin neytronda qolgan energiya:", ["≈ 72 %", "≈ 28 %", "≈ 50 %", "0"], 0, r"\((11/13)^2\)."),
  (r"Impulslar diagrammasidagi aylana radiusi:", [r"\(\mu v\)", r"\(m_1v\)", r"\(Mv\)", r"\(m_2v/2\)"], 0, "MM sistemadagi impuls.")],
 blits=["Nima uchun bilyard sharlari to‘g‘ri burchak ostida tarqaladi?", "Atom reaktorida nima uchun grafit yoki suv ishlatiladi?", "Raketa dvigateli “parchalanish” masalasimi?", "MM sistemasi qachon qulay?"]))

L.append(dict(
 n=12, short=r"Relyativistik mexanikaga kirish", sim="lorentz", refs=[1, 2, "Q1"], intl=["landau", "rindler", "taylor"], tn=["TN3", "TN11", "TN24"],
 title=r"Relyativistik mexanikaga kirish. Lorens almashtirishlari",
 goal=r"Eynshteyn postulatlaridan Lorens almashtirishlarini keltirib chiqarish, interval invariantligi, vaqt sekinlashuvi, uzunlik qisqarishi va tezliklarni qo‘shish qoidasini qo‘llash, relyativistik zarra uchun Lagranj funksiyasi va energiya-impuls bog‘lanishini kiritish.",
 outcomes=[r"Lorens almashtirishlarini yozadi va Minkovskiy diagrammasida talqin qiladi;",
           r"vaqt sekinlashuvi va uzunlik qisqarishini hisoblaydi;",
           r"relyativistik tezliklarni qo‘shadi;",
           r"\(L=-mc^2\sqrt{1-v^2/c^2}\) dan impuls va energiyani keltirib chiqaradi."],
 plan=["Nisbiylik prinsipi va yorug‘lik tezligi", "Interval va uning invariantligi", "Lorens almashtirishlari", "Relyativistik kinematika", "Relyativistik zarra dinamikasi"],
 terms=["interval", "Lorens almashtirishi", "xususiy vaqt", "vaqt sekinlashuvi", "to‘rt o‘lchamli vektor", "tinchlikdagi energiya"],
 theory=[
  ("Postulatlar va interval", r"""<p>Eynshteyn postulatlari: 1) barcha inersial sistemalarda fizika qonunlari bir xil; 2) yorug‘lik tezligi \(c\) manba harakatiga bog‘liq emas. Ikki voqea orasidagi interval</p>
$$s^2=c^2\Delta t^2-\Delta x^2-\Delta y^2-\Delta z^2$$
<p>barcha inersial sistemalarda bir xil. \(s^2>0\) — vaqtsimon (sababiy bog‘lanish mumkin), \(s^2<0\) — fazosimon, \(s^2=0\) — yorug‘liksimon.</p>"""),
  ("Lorens almashtirishlari", r"""<p>\(K'\) sistema \(K\) ga nisbatan \(x\) o‘qi bo‘ylab \(V\) tezlik bilan harakatlansa (\(\beta=V/c\), \(\gamma=1/\sqrt{1-\beta^2}\)):</p>
$$x'=\gamma(x-Vt),\quad t'=\gamma\left(t-\frac{Vx}{c^2}\right),\quad y'=y,\quad z'=z.$$
<p>\(V\ll c\) da ular Galiley almashtirishiga o‘tadi. Minkovskiy diagrammasida \(K'\) ning o‘qlari \(\operatorname{arctg}\beta\) burchak ostida yorug‘lik chizig‘iga qarab “qisiladi”.</p>"""),
  ("Relyativistik kinematika", r"""<p><b>Vaqt sekinlashuvi</b>: harakatlanayotgan soat ko‘rsatadigan xususiy vaqt \(\Delta\tau=\Delta t/\gamma\). <b>Uzunlik qisqarishi</b>: \(l=l_0/\gamma\). <b>Tezliklarni qo‘shish</b>:</p>
$$u=\frac{u'+V}{1+u'V/c^2}.$$
<p>Bir joyda bo‘lmagan voqealar uchun bir vaqtlilik nisbiy tushuncha. Ammo vaqtsimon voqealarning tartibi barcha sistemalarda bir xil, shuning uchun sabab-oqibat bog‘lanishi buzilmaydi.</p>"""),
  ("Relyativistik zarra dinamikasi", r"""<p>Erkin zarra uchun ta’sir \(S=-mc\int ds\) ga, Lagranjian esa quyidagiga teng:</p>
$$L=-mc^2\sqrt{1-\frac{v^2}{c^2}}\ \Rightarrow\ \vec p=\gamma m\vec v,\quad E=\gamma mc^2,\quad E^2=p^2c^2+m^2c^4.$$
<p>\(v\ll c\) da \(L\approx-mc^2+mv^2/2\) — klassik natija. Tinchlikdagi energiya \(mc^2\). \((E/c,\vec p)\) to‘rt o‘lchamli vektor bo‘lib, uning “uzunligi” \(mc\) invariant.</p>""")],
 example=(r"Kosmik nurlardagi myuonlar",
  r"Myuonning xususiy yashash vaqti \(\tau_0=2{,}2\) mks, tezligi \(v=0{,}995c\). Yer sistemasida yashash vaqti va bosib o‘tadigan masofa qancha? Relyativizm hisobga olinmasa-chi? 0,8c bilan uchayotgan raketadan oldinga 0,8c tezlikda zond otilsa, uning Yerga nisbatan tezligi qancha?",
  r"\(\gamma=1/\sqrt{1-0{,}995^2}=10{,}0\). \(\tau=\gamma\tau_0=22{,}0\) mks, masofa \(v\tau=0{,}995\cdot3\cdot10^8\cdot22{,}0\cdot10^{-6}\approx6{,}6\) km (klassik hisobda atigi 0,66 km) — myuonlar atmosferadan Yer sirtigacha yetib keladi. Tezliklar: \(u=1{,}6c/1{,}64=0{,}976c\lt c\)."),
 simtask=[r"\(\beta=0{,}6\) o‘rnating: \(\gamma=1{,}25\) ekanini va \(K'\) o‘qlari qanday burilishini kuzating.",
          r"Voqeani yorug‘lik konusi ichiga va tashqarisiga qo‘yib, intervalning ishorasi va \(t'\) ning ishorasi qanday o‘zgarishini tekshiring.",
          r"Fazosimon voqea uchun shunday \(\beta\) topingki, \(t'=0\) bo‘lsin (bir vaqtlilikning nisbiyligi)."],
 mistakes=[(r"“Massa tezlik bilan ortadi.”", r"Zamonaviy talqinda \(m\) — invariant; tezlik bilan \(\gamma m\) (energiya/\(c^2\)) ortadi."),
           (r"“Tezliklar oddiy qo‘shiladi: 0,8c + 0,8c = 1,6c.”", r"Relyativistik qo‘shish qoidasi bo‘yicha 0,976c."),
           (r"“Uzunlik qisqarishi — optik illyuziya.”", r"Bu fazo-vaqt geometriyasining real oqibati; o‘lchash natijasi sistemaga bog‘liq.")],
 ai=r"""Sen maxsus nisbiylik nazariyasi bo‘yicha repetitorsan. Mavzu: Lorens almashtirishlari.
Menga “egizaklar paradoksi”ni Minkovskiy diagrammasi yordamida tahlil qilishni savollar orqali o‘rgat. Keyin \(E^2=p^2c^2+m^2c^4\) ni relyativistik Lagranjiandan keltirib chiqarishimni so‘ra va tekshir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Lorens omili \(\gamma\) =", [r"\(1/\sqrt{1-v^2/c^2}\)", r"\(\sqrt{1-v^2/c^2}\)", r"\(1-v^2/c^2\)", r"\(v/c\)"], 0, "Ta’rif."),
  (r"\(v=0{,}6c\) da \(\gamma\) =", ["1,25", "1,6", "0,8", "2"], 0, r"\(1/0{,}8\)."),
  (r"Harakatlanayotgan soat:", ["sekin yuradi", "tez yuradi", "bir xil", "to‘xtaydi"], 0, r"\(\Delta\tau=\Delta t/\gamma\)."),
  (r"0,8c ⊕ 0,8c =", ["0,976c", "1,6c", "c", "0,8c"], 0, "Relyativistik qo‘shish."),
  (r"Invariant kattalik:", [r"\(c^2t^2-x^2\)", r"\(t\)", r"\(x\)", r"\(x+ct\)"], 0, "Interval."),
  (r"Relyativistik energiya-impuls bog‘lanishi:", [r"\(E^2=p^2c^2+m^2c^4\)", r"\(E=pc\)", r"\(E=p^2/2m\)", r"\(E=mc^2+pc\)"], 0, "To‘rt-impuls invarianti."),
  (r"Erkin relyativistik zarra Lagranjiani:", [r"\(-mc^2\sqrt{1-v^2/c^2}\)", r"\(mv^2/2\)", r"\(\gamma mc^2\)", r"\(mc^2\)"], 0, r"\(S=-mc\int ds\)."),
  (r"\(V\ll c\) da Lorens almashtirishlari:", ["Galiley almashtirishiga o‘tadi", "yo‘qoladi", "kvant mexanikasiga o‘tadi", "o‘zgarmaydi"], 0, "Chegaraviy holat."),
  (r"Vaqtsimon interval:", [r"\(s^2>0\)", r"\(s^2<0\)", r"\(s^2=0\)", r"\(s^2=c^2\)"], 0, "Sababiy bog‘lanish mumkin."),
  (r"Myuon \(v=0{,}995c\) da laboratoriyada necha marta uzoq yashaydi?", ["≈ 10", "≈ 2", "≈ 100", "1"], 0, r"\(\gamma\approx10\).")],
 blits=["GPS sun’iy yo‘ldoshlarida nisbiylik tuzatmasi nima uchun kerak?", "Yorug‘likdan tez signal yuborish mumkinmi?", "Bir vaqtlilik nisbiy bo‘lsa, sabab-oqibat buziladimi?", "Yadro reaksiyalaridagi energiya qayerdan keladi?"]))

L.append(dict(
 n=13, short=r"Parametrik rezonans", sim="param", refs=[1, 2, 3], intl=["landau", "kibble", "arnold"], tn=["TN9", "TN10", "TN22", "TN25"],
 title=r"Parametrik rezonans. Mexanik sistemalarda rezonans shartlari",
 goal=r"Parametrlari davriy o‘zgaradigan sistemalarda parametrik rezonans hodisasini o‘rganish, Matye tenglamasi uchun beqarorlik sohalari va o‘sish tezligini aniqlash, ishqalanish bo‘lganda chegaraviy shartni topish.",
 outcomes=[r"parametrik tebranishlarni majburiy tebranishlardan farqlaydi;",
           r"Matye tenglamasi \(\ddot q+\omega_0^2(1+h\cos\gamma t)q=0\) ni yozadi;",
           r"asosiy rezonans sohasini \(|\gamma-2\omega_0|\lt h\omega_0/2\) va o‘sish tezligini hisoblaydi;",
           r"so‘nish mavjudligida rezonans chegarasini \(h>4\beta/\omega_0\) aniqlaydi."],
 plan=["Parametrik tebranishlar tushunchasi", "Matye tenglamasi", "Asosiy parametrik rezonans", "Ishqalanishning ta’siri", "Diskret mexanik sistemalarda parametrik rezonans"],
 terms=["parametrik rezonans", "Matye tenglamasi", "beqarorlik sohasi", "o‘sish tezligi", "Floke nazariyasi", "Kapitsa mayatnigi"],
 theory=[
  ("Parametrik tebranishlar", r"""<p>Agar sistemaga tashqi kuch emas, balki uning <b>parametrlari</b> (uzunlik, bikrlik, inersiya momenti) davriy o‘zgartirilsa, tebranishlar parametrik deyiladi. Misollar: arg‘imchoqni o‘tirib-turib uchirish, osilish nuqtasi vertikal tebranayotgan mayatnik, sig‘imi davriy o‘zgaradigan kontur.</p>
$$\ddot q+\omega_0^2\left(1+h\cos\gamma t\right)q=0\qquad(\text{Matye tenglamasi}).$$"""),
  ("Asosiy rezonans", r"""<p>Eng kuchli rezonans \(\gamma\approx2\omega_0\) da yuz beradi, ya’ni parametr bir davrda ikki marta o‘zgaradi. \(\gamma=2\omega_0+\varepsilon\) yaqinida yechim \(q=a(t)\cos(\omega_0+\varepsilon/2)t+b(t)\sin(\ldots)\) ko‘rinishida izlanadi. Natijada amplituda \(e^{st}\) bo‘yicha o‘sadi, bunda</p>
$$s=\frac12\sqrt{\left(\frac{h\omega_0}{2}\right)^2-\varepsilon^2}.$$
<p>Beqarorlik sohasi \(|\gamma-2\omega_0|\lt h\omega_0/2\). Rezonans \(\gamma=2\omega_0/n\) (\(n=1,2,\ldots\)) chastotalarda ham bo‘ladi, ammo sohalar kengligi \(h^n\) kabi tez torayadi.</p>"""),
  ("Ishqalanishning ta’siri", r"""<p>So‘nish \(\beta\) bo‘lsa, amplituda \(e^{(s-\beta)t}\) kabi o‘zgaradi. Parametrik rezonans faqat \(s>\beta\) da, ya’ni quyidagi shartda bo‘ladi:</p>
$$h>h_{kr}=\frac{4\beta}{\omega_0}.$$
<p>Bu majburiy rezonansdan farqli: chegara (bo‘sag‘a) mavjud, va boshlang‘ich og‘ish nol bo‘lsa, tebranish boshlanmaydi.</p>"""),
  ("Mexanik sistemalarda qo‘llanilishi", r"""<p>Diskret mexanik tizimlarda parametrik rezonans valning tanqidiy aylanish tezliklarida, mashina qismlarining tebranishida, kemalarning chayqalishida (to‘lqin davri kema xos davrining yarmiga teng bo‘lganda) xavf tug‘diradi. Boshqa tomondan, parametrik kuchaytirgichlar va generatorlar shu hodisadan foydalanadi. <b>Kapitsa mayatnigi</b>da esa osilish nuqtasi tez tebrantirilganda yuqori (teskari) muvozanat turg‘un bo‘lib qoladi.</p>""")],
 example=(r"Beqarorlik sohasi va o‘sish tezligi",
  r"\(\omega_0=10\) rad/s, \(h=0{,}1\). Asosiy beqarorlik sohasini, \(\gamma=2\omega_0\) dagi o‘sish tezligini, amplitudaning \(e\) marta ortish vaqtini toping. \(\beta=0{,}1\) s⁻¹ so‘nishda rezonans bo‘ladimi?",
  r"Soha: \(|\gamma-20|\lt0{,}1\cdot10/2=0{,}5\) ⇒ \(19{,}5\lt\gamma\lt20{,}5\) rad/s. \(s=h\omega_0/4=0{,}25\) s⁻¹, \(e\) marta ortish vaqti 4 s. \(h_{kr}=4\cdot0{,}1/10=0{,}04\lt0{,}1\) — rezonans bor, sof o‘sish tezligi \(0{,}25-0{,}1=0{,}15\) s⁻¹."),
 simtask=[r"\(\gamma/\omega_0=2\) va \(h=0{,}1\) da amplituda o‘sishini kuzating va o‘sish tezligini grafikdan baholang.",
          r"\(\gamma/\omega_0\) ni 1,9 dan 2,1 gacha o‘zgartiring: qayerda o‘sish to‘xtaydi? Soha chegarasi bilan solishtiring.",
          r"\(\beta\) ni oshirib, rezonans yo‘qoladigan chegarani toping va \(4\beta/\omega_0\) bilan solishtiring."],
 mistakes=[(r"“Parametrik rezonans \(\gamma=\omega_0\) da kuchli.”", r"Asosiy rezonans \(\gamma\approx2\omega_0\) da; \(\gamma=\omega_0\) dagi soha ancha tor (\(\sim h^2\))."),
           (r"“Har qanday kichik \(h\) da rezonans bo‘ladi.”", r"So‘nish bo‘lsa, \(h>4\beta/\omega_0\) bo‘sag‘a mavjud."),
           (r"“Parametrik va majburiy tebranish bir xil.”", r"Majburiy tebranishda tenglamaning o‘ng tomoni bor, parametrikda esa koeffitsiyent davriy o‘zgaradi.")],
 ai=r"""Sen tebranishlar nazariyasi bo‘yicha repetitorsan. Mavzu: parametrik rezonans va Matye tenglamasi.
Menga arg‘imchoqni o‘tirib-turib uchirish nima uchun ishlashini savollar orqali tushuntir. So‘ng Python’da Matye tenglamasini RK4 bilan yechib, (\(\gamma/\omega_0\), \(h\)) tekisligida turg‘unlik xaritasini (Ince–Strutt diagrammasi) qurish algoritmini tuzishimni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Asosiy parametrik rezonans chastotasi:", [r"\(\gamma\approx2\omega_0\)", r"\(\gamma=\omega_0\)", r"\(\gamma=\omega_0/2\)", r"\(\gamma=4\omega_0\)"], 0, "Parametr bir davrda ikki marta o‘zgaradi."),
  (r"Matye tenglamasi:", [r"\(\ddot q+\omega_0^2(1+h\cos\gamma t)q=0\)", r"\(\ddot q+\omega_0^2q=F\cos\gamma t\)", r"\(\ddot q+2\beta\dot q=0\)", r"\(\dot q=\omega q\)"], 0, "Davriy koeffitsiyent."),
  (r"Asosiy beqarorlik sohasi kengligi:", [r"\(h\omega_0\)", r"\(h\omega_0/4\)", r"\(h^2\omega_0\)", r"\(2\omega_0\)"], 0, r"\(|\gamma-2\omega_0|\lt h\omega_0/2\)."),
  (r"\(\gamma=2\omega_0\) dagi o‘sish tezligi:", [r"\(h\omega_0/4\)", r"\(h\omega_0\)", r"\(h/4\)", r"\(\omega_0/4\)"], 0, r"\(s=\frac12\cdot\frac{h\omega_0}{2}\)."),
  (r"So‘nishda rezonans sharti:", [r"\(h>4\beta/\omega_0\)", r"\(h<\beta\)", r"\(\beta=0\)", r"\(h>\omega_0\)"], 0, r"\(s>\beta\)."),
  (r"Boshlang‘ich og‘ish nol bo‘lsa, parametrik rezonans:", ["boshlanmaydi", "baribir boshlanadi", "kuchliroq bo‘ladi", "faqat so‘nishda boshlanadi"], 0, "Tenglama bir jinsli."),
  (r"Arg‘imchoqni o‘tirib-turib uchirishda nima o‘zgaradi?", ["mayatnikning effektiv uzunligi", "massa", "og‘irlik kuchi", "havo qarshiligi"], 0, "Parametr."),
  (r"Kapitsa mayatnigida:", ["teskari muvozanat turg‘un bo‘ladi", "pastki muvozanat beqaror", "tebranish yo‘q", "rezonans bo‘lmaydi"], 0, "Tez vibratsiya."),
  (r"\(\omega_0=10\), \(h=0{,}1\): asosiy sohaning yuqori chegarasi:", ["20,5 rad/s", "20,1 rad/s", "21 rad/s", "25 rad/s"], 0, r"\(20+0{,}5\)."),
  (r"Yuqori tartibli rezonans sohalari kengligi:", [r"\(h^n\) kabi torayadi", "bir xil", "kengayadi", "nolga teng"], 0, "Perturbatsiya tartibi.")],
 blits=["Arg‘imchoqni qanday “o‘zi” uchirish mumkin?", "Kemaning chayqalishi qachon xavfli?", "Parametrik kuchaytirgich qayerda ishlatiladi?", "Nima uchun majburiy rezonansda bo‘sag‘a yo‘q?"]))

L.append(dict(
 n=14, short=r"Uzluksiz muhit mexanikasi elementlari", sim="bernoulli", refs=[1, 2, "Q4"], intl=["landau6", "feynman", "kibble"], tn=["TN1", "TN11", "TN24"],
 title=r"Uzluksiz muhit mexanikasi elementlari: Eyler va Bernulli tenglamalari",
 goal=r"Ideal suyuqlik uchun uzluksizlik va Eyler tenglamalarini, ulardan Bernulli tenglamasini keltirib chiqarish, gaz dinamikasi va qovushqoq suyuqlik (Stoks) tenglamalarining asosiy natijalarini qo‘llash.",
 outcomes=[r"uzluksizlik tenglamasini \(\partial\rho/\partial t+\nabla\cdot(\rho\vec v)=0\) ko‘rinishida yozadi;",
           r"Eyler tenglamasidan Bernulli integralini keltirib chiqaradi;",
           r"Venturi naychasi va Torrichelli formulasi bilan masalalar yechadi;",
           r"Stoks kuchi, Reynolds soni va tovush tezligini hisoblaydi."],
 plan=["Uzluksiz muhit modeli va Eyler o‘zgaruvchilari", "Uzluksizlik tenglamasi", "Ideal suyuqlik uchun Eyler tenglamasi", "Bernulli tenglamasi va uni integrallash", "Qovushqoqlik, Stoks qonuni, gaz dinamikasi"],
 terms=["zichlik maydoni", "uzluksizlik tenglamasi", "Eyler tenglamasi", "Bernulli tenglamasi", "Reynolds soni", "Stoks kuchi"],
 theory=[
  ("Uzluksizlik tenglamasi", r"""<p>Eyler tavsifida suyuqlik har bir nuqtada \(\rho(\vec r,t)\), \(\vec v(\vec r,t)\), \(p(\vec r,t)\) maydonlari bilan beriladi. Massaning saqlanishidan quyidagi tenglama kelib chiqadi:</p>
$$\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0.$$
<p>Siqilmaydigan suyuqlikda \(\nabla\cdot\vec v=0\). Naycha uchun bu \(S_1v_1=S_2v_2\) ni beradi.</p>"""),
  ("Eyler tenglamasi", r"""<p>Ideal (qovushqoq bo‘lmagan) suyuqlik elementi uchun Nyutonning ikkinchi qonuni:</p>
$$\rho\left(\frac{\partial\vec v}{\partial t}+(\vec v\cdot\nabla)\vec v\right)=-\nabla p+\rho\vec g.$$
<p>\((\vec v\cdot\nabla)\vec v\) — konvektiv tezlanish. U oqim statsionar bo‘lsa ham tezlik nuqtadan nuqtaga o‘zgarishini hisobga oladi.</p>"""),
  ("Bernulli tenglamasi", r"""<p>Statsionar oqimda Eyler tenglamasini oqim chizig‘i bo‘ylab integrallab, siqilmaydigan suyuqlik uchun Bernulli tenglamasini olamiz:</p>
$$p+\frac{\rho v^2}{2}+\rho gh=\text{const}.$$
<p>Bu energiyaning saqlanish qonunining suyuqlikdagi ko‘rinishi. Natijalari: tor joyda bosim kichik (Venturi), idishdan oqib chiqish tezligi \(v=\sqrt{2gh}\) (Torrichelli), samolyot qanotining ko‘tarish kuchi. Potensial oqimda (\(\operatorname{rot}\vec v=0\)) doimiy butun suyuqlik uchun bir xil.</p>"""),
  ("Qovushqoqlik va gaz dinamikasi", r"""<p>Qovushqoq suyuqlik uchun Navye–Stoks tenglamasida Eyler tenglamasiga \(\eta\nabla^2\vec v\) had qo‘shiladi. Kichik Reynolds sonlarida (\(Re=\rho vd/\eta\ll1\)) shar uchun <b>Stoks kuchi</b> \(F=6\pi\eta rv\) ga teng. Undan cho‘kishning oxirgi tezligi \(v_t=\frac{2r^2(\rho-\rho_0)g}{9\eta}\) kelib chiqadi. \(Re\gtrsim2000\) da quvurdagi oqim turbulent bo‘ladi. Gazda zichlik o‘zgaradi: tovush tezligi \(c=\sqrt{\gamma p/\rho}\), Max soni \(M=v/c\). \(M\ll1\) da gazni siqilmaydigan deb hisoblash mumkin.</p>""")],
 example=(r"Venturi naychasi va tuman tomchisi",
  r"1) Suv quvuri diametri 4 sm dan 2 sm gacha torayadi, keng qismda \(v_1=1\) m/s. Tor qismdagi tezlik, bosimlar farqi va Reynolds sonini toping (\(\eta=10^{-3}\) Pa·s). 2) Radiusi 10 mkm suv tomchisining havoda cho‘kish tezligi (\(\eta=1{,}8\cdot10^{-5}\) Pa·s)?",
  r"1) \(v_2=v_1(d_1/d_2)^2=4\) m/s. \(\Delta p=\rho(v_2^2-v_1^2)/2=1000\cdot15/2=7500\) Pa. \(Re=\rho v_1d_1/\eta=4\cdot10^4\) — oqim turbulent (ideal suyuqlik yaqinlashuvi taxminiy). 2) \(v_t=2r^2\rho g/9\eta=2\cdot10^{-10}\cdot1000\cdot9{,}81/(1{,}62\cdot10^{-4})=1{,}2\) sm/s — shuning uchun tuman havoda uzoq turadi."),
 simtask=[r"Tor qism diametrini 2 marta kamaytiring: tezlik va bosim farqi necha marta o‘zgaradi?",
          r"Misoldagi qiymatlarni o‘rnatib, \(\Delta p=7500\) Pa ekanini tekshiring.",
          r"Balandlik farqini qo‘shing: Bernulli tenglamasining qaysi hadi o‘zgaradi?"],
 mistakes=[(r"“Tor joyda bosim katta, chunki suv siqiladi.”", r"Tor joyda tezlik katta, shuning uchun Bernulli bo‘yicha bosim kichik."),
           (r"“Bernulli tenglamasi har qanday oqimda to‘g‘ri.”", r"U ideal, statsionar oqim uchun oqim chizig‘i bo‘ylab to‘g‘ri; qovushqoqlik va turbulentlikda tuzatma kerak."),
           (r"“Havo — siqiladigan, shuning uchun Bernulli unga qo‘llanmaydi.”", r"\(M\lesssim0{,}3\) da havoni siqilmaydigan deb hisoblash mumkin.")],
 ai=r"""Sen gidrodinamika bo‘yicha repetitorsan. Mavzu: Eyler va Bernulli tenglamalari.
Menga samolyot qanotining ko‘tarish kuchini Bernulli va impuls saqlanishi nuqtayi nazaridan tushuntirishni savollar bilan o‘rgat (keng tarqalgan “teng vaqt” afsonasining xatosini ham ko‘rsat). Keyin Stoks qonuni bo‘yicha laboratoriya masalasini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Bernulli tenglamasi:", [r"\(p+\rho v^2/2+\rho gh=\text{const}\)", r"\(p=\rho gh\)", r"\(Sv=\text{const}\)", r"\(p+\rho v=\text{const}\)"], 0, "Ideal statsionar oqim."),
  (r"Siqilmaydigan suyuqlik uchun uzluksizlik tenglamasi:", [r"\(\nabla\cdot\vec v=0\)", r"\(\nabla\times\vec v=0\)", r"\(\rho=0\)", r"\(\partial\vec v/\partial t=0\)"], 0, r"\(\rho=\text{const}\)."),
  (r"Diametri 2 marta kichik joyda tezlik:", ["4 marta katta", "2 marta katta", "teng", "2 marta kichik"], 0, r"\(S\propto d^2\)."),
  (r"Torrichelli formulasi:", [r"\(v=\sqrt{2gh}\)", r"\(v=gh\)", r"\(v=\sqrt{gh}\)", r"\(v=2gh\)"], 0, "Bernullidan."),
  (r"Stoks kuchi:", [r"\(6\pi\eta rv\)", r"\(\pi\eta r^2v\)", r"\(\rho v^2S\)", r"\(\eta v/r\)"], 0, "Kichik Re."),
  (r"Reynolds soni:", [r"\(\rho vd/\eta\)", r"\(\eta/\rho vd\)", r"\(v/c\)", r"\(\rho gh/p\)"], 0, "Inersiya / qovushqoqlik."),
  (r"Eyler tenglamasidagi \((\vec v\cdot\nabla)\vec v\):", ["konvektiv tezlanish", "qovushqoqlik", "bosim kuchi", "gravitatsiya"], 0, "Nostatsionarlikdan tashqari tezlik o‘zgarishi."),
  (r"Max soni:", [r"\(v/c\)", r"\(c/v\)", r"\(\rho v/\eta\)", r"\(v^2/gl\)"], 0, "Ta’rif."),
  (r"Misoldagi Venturi naychasida \(\Delta p\):", ["7500 Pa", "1500 Pa", "16 000 Pa", "750 Pa"], 0, r"\(500\cdot15\)."),
  (r"Cho‘kish tezligi tomchi radiusiga:", [r"\(r^2\) ga proporsional", r"\(r\) ga", r"\(1/r\) ga", "bog‘liq emas"], 0, r"\(v_t\propto r^2\).")],
 blits=["Shamolda tom nima uchun “ko‘tarilib” ketishi mumkin?", "Dush pardasi nima uchun ichkariga tortiladi?", "Tuman nima uchun tez tushmaydi?", "Qachon havoni siqilmaydigan deb hisoblash mumkin?"]))

L.append(dict(
 n=15, short=r"Diskret mexanika elementlari", sim="crank", refs=[1, "Q2", "Q3"], intl=["uicker", "kibble", "goldstein"], tn=["TN1", "TN12", "TN13", "TN25"],
 title=r"Diskret mexanika elementlari: mexanizmlar va mashinalar",
 goal=r"Mexanizm va mashinalarning ishlash prinsiplarini analitik mexanika nuqtayi nazaridan o‘rganish, kinematik juftliklar va erkinlik darajasini aniqlash, krivoship-shatunli mexanizm kinematikasini hisoblash, tasmali va tishli uzatishlarni tahlil qilish.",
 outcomes=[r"kinematik juftliklarni sinflarga ajratadi va Chebishev formulasi bilan erkinlik darajasini topadi;",
           r"krivoship-shatunli mexanizmda porshen holati, tezligi va tezlanishini hisoblaydi;",
           r"tasmali va tishli uzatishlarning uzatish nisbati va momentini aniqlaydi;",
           r"mexanizm tenglamalarini kompyuterda modellashtirish uchun algoritmik ko‘rinishga keltiradi."],
 plan=["Mexanizm, mashina, kinematik juftlik", "Erkinlik darajasi: Chebishev formulasi", "Krivoship-shatunli mexanizm kinematikasi", "Tasmali va tishli uzatishlar", "Diskret mexanik sistemalar dinamikasi"],
 terms=["kinematik juftlik", "zveno", "Chebishev formulasi", "krivoship-shatun", "uzatish nisbati", "foydali ish koeffitsiyenti"],
 theory=[
  ("Mexanizm va kinematik juftliklar", r"""<p><b>Mexanizm</b> — harakatni bir yoki bir necha zvenodan boshqalariga berilgan qonun bo‘yicha uzatuvchi zvenolar sistemasi. <b>Mashina</b> esa energiyani o‘zgartiradi yoki foydali ish bajaradi. Zvenolar <b>kinematik juftliklar</b> orqali bog‘lanadi. Juftliklar qo‘yadigan bog‘lanishlar soniga qarab I–V sinfga bo‘linadi. Masalan, sharnir (aylanma) va polzun (ilgarilanma) — V sinf, quyi juftliklar; tishli ilashma — IV sinf, yuqori juftlik.</p>"""),
  ("Chebishev formulasi", r"""<p>Tekis mexanizmda erkinlik darajasi (harakatchanlik)</p>
$$W=3n-2p_5-p_4,$$
<p>bunda \(n\) — harakatchan zvenolar, \(p_5\) — V sinf (quyi), \(p_4\) — IV sinf (yuqori) juftliklar soni. Krivoship-shatunli mexanizmda \(n=3\) (krivoship, shatun, porshen), \(p_5=4\) (uch sharnir va bitta polzun) ⇒ \(W=1\). Demak bitta umumlashgan koordinata — krivoship burchagi \(\varphi\) — mexanizmni to‘liq aniqlaydi.</p>"""),
  ("Krivoship-shatunli mexanizm", r"""<p>Krivoship radiusi \(r\), shatun uzunligi \(l\), \(\lambda=r/l\). Porshen holati:</p>
$$x=r\cos\varphi+\sqrt{l^2-r^2\sin^2\varphi}.$$
<p>\(\lambda\) kichik bo‘lganda tezlik va tezlanish taxminan quyidagicha:</p>
$$v\approx-r\omega\left(\sin\varphi+\frac\lambda2\sin2\varphi\right),\qquad a\approx-r\omega^2\left(\cos\varphi+\lambda\cos2\varphi\right).$$
<p>Yuqori chekka nuqtada \(a=r\omega^2(1+\lambda)\) (aniq). Inersiya kuchlari \(m a\) tirsakli valga katta yuklama beradi, shuning uchun muvozanatlash kerak.</p>"""),
  ("Uzatishlar va dinamika", r"""<p><b>Tishli uzatish</b>: \(i=\omega_1/\omega_2=z_2/z_1\), moment \(M_2=\eta\,i\,M_1\). <b>Tasmali uzatish</b>: \(i\approx d_2/d_1\) (sirpanish 1–2 %). Ko‘p pog‘onali uzatishda nisbatlar ko‘paytiriladi. Diskret mexanik sistemaning dinamikasi Lagranj tenglamasi bilan yoziladi: bitta erkinlik darajasida \(\frac{d}{dt}\left(\frac12J_{kel}(\varphi)\dot\varphi^2\right)=M_{harak}-M_{qarsh}\). Bu yerda \(J_{kel}(\varphi)\) — keltirilgan inersiya momenti.</p>""")],
 example=(r"Dvigatel krivoship-shatunli mexanizmi",
  r"\(r=5\) sm, \(l=20\) sm, aylanish chastotasi 3000 ayl/min. Porshen yo‘li, o‘rtacha tezligi, yuqori chekka nuqtadagi tezlanishi va maksimal tezligini toping. Erkinlik darajasini Chebishev formulasi bilan tekshiring.",
  r"\(\omega=314{,}2\) rad/s, \(\lambda=0{,}25\). Yo‘l \(2r=10\) sm; o‘rtacha tezlik \(2\cdot0{,}1\cdot50=10\) m/s. \(a_{YuChN}=r\omega^2(1+\lambda)=0{,}05\cdot98\,696\cdot1{,}25\approx6170\) m/s² (≈ 630 g!). Maksimal tezlik ≈ 16,2 m/s, u \(\varphi\approx77^\circ\) da erishiladi. \(W=3\cdot3-2\cdot4=1\)."),
 simtask=[r"Misoldagi qiymatlarni o‘rnatib, tezlanish grafigidan \(\varphi=0\) dagi qiymatni o‘qing va 6170 m/s² bilan solishtiring.",
          r"Shatunni uzaytiring (\(\lambda\to0\)): porshen harakati garmonik tebranishga qanday yaqinlashadi?",
          r"Tezlik qaysi burchakda maksimal? Nima uchun 90° da emas?"],
 mistakes=[(r"“Porshen sof garmonik harakat qiladi.”", r"Faqat \(\lambda\to0\) da; real dvigatelda \(\cos2\varphi\) tashkil etuvchisi (ikkinchi garmonika) bor."),
           (r"“Tishli uzatish quvvatni oshiradi.”", r"U momentni oshiradi, burchak tezlikni kamaytiradi; quvvat isroflar tufayli biroz kamayadi."),
           (r"“Mexanizmning erkinlik darajasi zvenolar soniga teng.”", r"Bog‘lanishlar hisobga olinadi: \(W=3n-2p_5-p_4\).")],
 ai=r"""Sen mashina va mexanizmlar nazariyasi bo‘yicha repetitorsan. Mavzu: krivoship-shatunli mexanizm.
Menga mexanizm uchun keltirilgan inersiya momenti \(J_{kel}(\varphi)\) ni Lagranj usulida topishni savollar orqali o‘rgat. Keyin Python’da porshen kinematikasini aniq formula bilan hisoblab, taqribiy formulalar xatoligini baholash topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Tekis mexanizm uchun Chebishev formulasi:", [r"\(W=3n-2p_5-p_4\)", r"\(W=6n-5p_5\)", r"\(W=n-p\)", r"\(W=3n+p_5\)"], 0, "Ta’rif."),
  (r"Krivoship-shatunli mexanizmning erkinlik darajasi:", ["1", "2", "3", "0"], 0, r"\(9-8\)."),
  (r"Porshen yo‘li:", [r"\(2r\)", r"\(r\)", r"\(2l\)", r"\(l+r\)"], 0, "Ikki chekka nuqta farqi."),
  (r"Yuqori chekka nuqtadagi tezlanish:", [r"\(r\omega^2(1+\lambda)\)", r"\(r\omega^2\)", r"\(r\omega^2(1-\lambda)\)", r"\(l\omega^2\)"], 0, "Aniq natija."),
  (r"Tishli uzatish nisbati:", [r"\(z_2/z_1\)", r"\(z_1/z_2\)", r"\(z_1z_2\)", r"\(z_1+z_2\)"], 0, r"\(\omega_1/\omega_2\)."),
  (r"Pasaytiruvchi reduktor:", ["momentni oshiradi, tezlikni kamaytiradi", "quvvatni oshiradi", "tezlikni oshiradi", "hech narsani o‘zgartirmaydi"], 0, r"\(M_2=\eta iM_1\)."),
  (r"Sharnir qaysi sinf juftlik?", ["V (quyi)", "IV", "I", "III"], 0, "Bitta erkinlik qoldiradi."),
  (r"Tishli ilashma:", ["yuqori juftlik (IV sinf)", "quyi juftlik", "VI sinf", "juftlik emas"], 0, "Chiziq bo‘yicha kontakt."),
  (r"\(\lambda\to0\) da porshen harakati:", ["garmonikka yaqinlashadi", "to‘xtaydi", "tekis bo‘ladi", "xaotik bo‘ladi"], 0, r"\(\cos2\varphi\) hadi yo‘qoladi."),
  (r"3000 ayl/min burchak tezligi:", ["314 rad/s", "50 rad/s", "3000 rad/s", "157 rad/s"], 0, r"\(2\pi\cdot50\).")],
 blits=["Dvigatelda nima uchun maxovik ishlatiladi?", "Velosiped uzatmalari qanday ishlaydi?", "Nima uchun dvigatel tirsakli vali muvozanatlanadi?", "Robot qo‘lining erkinlik darajasi nechta bo‘lishi kerak?"]))
