# Program mencari akar suatu bilangan
# Programer : Adil Al Rizky MK
# Tanggal = 05/02/2025 

# mengakses fungsi matematika
import math

# Meminta Input dari Pengguna
angka = float(input("Masukan angka: "))

# Pengecekan Bilangan Negatif
if angka < 0:
    
    # Menampilan pernyataan 
    print("Angka tidak boleh negatif")

# Menghitung Akar Kuadrat
else:
    Akar_Kuadrat = math.sqrt(angka)
    
    # Menampilkan hasil 
    print(f"Akar kuadrat dari {angka} adalah {Akar_Kuadrat}")