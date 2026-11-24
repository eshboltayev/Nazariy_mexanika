"""M1–M8 ma'ruzalar mazmuni (Nazariy mexanika, fan dasturi NM1406)."""

L = []

L.append(dict(
 n=1, short=r"Nazariy fizika va olam manzarasi", sim="forces", refs=[1, 2, "Q1"], intl=["landau", "feynman", "susskind"], tn=["TN1", "TN8", "TN11"],
 title=r"Nazariy fizika va olam manzarasi. Simmetriya va saqlanish qonunlari",
 goal=r"Nazariy fizikaning maqsad va vazifalarini, to‘rt fundamental o‘zaro ta’sirni hamda fazo-vaqt simmetriyalari bilan saqlanish qonunlari orasidagi chuqur bog‘lanishni (Nyoter teoremasi) tushuntirish.",
 outcomes=[r"to‘rt fundamental o‘zaro ta’sirni tashuvchisi, nisbiy kuchi va ta’sir radiusi bo‘yicha taqqoslaydi;",
           r"Yukava potensiali orqali ta’sir radiusi va tashuvchi zarra massasini bog‘laydi;",
           r"vaqt bir jinsliligi → energiya, fazo bir jinsliligi → impuls, izotropiya → impuls momenti saqlanishini izohlaydi;",
           r"yopiq sistema uchun additiv harakat integrallari sonini aniqlaydi."],
 plan=["Nazariy fizikaning predmeti va usullari", "Olamning klassik va zamonaviy manzarasi", "To‘rt fundamental o‘zaro ta’sir", "Simmetriya va saqlanish qonunlari", "Harakat integrallari va invariantlik"],
 terms=["fundamental o‘zaro ta’sir", "Yukava potensiali", "simmetriya", "Nyoter teoremasi", "harakat integrali", "Galiley invariantligi"],
 theory=[
  ("Nazariy fizika va olam manzarasi", r"""<p>Nazariy fizika tajriba faktlarini eng kam sonli prinsiplardan matematik yo‘l bilan keltirib chiqaradi va yangi hodisalarni bashorat qiladi. <b>Klassik manzara</b>da (Nyuton, Maksvell) fazo va vaqt mutlaq, harakat determinlangan, materiya zarralar va maydonlardan iborat. <b>Zamonaviy manzara</b> nisbiylik nazariyasi, kvant mexanikasi va standart modelga tayanadi. Ammo ularning barchasining umumiy tili — <b>Lagranj va Gamilton formalizmi</b>. Shu sababli nazariy mexanika butun nazariy fizikaning poydevoridir.</p>"""),
  ("To‘rt fundamental o‘zaro ta’sir", r"""<table class="t"><thead><tr><th>O‘zaro ta’sir</th><th>Tashuvchi</th><th>Nisbiy kuch</th><th>Radius</th></tr></thead><tbody><tr><td>Kuchli</td><td>glyuonlar (yadroda — pionlar)</td><td>1</td><td>\(\sim10^{-15}\) m</td></tr><tr><td>Elektromagnit</td><td>foton</td><td>\(\sim10^{-2}\)</td><td>\(\infty\)</td></tr><tr><td>Kuchsiz</td><td>\(W^\pm, Z^0\) bozonlar</td><td>\(\sim10^{-6}\)</td><td>\(\sim10^{-18}\) m</td></tr><tr><td>Gravitatsion</td><td>graviton (gipotetik)</td><td>\(\sim10^{-38}\)</td><td>\(\infty\)</td></tr></tbody></table>
<p>Massasiz tashuvchi uzoq ta’sirli \(1/r\) potensialni beradi. Massasi \(m\) bo‘lgan tashuvchi esa Yukava potensialini hosil qiladi:</p>
$$U(r)=-g^2\frac{e^{-r/a}}{r},\qquad a=\frac{\hbar}{mc}.$$
<p>Yukava 1935-yilda pion massasini aynan shu munosabatdan bashorat qilgan.</p>"""),
  ("Simmetriya va saqlanish qonunlari", r"""<p>Lagranj funksiyasi biror uzluksiz almashtirishda o‘zgarmasa, unga mos harakat integrali mavjud. Bu — <b>Nyoter teoremasi</b> (1918):</p>
<ul><li><b>Vaqt bir jinsliligi</b> (\(\partial L/\partial t=0\)) → energiya saqlanadi: \(E=\sum_i\dot q_i\frac{\partial L}{\partial\dot q_i}-L\).</li><li><b>Fazo bir jinsliligi</b> (siljishga invariantlik) → impuls saqlanadi: \(\vec P=\sum_a\partial L/\partial\vec v_a\).</li><li><b>Fazo izotropiyasi</b> (burilishga invariantlik) → impuls momenti saqlanadi: \(\vec M=\sum_a\vec r_a\times\vec p_a\).</li></ul>
<p>Simmetriya qisman buzilsa, faqat tegishli komponentlar saqlanadi. Masalan, \(z\) o‘qi bo‘ylab bir jinsli maydonda \(P_x, P_y\) va \(M_z\) saqlanadi.</p>"""),
  ("Harakat integrallari va invariantlik", r"""<p>\(s\) erkinlik darajali yopiq sistema \(2s-1\) ta mustaqil harakat integraliga ega (vaqt boshi hisobga olinmaydi). Ularning ichida yettitasi <b>additiv</b>: energiya, impulsning uch va impuls momentining uch komponenti. Fizika qonunlari koordinata boshini ko‘chirish, o‘qlarni burish va Galiley almashtirishiga \(\vec r'=\vec r-\vec Vt\) nisbatan invariant. Bu klassik mexanikaning nisbiylik prinsipidir.</p>""")],
 example=(r"O‘zaro ta’sirlarni taqqoslash",
  r"1) Ikki proton orasidagi kulon va gravitatsion tortishish kuchlari nisbatini toping (\(m_p=1{,}673\cdot10^{-27}\) kg). 2) Yadro kuchlari radiusi \(a\approx1{,}4\) fm bo‘lsa, tashuvchi zarraning massasi necha MeV (\(\hbar c=197{,}3\) MeV·fm)?",
  r"1) \(F_e/F_g=ke^2/(Gm_p^2)=2{,}307\cdot10^{-28}/(6{,}674\cdot10^{-11}\cdot2{,}80\cdot10^{-54})=1{,}24\cdot10^{36}\) — masofaga bog‘liq emas, chunki ikkalasi ham \(1/r^2\). 2) \(mc^2=\hbar c/a=197{,}3/1{,}4\approx141\) MeV — bu pion massasiga (\(\approx140\) MeV) mos."),
 simtask=[r"Yukava radiusini 1,4 fm ga o‘rnatib, \(r=3\) fm da Yukava va Kulon potensiallari nisbati necha marta kichik ekanini toping.",
          r"Radiusni 10 marta kamaytiring: tashuvchi massasi qanday o‘zgaradi? Kuchsiz o‘zaro ta’sir uchun bu nimani anglatadi?",
          r"Logarifmik grafikda Kulon va Yukava egri chiziqlari qaysi masofadan keskin ajrala boshlaydi?"],
 mistakes=[(r"“Gravitatsiya eng kuchli o‘zaro ta’sir, chunki sayyoralarni ushlab turadi.”", r"U eng kuchsiz. Lekin uzoq ta’sirli va doim tortuvchi bo‘lgani uchun katta massalarda ustun keladi; elektr zaryadlari esa odatda neytrallashgan."),
           (r"“Saqlanish qonunlari tajribadan olingan alohida postulatlar.”", r"Ular fazo-vaqt simmetriyalarining natijasi (Nyoter teoremasi). Simmetriya buzilsa, mos qonun ham bajarilmaydi."),
           (r"“Impuls momenti har qanday sistemada saqlanadi.”", r"Faqat burilishlarga nisbatan invariant (izotrop) sistemada saqlanadi, masalan markaziy maydonda — markazga nisbatan.")],
 ai=r"""Sen nazariy fizika bo‘yicha sokratik repetitorsan. Mavzu: fundamental o‘zaro ta’sirlar va Nyoter teoremasi.
Qoidalar: javobni darhol berma, avval 2 ta yo‘naltiruvchi savol ber; formulalarni LaTeX’da yoz; ishonching komil bo‘lmagan sonni “taxmin” deb belgila.
Topshiriq: menga vaqt bir jinsliligidan energiya saqlanishini 3 qadamda keltirib chiqarishni o‘rgat va oxirida 3 ta nazorat savoli ber.""",
 quiz=[
  (r"Energiyaning saqlanish qonuni qaysi simmetriya bilan bog‘liq?", ["vaqt bir jinsliligi", "fazo bir jinsliligi", "fazo izotropiyasi", "Galiley invariantligi"], 0, r"\(\partial L/\partial t=0\) dan \(E=\text{const}\) kelib chiqadi."),
  (r"Impuls saqlanishi qaysi simmetriyaning natijasi?", ["fazo bir jinsliligi", "vaqt bir jinsliligi", "fazo izotropiyasi", "zaryad juftligi"], 0, "Siljishga invariantlik."),
  (r"Impuls momenti saqlanishi qaysi simmetriyaga mos?", ["fazo izotropiyasi", "vaqt bir jinsliligi", "fazo bir jinsliligi", "masshtab invariantligi"], 0, "Burilishga invariantlik."),
  (r"Yukava potensialidagi ta’sir radiusi \(a\) =", [r"\(\hbar/(mc)\)", r"\(mc/\hbar\)", r"\(\hbar c/m\)", r"\(h/(2mc^2)\)"], 0, "Komptonning keltirilgan to‘lqin uzunligi."),
  (r"Qaysi o‘zaro ta’sir eng kuchsiz?", ["gravitatsion", "kuchsiz", "elektromagnit", "kuchli"], 0, r"Nisbiy kuchi \(\sim10^{-38}\)."),
  (r"Elektromagnit o‘zaro ta’sir tashuvchisi:", ["foton", "glyuon", "W-bozon", "graviton"], 0, "Massasiz tashuvchi — cheksiz radius."),
  (r"Yopiq sistemadagi additiv harakat integrallari soni:", ["7", "3", "6", "2s − 1"], 0, "Energiya (1) + impuls (3) + impuls momenti (3)."),
  (r"\(z\) o‘qi bo‘ylab bir jinsli og‘irlik maydonida qaysi kattalik saqlanadi?", [r"\(M_z\)", r"\(P_z\)", r"\(M_x\)", "hech biri"], 0, r"\(z\) o‘qi atrofidagi burilish simmetriyasi saqlanadi; \(P_x, P_y\) ham saqlanadi."),
  (r"Ikki proton uchun \(F_e/F_g\) taxminan:", [r"\(10^{36}\)", r"\(10^{6}\)", r"\(10^{18}\)", r"\(10^{42}\)"], 0, r"\(1{,}24\cdot10^{36}\)."),
  (r"\(s\) erkinlik darajali yopiq sistemaning mustaqil harakat integrallari soni:", [r"\(2s-1\)", r"\(s\)", r"\(2s\)", r"\(s+1\)"], 0, "Vaqt boshini tanlash ixtiyoriy.")],
 blits=["Nima uchun nazariy mexanika butun nazariy fizikaning tili deyiladi?", "Massasiz tashuvchi nima uchun uzoq ta’sirli kuch beradi?", "Qaysi tajriba vaqt bir jinsliligini tekshiradi?", "Simmetriya buzilishiga hayotdan misol keltiring."]))

