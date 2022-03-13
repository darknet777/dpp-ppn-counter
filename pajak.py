# Aplikasi Penghitung DPP dan PPn untuk
# tagihan pekerjaan vendor ke PLN

import os

def clearScreen():
    CLEAR_SCREEN = os.system('clear')

class MainApp():
    def dppCounter():
        while True:
            clearScreen()

            print('Hitungan berdasarkan nilai kontrak\n')
            nilaiKontrak = int(input('Masukkan nilai kontrak: '))
            dpp = nilaiKontrak * 11 / 100
            ppn = dpp * 10 / 100

            print('\nNilai kontrak: Rp{:,}'.format(nilaiKontrak))
            print('Nilai DPP: {:,.2f}'.format(dpp))
            print('Nilai PPn: {:,.2f}'.format(ppn))
            print('Pembulatan nilai PPn: {:,}'.format(round(ppn)))
            print()

            userInput = input('Hitung lagi (y/N)? ')

            if userInput == 'y' or userInput == 'Y':
                clearScreen()
                continue
            else:
                break

    def byPercent():
        while True:
            clearScreen()

            print('Hitungan berdasarkan progress(%) pekerjaan\n')
            nilaiKontrak = int(input('Masukkan nilai kontrak: '))
            persen = int(input('Masukkan nilai persen: '))
            dpp = nilaiKontrak * 11 / 100
            ppn = dpp * 10 / 100

            print('Nilai kontrak: Rp{:,}'.format(nilaiKontrak))
            print('Nilai DPP: {:,.2f}'.format(dpp))
            print('Nilai PPn: {:,.2f}'.format(ppn))
            print('Pembulatan nilai PPn: {:,}'.format(round(ppn)))
            print()

            userInput = input('Hitung lagi (y/N)? ')

            if userInput == 'y' or userInput == 'Y':
                clearScreen()
                continue
            else:
                break

def startApp():
    while True:
        clearScreen()
        print('Selamat datang!')
        print('Aplikasi Penghitung DPP dan PPn')
        print('Versi\t   : 1.0')
        print('Developer  : Billy Jeferson')
        print('Website\t   : https://darknet777.tech')
        print('Github\t   : https://github.com/darknet777')
        print('Twitter\t   : https://twitter.com/BillyJeferson5\n')
        
        print(5 * '-', 'Daftar isi', 5 * '-')
        print('1. Hitung DPP dan PPn (berdasarkan nilai kontrak)')
        print('2. Hitung DPP dan PPn (berdasarkan progress(%) pekerjaan)')
        print('0. Keluar aplikasi\n')

        userInput = input('Silakan pilih opsi: ')

        if userInput == '1':
            MainApp.dppCounter()
        elif userInput == '2':
            MainApp.byPercent()
        elif userInput == '0':
            print('Meninggalkan program...')
            break
        else:
            continue

startApp()

