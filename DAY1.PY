class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")

    def ubah_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru
        print(f"Jurusan {self.nama} telah diubah menjadi {self.jurusan}")

mahasiswa1 = Mahasiswa("Tata", "A710230027", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Enggar", "B675202794", "Bisnis Digital")

mahasiswa1.info()
print()

mahasiswa2.ubah_jurusan("Teknologi Informasi")
mahasiswa2.info()