L.append(dict(
 n=2, short=r"Klassik mexanikaning asosiy tushunchalari", sim="coords", refs=[1, 2, 3], intl=["goldstein", "taylor", "landau"], tn=["TN2", "TN3", "TN13", "TN14"],
 title=r"Klassik mexanikaning asosiy tushunchalari: modellar, bog‘lanishlar va umumlashgan koordinatalar",
 goal=r"Moddiy nuqta, absolyut qattiq jism va uzluksiz muhit modellarini, erkinlik darajalari va bog‘lanishlar turlarini hamda umumlashgan koordinatalarga o‘tishni o‘rganish.",
 outcomes=[r"masalaga mos modelni (moddiy nuqta, qattiq jism, uzluksiz muhit) tanlaydi va qo‘llanish chegarasini asoslaydi;",
           r"sistemaning erkinlik darajalarini \(s=3N-k\) formulasi bilan hisoblaydi;",
           r"bog‘lanishlarni holonom/noholonom, stasionar/nostasionar turlarga ajratadi;",
           r"Dekart, silindrik va sferik koordinatalar orasida o‘tadi, tezlik kvadratini yozadi."],
 plan=["Mexanikaning asosiy modellari", "Erkinlik darajalari", "Bog‘lanishlar va ularning tasnifi", "Umumlashgan koordinatalar, tezliklar", "Egri chiziqli koordinatalar"],
 terms=["moddiy nuqta", "absolyut qattiq jism", "uzluksiz muhit", "erkinlik darajasi", "holonom bog‘lanish", "umumlashgan koordinata"],
 theory=[
  ("Mexanika modellari", r"""<p><b>Moddiy nuqta</b> — o‘lchamlari masalada ahamiyatsiz bo‘lgan jism (Yerning Quyosh atrofidagi orbitasi). <b>Absolyut qattiq jism</b> — nuqtalari orasidagi masofa o‘zgarmaydigan jism; uning 6 ta erkinlik darajasi bor (3 ilgarilanma + 3 aylanma). <b>Uzluksiz muhit</b> — molekulalararo masofadan ancha katta, lekin makroskopik o‘lchamdan kichik “fizik cheksiz kichik” hajmlarda o‘rtachalangan zichlik, tezlik va bosim maydonlari bilan tavsiflanadigan jism (suyuqlik, gaz, elastik jism). <b>Absolyut erkin zarra</b> — tashqi ta’sirsiz zarra; inersial sanoq sistemasi aynan shu bilan ta’riflanadi.</p>"""),
  ("Erkinlik darajalari va bog‘lanishlar", r"""<p>\(N\) nuqtali sistemaga \(k\) ta mustaqil holonom bog‘lanish \(f_j(\vec r_1,\ldots,\vec r_N,t)=0\) qo‘yilsa, erkinlik darajalari soni</p>
$$s=3N-k.$$
<p><b>Holonom</b> bog‘lanish faqat koordinatalar (va vaqt) orasidagi tenglik bilan ifodalanadi. <b>Noholonom</b> bog‘lanish integrallanmaydigan tezliklar munosabati yoki tengsizlikdir (masalan, sirpanmasdan dumalayotgan disk, sfera ichidagi gaz molekulasi). <b>Stasionar</b> (skleronom) bog‘lanish vaqtga bog‘liq emas, <b>nostasionar</b> (reonom) bog‘lanish esa bog‘liq (masalan, osilish nuqtasi tebranayotgan mayatnik).</p>"""),
  ("Umumlashgan koordinatalar", r"""<p>Sistemaning holatini to‘liq aniqlaydigan \(s\) ta mustaqil kattalik \(q_1,\ldots,q_s\) <b>umumlashgan koordinatalar</b> deyiladi. Ularning vaqt bo‘yicha hosilalari \(\dot q_i\) esa umumlashgan tezliklardir. Dekart koordinatalari ular orqali \(\vec r_a=\vec r_a(q_1,\ldots,q_s,t)\) kabi ifodalanadi va \(\vec v_a=\sum_i\frac{\partial\vec r_a}{\partial q_i}\dot q_i+\frac{\partial\vec r_a}{\partial t}\). Bog‘lanish reaksiyalari umumlashgan koordinatalarda tenglamalardan avtomatik chiqib ketadi — bu analitik mexanikaning asosiy afzalligi.</p>"""),
  ("Egri chiziqli koordinatalar", r"""<p><b>Silindrik</b> \((\rho,\varphi,z)\): \(x=\rho\cos\varphi,\ y=\rho\sin\varphi\), \(v^2=\dot\rho^2+\rho^2\dot\varphi^2+\dot z^2\).</p>
<p><b>Sferik</b> \((r,\theta,\varphi)\): \(x=r\sin\theta\cos\varphi,\ y=r\sin\theta\sin\varphi,\ z=r\cos\theta\),</p>
$$v^2=\dot r^2+r^2\dot\theta^2+r^2\sin^2\theta\,\dot\varphi^2.$$
<p>Lame koeffitsiyentlari: silindrikda \((1,\rho,1)\), sferikda \((1,r,r\sin\theta)\). Ular hajm elementi \(dV=\rho\,d\rho\,d\varphi\,dz\) va \(dV=r^2\sin\theta\,dr\,d\theta\,d\varphi\) ni beradi.</p>""")],
 example=(r"Erkinlik darajalari va koordinatalar",
  r"1) Tekislikdagi qo‘sh mayatnik, 2) uch atomli chiziqli bo‘lmagan qattiq molekula, 3) sfera sirtida harakatlanuvchi zarra uchun \(s\) ni toping. 4) \((x,y,z)=(1;\,1;\,\sqrt2)\) nuqtaning sferik koordinatalarini toping.",
  r"1) 2 nuqta × 3 = 6, bog‘lanishlar: ikki nuqta tekislikda (2) + ikki sterjen uzunligi (2) ⇒ \(s=2\) (\(\varphi_1,\varphi_2\)). 2) Qattiq jism ⇒ \(s=6\) (\(9-3\)). 3) \(s=2\) (\(\theta,\varphi\)). 4) \(r=\sqrt{1+1+2}=2\), \(\cos\theta=\sqrt2/2\) ⇒ \(\theta=45^\circ\), \(\operatorname{tg}\varphi=1\) ⇒ \(\varphi=45^\circ\)."),
 simtask=[r"Sferik rejimda \(r=2\), \(\theta=45^\circ\), \(\varphi=45^\circ\) o‘rnating va Dekart koordinatalari misoldagidek chiqishini tekshiring.",
          r"\(\theta\) ni 0° dan 180° gacha o‘zgartiring: \(z\) va \(\rho=r\sin\theta\) qanday o‘zgaradi?",
          r"Silindrik rejimga o‘tib, bir xil nuqtani \((\rho,\varphi,z)\) orqali ifodalang."],
 mistakes=[(r"“Umumlashgan koordinata albatta uzunlik o‘lchamiga ega.”", r"U burchak, yuza yoki boshqa kattalik bo‘lishi mumkin; muhimi — holatni bir qiymatli aniqlashi."),
           (r"“Har qanday bog‘lanish erkinlik darajasini kamaytiradi.”", r"Faqat holonom bog‘lanish. Noholonom bog‘lanish koordinatalar sonini kamaytirmaydi, tezliklarga cheklov qo‘yadi."),
           (r"“Sferik koordinatada \(v^2=\dot r^2+\dot\theta^2+\dot\varphi^2\).”", r"Lame koeffitsiyentlari kerak: \(v^2=\dot r^2+r^2\dot\theta^2+r^2\sin^2\theta\,\dot\varphi^2\).")],
 ai=r"""Sen nazariy mexanika bo‘yicha repetitorsan. Mavzu: erkinlik darajalari va bog‘lanishlar.
Menga 5 ta mexanik sistemani (masalan, qiya tekislikdagi g‘ildirak, sharnirli mexanizm) berib, har biri uchun erkinlik darajasini va bog‘lanish turini topishni so‘ra. Javoblarimni tekshir, xato bo‘lsa yo‘naltiruvchi savol ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Absolyut qattiq jismning erkinlik darajalari soni:", ["6", "3", "9", "5"], 0, "3 ilgarilanma + 3 aylanma."),
  (r"Tekislikdagi matematik mayatnik uchun \(s\) =", ["1", "2", "3", "0"], 0, r"Bitta burchak \(\varphi\)."),
  (r"Holonom bog‘lanish:", ["koordinatalar orasidagi tenglik", "integrallanmaydigan tezliklar munosabati", "tengsizlik", "kuch cheklovi"], 0, r"\(f(\vec r,t)=0\)."),
  (r"Sirpanmasdan dumalayotgan disk (tekislikda, ixtiyoriy yo‘nalish) bog‘lanishi:", ["noholonom", "holonom stasionar", "holonom nostasionar", "bog‘lanish yo‘q"], 0, "Tezliklar munosabati integrallanmaydi."),
  (r"Sferik koordinatada \(v^2\) =", [r"\(\dot r^2+r^2\dot\theta^2+r^2\sin^2\theta\,\dot\varphi^2\)", r"\(\dot r^2+\dot\theta^2+\dot\varphi^2\)", r"\(\dot r^2+r^2\dot\varphi^2\)", r"\(r^2(\dot\theta^2+\dot\varphi^2)\)"], 0, "Lame koeffitsiyentlari bilan."),
  (r"\((x,y,z)=(0;0;3)\) nuqtaning sferik \(\theta\) burchagi:", ["0°", "90°", "45°", "180°"], 0, r"\(z\) o‘qi ustida."),
  (r"Silindrik koordinatada hajm elementi:", [r"\(\rho\,d\rho\,d\varphi\,dz\)", r"\(d\rho\,d\varphi\,dz\)", r"\(\rho^2d\rho\,d\varphi\,dz\)", r"\(r^2\sin\theta\,dr\,d\theta\,d\varphi\)"], 0, "Lame koeffitsiyentlari ko‘paytmasi."),
  (r"\(N\) nuqta va \(k\) holonom bog‘lanish uchun erkinlik darajasi:", [r"\(3N-k\)", r"\(3N+k\)", r"\(N-k\)", r"\(6N-k\)"], 0, "Ta’rif."),
  (r"Osilish nuqtasi vertikal tebranayotgan mayatnik bog‘lanishi:", ["nostasionar (reonom)", "stasionar", "noholonom", "ideal emas"], 0, "Bog‘lanish tenglamasi vaqtni o‘z ichiga oladi."),
  (r"Uzluksiz muhit modelida “nuqta” deganda:", ["molekulalardan ko‘p, lekin makroskopik o‘lchamdan kichik hajm", "bitta molekula", "atom yadrosi", "butun jism"], 0, "Fizik cheksiz kichik hajm.")],
 blits=["Yer — moddiy nuqtami? Qachon ha, qachon yo‘q?", "Velosiped g‘ildiragining erkinlik darajasi nechta?", "Nima uchun umumlashgan koordinatalarda reaksiya kuchlari yo‘qoladi?", "Qaysi masalada sferik koordinata qulay?"]))

L.append(dict(
 n=3, short=r"Eng kichik ta’sir prinsipi", sim="action", refs=[1, 2, 3], intl=["landau", "goldstein", "feynman"], tn=["TN4", "TN5", "TN7", "TN20"],
 title=r"Eng kichik ta’sir prinsipi. Lagranj funksiyasi va Lagranj tenglamalari",
 goal=r"Variatsion prinsiplarni (Ferma, Gamilton) o‘rganish, ta’sir funksionalidan Eyler–Lagranj tenglamalarini keltirib chiqarish, erkin zarra uchun Lagranj funksiyasini simmetriyadan topish va birinchi tur Lagranj tenglamalarini tuzish.",
 outcomes=[r"ta’sir \(S=\int L\,dt\) va uning variatsiyasini ta’riflaydi;",
           r"\(\delta S=0\) shartidan Eyler–Lagranj tenglamasini keltirib chiqaradi;",
           r"erkin zarra uchun \(L=mv^2/2\) ekanini fazo-vaqt xossalaridan asoslaydi;",
           r"bog‘lanishli sistema uchun Lagranj ko‘paytuvchilari bilan birinchi tur tenglamalarni yozadi."],
 plan=["Variatsion prinsiplar: Ferma va Gamilton", "Ta’sir funksionali va uning variatsiyasi", "Eyler–Lagranj tenglamalari", "Erkin zarra uchun Lagranj funksiyasi", "Birinchi tur Lagranj tenglamalari"],
 terms=["ta’sir", "variatsiya", "Eyler–Lagranj tenglamasi", "Lagranj funksiyasi", "Lagranj ko‘paytuvchisi", "Ferma prinsipi"],
 theory=[
  ("Variatsion prinsiplar", r"""<p><b>Ferma prinsipi</b>: yorug‘lik ikki nuqta orasida optik yo‘l uzunligi \(\int n\,ds\) ekstremal bo‘lgan yo‘ldan boradi — undan qaytish va sinish qonunlari kelib chiqadi. Mexanikada uning analogi <b>Gamilton prinsipi (eng kichik ta’sir prinsipi)</b>: sistema \(t_1\) va \(t_2\) paytlardagi berilgan holatlar orasida shunday harakatlanadiki, ta’sir</p>
$$S=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt$$
<p>statsionar (odatda minimal) qiymat oladi: \(\delta S=0\).</p>"""),
  ("Eyler–Lagranj tenglamalari", r"""<p>Haqiqiy trayektoriyaga chetlari mahkamlangan kichik qo‘shimcha \(\delta q(t)\) beramiz (\(\delta q(t_1)=\delta q(t_2)=0\)). Bo‘laklab integrallash quyidagini beradi:</p>
$$\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}-\frac{d}{dt}\frac{\partial L}{\partial\dot q}\right)\delta q\,dt=0\ \Rightarrow\ \frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=0.$$
<p>Bu \(s\) ta ikkinchi tartibli tenglama — harakat tenglamalari. \(L\) ga istalgan \(df(q,t)/dt\) qo‘shilsa, tenglamalar o‘zgarmaydi.</p>"""),
  ("Erkin zarra va zarralar sistemasi", r"""<p>Inersial sistemada fazo bir jinsli va izotrop, vaqt bir jinsli. Shuning uchun erkin zarraning \(L\) i \(\vec r\), \(t\) va \(\vec v\) yo‘nalishiga bog‘liq bo‘lolmaydi: \(L=L(v^2)\). Galiley invariantligi talabidan esa \(L=\frac{mv^2}{2}\) kelib chiqadi. O‘zaro ta’sirlashuvchi zarralar sistemasi uchun:</p>
