class Siswa:
    def __init__(self, nama):
        self.nama = nama

    def belajar(self):
        print(self.nama + " sedang belajar Python")

s = Siswa("Latifah")
s.belajar()
