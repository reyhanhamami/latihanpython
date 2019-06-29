# a = eval(input('masukan angka pertama = '))
# b = eval(input('masukan angka kedua = '))

# print('hasil pertambahan = ', a+b)
# print('hasil pengurangan = ', a-b)
# print('hasil perkalian = ', a*b)
# print('hasil pembagian = ', a/b)

# print ('Program dijalankan ...')
# a = input('apakah ingin dijalankan lagi y/n ')
# while (a == 'y' or a == 'Y'):
#     print('program dijalankan ...')
#     a = input('apakah ingin dijalankan lagi y/n ')
# print ('program dihentikan')

# a = eval(input('masukan langkah anda = '))
# while (a > 1):
#     a = a - 1
#     print('langkah anda ', a)
# print('langkah anda selesai')

# kata = input('masukin kata mutiara lw = ')
# nama = input('nama siapa? ')
# print('kata-kata mutiara "%s" ~ author : %s' %(kata,nama))

# lists = ['email', 'inbox', 'sent']
# for listss in lists:
#     print(listss, end='\n')

# print('Pengecekan Angka Ganjil atau Genap')
# lagi = 'y'
# while(lagi == 'y' or lagi =='Y'):
#     angka = eval(input('Masukan angka = '))
#     if angka % 2 == 0:
#         print(angka, 'Bilangan Genap')
#     else:
#         print(angka, 'bilangan Ganjil')
#     lagi = input('apakah ingin mencoba lagi? y/n ')
# print('program berhenti')

# from random import randint
# print("="*21)
# print("Permainan Tebak Angka")
# print("~ cara main ~ " "\n" "tebak angka yang di keluarkan oleh program secara acak")
# print("="*21)
# angkaacak = randint(1,10)
# i = 0
# tebakan = eval(input('tebak angka = '))
# while tebakan != angkaacak:
#     if tebakan < angkaacak:
#         print('tebakan anda lebih kecil')
#     else:
#         print('tebakan anda lebih besar')
#     tebakan = eval(input('Coba tebak lagi, masukan angka lagi = '))
#     i = i+1
# print('selamat anda berhasil menjawab, angka acaknya : %d' % (angkaacak))
# print('Jumlah Tebakan kamu : %d' % (i))

# def bilanganPrima(angkaAwal, angkaAkhir):

#     bil_prima = []
#     for angka in range(angkaAwal, angkaAkhir):
#         if angka > 1:
#             for i in range(2, angka):
#                 if (angka % i ) == 0:
#                     break
#             else:
#                 bil_prima.append(angka)
#     return(bil_prima)

# print(bilanganPrima(5,50))
# print(bilanganPrima(500,600))
# print(bilanganPrima(99,200))

# def cekganjilgenap(angka):
#     if angka % 2 == 0:
#         print('bilangan genap')
#     else:
#         print('bilangan ganjil')

# cekganjilgenap(3)
# cekganjilgenap(30)
# cekganjilgenap(6)

# def kalkulator(pertama, kedua, operator):
#     if operator == '+':
#         print('hasil pertambahan adalah =  ',pertama+kedua)
#     elif operator == '-':
#         print('hasil pengurangan adalah =  ',pertama-kedua)
#     elif operator == "*":
#         print('hasil perkalian adalah =  ', pertama*kedua)
#     elif operator == "/":
#         print('hasil dari pembagian adalah =  ', pertama/kedua)
#     else:
#         print('operator tidak dikenali')
# a = input('masukin angka = ')
# b = input('masukin angka = ')
# c = input('masukin operator = ')

# kalkulator(int(a), int(b), c)

# menu = input('mau makan apa hari ini? ')
# menus = menu.split(',')
# for menuss in menus:
#     print('anda memesan  = %s ' %(menuss))

# pesertatraining = ['anelka', 'hafidz', 'ilham', 'ayu', 'bayu']
 
# print (pesertatraining[3])
# print ('semua teman ada %s orang' % (len(pesertatraining)))
# print ('tampilkan semua teman dengan perulangan')
# for teman in pesertatraining:
#     print(teman)

i = 0
hobi = []
lagi = 'y'
while (lagi == 'y' or lagi == 'Y'):
    hobi_baru = input('inputkan hobi yang ke-%d: ' %(i))
    hobi.append(hobi_baru)
    lagi = input('isi lagi gak? y/n: ')
    i += 1
print('='*20)

print('kamu memiliki %d hobi' % (i))
for hobis in hobi:
    print('- %s' %(hobis))