# Mini Project Individual - Monitoring Kualitas Sinyal / SNR

**Mata kuliah:** Dasar Komputer dan Pemrograman

**Kelompok:** B - Telekomunikasi

**Nama / NIM:** Bagas Abyan Pradipta / 03041282631091

## 1. Deskripsi Singkat

Program Python untuk memonitor kualitas sinyal telekomunikasi berdasarkan nilai *Signal-to-Noise Ratio* (SNR) dalam dB. Program memproses tepat **20 data** (15 data inti dari soal + 5 data tambahan), menentukan status tiap data, lalu menampilkan ringkasan akhir.

Aturan status:

| Rentang SNR | Status |
|---|---|
| SNR < 10 dB | RENDAH |
| 10 <= SNR < 20 dB | BAIK |
| SNR >= 20 dB | SANGAT BAIK |

## 2. Cara Menjalankan

```
python main.py          # menjalankan program
python test_main.py     # menjalankan pengujian (unittest bawaan Python)
```

Hanya memakai Python 3 standar, tanpa input interaktif dan tanpa pustaka pihak ketiga.

## 3. Struktur File

| File | Keterangan |
|---|---|
| main.py | Program utama |
| test_main.py | Pengujian fungsi |
| flowchart.png | Flowchart alur program |
| README.md | Dokumentasi ini |

## 4. Alur Input - Process - Output

- **Input:** list `data_snr` berisi 20 nilai SNR (dB), tertulis langsung di kode.
- **Process:** tiap nilai diklasifikasikan dengan if/elif/else, jumlah tiap kategori dihitung, lalu rata-rata, maksimum, dan minimum dicari.
- **Output:** status tiap data dan ringkasan akhir.

![Flowchart](flowchart.png)

## 5. Konsep Python yang Digunakan

| Konsep | Penerapan di main.py |
|---|---|
| List | `DATA_INTI`, `DATA_TAMBAHAN`, `data_snr` (20 data) |
| Function | `kualitas_sinyal(snr)`, `hitung_kategori(data)`, `rata_rata(data)`, `tampilkan_hasil_per_data(data)`, `tampilkan_ringkasan(data)`, `main()` |
| Decision | if/elif/else pada `kualitas_sinyal` |
| Loop | `for` pada `hitung_kategori`, `rata_rata`, dan `tampilkan_hasil_per_data` |
| Return | `kualitas_sinyal` mengembalikan status; `hitung_kategori` mengembalikan dictionary; `rata_rata` mengembalikan nilai rata-rata |
| Perhitungan | Rata-rata = jumlah seluruh SNR / banyak data; plus maksimum dan minimum |
| Ringkasan | Jumlah tiap kategori, rata-rata, maksimum, minimum |

## 6. Alasan Pemilihan 5 Data Tambahan

15 data inti dipertahankan tanpa perubahan (nilainya 5 sampai 30 dB). Data inti tidak ada yang tepat di batas bawah kategori BAIK (10 dB) dan tidak ada yang sangat dekat dengan batas. Maka 5 data tambahan dipilih untuk menguji batas kategori dan menambah variasi:

| No | Data tambahan (dB) | Alasan pemilihan | Status |
|---|---|---|---|
| 16 | 10 | Tepat di batas bawah BAIK. Menguji bahwa operator `<` bukan `<=`, sehingga 10 dB sudah BAIK. | BAIK |
| 17 | 9.9 | Sesaat di bawah batas 10 dB. Menguji bahwa nilai desimal tipis di bawah batas tetap RENDAH. | RENDAH |
| 18 | 19.9 | Sesaat di bawah batas 20 dB. Menguji bahwa nilai ini masih BAIK, bukan SANGAT BAIK. | BAIK |
| 19 | 2 | Nilai sangat rendah (mendekati sinyal yang hampir tenggelam oleh noise), memperluas variasi sisi bawah. | RENDAH |
| 20 | 36 | Nilai tinggi untuk link yang sangat bersih, memperluas variasi sisi atas di luar maksimum data inti (30 dB). | SANGAT BAIK |

**Kewajaran nilai:** SNR pada sistem telekomunikasi nirkabel dan kabel umumnya berkisar sekitar 0 sampai 40 dB. Seluruh nilai tambahan (2 sampai 36 dB) berada pada rentang realistis tersebut. Nilai 10, 19.9, dan 20 (data inti) berada tepat di titik pindah kategori, sehingga cocok untuk pengujian batas. Data inti bernilai 20 sudah menguji batas SANGAT BAIK dari sisi atas, sedangkan 19.9 menguji dari sisi bawah.

Hasil pengolahan 20 data mencakup ketiga kategori (RENDAH, BAIK, SANGAT BAIK).

## 7. Contoh Output

```
MONITORING KUALITAS SINYAL / SNR

HASIL PER DATA
No  SNR (dB)    Status
------------------------------
1   5           RENDAH
2   8           RENDAH
3   11          BAIK
4   14          BAIK
5   18          BAIK
6   22          SANGAT BAIK
7   27          SANGAT BAIK
8   9           RENDAH
9   16          BAIK
10  24          SANGAT BAIK
11  12          BAIK
12  30          SANGAT BAIK
13  7           RENDAH
14  20          SANGAT BAIK
15  15          BAIK
16  10          BAIK
17  9.9         RENDAH
18  19.9        BAIK
19  2           RENDAH
20  36          SANGAT BAIK

RINGKASAN AKHIR
------------------------------
Jumlah data        : 20
Jumlah RENDAH      : 6
Jumlah BAIK        : 8
Jumlah SANGAT BAIK : 6
Rata-rata SNR      : 15.79 dB
SNR maksimum       : 36 dB
SNR minimum        : 2 dB
```

Pengecekan manual rata-rata: jumlah data inti = 238, jumlah data tambahan = 10 + 9.9 + 19.9 + 2 + 36 = 77.8, total = 315.8, dibagi 20 = **15.79 dB**.

## 8. Testing

Pengujian dilakukan dengan `python test_main.py` (9 test, semuanya lulus).

| Pengujian | Masukan | Hasil yang diharapkan |
|---|---|---|
| Batas RENDAH / BAIK | 9.9 dan 10 | RENDAH dan BAIK |
| Batas BAIK / SANGAT BAIK | 19.9 dan 20 | BAIK dan SANGAT BAIK |
| Nilai ekstrem | 2 dan 36 | RENDAH dan SANGAT BAIK |
| Hitung kategori data kecil | [5, 10, 15, 20, 25] | RENDAH 1, BAIK 2, SANGAT BAIK 2 |
| Hitung kategori 20 data | data_snr | RENDAH 6, BAIK 8, SANGAT BAIK 6 (total 20) |
| Rata-rata data kecil | [10, 20, 30] | 20 |
| Rata-rata 20 data | data_snr | 15.79 |
| Jumlah data | data_snr | tepat 20 |
| Kategori muncul semua | data_snr | 3 kategori berbeda muncul |
