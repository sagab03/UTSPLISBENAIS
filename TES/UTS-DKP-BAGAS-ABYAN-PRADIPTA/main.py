"""Mini Project Individual - Kelompok B (Telekomunikasi)
Monitoring Kualitas Sinyal / SNR

Aturan status:
    SNR < 10 dB         -> RENDAH
    10 <= SNR < 20 dB   -> BAIK
    SNR >= 20 dB        -> SANGAT BAIK
"""

BATAS_RENDAH = 10    # dB, di bawah nilai ini status RENDAH
BATAS_BAIK = 20      # dB, mulai nilai ini status SANGAT BAIK

# 15 data inti dari soal (urutan dan nilai dipertahankan)
DATA_INTI = [5, 8, 11, 14, 18, 22, 27, 9, 16, 24, 12, 30, 7, 20, 15]

# 5 data tambahan untuk menguji batas kategori dan variasi nilai
DATA_TAMBAHAN = [10, 9.9, 19.9, 2, 36]

data_snr = DATA_INTI + DATA_TAMBAHAN  # total tepat 20 data


def kualitas_sinyal(snr):
    """Menentukan status kualitas sinyal dari satu nilai SNR (dB)."""
    if snr < BATAS_RENDAH:
        return "RENDAH"
    elif snr < BATAS_BAIK:
        return "BAIK"
    else:
        return "SANGAT BAIK"


def hitung_kategori(data):
    """Menghitung jumlah data pada setiap kategori kualitas sinyal."""
    jumlah = {"RENDAH": 0, "BAIK": 0, "SANGAT BAIK": 0}
    for snr in data:
        jumlah[kualitas_sinyal(snr)] += 1
    return jumlah


def rata_rata(data):
    """Menghitung nilai rata-rata SNR (dB)."""
    total = 0
    for snr in data:
        total += snr
    return total / len(data)


def tampilkan_hasil_per_data(data):
    """Mencetak status setiap data SNR."""
    print("HASIL PER DATA")
    print(f"{'No':<4}{'SNR (dB)':<12}Status")
    print("-" * 30)
    for nomor, snr in enumerate(data, start=1):
        print(f"{nomor:<4}{snr:<12}{kualitas_sinyal(snr)}")


def tampilkan_ringkasan(data):
    """Mencetak ringkasan: jumlah tiap kategori, rata-rata, maksimum, minimum."""
    jumlah = hitung_kategori(data)
    print("\nRINGKASAN AKHIR")
    print("-" * 30)
    print(f"{'Jumlah data':<19}: {len(data)}")
    for kategori, banyak in jumlah.items():
        print(f"{'Jumlah ' + kategori:<19}: {banyak}")
    print(f"{'Rata-rata SNR':<19}: {rata_rata(data):.2f} dB")
    print(f"{'SNR maksimum':<19}: {max(data)} dB")
    print(f"{'SNR minimum':<19}: {min(data)} dB")


def main():
    print("MONITORING KUALITAS SINYAL / SNR\n")
    tampilkan_hasil_per_data(data_snr)
    tampilkan_ringkasan(data_snr)


if __name__ == "__main__":
    main()
