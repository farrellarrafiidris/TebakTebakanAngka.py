import random

angkaRahasia = random.randint(1, 100)
angkaTebakan = None
percobaan = 0

while angkaTebakan != angkaRahasia:
    angkaTebakan = int(input("Masukkan angka tebakan 1-100: "))
    percobaan += 1  # Tambahkan perhitungan percobaan di sini

    if angkaTebakan < angkaRahasia:
        print("Angka tebakan terlalu kecil!")
    elif angkaTebakan > angkaRahasia:
        print("Angka tebakan terlalu besar!")
    else:
        print(f'Selamat, Anda berhasil menebak angka dalam {percobaan} percobaan!')
