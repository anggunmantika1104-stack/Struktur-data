nama = input("Masukkan Nama Anda: ")

if nama == "Anggun":  
    angka = input("Masukkan Angka: ")

    for i in range(1, 11):
        print(f"{angka} * {i} = {angka * i}")

else:
    print("Maaf, Silakan Coba Lagi")
