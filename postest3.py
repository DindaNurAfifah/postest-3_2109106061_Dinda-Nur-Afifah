#Program Kalkulator Diskon Pembelian bunga
def Tampilkan_menu() :
    print("1. Bunga Mawar Merah/Putih=10000")
    print("2. Bunga Mawar Pelangi=20000")
    print("3. Bunga Matahari=16000")
    print("4. Bunga Kapas=18000")
    print("5. SELESAI")
list_diskon = ["Pembelian Bunga Mawar Merah/putih > 10 tangkai bunga diskon 10%"
               "Pembelian Bunga Mawar Pelang >10 tangkai bunga diskon 20%"
               "Pembelian Bunga Matahari >5 tangkai bunga diskon 20%"
               "Pembelian Bunga Kapas >10 tangkai bunga diskon 25%"]
 
while True:
    Tampilkan_menu()
    menu = int(input("Masukkan pilihan="))

    if menu==1 :
        jumlah = int(input("Masukan jumlah tangkai="))
        if jumlah <10 :
            bayar = jumlah * 10000
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

        elif jumlah >= 10:
            hitung = jumlah * 10000
            potongan = jumlah * 10000 * 0.01
            bayar    = hitung - potongan
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

    elif menu==2 :
        jumlah = int(input("Masukan jumlah tangkai="))
        if jumlah <10 :
            bayar = jumlah * 20000
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

        elif jumlah >= 10:
            hitung = jumlah * 20000
            potongan = jumlah * 20000 * 0.02
            bayar    = hitung - potongan
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

    elif menu==3 :
        jumlah = int(input("Masukan jumlah tangkai="))
        if jumlah <5 :
            bayar = jumlah * 16000
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

        elif jumlah >= 5:
            hitung = jumlah * 16000
            potongan = jumlah * 16000 * 0.02
            bayar    = hitung - potongan
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

    elif menu==4 :
        jumlah = int(input("Masukan jumlah tangkai="))
        if jumlah <10 :
            bayar = jumlah * 18000
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

        elif jumlah >= 10:
            hitung = jumlah * 18000
            potongan = jumlah * 18000 * 0.25
            bayar    = hitung - potongan
            print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
            print("Ditunggu pembelian berikutnya")

    else :
        print("SELESAI")
        break

        

    