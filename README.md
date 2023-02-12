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
![Flowcode](https://user-images.githubusercontent.com/123977443/218324598-a08575eb-0b67-44d4-b3f4-7efbdd300c95.jpg)

# Method
1. Method `add_item` untuk menambahkan item ke dalam transaksi.
4. Method `update_item_name`, `update_item_quantity`, dan `update_item_price` untuk mengubah nama item, jumlah item, dan harga per item jika terjadi kesalahan.
5. Method `delete_item` untuk menghapus item dari transaksi.
6. Method `reset_transaction` untuk mengosongkan atau menghapus semua item dari keranjang belanja.
7. Method `check_order` untuk menampilkan seluruh pemesanan yang telah dibuat dalam bentuk tabel.
8. Method `hitung_total_price` untuk menghitung harga total dan diskon yang didapatkan dari seluruh item yang telah ditambahkan.
