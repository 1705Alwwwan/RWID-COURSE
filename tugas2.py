def main():
    DaftarBarang = []
    
    choice = 0 #variable pilihan angka
    #lakukan pengulangan pada opsi
    while choice != 4:
        print ("========Store Manager System========")
        print("1. Tambah Asset")
        print ("2. Cari Asset")
        print ("3. Tampilkan Asset")
        print ("4. Keluar")
        choice =  int(input())

        if choice == 1:
            print("========Input Data Untuk Barang========")
            nBarang = input("Input jenis barang ===>  ")
            nBrand = input("Input brand ===>  ")
            njumlah = int(input("Masukan Jumlah Barang ==>"))

            DaftarBarang.append([nBarang, nBrand, njumlah]) 
        elif choice == 2:
            print("========Cari Asset ========")
            keyword = input("masukan nama aset .....")
            for Barang in DaftarBarang:
                if keyword in Barang:
                    print(Barang) 

        elif choice == 3:
            print("========Tampilkan Asset========")
            for i in range(len(DaftarBarang)):
                print(DaftarBarang[i])


        elif choice == 4:
            print ("Keluar Program!")

        print ("Program Selesai!")


if __name__ == '__main__':
    main()