$$L=\sum_a\frac{m_av_a^2}{2}-U(\vec r_1,\vec r_2,\ldots)=T-U.$$
<p>Bundan Nyuton tenglamasi \(m_a\ddot{\vec r}_a=-\partial U/\partial\vec r_a\) kelib chiqadi.</p>"""),
  ("Birinchi tur Lagranj tenglamalari", r"""<p>Dekart koordinatalarida \(k\) ta holonom bog‘lanish \(f_j(\vec r,t)=0\) bo‘lsa, Lagranj ko‘paytuvchilari usuli quyidagini beradi:</p>
$$m_a\ddot{\vec r}_a=\vec F_a+\sum_{j=1}^{k}\lambda_j\nabla_af_j.$$
<p>\(\lambda_j\nabla f_j\) — bog‘lanish reaksiya kuchlari. Bu tenglamalar reaksiyani ham topishga imkon beradi, ammo tenglamalar soni ko‘p (\(3N+k\)). Shuning uchun amalda ikkinchi tur tenglamalar qulayroq.</p>""")],
 example=(r"Ta’sirning minimalligini tekshirish",
  r"Massasi \(m=1\) kg jism \(T=1\) s davomida erkin tushmoqda. Haqiqiy yo‘lga \(\eta(t)=\varepsilon\sin(\pi t/T)\) qo‘shimcha berilsa, ta’sir qanchaga o‘zgaradi? \(\varepsilon=0{,}1\) m uchun hisoblang.",
  r"\(L=m\dot y^2/2-mgy\) — potensial \(y\) bo‘yicha chiziqli, shuning uchun birinchi tartibli hadlar \(\delta S=0\) tufayli yo‘qoladi. Faqat kinetik qism qoladi: \(\Delta S=\frac m2\int_0^T\dot\eta^2dt=\frac m2\varepsilon^2\frac{\pi^2}{T^2}\cdot\frac T2=\frac{m\pi^2\varepsilon^2}{4T}\). Son bilan: \(\Delta S=9{,}87\cdot0{,}01/4=0{,}0247\) J·s \(>0\) — haqiqiy yo‘lda ta’sir minimal."),
 simtask=[r"\(\varepsilon\) ni 0 dan 0,3 m gacha oshirib, \(\Delta S\) parabola bo‘yicha o‘sishini tekshiring.",
          r"Garmonikani 2 ga o‘zgartiring (\(\sin2\pi t/T\)): bir xil \(\varepsilon\) da \(\Delta S\) necha marta katta?",
          r"Manfiy \(\varepsilon\) da ham \(\Delta S>0\) ekanini kuzating. Bu nimani anglatadi?"],
 mistakes=[(r"“Ta’sir har doim minimal bo‘ladi.”", r"Prinsip statsionarlikni talab qiladi; uzun vaqt oraliqlarida (masalan, ossilyatorda yarim davrdan ko‘p) egar nuqta bo‘lishi mumkin."),
           (r"“\(L=T+U\).”", r"Lagranj funksiyasi \(L=T-U\); \(T+U\) — energiya."),
           (r"“Lagranj funksiyasi yagona.”", r"Unga to‘liq hosila \(df(q,t)/dt\) qo‘shish tenglamalarni o‘zgartirmaydi.")],
 ai=r"""Sen variatsion hisob bo‘yicha repetitorsan. Mavzu: eng kichik ta’sir prinsipi.
