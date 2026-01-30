import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager() #Kreiranje instance
p1 = Product("Laptop", 50000, 10) #Kreiranje proizvoda p1
p2 = Product("Miš", 2000, 10) #Kreiranje proizvoda p2
p3 = Product("TV", 60000, 3)
p4 = Product("Slušalice", 3000, 6)
p5 = Product("USB kabl", 1000, 10)

manager.add_product(p1) #Pozivanje funkcije
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)
manager.add_product(p5)

print("\n---- TESTIRANJE BRISANJA ----")
manager.remove_product("Miš") #Pozivanje funkcije

print("\n---- DODATI PROIZVODI ----")

moja_korpa = Cart() #Instanca klase Cart

nasumicni_proizvodi = random.sample(manager.products, 3) #Python funkcija random.sample() bira nasumična tri proizvoda
for p in nasumicni_proizvodi:
    moja_korpa.add_to_cart(p) #Ddodavanje u korpu

moja_korpa.display_cart() #Pozivanje funkcije 
manager.display_all_products() #Pozivanje funkcije

print()
print(f"Ukupna vrednost: {manager.total_value()} dinara.")
print()