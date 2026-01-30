from product import Product

class ProductManager:
    
    def __init__(self):
        self.products = [] #Prazna lista kao atribut
        
    def add_product(self, product):
        if isinstance(product, Product): #Python funkcija koja proverava da li je objekat importovan
            self.products.append(product) #Dodavanje proizvoda u listu
        else:
            print("Greška: Možete uneti samo objekte klase Product.")
            
    def display_all_products(self):
        for p in self.products:
            p.display_info() #Prikaz svih proizvoda
            
    def total_value(self):
        try:
            return sum(p.price * p.quantity for p in self.products)  #Prikaz ukupne vrednosti proizvoda
        except TypeError:
            print("Greška: Neki proizvodi imaju neispravnu cenu ili količinu.")
        #try except blok kao zaštita od pucanja programa ukoliko je neki podatak pogrešan
        
    def remove_product(self, name):
        pocetni_broj = len(self.products) #Dužina liste postaje vrednost promenljive
        self.products = [p for p in self.products if p.name != name] #Brisanje proizvoda
        
        if len(self.products) == pocetni_broj: #Upoređivanje dužine liste nakon brisanja i ispis prema stanju
            print(f"Obaveštenje: Proizvod '{name}' nije pronađen.")
        else:
            print(f"Proizvod: '{name}' je uspešno uklonjen.")        
    
        
    