"""Interaktiv modellar uchun ovozli avtomatik namoyish ssenariylari.
Har bir qadam: (parametrlar, izoh). Tanlov (select) uchun qiymat '#indeks' ko'rinishida beriladi."""

T = {
 "forces": [
  ({"a": 1.4, "r": 3}, "Bu model Kulon va Yukava potensiallarini taqqoslaydi. Ta’sir radiusi bir butun o‘ndan to‘rt femtometr. Bu radiusga taxminan bir yuz qirq megaelektronvolt massali tashuvchi zarra mos keladi — bu pion."),
  ({"r": 6}, "Masofani olti femtometrgacha oshiramiz. Yukava potensiali Kulon potensialidan yuz martadan ko‘proq kichik bo‘lib qoldi: yadro kuchlari qisqa masofada keskin so‘nadi."),
  ({"a": 0.2, "r": 3}, "Radiusni yetti marta kamaytiramiz. Tashuvchi massasi ham yetti marta ortdi. Kuchsiz o‘zaro ta’sirning juda kichik radiusi og‘ir W va Z bozonlar bilan aynan shunday tushuntiriladi."),
  ({"a": 10, "r": 3}, "Radius katta bo‘lganda Yukava egri chizig‘i Kulon chizig‘iga deyarli yopishadi. Massasiz tashuvchi esa cheksiz radiusli, uzoq ta’sirli kuch beradi."),
  ({"a": 1.4, "r": 3}, "Namoyish tugadi. Endi o‘zingiz radiusni o‘zgartirib, tashuvchi massasi qanday o‘zgarishini kuzating.")],
 "coords": [
  ({"mode": "#0", "r": 2, "th": 45, "ph": 45}, "Bu model nuqtaning Dekart, silindrik va sferik koordinatalarini birga ko‘rsatadi. Radius ikki, teta va fi qirq besh gradus. Dekart koordinatalari bir, bir va ikkining ildizi."),
  ({"th": 90}, "Teta burchagini to‘qson gradusga o‘zgartiramiz. Nuqta ekvator tekisligiga tushdi, z koordinata nolga teng bo‘ldi."),
  ({"th": 150, "ph": 220}, "Teta yuz ellik, fi ikki yuz yigirma gradus. Nuqta pastki yarim fazoga va uchinchi chorakka o‘tdi. Sferik koordinatalar markaziy simmetriyali masalalarda qulay."),
  ({"mode": "#1", "r": 1.5, "ph": 60, "z": 1.5}, "Silindrik sistemaga o‘tamiz. Endi nuqta o‘qdan masofa, fi burchagi va balandlik bilan beriladi. Kulrang halqa — o‘zgarmas ro radiusli aylana."),
  ({"mode": "#0", "r": 2, "th": 45, "ph": 45, "z": 1}, "Namoyish tugadi. Ishlangan misoldagi nuqtani o‘zingiz kiritib, javobni tekshiring.")],
 "action": [
  ({"eps": 0, "n": 1}, "Bu model eng kichik ta’sir prinsipini ko‘rsatadi. Havorang chiziq — erkin tushishdagi haqiqiy yo‘l. Hozir variatsiya nolga teng, ta’sir eng kichik qiymatda."),
  ({"eps": 0.1}, "Yo‘lga o‘n santimetr amplitudali sinusoidal qo‘shimcha beramiz. Ta’sir ikki yuz qirq yetti o‘n mingdan bir joul sekundga ortdi. Bu ishlangan misoldagi javob."),
  ({"eps": -0.2}, "Qo‘shimchani teskari tomonga va ikki marta kattaroq olamiz. Ta’sir yana ortdi va to‘rt marta katta bo‘ldi: o‘zgarish epsilonning kvadratiga proporsional."),
  ({"eps": 0.1, "n": 3}, "Uchinchi garmonikani tanlaymiz. Yo‘l tez-tez tebranadi, kinetik energiya ortadi va ta’sir to‘qqiz marta ko‘proq oshadi."),
  ({"eps": 0.1, "n": 1}, "Xulosa: har qanday chetga chiqish ta’sirni oshiradi, demak tabiat ta’sir statsionar bo‘lgan yo‘lni tanlaydi. Endi o‘zingiz sinab ko‘ring.")],
 "pendulum": [
  ({"th0": 10, "l": 1, "gam": 0}, "Bu model matematik mayatnikni ko‘rsatadi. Uzunlik bir metr, boshlang‘ich burchak o‘n gradus. Aniq yechim va kichik burchak taqribi deyarli ustma-ust tushadi, davr taxminan ikki sekund."),
  ({"th0": 60}, "Amplitudani oltmish gradusga oshiramiz. Endi aniq yechim taqribiy yechimdan orqada qola boshladi: davr yetti foizga uzaydi."),
  ({"th0": 170}, "Yuz yetmish gradusda mayatnik yuqori muvozanat holati yaqinida uzoq to‘xtab turadi va davr bir necha marta ortadi."),
  ({"th0": 60, "gam": 0.3}, "So‘nishni yoqamiz. Amplituda eksponensial kamayadi, nopotensial kuch energiyani issiqlikka aylantiradi."),
  ({"th0": 60, "l": 1, "gam": 0}, "Namoyish tugadi. Uzunlikni o‘zgartirib, davr uzunlikning kvadrat ildiziga proporsional ekanini tekshiring.")],
 "noether": [
  ({"pot": "#0", "v0": 1.1}, "Bu model simmetriya va saqlanish qonunlari bog‘lanishini ko‘rsatadi. Markaziy maydonda trayektoriya ellips. Energiya va impuls momenti grafikda to‘g‘ri chiziq — ular saqlanadi, impuls esa o‘zgaradi."),
  ({"pot": "#1"}, "Bir jinsli maydonni tanlaymiz. Endi gorizontal impuls va energiya saqlanadi, chunki maydon x bo‘ylab siljishda o‘zgarmaydi. Impuls momenti esa saqlanmaydi."),
  ({"pot": "#2"}, "Anizotrop ossilyatorda bikrliklar har xil. Burilish simmetriyasi yo‘q, shuning uchun impuls momenti ham saqlanmaydi. Faqat energiya qoladi."),
  ({"pot": "#3"}, "Erkin zarrada barcha simmetriyalar bor: energiya, impulsning ikkala tashkil etuvchisi va impuls momenti saqlanadi."),
  ({"pot": "#0", "v0": 1.1}, "Bu Nyoter teoremasi: har bir uzluksiz simmetriyaga bitta saqlanish qonuni mos keladi. Endi tezlikni o‘zgartirib tekshiring.")],
 "oscill": [
  ({"m": 0.5, "k": 200, "b": 1, "F": 2, "g": 10}, "Bu model majburiy tebranishlarni ko‘rsatadi. Xos chastota yigirma radian sekund. Majburlovchi chastota o‘n, amplituda kichik."),
  ({"g": 20}, "Chastotani yigirmaga tenglashtiramiz. Rezonans: amplituda o‘n santimetrgacha o‘sdi, bu statik siljishdan o‘n marta katta. Asllik o‘nga teng."),
  ({"b": 4}, "So‘nishni to‘rt marta oshiramiz. Rezonans egri chizig‘i pasaydi va kengaydi, amplituda to‘rt marta kamaydi."),
  ({"b": 1, "g": 35}, "Chastota xos chastotadan ancha katta bo‘lsa, jism inersiyasi tufayli deyarli harakatlanmaydi va qarama-qarshi fazada tebranadi."),
  ({"m": 0.5, "k": 200, "b": 1, "F": 2, "g": 20}, "O‘ng grafikda tebranish tinchlikdan boshlanib, o‘tish jarayonidan keyin barqaror amplitudaga chiqadi. Endi o‘zingiz tajriba qiling.")],
 "orbit": [
  ({"k": 1, "a": 0}, "Bu model markaziy maydondagi orbitani va effektiv potensialni ko‘rsatadi. Tezlik aylana tezligiga teng, eksentrisitet nol — orbita aylana. Energiya effektiv potensial minimumida."),
  ({"k": 1.2}, "Tezlikni yigirma foizga oshiramiz. Orbita ellipsga aylandi, eksentrisitet nol butun qirq to‘rt yuzdan. Energiya chizig‘i potensial chuqurni ikki nuqtada kesadi: bu perigey va apogey."),
  ({"k": 1.42}, "Tezlik ikkining ildizidan katta bo‘ldi. Energiya musbat, orbita ochiq — giperbola. Bu qochish tezligi."),
  ({"k": 0.9, "a": 30}, "Tezlik yo‘nalishini o‘ttiz gradusga buramiz. Impuls momenti kamaydi, orbita cho‘zilib, markazga yaqinroq o‘tadi."),
  ({"k": 1.2, "a": 0}, "Namoyish tugadi. Davr Keplerning uchinchi qonuniga mosligini o‘zingiz tekshiring.")],
 "scatter": [
  ({"E": 5, "Z": 79, "b": 22.75}, "Bu model alfa-zarralarning oltin yadrosida sochilishini ko‘rsatadi. Energiya besh megaelektronvolt. Nishon parametri yigirma ikki butun yetmish besh femtometr bo‘lganda, zarra to‘qson gradusga buriladi."),
  ({"b": 8}, "Nishon parametrini kamaytiramiz. Zarra yadroga yaqinroq keladi va orqaga, yuz o‘ttiz gradusdan ko‘proq burchakka qaytadi. Rezerford aynan shunday sochilishlarni ko‘rib, yadroni kashf etgan."),
  ({"b": 80}, "Uzoqdan o‘tgan zarra deyarli og‘maydi. O‘ng grafikka qarang: kesim kichik burchaklarda keskin o‘sadi, shuning uchun ko‘p zarralar kichik burchakka sochiladi."),
  ({"E": 10, "b": 22.75}, "Energiyani ikki marta oshiramiz. Bir xil nishon parametrida burchak kamaydi, eng yaqin kelish masofasi ham ikki marta qisqardi."),
  ({"E": 5, "Z": 79, "b": 22.75}, "Namoyish tugadi. Turli yadrolarni tanlab, sochilish burchagi zaryadga qanday bog‘liqligini kuzating.")],
 "inertia": [
  ({"sh": "#0", "M": 2, "R": 0.2, "d": 0, "al": 30}, "Bu model inersiya momenti va dumalashni ko‘rsatadi. Yaxlit shar uchun inersiya momenti massa va radius kvadrati ko‘paytmasining beshdan ikki qismiga teng. O‘ttiz gradusli qiyalikda tezlanish uch yarim metr sekund kvadrat."),
  ({"sh": "#2"}, "Halqani tanlaymiz. Uning butun massasi chetda, inersiya momenti katta, shuning uchun tezlanish eng kichik: ikki butun qirq besh."),
  ({"sh": "#0", "M": 8}, "Massani to‘rt marta oshiramiz. Dumalash tezlanishi o‘zgarmadi: u faqat jism shakliga bog‘liq."),
  ({"sh": "#1", "M": 2, "d": 0.2}, "Disk uchun aylanish o‘qini chetga siljitamiz. Shteyner teoremasiga ko‘ra inersiya momenti massa va siljish kvadrati ko‘paytmasiga ortdi."),
  ({"sh": "#0", "M": 2, "R": 0.2, "d": 0, "al": 30}, "Namoyish tugadi. Qiyalik burchagini o‘zgartirib, poyga natijasini tekshiring.")],
 "phase": [
  ({"mode": "#0", "E": 8, "w": 2}, "Bu model fazaviy fazoni ko‘rsatadi. Garmonik ossilyatorning trayektoriyasi ellips. Energiya sakkiz joul, ellips yuzasi sakkiz pi."),
  ({"E": 20}, "Energiyani oshirsak, ellips kattalashadi. Lekin davr o‘zgarmaydi: garmonik ossilyator izoxron."),
  ({"mode": "#1", "E": 8}, "Mayatnikka o‘tamiz. Kichik energiyada trayektoriya yopiq egri chiziq — tebranish. Qizil uzuq chiziq — separatrisa."),
  ({"E": 19.4}, "Energiyani separatrisaga yaqinlashtiramiz. Davr keskin ortadi: mayatnik yuqori nuqtada uzoq to‘xtab qoladi."),
  ({"E": 26}, "Separatrisadan yuqori energiyada mayatnik to‘xtamasdan aylanadi, trayektoriya ochiq. Namoyish tugadi.")],
 "collision": [
  ({"mr": 3, "chi": 90, "v": 4}, "Bu model elastik to‘qnashuvning impulslar diagrammasini ko‘rsatadi. Ikkinchi zarra uch marta og‘ir. Massa markazi sistemasida to‘qson gradusga sochilganda, birinchi zarra yetmish bir gradus, ikkinchisi qirq besh gradusga uchadi."),
  ({"mr": 1}, "Massalarni tenglashtiramiz. Burchaklar yig‘indisi doim to‘qson gradus — bilyard sharlari to‘g‘ri burchak ostida tarqaladi."),
  ({"mr": 0.33, "chi": 120}, "Endi birinchi zarra og‘ir. A nuqta aylanadan tashqarida, shuning uchun sochilish burchagi taxminan o‘n to‘qqiz gradusdan oshmaydi."),
  ({"mr": 12, "chi": 180}, "Neytronning uglerod yadrosiga markaziy urilishi. Bir to‘qnashuvda energiyaning yigirma sakkiz foizi uzatiladi."),
  ({"mr": 3, "chi": 90, "v": 4}, "Namoyish tugadi. Massalar nisbatini o‘zgartirib, diagramma qanday o‘zgarishini kuzating.")],
 "lorentz": [
  ({"b": 0, "x": 1, "t": 2}, "Bu Minkovskiy diagrammasi. Sariq chiziqlar yorug‘lik konusi. Tezlik nol bo‘lganda, ikkinchi sistemaning o‘qlari birinchisi bilan ustma-ust."),
  ({"b": 0.6}, "Tezlikni yorug‘lik tezligining oltmish foiziga oshiramiz. Binafsha o‘qlar yorug‘lik chizig‘iga qarab qisildi, Lorens omili bir butun yigirma besh."),
  ({"x": 2, "t": 1}, "Voqeani yorug‘lik konusidan tashqariga qo‘yamiz. Interval manfiy, fazosimon. Bunday voqealar sababiy bog‘lanmagan."),
  ({"b": 0.5}, "Tezlik yarim yorug‘lik tezligida voqeaning ikkinchi sistemadagi vaqti nolga teng: u koordinata boshi bilan bir vaqtda sodir bo‘ladi. Bir vaqtlilik nisbiy."),
  ({"b": 0.6, "x": 1, "t": 2}, "Interval qiymati barcha sistemalarda bir xil qolganini tekshiring. Namoyish tugadi.")],
 "param": [
  ({"h": 0.1, "r": 2, "b": 0}, "Bu model parametrik rezonansni ko‘rsatadi. Bikrlik o‘n foizga davriy o‘zgaradi, uning chastotasi xos chastotadan ikki marta katta. Amplituda eksponensial o‘smoqda."),
  ({"r": 2.07}, "Chastotani beqarorlik sohasi chegarasidan tashqariga siljitamiz. O‘sish to‘xtadi, tebranishlar faqat tepkilar hosil qiladi."),
  ({"r": 2, "h": 0.3}, "Modulyatsiyani kuchaytiramiz. Soha kengaydi va o‘sish tezligi uch marta ortdi."),
  ({"h": 0.1, "b": 0.3}, "So‘nish qo‘shamiz. So‘nish o‘sish tezligidan katta, chegaraviy chuqurlikdan kam modulyatsiyada rezonans yo‘qoladi."),
  ({"h": 0.1, "r": 2, "b": 0}, "Arg‘imchoqni uchirish ham shu hodisa. Namoyish tugadi.")],
 "bernoulli": [
  ({"d1": 4, "d2": 2, "v1": 1, "h": 0}, "Bu model Venturi naychasini ko‘rsatadi. Diametr ikki marta torayadi, demak tezlik to‘rt marta ortadi: bir metr sekunddan to‘rt metr sekundgacha. Bosim yetti ming besh yuz paskalga kamaydi."),
  ({"d2": 1}, "Tor qismni yana ikki marta toraytiramiz. Tezlik o‘n olti marta ortib, bosim farqi keskin o‘sdi."),
  ({"d2": 2, "v1": 2}, "Boshlang‘ich tezlikni ikki marta oshiramiz. Bosimlar farqi to‘rt marta ortdi, chunki u tezlik kvadratiga proporsional."),
  ({"v1": 1, "h": 1}, "Tor qismni bir metr yuqoriga ko‘taramiz. Bernulli tenglamasidagi balandlik hadi qo‘shimcha to‘qqiz ming sakkiz yuz paskal bosim kamayishini beradi."),
  ({"d1": 4, "d2": 2, "v1": 1, "h": 0}, "Namoyish tugadi. Reynolds soniga qarab, ideal suyuqlik yaqinlashuvi qachon o‘rinli ekanini muhokama qiling.")],
 "crank": [
  ({"r": 5, "l": 20, "n": 3000}, "Bu model krivoship-shatunli mexanizmni ko‘rsatadi. Krivoship radiusi besh, shatun yigirma santimetr, aylanish chastotasi minutiga uch ming. Yuqori chekka nuqtada tezlanish olti ming metr sekund kvadratdan oshadi."),
  ({"l": 60}, "Shatunni uzaytiramiz. Tezlanish grafigi garmonik egri chiziqqa yaqinlashdi, ikkinchi garmonika kichraydi."),
  ({"l": 12}, "Qisqa shatunda ikkinchi garmonika kuchli, yuqori va pastki chekka nuqtalardagi tezlanishlar keskin farq qiladi."),
  ({"l": 20, "n": 6000}, "Chastotani ikki marta oshiramiz. Tezlik ikki, tezlanish esa to‘rt marta ortdi: inersiya kuchlari burchak tezlik kvadratiga proporsional."),
  ({"r": 5, "l": 20, "n": 3000}, "Namoyish tugadi. Maksimal tezlik qaysi burchakda bo‘lishini o‘zingiz toping.")],
 "traj": [
  ({"mode": "#0", "t": 1}, "Bu model trayektoriya, tezlik va tezlanish vektorlarini ko‘rsatadi. Parabolik harakatda bir sekundda tezlik ikki butun sakson uch, egrilik radiusi besh butun oltmish olti metr."),
  ({"t": 2}, "Ikki sekundda jism eng yuqori nuqtada. Tezlik gorizontal, tezlanish unga tik, tangensial tezlanish nol."),
  ({"mode": "#1", "t": 0}, "Ellips bo‘ylab harakatda tezlanish doim markazga yo‘nalgan. Binafsha aylana — egrilik aylanasi."),
  ({"mode": "#2", "t": 3.14}, "Sikloidada nuqta eng yuqorida va tezligi maksimal. Pastki nuqtada esa tezlik nolga teng bo‘ladi."),
  ({"mode": "#4", "t": 1.2}, "Havo qarshiligi bilan qiya otishda trayektoriya nosimmetrik: tushish qismi tikroq. Namoyish tugadi.")],
 "dpend": [
  ({"a": 20, "b": 28, "mr": 1}, "Bu qo‘sh mayatnik. Kichik burchaklarda harakat ikki normal moda yig‘indisi va oldindan aytib bo‘ladigan. Pushti nusxa asosiy mayatnik bilan ustma-ust ketmoqda."),
  ({"a": 120, "b": -10}, "Katta burchaklarda harakat xaotik bo‘ladi. Pushti nusxaning boshlang‘ich burchagi atigi mingdan bir gradusga farq qiladi, lekin bir necha sekunddan keyin ular butunlay ajraladi."),
  ({"mr": 2.5}, "Pastki yukni og‘irlashtiramiz. Normal chastotalar o‘zgardi, lekin energiya xatosi juda kichik: Runge–Kutta usuli to‘g‘ri ishlayapti."),
  ({"a": 120, "b": -10, "mr": 1}, "Namoyish tugadi. Bu model amaliy mashg‘ulotdagi Lagranj tenglamalarining sonli yechimidir.")],
 "brach": [
  ({"X": 3.14, "Y": 2}, "Bu braxistoxrona masalasi. Uchta sharcha bir vaqtda tushadi: to‘g‘ri chiziq, aylana yoyi va sikloida bo‘ylab. Sikloida bo‘ylab tushish bir sekund, to‘g‘ri chiziq bo‘ylab bir butun o‘n to‘qqiz sekund."),
  ({"X": 4.5, "Y": 1}, "Oxirgi nuqtani uzoqroq va pastroq qo‘yamiz. Sikloida oxirgi nuqtadan pastga tushib, so‘ng ko‘tariladi va baribir eng tez bo‘ladi."),
  ({"X": 1, "Y": 2.5}, "Deyarli vertikal holatda uchala chiziqning vaqtlari bir-biriga yaqinlashadi."),
  ({"X": 3.14, "Y": 2}, "Eng qisqa yo‘l eng tez yo‘l emas. Variatsion hisob eng tez yo‘l sikloida ekanini isbotlaydi. Namoyish tugadi.")],
}