Menga Eyler–Lagranj tenglamasini keltirib chiqarishni bosqichma-bosqich, har qadamda savol berib o‘rgat. Keyin braxistoxrona masalasini qanday qo‘yishni tushuntir (yechimni men topaman). Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Ta’sir funksionali:", [r"\(S=\int L\,dt\)", r"\(S=\int H\,dt\)", r"\(S=\int F\,dx\)", r"\(S=\int p\,dt\)"], 0, "Ta’rif."),
  (r"Eyler–Lagranj tenglamasi:", [r"\(\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}=0\)", r"\(\frac{\partial L}{\partial q}=0\)", r"\(\frac{dL}{dt}=0\)", r"\(\dot p=\partial H/\partial p\)"], 0, r"\(\delta S=0\) dan."),
  (r"Erkin zarra uchun \(L\) =", [r"\(mv^2/2\)", r"\(mv\)", r"\(mv^2\)", r"\(-mv^2/2\)"], 0, "Bir jinslilik, izotropiya va Galiley invariantligi."),
  (r"Potensial maydonda \(L\) =", [r"\(T-U\)", r"\(T+U\)", r"\(U-T\)", r"\(TU\)"], 0, "Ta’rif."),
  (r"Ferma prinsipi qaysi kattalikning ekstremalligini talab qiladi?", ["optik yo‘l uzunligi", "geometrik uzunlik", "energiya", "impuls"], 0, r"\(\int n\,ds\)."),
  (r"\(L\) ga \(df(q,t)/dt\) qo‘shilsa, harakat tenglamalari:", ["o‘zgarmaydi", "ikki marta ko‘payadi", "teskari ishora oladi", "yo‘qoladi"], 0, "Ta’sir faqat doimiy songa o‘zgaradi."),
  (r"Variatsiyada chetki shartlar:", [r"\(\delta q(t_1)=\delta q(t_2)=0\)", r"\(\delta\dot q=0\)", r"\(\delta L=0\)", r"\(q(t_1)=0\)"], 0, "Uchlari mahkamlangan."),
  (r"Birinchi tur Lagranj tenglamalarida \(\lambda\nabla f\) nimani ifodalaydi?", ["bog‘lanish reaksiya kuchini", "inersiya kuchini", "ishqalanishni", "umumlashgan impulsni"], 0, "Lagranj ko‘paytuvchilari."),
  (r"Misoldagi \(\Delta S\) qo‘shimcha amplitudasi 2 marta oshsa:", ["4 marta ortadi", "2 marta ortadi", "o‘zgarmaydi", "kamayadi"], 0, r"\(\Delta S\propto\varepsilon^2\)."),
  (r"Ta’sirning birligi:", ["J·s", "J", "N·m", "kg·m/s"], 0, "Energiya × vaqt — Plank doimiysi bilan bir xil.")],
 blits=["Yorug‘lik “eng tez yo‘lni qayerdan biladi”?", "Nima uchun \\(L=T-U\\) bo‘ladi, \\(T+U\\) emas?", "Ta’sirning birligi qaysi fundamental doimiyga mos?", "Variatsion prinsip va Nyuton qonunlari teng kuchlimi?"]))

