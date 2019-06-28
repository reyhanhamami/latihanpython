# # latihan 1
# a = input('masukan angka pertama : ')
# b = input('masukan angka kedua : ')
# c = eval(a)+eval(b)
# d = eval(a)-eval(b)
# print ('hasil penjumlahan : ',c)
# print ('hasil pengurangan : ',d)
# print ('hasil perkalian : ',eval(a)*eval(b))
# print ('hasil pembagian : ',eval(a)/eval(b))

# # latiahan 2
# print ('program dijalankan ...')
# jalan = input('apakah program ingin dijalankan ulang? y/n')
# while jalan == 'y' or jalan == 'Y':
#     print('program dijalankan....')
#     jalan = input('apakah ingin dijaankan lagi? y/n')
# print ('program dihentikan....')

# # latihan 3
# angka = input('masukan langkah anda : ')
# while int(angka) > 0:
#     print('langkah anda', angka)
#     angka = int(angka) -1
# print('langkah selesai')

# # latihan 4
# quote = input('masukan quote anda ')
# author = input('masukan nama autor ')
# print ('"%s" ~ %s ' % (quote, author))

# # latihan 5
# for word in ["spam", "inbox", "sent"]:
#     print(word, end='\n')

# # latihan 6
# a = [1,3,5,7,9]
# for angka in a:
#     print('cetak angka', angka)

# # latihan 7
# makanan = ['nasi goreng', 'cap cay']
# for item in makanan:
#     print('saya makan', item)

# # latihan 8
# age = eval(input('Enter your age : '))
# if age * 365 > 20000:
#     print('Time to retire!')
# elif age * 365 > 10000:
#     print('Lots of time left!')
# else:
#     print('Time to get started!')

# # latihan 9
# lagi = 'y' 
# while lagi == 'y' or lagi == 'Y':
#     angka = input('masukan angka : ')
#     if int(angka) % 2 == 0:
#         print(angka, "bilangan genap")
#     else:
#         print(angka, 'bilangan ganjil')
#     lagi = input('apakah ingin menjalankan lagi? y/n ')
# print('program berhenti')

# # latihan 10
# from random import randint
# a = randint(1,10)
# print ('Permainan tebak angka')
# tebakan = input('masukan tebakan anda : ' )
# i = 1
# while int(tebakan) != a:
#     if int(tebakan) < a:
#         print('tebakan anda lebih kecil')
#     else:
#         print('tebakan anda lebih besar')
#     i +=  1
#     tebakan = input('masukan tebakan anda : ')
# print ('angka rahasia anda : ', a)
# print ('anda sudah menebak %d kali' % (i)) 

# latihan 11
# cek bilangan prima
def bilanganPrima(angkaAwal, angkaAkhir):

    bil_prima = []
    for angka in range(angkaAwal, angkaAkhir):
        if angka > 1:
            for i in range(2, angka):
                if (angka % i) == 0:
                    break
            else:
                bil_prima.append(angka)
    return(bil_prima)

print(bilanganPrima(5,50))
print(bilanganPrima(500,600))
print(bilanganPrima(99,200))

# # latihan 12
# # contoh fungsi
# def cek_bilangan(angka):
#     if angka % 2 == 0:
#         print('bilangan genap')
#     else:
#         print('bilangan ganjil')

# cek_bilangan(100)
# cek_bilangan(1)
# cek_bilangan(67321)

# # latihan 13
# # fungsi dengan pengembalian nilai
# def penjumlahan(a,b):
#     return a + b

# angka1 = penjumlahan(10,5)
# angka2 = penjumlahan(5,9)

# print(angka1)
# print(angka2)
# print(angka1+angka2)

# # latihan 14
# def kalkulator(pertama, kedua, operator):
#     if operator == '+':
#         print ('hasilnya adalah =',pertama+kedua) 
#     elif operator == '-':
#         print ('hasilnya adalah =',pertama-kedua)
#     elif operator == '*':
#         print ('hasilnya adalah =',pertama*kedua) 
#     elif operator == '/':
#         print ('hasilnya adalah =',pertama/kedua)
#     else:
#         print('operator tidak dikenali')

# a = input('masukan angka pertama = ')
# b = input('masukan angka kedua = ')
# c = input('masukan operator = ')
# kalkulator(int(a), int(b), c)

# # latihan 15
# pesanan = input('masukan pesanan anda = ')
# data = pesanan.split(',')

# for pesan in data:
#     print('Saya pesan', pesan)

# # latihan 16
# hitung = input('masukan string : ')
# list(hitung)
# angka = 0
# huruf = 0
# for test in hitung:
#     if test in ['1','2','3','4','5','6','7','8','9','0']:
#         angka += 1 
#     elif test == ' ':
#         space = 0
#     else:
#         huruf += 1

# print ('Jumlah huruf', huruf)
# print ('Jumlah angka', angka)

# # latihan 17
# nama  = input('masukan nama = ')
# nama_pecahan = list(nama)
# angka = 0
# for nama2 in nama_pecahan:
#     if nama2 == ' ':
#         space = 0
#     else:
#         angka += 1 

# # for t in range(0,angka):
# #     print (nama)
# print (angka)