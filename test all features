import Transaction

# TEST CASE: ALL FEATURES

transaction_1 = Transaction()

# FEATURE: ADD ITEM 
print("Step 1: Add item")
transaction_1.add_item(["Yakult", 2, 9800.00])
transaction_1.add_item(["Minyak 2L", 1, 49000.00])
transaction_1.add_item(["Ayam broiler", 2, 32000.00])
transaction_1.add_item(["Telur 12 pcs", 2, 24900.00])
transaction_1.add_item(["Pakchoy", 2, 9900.00])
transaction_1.add_item(["Cabe rawit", 2, 12000.00])
transaction_1.add_item(["Kopi Good Day", 3, 22000.00])
transaction_1.add_item(["Aqua galon isi ulang", 2, 19000.00])

print("Item yang dibeli adalah: ", transaction_1.items)
print(" ")

# FEATURE: UPDATE ITEM NAME

print("Step 2: Update item name")
transaction_1.update_item_name("Pakchoy", "Brokoli")

print("Item yang dibeli adalah: ", transaction_1.items)
print(" ")

# FEATURE: UPDATE ITEM QUANTITY
print("Step 3: Update item quantity")
transaction_1.update_item_quantity("Brokoli", 1)

print("Item yang dibeli adalah: ", transaction_1.items)
print(" ")

# FEATURE: UPDATE ITEM PRICE
print("Step 4: Update item price")
transaction_1.update_item_price("Brokoli", 15900.00)

print("Item yang dibeli adalah: ", transaction_1.items)
print(" ")

# FEATURE: DELETE ITEM
print("Step 5: Delete item")
transaction_1.delete_item("Brokoli")

print("Item yang dibeli adalah: ", transaction_1.items)
print(" ")

# FEATURE: HITUNG HARGA
print("Step 6: Hitung total harga")
transaction_1.hitung_total_price()
print(" ")

# FEATURE: CHECK ORDER
print("Step 7: Check order")
transaction_1.check_order()
