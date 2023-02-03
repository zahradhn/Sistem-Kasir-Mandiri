# FINALLLLLLLL

# Class
class Transaction:
    
    items = []
    total_price = 0.0
    discount = 0.0
    
    def __init__(self):
        #Inisialitasi atribut pada class Transaction
        self.items = []
        self.total_price = 0.0
        self.discount = 0.0
    
    def add_item(self, item):
        #Menambahkan transaksi ke dalam list "items" yang berisi nama item [0], jumlah item [1], dan harga per item [2].
        self.items.append(item)
    
    def update_item_name(self, item_name, new_item):
        #Mengganti nama item yang sudah ditambahkan ke dalam list "items"
        for item in self.items:
            if item == item_name:
                item[0] = new_item
    
    def update_item_quantity(self, item_name, new_quantity):
        #blabla
        for item in self.items:
            if item[0] == item_name:
                item[1] = new_quantity
    
    def update_item_price(self, item_name, new_price):
        #blabla
        for item in self.items:
            if item[0] == self.item_name:
                item[3] = new_price
    
    def delete_item(self, item_name):
        #Delete item
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
    
    def reset_transaction(self):
        #Reset transaksi
        self.items = []
        print("Cart is empty!")
    
    def hitung_total_price(self):
        
        #Menghitung total transaksi sebelum diskon
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
            
        return self.total_price
    
    def check_order(self):
        #Tabel pemesanan
        
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
       