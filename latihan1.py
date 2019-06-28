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

from random import randint
print("="*21)
print("Permainan Tebak Angka")
print("~ cara main ~ " "\n" "tebak angka yang di keluarkan oleh program secara acak")
print("="*21)
angkaacak = randint(1,10)
i = 0
tebakan = eval(input('tebak angka = '))
while tebakan != angkaacak:
    if tebakan < angkaacak:
        print('tebakan anda lebih kecil')
    else:
        print('tebakan anda lebih besar')
    tebakan = eval(input('Coba tebak lagi, masukan angka lagi = '))
    i = i+1
print('selamat anda berhasil menjawab, angka acaknya : %d' % (angkaacak))
print('Jumlah Tebakan kamu : %d' % (i))