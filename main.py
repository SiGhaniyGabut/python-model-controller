# Tambahan informasi, sebaiknya pelajari sumber2 berikut untuk membuat kode Python yang baik:
# - https://www.python.org/dev/peps/pep-0008/
# - https://testdriven.io/blog/clean-code-python/

from app.controllers.students_controller import *

# Main Methods
def main():
    print('Selamat datang di Sistem Informasi Mahasiswa')
    while True:
        print('Menu:')
        print('1. Daftar Mahasiswa')
        print('2. Lihat Detil Mahasiswa')
        print('3. Tambah Mahasiswa')
        print('4. Ubah Mahasiswa')
        print('5. Hapus Mahasiswa')
        print('6. Keluar')
        menu = int(input('Pilih menu: '))
        if menu == 1:
            index()
        elif menu == 2:
            show()
        elif menu == 3:
            add()
        elif menu == 4:
            update()
        elif menu == 5:
            delete()
        elif menu == 6:
            break
        else:
            print('Menu tidak tersedia')

main()