L.append(dict(
 n=4, short=r"Ikkinchi tur Lagranj tenglamalari", sim="pendulum", refs=[1, 2, 4], intl=["goldstein", "taylor", "thornton"], tn=["TN4", "TN5", "TN6", "TN17"],
 title=r"Potensial va nopotensial kuchlar uchun ikkinchi tur Lagranj tenglamalari",
 goal=r"Ikkinchi tur Lagranj tenglamalarini umumlashgan kuchlar bilan yozish, potensial, dissipativ va giroskopik kuchlarni farqlash hamda tenglamalarni tuzish algoritmini o‘zlashtirish.",
 outcomes=[r"umumlashgan kuchni \(Q_i=\sum\vec F_a\cdot\partial\vec r_a/\partial q_i\) bo‘yicha hisoblaydi;",
           r"potensial va nopotensial kuchlar xossalarini ajratadi;",
           r"Reley dissipativ funksiyasi bilan so‘nuvchi harakat tenglamasini yozadi;",
           r"5 qadamli algoritm bo‘yicha mayatnik va boshqa sistemalar tenglamalarini tuzadi."],
 plan=["Umumlashgan kuchlar", "Ikkinchi tur Lagranj tenglamalari", "Potensial kuchlar xossalari", "Nopotensial kuchlar: dissipativ va giroskopik", "Tenglamalarni tuzish algoritmi"],
 terms=["umumlashgan kuch", "potensial kuch", "Reley funksiyasi", "giroskopik kuch", "umumlashgan potensial", "matematik mayatnik"],
 theory=[
  ("Umumlashgan kuchlar va tenglamalar", r"""<p>Mumkin bo‘lgan ko‘chishdagi ish \(\delta A=\sum_a\vec F_a\cdot\delta\vec r_a=\sum_iQ_i\,\delta q_i\). Bundan <b>umumlashgan kuch</b> \(Q_i=\sum_a\vec F_a\cdot\partial\vec r_a/\partial q_i\) kelib chiqadi. Ideal bog‘lanishlarda (reaksiyalar ish bajarmaydi) Dalamber–Lagranj prinsipidan quyidagi tenglamalar olinadi:</p>
$$\frac{d}{dt}\frac{\partial T}{\partial\dot q_i}-\frac{\partial T}{\partial q_i}=Q_i,\qquad i=1,\ldots,s.$$"""),
  ("Potensial kuchlar", r"""<p>Agar \(Q_i=-\partial U/\partial q_i\) bo‘lsa (konservativ kuchlar, \(\operatorname{rot}\vec F=0\), yopiq yo‘ldagi ish nol), \(L=T-U\) kiritib quyidagini olamiz:</p>
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}=Q_i^{\text{nopot}}.$$
<p>Potensial kuchlarning ishi yo‘lga bog‘liq emas, mexanik energiya saqlanadi. Misollar: og‘irlik, elastiklik, Kulon kuchlari.</p>"""),
  ("Nopotensial kuchlar", r"""<p><b>Dissipativ kuchlar</b> (qovushqoq ishqalanish \(\vec F=-b\vec v\)) Reley funksiyasi \(R=\frac12\sum b_{ik}\dot q_i\dot q_k\) bilan kiritiladi:</p>
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}+\frac{\partial R}{\partial\dot q_i}=0,\qquad\frac{dE}{dt}=-2R.$$
<p><b>Giroskopik kuchlar</b> (Lorens kuchining magnit qismi, Koriolis kuchi) ish bajarmaydi va tezlikka perpendikulyar. Ular <b>umumlashgan potensial</b> \(U=q\varphi-q\vec v\cdot\vec A\) orqali kiritiladi: \(L=\frac{mv^2}{2}-q\varphi+q\vec v\cdot\vec A\).</p>"""),
  ("Tenglamalarni tuzish algoritmi", r"""<ol><li>Erkinlik darajalarini aniqlang va umumlashgan koordinatalarni tanlang.</li><li>Kinetik energiyani \(T(q,\dot q)\) ko‘rinishida yozing.</li><li>Potensial energiyani \(U(q)\) yozing, nopotensial kuchlar uchun \(Q_i\) yoki \(R\) ni toping.</li><li>\(L=T-U\) ni tuzing va hosilalarni hisoblang.</li><li>Tenglamalarni soddalashtiring, chegaraviy holatlarda tekshiring (masalan, kichik burchaklar).</li></ol>
<p>Matematik mayatnik uchun: \(L=\frac12ml^2\dot\theta^2+mgl\cos\theta\) ⇒ \(\ddot\theta+\frac gl\sin\theta=0\).</p>""")],
 example=(r"Katta amplitudali mayatnik",
  r"\(l=1\) m mayatnik. Kichik tebranishlar davri va \(\theta_0=60^\circ\) amplitudadagi davrni toping (\(g=9{,}81\) m/s²).",
  r"\(T_0=2\pi\sqrt{l/g}=2{,}006\) s. Aniq: \(T=4\sqrt{l/g}\,K(k)\), \(k=\sin(\theta_0/2)=0{,}5\), \(K(0{,}5)=1{,}686\) ⇒ \(T=4\cdot0{,}3193\cdot1{,}686=2{,}153\) s. Qator bo‘yicha: \(T\approx T_0(1+\theta_0^2/16+11\theta_0^4/3072)=2{,}006\cdot1{,}0728=2{,}152\) s — 7 % uzun."),
 simtask=[r"\(\theta_0\) ni 10° dan 170° gacha oshirib, davr kichik tebranishlar davridan qanchalik farq qilishini jadvalga yozing.",
          r"\(\theta_0=60^\circ\) da model davri misoldagi 2,15 s ga teng ekanini tekshiring.",
          r"So‘nishni yoqib, \(\theta(t)\) amplitudasi eksponensial kamayishini kuzating va \(\gamma\) ni grafikdan baholang."],
 mistakes=[(r"“Umumlashgan kuchning o‘lchami har doim nyuton.”", r"\(Q_i\delta q_i\) — ish; agar \(q_i\) burchak bo‘lsa, \(Q_i\) kuch momenti (N·m)."),
           (r"“Ishqalanishni \(U\) ga qo‘shish mumkin.”", r"Dissipativ kuchning potensiali yo‘q; u \(Q_i\) yoki Reley funksiyasi orqali kiritiladi."),
           (r"“Mayatnik davri amplitudaga bog‘liq emas.”", r"Bu faqat kichik amplitudalar uchun to‘g‘ri; 60° da davr 7 % uzun.")],
 ai=r"""Sen analitik mexanika bo‘yicha repetitorsan. Mavzu: ikkinchi tur Lagranj tenglamalari.
Menga 3 ta sistema ber (aylanayotgan halqadagi munchoq, qiya tekislikda dumalayotgan silindr, prujinali mayatnik). Har biri uchun 5 qadamli algoritm bo‘yicha tenglama tuzishimni so‘ra va har bir qadamimni tekshir. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Ikkinchi tur Lagranj tenglamasi (potensial kuchlar):", [r"\(\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}=0\)", r"\(m\ddot q=Q\)", r"\(\dot p=\partial H/\partial p\)", r"\(\delta L=0\)"], 0, "Ta’rif."),
  (r"Umumlashgan kuch:", [r"\(\sum\vec F_a\cdot\partial\vec r_a/\partial q_i\)", r"\(\partial L/\partial\dot q_i\)", r"\(m\ddot q_i\)", r"\(\partial T/\partial q_i\)"], 0, "Ish orqali ta’rif."),
  (r"Matematik mayatnik tenglamasi:", [r"\(\ddot\theta+\frac gl\sin\theta=0\)", r"\(\ddot\theta+\frac lg\theta=0\)", r"\(\ddot\theta=g\cos\theta\)", r"\(\dot\theta=\sqrt{g/l}\)"], 0, r"\(L=\frac12ml^2\dot\theta^2+mgl\cos\theta\)."),
  (r"Reley funksiyasi bilan energiyaning o‘zgarish tezligi:", [r"\(dE/dt=-2R\)", r"\(dE/dt=R\)", r"\(dE/dt=0\)", r"\(dE/dt=-R/2\)"], 0, "Dissipatsiya quvvati."),
  (r"Lorens kuchining magnit qismi qanday kuch?", ["giroskopik", "dissipativ", "potensial", "reaksiya"], 0, "Ish bajarmaydi."),
  (r"Zaryadli zarra uchun umumlashgan potensial:", [r"\(q\varphi-q\vec v\cdot\vec A\)", r"\(q\varphi\)", r"\(q\vec v\cdot\vec A\)", r"\(qE\)"], 0, "Maydondagi zarra Lagranjiani."),
  (r"\(q\) burchak bo‘lsa, \(Q\) ning birligi:", ["N·m", "N", "J/m", "rad"], 0, "Kuch momenti."),
  (r"\(l=1\) m mayatnikning kichik tebranishlar davri:", ["≈ 2,0 s", "≈ 1,0 s", "≈ 3,1 s", "≈ 6,3 s"], 0, r"\(2\pi\sqrt{1/9{,}81}\)."),
  (r"Potensial kuchning ishi:", ["yo‘lga bog‘liq emas", "yo‘lga bog‘liq", "har doim nol", "tezlikka bog‘liq"], 0, "Konservativlik."),
  (r"Ideal bog‘lanish:", ["mumkin bo‘lgan ko‘chishlarda reaksiyalar ishi nol", "ishqalanishsiz har qanday bog‘lanish", "stasionar bog‘lanish", "noholonom bog‘lanish"], 0, "Ta’rif.")],
 blits=["Qachon Nyuton tenglamasidan Lagranj tenglamasi qulayroq?", "Ishqalanishni Lagranjianga kiritish mumkinmi?", "Magnit maydon zarraning energiyasini o‘zgartiradimi?", "Mayatnik davri amplitudaga qanday bog‘liq?"]))

L.append(dict(
 n=5, short=r"Saqlanish qonunlari va Lagranj tenglamalari", sim="noether", refs=[1, 2, "Q1"], intl=["landau", "goldstein", "hand"], tn=["TN8", "TN14", "TN21"],
 title=r"Saqlanish qonunlari va Lagranj tenglamalari: energiya, impuls va impuls momenti",
 goal=r"Lagranj tenglamalaridan energiya, impuls va impuls momentining saqlanish qonunlarini keltirib chiqarish, siklik koordinatalar va umumlashgan impulslarni harakat integrallarini topish uchun qo‘llash.",
 outcomes=[r"umumlashgan impuls \(p_i=\partial L/\partial\dot q_i\) va umumlashgan energiyani ta’riflaydi;",
           r"siklik koordinatani aniqlab, unga mos saqlanuvchi impulsni topadi;",
           r"energiya, impuls va impuls momenti saqlanishini Lagranj tenglamalaridan keltirib chiqaradi;",
           r"Kepler ikkinchi qonunini impuls momenti saqlanishi bilan izohlaydi."],
 plan=["Umumlashgan impuls va siklik koordinatalar", "Energiyaning saqlanishi", "Impulsning saqlanishi", "Impuls momentining saqlanishi", "Nyoter teoremasining umumiy shakli"],
 terms=["umumlashgan impuls", "siklik koordinata", "umumlashgan energiya", "Kepler ikkinchi qonuni", "massa markazi", "Nyoter teoremasi"],
 theory=[
  ("Umumlashgan impuls va siklik koordinatalar", r"""<p><b>Umumlashgan impuls</b> \(p_i=\partial L/\partial\dot q_i\). Agar \(L\) biror \(q_j\) ga bog‘liq bo‘lmasa (\(q_j\) — <b>siklik</b>), Lagranj tenglamasidan</p>
$$\dot p_j=\frac{\partial L}{\partial q_j}=0\ \Rightarrow\ p_j=\text{const}.$$
<p>Siklik koordinatalar harakat integrallarini bevosita beradi va masalani soddalashtiradi. Shuning uchun koordinatalarni tanlashda simmetriyaga mosini olish kerak.</p>"""),
  ("Energiyaning saqlanishi", r"""<p>\(L\) vaqtga oshkor bog‘liq bo‘lmasa, uning to‘liq hosilasini Lagranj tenglamalari bilan hisoblab quyidagini olamiz:</p>
$$\frac{d}{dt}\Big(\sum_i\dot q_i\frac{\partial L}{\partial\dot q_i}-L\Big)=-\frac{\partial L}{\partial t}=0\ \Rightarrow\ h=\sum_ip_i\dot q_i-L=\text{const}.$$
<p>\(h\) — umumlashgan energiya. Stasionar bog‘lanishlarda \(T\) tezliklarning kvadratik formasi bo‘ladi va Eyler teoremasi bo‘yicha \(\sum\dot q\,\partial T/\partial\dot q=2T\), demak \(h=T+U=E\).</p>"""),
  ("Impuls va impuls momenti", r"""<p>Butun sistemani \(\delta\vec r\) ga siljitganda \(\delta L=\delta\vec r\cdot\sum_a\partial L/\partial\vec r_a=0\) bo‘lsa, \(\sum_a\dot{\vec p}_a=0\), ya’ni \(\vec P=\sum\vec p_a=\text{const}\). Natijada massa markazi to‘g‘ri chiziqli tekis harakatlanadi: \(\vec V=\vec P/M\).</p>
<p>Cheksiz kichik burilishda \(\delta\vec r_a=\delta\vec\varphi\times\vec r_a\). Invariantlikdan \(\vec M=\sum_a\vec r_a\times\vec p_a=\text{const}\). Markaziy maydonda qutb koordinatalarida \(L=\frac m2(\dot r^2+r^2\dot\varphi^2)-U(r)\), \(\varphi\) siklik ⇒ \(M=mr^2\dot\varphi=\text{const}\). Bu sektorial tezlik \(\dot\sigma=M/2m\) ning doimiyligi, ya’ni Keplerning ikkinchi qonunidir.</p>"""),
  ("Nyoter teoremasi", r"""<p>Agar \(L\) koordinatalarning bir parametrli \(q_i\to q_i+\epsilon\,\xi_i(q)\) almashtirishiga nisbatan invariant bo‘lsa, quyidagi kattalik harakat integrali bo‘ladi:</p>
$$I=\sum_i\frac{\partial L}{\partial\dot q_i}\,\xi_i(q).$$
<p>Siljish uchun \(\xi\) birlik vektor bo‘lib, \(I\) impulsni beradi. Burilish uchun \(\xi=\hat n\times\vec r\) bo‘lib, \(I\) impuls momentini beradi.</p>""")],
 example=(r"Yer orbitasining sektorial tezligi",
  r"Yer perigeliyda Quyoshdan \(r=1{,}471\cdot10^{11}\) m masofada \(v=30{,}29\) km/s tezlik bilan harakatlanadi. Birlik massaga impuls momenti va sektorial tezlikni toping. Afeliyda (\(r=1{,}521\cdot10^{11}\) m) tezlik qancha?",
  r"\(M/m=rv=1{,}471\cdot10^{11}\cdot3{,}029\cdot10^4=4{,}456\cdot10^{15}\) m²/s. Sektorial tezlik \(\dot\sigma=M/2m=2{,}23\cdot10^{15}\) m²/s. Afeliyda tezlik radiusga perpendikulyar: \(v_a=4{,}456\cdot10^{15}/1{,}521\cdot10^{11}=29{,}30\) km/s."),
 simtask=[r"“Markaziy” potensialni tanlab, \(L_z\) saqlanishini, impuls esa saqlanmasligini grafikda ko‘ring.",
          r"“Bir jinsli maydon” rejimida qaysi kattaliklar saqlanadi? Simmetriya bilan izohlang.",
          r"“Anizotrop ossilyator”da \(k_x\ne k_y\) bo‘lsa, \(L_z\) nima uchun saqlanmaydi?"],
 mistakes=[(r"“Umumlashgan impuls har doim \(m\dot q\).”", r"\(p=\partial L/\partial\dot q\); burchak uchun bu \(mr^2\dot\varphi\), magnit maydonda esa \(m\vec v+q\vec A\)."),
           (r"“Umumlashgan energiya har doim \(T+U\).”", r"Bu faqat stasionar bog‘lanishlarda to‘g‘ri; aylanayotgan sistemalarda \(h\ne E\)."),
           (r"“Siklik koordinata \(L\) da umuman qatnashmaydi.”", r"Uning tezligi \(\dot q_j\) qatnashishi mumkin; faqat \(q_j\) ning o‘zi yo‘q.")],
 ai=r"""Sen nazariy mexanika repetitorisan. Mavzu: siklik koordinatalar va saqlanish qonunlari.
Menga 4 ta Lagranj funksiyasini ber, har birida siklik koordinatalarni va ularga mos saqlanuvchi kattaliklarni topishimni so‘ra. Oxirida Nyoter teoremasini o‘z so‘zlarim bilan tushuntirishimni so‘ra va baholab ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Umumlashgan impuls:", [r"\(\partial L/\partial\dot q\)", r"\(\partial L/\partial q\)", r"\(m\dot q\) har doim", r"\(\partial H/\partial q\)"], 0, "Ta’rif."),
  (r"Siklik koordinata:", [r"\(L\) da oshkor qatnashmaydigan koordinata", "vaqtga bog‘liq koordinata", "davriy o‘zgaradigan koordinata", "burchak koordinatasi"], 0, r"\(\partial L/\partial q_j=0\)."),
  (r"Markaziy maydonda qutb koordinatalarida siklik koordinata:", [r"\(\varphi\)", r"\(r\)", r"\(t\)", "hech biri"], 0, r"\(L\) faqat \(\dot\varphi\) ga bog‘liq."),
  (r"Umumlashgan energiya:", [r"\(\sum p_i\dot q_i-L\)", r"\(L-\sum p\dot q\)", r"\(T-U\)", r"\(\partial L/\partial t\)"], 0, "Ta’rif."),
  (r"Kepler ikkinchi qonuni qaysi saqlanish qonunining natijasi?", ["impuls momenti", "energiya", "impuls", "massa"], 0, r"\(\dot\sigma=M/2m\)."),
  (r"Yopiq sistema massa markazi:", ["to‘g‘ri chiziqli tekis harakatlanadi", "tinch turadi har doim", "aylana bo‘ylab harakatlanadi", "tezlanish bilan harakatlanadi"], 0, r"\(\vec P=\text{const}\)."),
  (r"Stasionar bog‘lanishlarda \(\sum\dot q\,\partial T/\partial\dot q\) =", [r"\(2T\)", r"\(T\)", "0", r"\(T/2\)"], 0, "Bir jinsli kvadratik forma uchun Eyler teoremasi."),
  (r"Bir jinsli og‘irlik maydonida (\(y\) vertikal) saqlanadi:", [r"\(p_x\) va \(E\)", r"\(p_y\)", r"\(L_z\)", "hech narsa"], 0, r"\(x\) bo‘yicha siljish simmetriyasi."),
  (r"Afeliyda Yer tezligi perigeliydagidan:", ["kichik", "katta", "teng", "nol"], 0, r"\(rv=\text{const}\), \(r\) katta."),
  (r"Nyoter teoremasidagi saqlanuvchi kattalik:", [r"\(\sum\frac{\partial L}{\partial\dot q_i}\xi_i\)", r"\(\sum q_i\xi_i\)", r"\(L\xi\)", r"\(\partial L/\partial t\)"], 0, "Generator bo‘yicha proyeksiya.")],
 blits=["Nima uchun qutb koordinatalari markaziy masalada qulay?", "Aylanayotgan karuselda energiya saqlanadimi?", "Siklik koordinata va simmetriya qanday bog‘langan?", "Kosmonavt fazoda qanday burilishi mumkin?"]))

