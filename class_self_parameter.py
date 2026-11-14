class Siswa:
    def __init__(sendiri, nama):
        sendiri.nama = nama

    def sapa(sendiri):
        print("Halo, saya " + sendiri.nama)

s = Siswa("Latifah")
s.sapa()
