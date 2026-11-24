# Nazariy mexanika — interaktiv elektron darslik

**60530500 — Fizika (bakalavriat) · NM1406 · 6 ECTS (180 soat) · 4-semestr**
Muallif: Eshboltayev Iqbol Mamirjonovich, professor, PhD (Qo‘qon davlat universiteti)

Sayt: https://eshboltayev.github.io/Nazariy_mexanika/

## Tarkibi (fan dasturi asosida)

| Bo‘lim | Hajm | Sahifalar |
|---|---|---|
| Ma’ruzalar M1–M15 | 30 soat | `lecture1.html` … `lecture15.html` — nazariya, ishlangan misol, interaktiv model, SI topshirig‘i, 10 savolli test |
| Amaliy mashg‘ulotlar A1–A15 | 30 soat | `amaliy1.html` … `amaliy15.html` — ishlangan va javobli masalalar, Python kodi |
| Seminarlar S1–S6 | 12 soat | `seminar.html` |
| Mustaqil ta’lim (30 mavzu) | 108 soat | `mustaqil.html` — taqdimot rejalari, 8 ta keys-stadi |
| Baholash | JN 30 + ON 20 + YaN 50 | `baholash.html` — rubrikalar, TN–nazorat matritsasi, kalkulyator |
| O‘qituvchi uchun | 15 hafta × 5 soat | `oqituvchi.html` |
| Ilovalar | — | `glossariy.html`, `vositalar.html`, `annotatsiya.html` |

18 ta interaktiv model (`js/sims.js`): Kulon/Yukava, koordinatalar, ta’sir funksionali, mayatnik, Nyoter teoremasi, rezonans, Kepler orbitasi, Rezerford sochilishi, inersiya momenti, fazaviy portret, impulslar diagrammasi, Minkovskiy diagrammasi, parametrik rezonans, Bernulli, krivoship-shatun, trayektoriya, qo‘sh mayatnik, braxistoxrona. Har birida ovozli namoyish (`gen/tours.py`).

## Ovoz

O‘zbekcha matnlar neyron ovozda (Microsoft Edge TTS, `uz-UZ-SardorNeural`) oldindan MP3 qilib tayyorlanadi va barcha qurilmalarda bir xil eshitiladi. `*.html` yoki `js/app.js` o‘zgarib GitHub’ga yuklanganda **Actions → “Ovoz (o‘zbekcha MP3)”** avtomatik ishga tushib, faqat yangi xatboshilarni ovozlaydi (`audio/uz/`).

## Yangilash

Mazmun `gen/` papkasida: `lectures_a.py`, `lectures_b.py`, `amaliy.py` (amaliy va seminarlar), `other.py`, `tours.py`, `common.py`.

```bash
python3 gen/build.py .
```

## GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

Litsenziya: CC BY-SA 4.0.