L.append(dict(
 n=6, short=r"Kichik tebranishlar", sim="oscill", refs=[1, 2, 3], intl=["landau", "taylor", "goldstein"], tn=["TN9", "TN10", "TN22", "TN23"],
 title=r"Kichik tebranishlar: erkin, so‘nuvchi va majburiy tebranishlar. Rezonans",
 goal=r"Turg‘un muvozanat atrofidagi kichik tebranishlar uchun Lagranj funksiyasini tuzish, erkin, so‘nuvchi va majburiy tebranishlar tenglamalarini yechish, rezonans shartini va ko‘p erkinlik darajali sistemalarning xos chastotalarini aniqlash.",
 outcomes=[r"muvozanat atrofida \(U\) ni Teylor qatoriga yoyib, \(L=\frac12m\dot q^2-\frac12kq^2\) ko‘rinishiga keltiradi;",
           r"so‘nuvchi tebranishlar chastotasi va asllikni hisoblaydi;",
           r"majburiy tebranishlar amplitudasi va fazasining chastotaga bog‘liqligini tahlil qiladi;",
           r"bir necha erkinlik darajali sistemaning xos chastotalarini \(\det(K-\omega^2M)=0\) dan topadi."],
 plan=["Muvozanat va uning turg‘unligi", "Erkin chiziqli tebranishlar", "So‘nuvchi tebranishlar", "Majburiy tebranishlar va rezonans", "Ko‘p erkinlik darajali sistemalar"],
 terms=["turg‘un muvozanat", "xos chastota", "so‘nish koeffitsiyenti", "asllik", "rezonans", "normal moda"],
 theory=[
  ("Muvozanat va kichik tebranishlar", r"""<p>Muvozanat nuqtasida \(\partial U/\partial q=0\). Agar \(U\) minimum bo‘lsa (\(U''>0\)), muvozanat <b>turg‘un</b> (Lagranj–Dirixle teoremasi). Uning atrofida \(U\approx U_0+\frac12kq^2\), \(k=U''(q_0)\), va kinetik energiya \(\frac12m\dot q^2\) bo‘ladi:</p>
$$L=\frac{m\dot q^2}{2}-\frac{kq^2}{2}\ \Rightarrow\ \ddot q+\omega_0^2q=0,\quad\omega_0=\sqrt{k/m},\quad q=a\cos(\omega_0t+\alpha).$$
<p>Prujina uchun elastiklik energiyasi \(U=\frac12k\,\Delta l^2\).</p>"""),
  ("So‘nuvchi tebranishlar", r"""<p>Qovushqoq ishqalanishda (\(R=\frac12b\dot q^2\)) tenglama quyidagicha bo‘ladi:</p>
$$\ddot q+2\beta\dot q+\omega_0^2q=0,\quad\beta=\frac{b}{2m},\qquad q=a\,e^{-\beta t}\cos(\omega t+\alpha),\quad\omega=\sqrt{\omega_0^2-\beta^2}.$$
<p>Asllik \(Q=\omega_0/2\beta\) — energiya bir radianda qanchalik kam yo‘qolishini ko‘rsatadi. \(\beta\ge\omega_0\) bo‘lsa, harakat aperiodik.</p>"""),
  ("Majburiy tebranishlar va rezonans", r"""<p>Tashqi davriy kuch \(F_0\cos\gamma t\) ta’sirida:</p>
$$\ddot q+2\beta\dot q+\omega_0^2q=\frac{F_0}{m}\cos\gamma t.$$
<p>Uning barqaror yechimi \(q=b\cos(\gamma t-\delta)\), bunda:</p>
$$b=\frac{F_0/m}{\sqrt{(\omega_0^2-\gamma^2)^2+4\beta^2\gamma^2}},\qquad\operatorname{tg}\delta=\frac{2\beta\gamma}{\omega_0^2-\gamma^2}.$$
<p>Amplituda \(\gamma_r=\sqrt{\omega_0^2-2\beta^2}\) da maksimal. Kichik so‘nishda \(b_{max}\approx F_0/(2m\beta\omega_0)\), faza esa \(\pi/2\) ga siljiydi. So‘nish bo‘lmasa, rezonansda amplituda vaqt bo‘yicha chiziqli o‘sadi.</p>"""),
  ("Bir necha erkinlik darajali sistemalar", r"""<p>\(L=\frac12\sum m_{ik}\dot q_i\dot q_k-\frac12\sum k_{ik}q_iq_k\) uchun \(q_k=A_ke^{i\omega t}\) yechim izlanadi. Natijada xarakteristik tenglama hosil bo‘ladi:</p>
$$\det\left(k_{ik}-\omega^2m_{ik}\right)=0.$$
<p>Uning ildizlari xos chastotalar, mos vektorlari esa <b>normal modalar</b> (xos shakllar). Masalan, uchlari devorga mahkamlangan uch prujina bilan bog‘langan ikki teng massa uchun \(\omega_1=\sqrt{k/m}\) (massalar bir tomonga, “fazada”) va \(\omega_2=\sqrt{3k/m}\) (qarama-qarshi fazada).</p>""")],
 example=(r"Rezonans amplitudasi va asllik",
  r"\(m=0{,}5\) kg, \(k=200\) N/m, \(\beta=1\) s⁻¹, \(F_0=2\) N. \(\omega_0\), rezonans chastotasi, rezonansdagi amplituda va asllikni toping.",
  r"\(\omega_0=\sqrt{200/0{,}5}=20\) rad/s (\(f=3{,}18\) Gs). \(\gamma_r=\sqrt{400-2}=19{,}95\) rad/s. \(b_{max}\approx F_0/(2m\beta\omega_0)=2/(2\cdot0{,}5\cdot1\cdot20)=0{,}10\) m. Asllik \(Q=\omega_0/2\beta=10\). Statik siljish \(F_0/k=0{,}01\) m — rezonansda amplituda \(Q\) marta katta."),
 simtask=[r"Majburlovchi chastotani 10 dan 30 rad/s gacha o‘zgartirib, amplituda maksimumini toping va \(\gamma_r\) bilan solishtiring.",
          r"\(\beta\) ni 0,5 dan 4 s⁻¹ gacha oshiring: rezonans egri chizig‘i qanday kengayadi?",
          r"\(\gamma\ll\omega_0\) va \(\gamma\gg\omega_0\) da amplituda qanday chegaraviy qiymatlarga intiladi?"],
 mistakes=[(r"“Rezonans har doim \(\gamma=\omega_0\) da.”", r"Amplituda rezonansi \(\gamma_r=\sqrt{\omega_0^2-2\beta^2}\) da; kichik so‘nishda farq sezilmaydi."),
           (r"“So‘nish chastotaga ta’sir qilmaydi.”", r"\(\omega=\sqrt{\omega_0^2-\beta^2}\) — so‘nish chastotani kamaytiradi."),
           (r"“Ikki massali sistemada chastota bitta.”", r"Erkinlik darajasi nechta bo‘lsa, shuncha xos chastota (normal moda) bor.")],
 ai=r"""Sen tebranishlar nazariyasi bo‘yicha repetitorsan. Mavzu: majburiy tebranishlar va rezonans.
Menga ikki bog‘langan ossilyator masalasini ber: Lagranj funksiyasini, xarakteristik tenglamani va normal modalarni topishimni bosqichma-bosqich so‘ra. Javoblarimni tekshir, oxirida Python’da \(\det(K-\omega^2M)=0\) ni sonli yechish algoritmini taklif qil. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"\(m=2\) kg, \(k=50\) N/m. \(\omega_0\) =", ["5 rad/s", "25 rad/s", "10 rad/s", "0,2 rad/s"], 0, r"\(\sqrt{25}\)."),
  (r"Turg‘un muvozanat sharti:", [r"\(U\) minimum (\(U''>0\))", r"\(U\) maksimum", r"\(U=0\)", r"\(T=0\)"], 0, "Lagranj–Dirixle teoremasi."),
  (r"So‘nuvchi tebranishlar chastotasi:", [r"\(\sqrt{\omega_0^2-\beta^2}\)", r"\(\omega_0+\beta\)", r"\(\omega_0\)", r"\(\sqrt{\omega_0^2+\beta^2}\)"], 0, "Yechimdan."),
  (r"Asllik \(Q\) =", [r"\(\omega_0/2\beta\)", r"\(2\beta/\omega_0\)", r"\(\omega_0\beta\)", r"\(1/\beta\)"], 0, "Ta’rif."),
  (r"Amplituda rezonansi chastotasi:", [r"\(\sqrt{\omega_0^2-2\beta^2}\)", r"\(\omega_0\)", r"\(\sqrt{\omega_0^2-\beta^2}\)", r"\(2\omega_0\)"], 0, "Amplituda maksimumi."),
  (r"Rezonansda kuch va siljish orasidagi faza siljishi:", [r"\(\pi/2\)", "0", r"\(\pi\)", r"\(\pi/4\)"], 0, r"\(\operatorname{tg}\delta\to\infty\)."),
  (r"\(\gamma\gg\omega_0\) da majburiy tebranish amplitudasi:", [r"\(\approx F_0/(m\gamma^2)\) — nolga intiladi", "maksimal", r"\(F_0/k\)", "cheksiz"], 0, "Inersiya ustun."),
  (r"\(\gamma\to0\) da amplituda:", [r"\(F_0/k\) (statik siljish)", "0", "cheksiz", r"\(F_0/m\)"], 0, "Kvazistatik."),
  (r"Uch prujina bilan bog‘langan ikki teng massa xos chastotalari:", [r"\(\sqrt{k/m}\) va \(\sqrt{3k/m}\)", r"\(\sqrt{k/m}\) va \(\sqrt{2k/m}\)", r"faqat \(\sqrt{k/m}\)", r"\(\sqrt{2k/m}\) va \(\sqrt{4k/m}\)"], 0, "Fazada va qarama-qarshi fazada."),
  (r"Rezonansda amplitudaning statik siljishga nisbati taxminan:", [r"\(Q\)", r"\(1/Q\)", r"\(Q^2\)", "1"], 0, r"\(b_{max}k/F_0\approx Q\).")],
 blits=["Ko‘prik nima uchun askarlar qadami bilan qulashi mumkin?", "Rezonansdan foydalanadigan qurilmalarni ayting.", "Mashinaning amortizatori so‘nishni qanday tanlaydi?", "Molekulalarning tebranish spektri bilan bog‘liqlik nimada?"]))

L.append(dict(
 n=7, short=r"Markaziy simmetrik maydonda harakat", sim="orbit", refs=[1, 2, 4], intl=["landau", "goldstein", "taylor"], tn=["TN1", "TN5", "TN8", "TN21"],
 title=r"Markaziy simmetrik maydonda zarra harakati. Ikki jism masalasi",
 goal=r"Ikki jism masalasini keltirilgan massa yordamida bir jism masalasiga keltirish, markaziy maydondagi harakat integrallari va effektiv potensialni qo‘llab, Kepler masalasining trayektoriyalarini tasniflash.",
 outcomes=[r"ikki jism masalasini \(\mu=m_1m_2/(m_1+m_2)\) bilan soddalashtiradi;",
           r"effektiv potensial \(U_{eff}=U+M^2/2\mu r^2\) bo‘yicha radial harakatni tahlil qiladi;",
           r"Kepler masalasida orbita parametrlari \(p\), \(e\) ni energiya va impuls momenti orqali topadi;",
           r"Gauss teoremasi bilan sferik simmetrik maydonni hisoblaydi."],
 plan=["Markaziy simmetrik maydon xossalari va Gauss teoremasi", "Ikki jism masalasi", "Harakat integrallari va effektiv potensial", "Trayektoriya tenglamasi", "Kepler masalasi"],
 terms=["markaziy maydon", "keltirilgan massa", "effektiv potensial", "eksentrisitet", "Kepler qonunlari", "Gauss teoremasi"],
 theory=[
  ("Markaziy maydon va Gauss teoremasi", r"""<p>Markaziy maydonda kuch markazga yo‘nalgan va faqat masofaga bog‘liq: \(\vec F=F(r)\hat r\), \(U=U(r)\). Sferik simmetrik massa (zaryad) taqsimotining tashqarisidagi maydon Gauss teoremasi bilan topiladi: \(\oint\vec g\cdot d\vec S=-4\pi GM_{ich}\) ⇒ \(g=GM/r^2\). Elektrostatikada \(\oint\vec E\cdot d\vec S=Q/\varepsilon_0\). Shuning uchun shar tashqarisida uning butun massasi markazda to‘plangandek bo‘ladi.</p>"""),
  ("Ikki jism masalasi", r"""<p>\(L=\frac{m_1v_1^2}{2}+\frac{m_2v_2^2}{2}-U(|\vec r_1-\vec r_2|)\). Massa markazi \(\vec R\) va nisbiy vektor \(\vec r=\vec r_1-\vec r_2\) kiritilsa, Lagranjian ikki qismga ajraladi:</p>
$$L=\frac{(m_1+m_2)\dot R^2}{2}+\frac{\mu\dot r^2}{2}-U(r),\qquad\mu=\frac{m_1m_2}{m_1+m_2}.$$
<p>Massa markazi tekis harakatlanadi, nisbiy harakat esa massasi \(\mu\) bo‘lgan bitta zarraning markaziy maydondagi harakatiga teng.</p>"""),
  ("Harakat integrallari va effektiv potensial", r"""<p>Impuls momenti saqlangani uchun harakat tekis. Qutb koordinatalarida ikki integral bor: \(M=\mu r^2\dot\varphi\) va \(E=\frac{\mu\dot r^2}{2}+U_{eff}(r)\), bunda</p>
$$U_{eff}(r)=U(r)+\frac{M^2}{2\mu r^2}.$$
<p>Radial harakat \(E\ge U_{eff}\) sohasida bo‘ladi. Burilish nuqtalari \(E=U_{eff}\) tenglamadan topiladi. Ikkinchi had “markazdan qochma to‘siq” bo‘lib, zarrani markazga tushishdan saqlaydi.</p>"""),
  ("Kepler masalasi", r"""<p>\(U=-\alpha/r\) (\(\alpha=Gm_1m_2\)) uchun orbita tenglamasi konus kesimi bo‘ladi:</p>
$$\frac pr=1+e\cos\varphi,\qquad p=\frac{M^2}{\mu\alpha},\qquad e=\sqrt{1+\frac{2EM^2}{\mu\alpha^2}}.$$
<p>\(E<0\) — ellips (\(e<1\)), \(E=0\) — parabola, \(E>0\) — giperbola. Ellipsning katta yarim o‘qi \(a=\alpha/2|E|\). Keplerning uchinchi qonuni: \(T^2=\dfrac{4\pi^2a^3}{G(m_1+m_2)}\).</p>""")],
 example=(r"Yer sun’iy yo‘ldoshi",
  r"Yo‘ldosh Yer sirtidan \(h=400\) km balandlikda aylana orbita bo‘ylab harakatlanadi (\(GM=3{,}986\cdot10^{14}\) m³/s², \(R=6371\) km). Tezlik, davr va shu balandlikdagi qochish tezligini toping.",
  r"\(r=6{,}771\cdot10^6\) m. \(v=\sqrt{GM/r}=7{,}67\) km/s. \(T=2\pi r/v=5545\) s ≈ 92,4 min. Qochish tezligi \(\sqrt2v=10{,}85\) km/s (\(E=0\), parabolik orbita)."),
 simtask=[r"Boshlang‘ich tezlikni aylana tezligining 1,0 marta qiymatiga o‘rnating: \(e=0\) ekanini tekshiring.",
          r"Tezlikni 1,2 ga oshiring: eksentrisitet va katta yarim o‘q qanday bo‘ldi? Davr Kepler III qonuniga mosmi?",
          r"Tezlikni \(\sqrt2\approx1{,}414\) dan oshiring: orbita turi qanday o‘zgaradi? Effektiv potensial grafigida energiya chizig‘ini kuzating."],
 mistakes=[(r"“Orbitadagi yo‘ldoshga kuch ta’sir qilmaydi, u vaznsiz.”", r"Gravitatsiya ta’sir qiladi va markazga intilma tezlanish beradi. Vaznsizlik — erkin tushish holati."),
           (r"“Ikki jism masalasida og‘ir jism qo‘zg‘almas.”", r"Ikkalasi massa markazi atrofida aylanadi; nisbiy harakat keltirilgan massa bilan tavsiflanadi."),
           (r"“Tezlik oshsa, davr kamayadi.”", r"Tezlik oshsa orbita kattalashadi va Kepler III qonuniga ko‘ra davr ortadi.")],
 ai=r"""Sen osmon mexanikasi bo‘yicha repetitorsan. Mavzu: Kepler masalasi.
Menga effektiv potensialdan foydalanib orbita turini aniqlashni o‘rgat: avval savol ber, keyin javobimni tekshir. Python’da Kepler orbitasini RK4 bilan sonli integrallash algoritmini menga tuzdirib, energiya va impuls momenti saqlanishini tekshirishni so‘ra. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Keltirilgan massa:", [r"\(m_1m_2/(m_1+m_2)\)", r"\(m_1+m_2\)", r"\(\sqrt{m_1m_2}\)", r"\((m_1+m_2)/2\)"], 0, "Ta’rif."),
  (r"Effektiv potensial:", [r"\(U+M^2/2\mu r^2\)", r"\(U-M^2/2\mu r^2\)", r"\(U+\mu r^2\)", r"\(M^2/2\mu r^2\)"], 0, "Markazdan qochma to‘siq bilan."),
  (r"Kepler masalasida \(E<0\) bo‘lsa, orbita:", ["ellips", "parabola", "giperbola", "to‘g‘ri chiziq"], 0, r"\(e<1\)."),
  (r"Eksentrisitet:", [r"\(\sqrt{1+2EM^2/\mu\alpha^2}\)", r"\(1+2EM^2/\mu\alpha^2\)", r"\(M^2/\mu\alpha\)", r"\(\alpha/2|E|\)"], 0, "Orbita tenglamasidan."),
  (r"Aylana orbitadagi tezlikdan \(\sqrt2\) marta katta tezlikda orbita:", ["parabola", "ellips", "aylana", "giperbola"], 0, r"\(E=0\)."),
  (r"Kepler III qonuni:", [r"\(T^2\propto a^3\)", r"\(T\propto a\)", r"\(T^3\propto a^2\)", r"\(T\propto a^2\)"], 0, r"\(T^2=4\pi^2a^3/GM\)."),
  (r"400 km balandlikdagi aylana orbita davri taxminan:", ["92 min", "24 soat", "45 min", "3 soat"], 0, "Misoldan."),
  (r"Markaziy maydonda harakat:", ["bitta tekislikda bo‘ladi", "har doim aylana", "fazoviy spiral", "to‘g‘ri chiziq"], 0, r"\(\vec M=\text{const}\)."),
  (r"Bir jinsli shar tashqarisidagi gravitatsion maydon:", ["butun massa markazda bo‘lgandek", "nolga teng", "masofaga bog‘liq emas", r"\(r\) ga proporsional"], 0, "Gauss teoremasi."),
  (r"Katta yarim o‘q \(a\) =", [r"\(\alpha/2|E|\)", r"\(M^2/\mu\alpha\)", r"\(\alpha/|E|\)", r"\(2|E|/\alpha\)"], 0, "Ellips uchun.")],
 blits=["Nima uchun sayyoralar orbitasi tekis?", "Oy Yer atrofida aylanadimi yoki ikkalasi umumiy markaz atrofida?", "Kosmik kema orbitani oshirish uchun tezlikni oshiradimi yoki kamaytiradimi?", "Kometalar nima uchun cho‘zilgan orbitalarda harakatlanadi?"]))

