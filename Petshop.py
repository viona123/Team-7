# Get user input for owner's name, animal's name, and animal's condition
nama_pemilik = input("Masukkan nama pemilik hewan: ")
nama_hewan = input("Masukkan nama hewan: ")
kondisi_hewan = input("Masukkan kondisi hewan: ")

# jenis hewan
jenis_hewan = """
|==============================================|
|              Pilih Jenis Hewan               |
|==============================================|
| 1. Hewan Anjing                              |
| 2. Hewan Kucing                              |
|==============================================|
"""

# Menampilkan daftar makanan dan minuman
print("|==============================================|")
print("|              Pet Shop Lovely hart            |")
print("|==============================================|")
print(jenis_hewan)


def grooming_cat():
    print("|=======================================================|")
    print("|             Pilihan grooming untuk kucing             |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.20.000      |")
    print("|2. Grooming basic                       Rp.25.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.30.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.30.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.60.000      |")
    print("|6. Grooming shampoo whitening           Rp.80.000      |")
    print("|=======================================================|")
    choice = input("Masukkan pilihan grooming kucing (1-6):")
    return  choice

def grooming_anjing():
    print("|=======================================================|")
    print("|        Pilihan grooming untuk anjing                  |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.40.000      |")
    print("|2. Grooming basic                       Rp.50.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.60.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.70.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.80.000      |")
    print("|6. Grooming shampoo whitening           Rp.100.000     |")
    print("|=======================================================|")
    choice = input("Masukkan pilihan grooming anjing (1-6):")
    return  choice

def print_nota(reservasi):
  groomings = ["nanti masukin list grooming"]
  total_harga = 0
  print("\n--- Nota Reservasi Grooming ---")
  for idx, data in enumerate(reservasi):
    print("Reservasi", idx + 1)
    print("Nama Pemilik:", data["nama_pemilik"])
    print("Nomor Pemilik:", data["nomor_pemilik"])
    print("Alamat Pemilik:", data["alamat_pemilik"])
    print("Nama Hewan:", data["nama_hewan"])
    print("Kondisi Hewan:", data["kondisi_hewan"])
    print("Pilihan Grooming:", groomings[int(data["pilihan_grooming"])-1])
    harga = calculate_price(data["pilihan_grooming"], data["jenis_hewan"])
    print("Harga:", harga)
    total_harga += harga
  print("Total Harga: Rp", total_harga)
  print("---------------------------------")

# Pilihan jenis hewan
hewan = int(input("Pilih jenis hewan [1/2]: "))

if hewan == 1:   
# List untuk menyimpan treatment anjing
    treatment_anjing = []

# Percabangan pilihan anjing
    while True:
        hewan_anjing = int(input("Pilih treatment [1/6] atau pilih 0 jika sudah memilih: "))
        if hewan_anjing == 0:
            break

        if 1 <= hewan_anjing <= 6:
            harga = [40000, 50000, 60000, 70000, 80000, 100000]
            treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu", "Grooming shampoo Anti jamur", "Grooming Shampoo Anti kutu & jamur", "Grooming shampoo Whitening"]
            treatment_anjing.append((treatment, harga))
        else:
            print("Pilihan tidak valid")


if hewan == 2:
# List untuk menyimpan treatment kucing 
    treatment_kucing = []

# Percabangan pilihan kucing
while True:
    hewan_kucing = int(input("Pilih treatment [1/6] atau pilih 0 jika sudah memilih: " ))
    if hewan_kucing == 0:
            break
    
    if 1 <= hewan_kucing <= 6:
        harga = [20000, 25000, 30000, 30000, 60000, 80000]
        treatment = ["Grooming kering'", "Grooming basic", "Grooming shampo Anti kutu", "Grooming shampoo Anti jamur", "Grooming Shampoo anti kutu & jamur", "Grooming shampoo whitehing"]
        treatment_kucing.append((treatment, harga))

else:
    print("Pilihan tidak valid")