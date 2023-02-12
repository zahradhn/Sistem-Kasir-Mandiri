# Sistem Kasir Mandiri
Sistem kasir mandiri sederhana yang dibuat menggunakan bahasa pemrograman Python untuk memudahkan customer dalam melakukan transaksi belanja. Fitur utama dalam sistem kasir ini adalah menambahkan nama item, jumlah item, dan harga item yang ingin dibeli. Lalu customer juga dapat mengubah nama item, jumlah item, dan harga item jika terdapat kesalahan saat melakukan input. Customer juga bisa menghapus salah satu atau seluruh item sekaligus jika ingin mengulang transaksi dari awal. Setelah selesai memilih item, customer dapat mengecek ulang daftar item dalam bentuk tabel, lalu menghitung total harga item yang dibeli dan diskon yang didapatkan.

# Tujuan Pengerjaan Project
1. Membuat sistem kasir mandiri sederhana menggunakan bahasa pemrograman Python yang memiliki fitur:
    - Menambahkan transaksi berupa nama item, jumlah item, dan harga per item.
    - Mengubah nama item, jumlah item, dan harga item yang telah ditambahkan jika terdapat kesalahan input.
    - Menghapus salah satu item yang tidak jadi dibeli.
    - Mengosongkan keranjang belanja atau menghapus semua item.
    - Menampilkan seluruh pemesanan yang telah dibuat dalam bentuk tabel.
    - Menghitung harga total dan diskon yang didapatkan dari seluruh item yang telah ditambahkan.
2. Mengimplementasikan modular code, clean code (PEP 8), dokumentasi docstring dalam function atau class yang dibuat, dan defense programming.

# Deskripsi Module
1. Module 'cashier.py' memuat class Transaction yang memiliki fungsi dan kode yang berkaitan dengan sistem kasir mandiri.
2. Module 'test-all-features.py' berisi tes seluruh fitur yang terdapat dalam class Transaction.
3. Module 'test.py' berisi berfungsi untuk menjalankan test case yang diberikan oleh Pacmann.

# Flowchart
Alur program sistem kasir mandiri ini sebagai berikut:
![Flowchart cashier 2](https://user-images.githubusercontent.com/123977443/218341621-f3f91157-b5ce-4c27-89aa-736815b6e05f.png)

# Penjelasan Attribute
1. Attribute `items` memiliki tipe list, digunakan untuk menyimpan seluruh item yang ada dalam transaksi.
2. Attribute `total_price` merupakan variabel yang memiliki tipe float, digunakan untuk menyimpan jumlam total harga item setelah diskon.
3. Attribute `discount` merupakan variabel yang memiliki tipe float, digunakan untuk menyimpan jumlah total diskon yang didapatkan.

# Penjelasan Method
1. Method `add_item(self, item):` untuk menambahkan item ke dalam transaksi ke dalam list "items" yang berisi tiga elemen, diantaranya: nama item [0], jumlah item [1], dan harga per item [2].
4. Method `update_item_name`, `update_item_quantity`, dan `update_item_price` untuk mengubah nama item, jumlah item, dan harga per item jika terjadi kesalahan.
5. Method `delete_item` untuk menghapus item dari transaksi.
6. Method `reset_transaction` untuk mengosongkan atau menghapus semua item dari keranjang belanja.
7. Method `check_order` untuk menampilkan seluruh pemesanan yang telah dibuat dalam bentuk tabel.
8. Method `hitung_total_price` untuk menghitung harga total dan diskon yang didapatkan dari seluruh item yang telah ditambahkan.