L.append(dict(
 n=8, short=r"Markaziy maydonda sochilish", sim="scatter", refs=[1, 2, "Q1"], intl=["landau", "goldstein", "thornton"], tn=["TN1", "TN5", "TN11"],
 title=r"Markaziy simmetrik maydonda zarralar sochilishi. Rezerford formulasi",
 goal=r"Sochilish burchagining nishon parametriga bog‘liqligini aniqlash, differensial va to‘liq effektiv kesim tushunchalarini kiritish, Kulon maydonida sochilish uchun Rezerford formulasini keltirib chiqarish.",
 outcomes=[r"sochilish burchagi \(\chi(b)\) ni integral orqali yozadi;",
           r"differensial kesim \(d\sigma/d\Omega\) ni \(b(\chi)\) dan hisoblaydi;",
           r"Rezerford formulasini qo‘llab, alfa-zarralar sochilishini tahlil qiladi;",
           r"qattiq shar uchun to‘liq kesimni topadi va Kulon kesimining uzoqlashuvchanligini izohlaydi."],
 plan=["Sochilish masalasi: nishon parametri va burchak", "Effektiv kesim", "Kulon maydonida sochilish", "Rezerford formulasi va tajriba", "Qattiq shar; to‘liq kesim"],
 terms=["nishon parametri", "sochilish burchagi", "differensial kesim", "to‘liq kesim", "Rezerford formulasi", "eng yaqin kelish masofasi"],
 theory=[
  ("Sochilish burchagi", r"""<p>Cheksizlikdan \(v_\infty\) tezlik bilan kelayotgan zarraning maydon markazidan chetlanishi <b>nishon parametri</b> \(b\) deyiladi. Harakat integrallari \(E=\mu v_\infty^2/2\), \(M=\mu v_\infty b\). Orbita simmetriyasidan sochilish burchagi quyidagicha topiladi:</p>
$$\chi=\pi-2\varphi_0,\qquad\varphi_0=\int_{r_{min}}^{\infty}\frac{(b/r^2)\,dr}{\sqrt{1-b^2/r^2-U(r)/E}}.$$"""),
  ("Effektiv kesim", r"""<p>Birlik vaqtda birlik yuzadan \(n\) ta zarra o‘tsa, \(d\Omega\) fazoviy burchakka sochilganlar soni \(dN=n\,d\sigma\). Bu yerda \(d\sigma=2\pi b\,db\) — <b>differensial effektiv kesim</b>:</p>
$$\frac{d\sigma}{d\Omega}=\frac{b}{\sin\chi}\left|\frac{db}{d\chi}\right|.$$
<p>To‘liq kesim \(\sigma=\int(d\sigma/d\Omega)d\Omega\). Qattiq shar (radius \(R\)) uchun \(b=R\cos(\chi/2)\), \(d\sigma/d\Omega=R^2/4\) (izotrop) va \(\sigma=\pi R^2\).</p>"""),
  ("Rezerford formulasi", r"""<p>Itaruvchi Kulon maydoni \(U=\alpha/r\) (\(\alpha=Z_1Z_2e^2/4\pi\varepsilon_0\)) uchun quyidagi bog‘lanish olinadi:</p>
$$\operatorname{tg}\frac\chi2=\frac{\alpha}{2Eb},\qquad\frac{d\sigma}{d\Omega}=\left(\frac{\alpha}{4E}\right)^2\frac{1}{\sin^4(\chi/2)}.$$
<p>Kesim kichik burchaklarda cheksiz o‘sadi, shuning uchun to‘liq Kulon kesimi uzoqlashadi (maydon uzoq ta’sirli). Real atomlarda elektronlar ekranlashi buni cheklaydi. Rezerford tajribasida (1911) katta burchakli sochilishlar soni formula bilan aniq mos keldi — atom yadrosi shu tarzda kashf etilgan.</p>"""),
  ("Eng yaqin kelish masofasi", r"""<p>To‘qnashuv markaziy bo‘lsa (\(b=0\)), zarra \(d_0=\alpha/E\) masofagacha yaqinlashadi. Umumiy holda \(r_{min}=\frac{\alpha}{2E}\left(1+\frac{1}{\sin(\chi/2)}\right)\). Agar \(d_0\) yadro radiusidan kichik bo‘lsa, Rezerford formulasi buziladi va yadro kuchlari namoyon bo‘ladi.</p>""")],
 example=(r"Alfa-zarralarning oltinda sochilishi",
  r"\(E=5\) MeV alfa-zarra oltin yadrosida (\(Z=79\)) sochilmoqda (\(e^2/4\pi\varepsilon_0=1{,}44\) MeV·fm). Eng yaqin kelish masofasi, \(\chi=90^\circ\) uchun nishon parametri va differensial kesimni toping.",
  r"\(\alpha=2\cdot79\cdot1{,}44=227{,}5\) MeV·fm. \(d_0=\alpha/E=45{,}5\) fm — oltin yadrosi radiusidan (≈ 7 fm) katta, formula o‘rinli. \(b=\frac{\alpha}{2E}\operatorname{ctg}45^\circ=22{,}75\) fm. \(d\sigma/d\Omega=(\alpha/4E)^2/\sin^445^\circ=11{,}38^2/0{,}25=518\) fm² = 5,18 barn/sr."),
 simtask=[r"Energiyani 5 MeV, \(Z=79\) qilib o‘rnating: \(\chi=90^\circ\) bo‘ladigan nishon parametri 22,75 fm ekanini tekshiring.",
          r"Energiyani 2 marta oshiring: bir xil \(b\) da sochilish burchagi qanday o‘zgaradi?",
          r"Nishon parametri kichrayganda burchak qanday o‘zgaradi? Orqaga sochilish (\(\chi>90^\circ\)) qaysi \(b\) larda bo‘ladi?"],
 mistakes=[(r"“Effektiv kesim — yadroning geometrik yuzasi.”", r"Bu o‘zaro ta’sir ehtimolining o‘lchovi; Kulon maydonida u geometrik o‘lchamga bog‘liq emas va cheksiz."),
           (r"“Katta burchakli sochilish ko‘p uchraydi.”", r"\(d\sigma/d\Omega\propto\sin^{-4}(\chi/2)\) — kichik burchaklar ustun, orqaga sochilish kam."),
           (r"“Rezerford formulasi har qanday energiyada to‘g‘ri.”", r"\(d_0\) yadro radiusiga yaqinlashsa, yadro kuchlari ta’sir qiladi va formula buziladi.")],
 ai=r"""Sen yadro fizikasi va klassik sochilish bo‘yicha repetitorsan. Mavzu: Rezerford formulasi.
Menga \(\operatorname{tg}(\chi/2)=\alpha/2Eb\) dan \(d\sigma/d\Omega\) ni keltirib chiqarishni qadamma-qadam savollar orqali o‘rgat. So‘ng Geyger–Marsden tajribasi natijalarini formula bilan solishtirish topshirig‘ini ber. Formulalarni LaTeX’da yoz.""",
 quiz=[
  (r"Rezerford formulasi:", [r"\(\frac{d\sigma}{d\Omega}=\left(\frac{\alpha}{4E}\right)^2\frac{1}{\sin^4(\chi/2)}\)", r"\(\frac{d\sigma}{d\Omega}=\frac{R^2}{4}\)", r"\(\sigma=\pi R^2\)", r"\(\frac{d\sigma}{d\Omega}\propto\sin^2\chi\)"], 0, "Kulon maydoni."),
  (r"Kulon maydonida \(\operatorname{tg}(\chi/2)\) =", [r"\(\alpha/2Eb\)", r"\(2Eb/\alpha\)", r"\(\alpha/Eb\)", r"\(b/\alpha\)"], 0, "Orbita tenglamasidan."),
  (r"Differensial kesim birligi:", ["m²/sr (barn/sr)", "m", "sr", "J·m"], 0, "Yuza / fazoviy burchak."),
  (r"Qattiq shar uchun to‘liq kesim:", [r"\(\pi R^2\)", r"\(4\pi R^2\)", r"\(2\pi R^2\)", "cheksiz"], 0, "Geometrik kesim."),
  (r"Kulon to‘liq kesimi:", ["uzoqlashadi (cheksiz)", r"\(\pi d_0^2\)", "nol", "chekli"], 0, "Kichik burchaklar hissasi."),
  (r"Energiya 2 marta oshsa, bir xil burchakdagi \(d\sigma/d\Omega\):", ["4 marta kamayadi", "2 marta kamayadi", "o‘zgarmaydi", "4 marta ortadi"], 0, r"\(\propto1/E^2\)."),
  (r"Markaziy to‘qnashuvda eng yaqin kelish masofasi:", [r"\(\alpha/E\)", r"\(\alpha/2E\)", r"\(2\alpha/E\)", r"\(E/\alpha\)"], 0, r"\(E=\alpha/d_0\)."),
  (r"\(b=0\) da sochilish burchagi (itarish):", ["180°", "0°", "90°", "45°"], 0, "Orqaga qaytadi."),
  (r"Rezerford tajribasi nimani isbotladi?", ["atomda kichik og‘ir yadro borligini", "elektron zaryadini", "foton mavjudligini", "atom bo‘linmasligini"], 0, "1911-yil."),
  (r"\(d\sigma=\) …", [r"\(2\pi b\,db\)", r"\(\pi b^2\)", r"\(b\,db\)", r"\(2\pi\,db\)"], 0, "Halqa yuzasi.")],
 blits=["Nima uchun kesim “yuza” o‘lchamiga ega?", "Rezerford alfa-zarralarni nima uchun yupqa folgaga yo‘naltirgan?", "Ekranlash kesimni qanday chekli qiladi?", "Zamonaviy kollayderlarda kesim qanday birlikda o‘lchanadi?"]))
