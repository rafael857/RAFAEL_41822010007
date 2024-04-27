#ini adalah program untuk menghitung nilai akhir siswa

print('selamat datang di aplikasi perhitungan nilai mahasiswa')
print('---------------------------------------------------------')

def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.4 * uas
    return nilai_akhir

def kategori_penilaian(nilai_akhir):
    if nilai_akhir > 85:
        return "A"
    elif nilai_akhir > 80:
        return "A-"
    elif nilai_akhir > 75:
        return "B+"
    elif nilai_akhir > 70:
        return "B"
    elif nilai_akhir > 65:
        return "B-"
    elif nilai_akhir > 60:
        return "C+"
    elif nilai_akhir > 55:
        return "C"
    elif nilai_akhir > 50:
        return "C-"
    elif nilai_akhir > 30:
        return "D"
    else:
        return "E"

def main():

    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))


    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)


    kategori = kategori_penilaian(nilai_akhir)


    print("Nilai akhir:", nilai_akhir)
    print("Kategori penilaian:", kategori)

if __name__ == "__main__":
    main()

