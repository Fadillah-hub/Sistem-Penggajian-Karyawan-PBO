
# ==========================================
# SISTEM PENCATATAN DAN PERHITUNGAN GAJI
# MENGGUNAKAN OBJECT-ORIENTED PROGRAMMING
# ==========================================

# 1. SUPERCLASS: Karyawan
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.__gaji_pokok = gaji_pokok

    # Getter untuk mengambil gaji pokok
    @property
    def gaji_pokok(self):
        return self.__gaji_pokok

    # Setter untuk mengubah gaji pokok
    @gaji_pokok.setter
    def gaji_pokok(self, nilai):
        if nilai <= 0:
            print("Peringatan: Gaji pokok harus lebih dari 0!")
        else:
            self.__gaji_pokok = nilai
            print("Gaji pokok berhasil diperbarui.")

    # Method perhitungan gaji dasar
    def hitung_gaji_total(self):
        return self.__gaji_pokok

    # Method menampilkan informasi karyawan
    def tampilkan_info(self):
        print(f"Nama        : {self.nama}")
        print(f"ID Karyawan : {self.id_karyawan}")
        print(f"Gaji Pokok  : Rp{self.gaji_pokok:,.0f}")


# 2. CHILD CLASS: Karyawan Tetap
class KaryawanTetap(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # Overriding perhitungan gaji
    def hitung_gaji_total(self):
        return self.gaji_pokok + self.tunjangan

    # Overriding tampilan informasi
    def tampilkan_info(self):
        print("\n===== DATA KARYAWAN TETAP =====")
        super().tampilkan_info()
        print(f"Tunjangan   : Rp{self.tunjangan:,.0f}")
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.0f}")


# 3. CHILD CLASS: Karyawan Kontrak
class KaryawanKontrak(Karyawan):
    def __init__(
        self, nama, id_karyawan, gaji_pokok,
        jam_lembur, tarif_lembur
    ):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.jam_lembur = jam_lembur
        self.tarif_lembur = tarif_lembur

    # Overriding perhitungan gaji
    def hitung_gaji_total(self):
        return (
            self.gaji_pokok
            + (self.jam_lembur * self.tarif_lembur)
        )

    # Overriding tampilan informasi
    def tampilkan_info(self):
        print("\n===== DATA KARYAWAN KONTRAK =====")
        super().tampilkan_info()
        print(f"Jam Lembur  : {self.jam_lembur} jam")
        print(f"Tarif/Jam   : Rp{self.tarif_lembur:,.0f}")
        print(
            f"Total Lembur: "
            f"Rp{self.jam_lembur * self.tarif_lembur:,.0f}"
        )
        print(f"Total Gaji  : Rp{self.hitung_gaji_total():,.0f}")


# ==========================================
# 4. MAIN PROGRAM
# ==========================================

# Membuat objek karyawan tetap
karyawan1 = KaryawanTetap(
    "Andi Saputra",
    "K001",
    5000000,
    1000000
)

# Membuat objek karyawan kontrak
karyawan2 = KaryawanKontrak(
    "Budi Santoso",
    "K002",
    3000000,
    10,
    50000
)

# Menyimpan objek ke dalam list
daftar_karyawan = [karyawan1, karyawan2]

# Demonstrasi polymorphism
print("===================================")
print(" DATA KARYAWAN DAN TOTAL GAJI")
print("===================================")

for karyawan in daftar_karyawan:
    karyawan.tampilkan_info()

# Demonstrasi encapsulation
print("\n===================================")
print(" PENGUJIAN ENCAPSULATION")
print("===================================")

print("\nMengubah gaji pokok menjadi nilai tidak valid:")
karyawan1.gaji_pokok = -1000000

print("\nMengubah gaji pokok menjadi nilai valid:")
karyawan1.gaji_pokok = 6000000

# Menampilkan kembali informasi setelah perubahan
print("\nData karyawan setelah gaji diperbarui:")
karyawan1.tampilkan_info()
