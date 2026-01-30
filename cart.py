from product import Product

class Cart:
    def __init__(self):
        self.cart_items = [] #Atribut = Prazna lista za objekte klase Product

    def add_to_cart(self, product):
        self.cart_items.append(product) #Dodavanje proizvoda u listu
        print(f"Dodato u korpu: {product.name}")
        
    def calculate_total(self):
        return sum(item.price for item in self.cart_items) #Sabiranje cena proizvoda koji se nalaze u listi        
    
    def display_cart(self):
        print("\n---- SADRŽAJ KORPE ----")
        for item in self.cart_items:
            print(f"- {item.name} : {item.price}")
        print()
        print(f"Ukupan iznos za naplatu: {self.calculate_total()}")
        print()