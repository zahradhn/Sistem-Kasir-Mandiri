# Import table
from tabulate import tabulate

# Class
class Transaction:
    
    """
    Class ini menyimpan dan memproses informasi transaksi customer, yaitu item yang dibeli, total harga sebelum diskon, dan jumlah diskon.

    Atribut:
        items (list): List yang berisi nama item (str), jumlah item (int), dan harga per item (float).
        total_price (float): Total harga sebelum diskon.
        discount (float): Jumlah diskon.
    """
    
    items = []
    total_price = 0.0
    discount = 0.0
    
    def __init__(self):
        # Inisialitasi atribut pada class Transaction
        self.items = []
        self.total_price = 0.0
        self.discount = 0.0
    
    def add_item(self, item):
        """
        Menambahkan transaksi ke dalam list "items" yang berisi nama item [0], jumlah item [1], dan harga per item [2].

        Raises:
            TypeError: Apabila format nama item, jumlah item, atau harga item salah.
        """

        if type(item[0]) != str:
           raise TypeError("Format nama item yang anda masukkan salah (gunakan tanda petik sebelum dan sesudah nama item).")
        if type(item[1]) != int:
           raise TypeError("Format jumlah item yang anda masukkan salah (misalnya: 12).")
        if type(item[2]) != float:
           raise TypeError("Format harga item yang anda masukkan salah (misalnya: 25000.00).")
    
        self.items.append(item)
    
    def update_item_name(self, item_name, new_item):
        """
        Mengganti/memperbarui nama item.

        Parameter:
        - item_name (str): Nama item yang ingin diganti.
        - new_item (str): Nama item baru.

        Raises:
        TypeError: Apabila format nama item baru salah.
        """
        
        for item in self.items:
            if item[0] == item_name:
                item[0] = new_item

        if type(new_item) != str:
            raise TypeError("Format nama item yang anda masukkan salah (gunakan tanda petik sebelum dan sesudah nama item).")
    
    def update_item_quantity(self, item_name, new_quantity):
        """
        Mengubah/memperbarui jumlah item.

        Parameter:
        item_name (str): Nama item yang jumlahnya ingin diganti.
        new_quantity (int): Jumlah item baru.

        Raises:
        TypeError: Apabila format jumlah item baru salah.
        """
        
        for item in self.items:
            if item[0] == item_name:
                item[1] = new_quantity

        if type(new_quantity) != int:
            raise TypeError("Format jumlah item yang anda masukkan salah (misalnya: 12).")
    
    def update_item_price(self, item_name, new_price):
        """
        Mengubah/memperbarui harga item.

        Parameter:
        item_name (str): Nama item yang harganya ingin diganti.
        new_price (float): Harga item baru.

        Raises:
        TypeError: Apabila format harga item yang baru salah.
        """
        
        for item in self.items:
            if item[0] == item_name:
                item[2] = new_price
    
        if type(new_price) != float:
           raise TypeError("Format harga item yang anda masukkan salah (misalnya: 25000.00).")

    def delete_item(self, item_name):
        """
        Menghapus item dari list items.
        
        Parameter:
        item_name (str): Nama item yang ingin dihapus.
        
        Raises:
        TypeError: Apabila format nama item baru salah.
        """
        
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)

        if type(item_name) != str:
            raise TypeError("Format nama item yang anda masukkan salah (gunakan tanda petik sebelum dan sesudah nama item).")
    
    def reset_transaction(self):
        """
        Method ini berfungsi untuk mengosongkan atau menghapus semua item dari keranjang belanja. Method ini memiliki output print text "Keranjang belanja telah dikosongkan!."
        """
        
        self.items = []
        print("Keranjang belanja telah dikosongkan!")
    
    def hitung_total_price(self):
        """
        Method ini berfungsi untuk menghitung harga total dan diskon yang didapatkan dari seluruh item yang telah ditambahkan ke dalam list items.       
 
        """
       
        total_price = 0.0
        
        for item in self.items:
            self.total_price += item[1] * item [2]
            
        #Menghitung diskon yang didapatkan
        discount = 0.0
        
        if self.total_price > 500_000:
            self.discount = 0.1
        elif self.total_price > 300_000:
            self.discount = 0.08
        elif self.total_price > 200_000:
            self.discount = 0.05

        print("Total harga sebelum diskon: ", self.total_price)
        print("Diskon yang didapatkan: ", self.total_price * self.discount)
        print("Total harga setelah diskon: ", self.total_price - (self.total_price * self.discount))

        return self.total_price
    
    def check_order(self):
        """
        Method ini berfungsi untuk menampilkan semua item yang telah ditambahkan pada list items dalam bentuk tabel.
        """
        
        order_table = []

        for index, item in enumerate(self.items):
            order_table.append([index+1, item[0], item[1], item[2], item[1] * item[2]])

        headers = ["No.", "Item", "Quantity", "Price", "Total Price"]

        
        #Print Tablenya
        print("Check your shopping cart:")
        print("")
        print(tabulate(order_table, headers, tablefmt='fancy_grid'))
        print("")
        print("Total harga sebelum diskon: ", self.total_price)
        print("Diskon yang didapatkan: ", self.total_price * self.discount)
        print("Total harga setelah diskon: ", self.total_price - (self.total_price * self.discount))
       
