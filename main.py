# Import module cashier.py
import cashier

# Instance for test case
trnsct_123 = cashier.Transaction()

# Test Case 1
print("Test Case 1")

trnsct_123.add_item(["Ayam Goreng", 2, 20000.00])
trnsct_123.add_item(["Pasta Gigi", 3, 15000.00])
print("Item yang dibeli adalah: ", trnsct_123.items)
print(" ")

# Test Case 2
print("Test Case 2")

trnsct_123.delete_item("Pasta Gigi")
print("Item yang dibeli setelah didelete : ", trnsct_123.items)
print(" ")

# Test Case 3
print("Test Case 3")

trnsct_123.reset_transaction()
print(" ")

# Test Case 4
print("Test Case 4")

trnsct_123.add_item(["Ayam goreng", 2, 20000.00])
trnsct_123.add_item(["Pasta gigi", 3, 15000.00])
trnsct_123.add_item(["Mainan mobil", 1, 200000.00])
trnsct_123.add_item(["Indomie :D", 5, 3000.00])
print(trnsct_123.items)
print(" ")

trnsct_123.hitung_total_price()
print(" ")

trnsct_123.check_order()
