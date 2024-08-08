import random

angkaRahasia =  random.randint(1,100);
angkaTebakan = None;

while angkaTebakan != angkaRahasia:
    angkaTebakan = int(input("Masukkan angka tebakan 1-100: "))
    
    if angkaTebakan < angkaRahasia:
        print("Angka tebakan terlalu kecil!")
    elif angkaTebakan > angkaRahasia:
        print("Angka tebakan terlalu besar!")
    else:
        print("Selamat, anda berhasil menebak angka!")
        break;