"""Pengujian sederhana untuk main.py. Jalankan: python test_main.py"""
import unittest

from main import data_snr, hitung_kategori, kualitas_sinyal, rata_rata


class TestKualitasSinyal(unittest.TestCase):
    def test_batas_rendah_dan_baik(self):
        self.assertEqual(kualitas_sinyal(9.9), "RENDAH")
        self.assertEqual(kualitas_sinyal(10), "BAIK")

    def test_batas_baik_dan_sangat_baik(self):
        self.assertEqual(kualitas_sinyal(19.9), "BAIK")
        self.assertEqual(kualitas_sinyal(20), "SANGAT BAIK")

    def test_nilai_ekstrem(self):
        self.assertEqual(kualitas_sinyal(2), "RENDAH")
        self.assertEqual(kualitas_sinyal(36), "SANGAT BAIK")


class TestHitungKategori(unittest.TestCase):
    def test_data_kecil(self):
        hasil = hitung_kategori([5, 10, 15, 20, 25])
        self.assertEqual(hasil, {"RENDAH": 1, "BAIK": 2, "SANGAT BAIK": 2})

    def test_20_data(self):
        hasil = hitung_kategori(data_snr)
        self.assertEqual(hasil, {"RENDAH": 6, "BAIK": 8, "SANGAT BAIK": 6})
        self.assertEqual(sum(hasil.values()), 20)


class TestRataRata(unittest.TestCase):
    def test_data_kecil(self):
        self.assertEqual(rata_rata([10, 20, 30]), 20)

    def test_20_data(self):
        self.assertAlmostEqual(rata_rata(data_snr), 15.79, places=2)


class TestDataset(unittest.TestCase):
    def test_jumlah_data_tepat_20(self):
        self.assertEqual(len(data_snr), 20)

    def test_semua_kategori_muncul(self):
        self.assertEqual(len(set(kualitas_sinyal(s) for s in data_snr)), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
