import random

print("=== GAME TEBAK ANGKA ===")
print("Saya sudah memilih angka dari 1 sampai 100.")
print("Coba tebak ya!\n")

angka_rahasia = random.randint(1, 100)
percobaan = 0

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!\n")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!\n")
    else:
        print(f"Selamat! Kamu benar dalam {percobaan} percobaan 🎉")
        break