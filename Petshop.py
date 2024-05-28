# Get user input for owner's name, animal's name, and animal's condition
nama_pemilik = input("Masukkan nama pemilik hewan: ")
nama_hewan = input("Masukkan nama hewan: ")
kondisi_hewan = input("Masukkan kondisi hewan: ")

# Daftar makanan dan minuman
daftar_makanan = """
|==============================================|
|              Pilih Jenis Hewan               |
|==============================================|
| 1. Hewan Anjing                              |
| 2. Hewan Kucing                              |
|==============================================|
"""

daftar_minuman = """
|===============================|
|         Pilih Grooming        |
|===============================|
| 1. Hot Chocolate  Rp 30.000   |
| 2. Frappuccino    Rp 40.000   |
| 3. Macchiato      Rp 25.000   |
| 4. Latte          Rp 30.000   |
| 5. Matcha Latte   Rp 24.000   |
|===============================|
"""

# Menampilkan daftar makanan dan minuman
print("|==============================================|")
print("|              Pet Shop Lovely hart            |")
print("|==============================================|")
print(daftar_makanan)
print(daftar_minuman)

# Inisialisasi total_makanan sebelum loop
total_makanan = 0

# Inisialisasi total_minum sebelum loop
total_minum = 0

# List untuk menyimpan pesanan makanan dan minuman

pesanan_makanan = []
pesanan_minuman = []

# Loop untuk meminta pesanan makanan
while True:
    menu_makanan = int(input("Pilih Menu (1-6) atau masukkan 0 jika sudah selesai memilih makanan: "))
    if menu_makanan == 0:
        break

    jumlah_porsi = int(input("Berapa Porsi: "))

    if 1 <= menu_makanan <= 6:
        harga = [25000, 25000, 30000, 35000, 30000, 40000][menu_makanan - 1]
        nama_makanan = ["Nasi Goreng", "Mie Goreng Jawa", "Rice Bowl Chicken Teriyaki", "Rice Bowl Beef Bulgogi", "Rice Bowl Chicken Katsu Curry", "Pasta Aglio Olio"][menu_makanan - 1]
        total_makanan += harga * jumlah_porsi
        pesanan_makanan.append((nama_makanan, jumlah_porsi, harga * jumlah_porsi))
    else:
        print("Pilihan tidak valid.")

# Loop untuk meminta pesanan minuman
while True:
    menu_minuman = int(input("Pilih Menu (1-5) atau masukkan 0 jika sudah selesai memilih minuman: "))
    if menu_minuman == 0:
        break

    jumlah_gelas = int(input("Berapa Gelas: "))

    if 1 <= menu_minuman <= 5:
        harga_minuman = [30000, 40000, 25000, 30000, 24000][menu_minuman - 1]
        nama_minuman = ["Hot Chocolate", "Frappuccino", "Macchiato", "Latte", "Matcha Latte"][menu_minuman - 1]
        total_minum += harga_minuman * jumlah_gelas
        pesanan_minuman.append((nama_minuman, jumlah_gelas, harga_minuman * jumlah_gelas))
    else:
        print("Pilihan tidak valid.")

# Cetak Struk Pembelian
print("\n|=====================================|")
print("|        Struk Pembelian        |")
print("|=======================================|")
print("|           Makanan             |")
print("|=======================================|")
for makanan in pesanan_makanan:
    print(f"|{makanan[0]:<30} {makanan[1]:<10} {makanan[2]:>10}|")
print("|           Minuman             |")
print("|===============================|")
for minuman in pesanan_minuman:
    print(f"|{minuman[0]:<30} {minuman[1]:<10} {minuman[2]:>10}|")
print("|===============================|")
print(f"| Total                      {total_makanan + total_minum:>20} |")
print("|===============================|")