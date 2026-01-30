class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def display_info(self):
        print(f"Proizvod: {self.name}, Cena: {self.price} din., Količina: {self.quantity} kom.")
        #Metod za prikazivanje informacija o proizvodu
        
    def update_quantity(self, amount):
        self.quantity += amount
        #Metod za ažuriranje količine proizvoda