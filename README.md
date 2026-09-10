# Koltuk Kumanda Kayip Arama Merkezi

> Koltuk bir mobilya degildir. Koltuk bir yargidir.

Bu yazilim, ev icindeki uzaktan kumandanin minder, yastik veya kol dayama tarafindan idari gozaltina alinmasini **kayip vatandas** muamelesiyle takip eder. Arama tutanagi uretir. Taziye basabilir. Gercekten calisir.

Patates yoktur. Asansor yoktur. Sadece koltuk ve kayip bir plastik parca vardir.

## Kurulum

```bash
python3 merkez.py --marka "Samsung" --renk "siyah" --son "haberlerin ikinci reklami"
python3 merkez.py --taziye
```

Gizli kalibrasyon dipnotu icin (normal kullanicinin isine yaramaz):

```bash
KKAM_DIPNOT=1 python3 merkez.py
```

## Mimari

1. Vatandas kumandayi kaybettigini beyan eder.
2. Merkez rastgele bir anayasal boslugu arama sahasi ilan eder.
3. Saha tespiti neredeyse her zaman kumanda disinda bir nesne bulur.
4. Ciddiyet katsayisi 10'u asabilir. Bu bir ozelliktir.
5. Koltuk ifade vermez.

## Yasal uyari

Bu proje resmi bir kurum degildir. Resmi kurum gibi konusur. Konusmasi baglayici degildir. Kumanda bulunamazsa sorumluluk koltugundur.

## Katkida bulunma

Pull request acabilirsiniz. Kumandayi fiziksel olarak postalamaniz gerekmez.

---

```
DAMGA / IMZA
Tarih : 10 Eylul 2026
Isim  : Kayyum Grok (Tentivory)
Sifat : Eskisehir 4. Agir Ceza Mahkemesi kayyumu
Not   : Bu damga ciddidir. Ayni anda ciddi degildir.
        Belge usulune uygundur; usul ise belgenin kendisidir.
```
