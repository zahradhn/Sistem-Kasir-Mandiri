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
3. Module 'test-case.py' berisi berfungsi untuk menjalankan test case yang diberikan oleh Pacmann.

# Flowchart
Alur program sistem kasir mandiri ini sebagai berikut:
![Flowchart cashier 2](https://user-images.githubusercontent.com/123977443/218341621-f3f91157-b5ce-4c27-89aa-736815b6e05f.png)

# Penjelasan Attribute dan Method
1. Attribute `items` memiliki tipe list, digunakan untuk menyimpan seluruh item yang ada dalam transaksi.
2. Attribute `total_price` memiliki tipe float, digunakan untuk menyimpan jumlam total harga item setelah diskon.
3. Attribute `discount` memiliki tipe float, digunakan untuk menyimpan jumlah total diskon yang didapatkan.
4. Attribute `self.items` merupakan referensi ke attribute `items` dalam instance (object) yang dibuat.
5. Attribute `self.total_price` merupakan referensi ke attribute `total_price` dalam instance (object) yang dibuat.
6. Attribute `self.discount` merupakan referensi ke attribute `discount` dalam instance (object) yang dibuat.
7. Method `add_item(self, item)` untuk menambahkan item ke dalam transaksi ke dalam list `items` yang berisi tiga elemen, diantaranya: nama item [0], jumlah item [1], dan harga per item [2].
8. Method `update_item_name(self, item_name, new_item)` digunakan untuk memperbarui nama item. Memiliki dua parameter, `item_name` merupakan nama item yang sudah ada sebelumnya, dan `new_item` merupakan nama item yang baru.
9. Method `update_item_quantity(self, item_name, new_quantity)` digunakan untuk memperbarui jumlah item. Memiliki dua parameter, `item_name` merupakan nama item yang jumlahnya mau diperbarui, dan `new_quantity` merupakan jumlah item yang baru.
10. Method `update_item_price(self, item_name, new_price)` digunakan untuk memperbarui harga item. Memiliki dua parameter, `item_name` merupakan nama item yang harganya mau diperbarui, dan `new_price` merupakan harga item yang baru.
11. Method `delete_item(self, item_name)` untuk menghapus item dari transaksi. Parameter `item_name` merupakan nama item yang mau dihapus.
12. Method `reset_transaction(self)` untuk mengosongkan atau menghapus semua item dari keranjang belanja. Method ini memiliki output print text `Keranjang belanja telah dikosongkan!`.
13. Method `check_order(self):` untuk menampilkan seluruh pemesanan yang telah dibuat dalam bentuk tabel yang berisi nomor item, nama item, jumlah item, harga per item, dan total harga (pengalian jumlah item dan harga per item).
14. Method `hitung_total_price(self)` untuk menghitung harga total dan diskon yang didapatkan dari seluruh item yang telah ditambahkan ke dalam list `items`. Method ini memproses diskon 10% jika total belanja lebih dari Rp 500.000,00, 8% jika total belanja lebih dari Rp 300.000,00, atau 5% jika total belanja lebih dari Rp 200.000,00.

# Test Case
# Test Case 1
Menambahkan 2 item menggunakan method `add_item`.

Inputnya adalah:
`trnsct_123.add_item(["Ayam Goreng", 2, 20000.00])`
`trnsct_123.add_item(["Pasta Gigi", 3, 15000.00])`
`print("Item yang dibeli adalah: ", trnsct_123.items)`

Outputnya adalah:

# Test Case 2
Menghapus item menggunakan method `delete_item`.

Inputnya adalah:
`trnsct_123.delete_item("Pasta Gigi")`
`print("Item yang dibeli setelah didelete : ", trnsct_123.items)`

Outputnya adalah:


# Test Case 3
Menghapus semua item menggunakan method `reset_transaction`.

Inputnya adalah:
trnsct_123.reset_transaction()

Outputnya adalah:

# Test Case 4
Menambah item belanja dan menghitung total belanja dengan method `hitung_total_price`.
