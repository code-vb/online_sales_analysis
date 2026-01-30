from product import Product
from product_manager import ProductManager

manager = ProductManager() #Kreiranje instance
p1 = Product("Laptop", 50000, 5) #Kreiranje proizvoda p1
p2 = Product("Miš", 2000, 10) #Kreiranje proizvoda p2
manager.add_product(p1) #Pozivanje funkcije
manager.add_product(p2)

manager.display_all_products() #Pozivanje funkcije
print(f"Ukupna vrednost: {manager.total_value()} dinara.")