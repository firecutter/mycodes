class ClothingItem:
    def __init__(self, size, name, price, color):
        self.size = size
        self.name = name
        self.price = price
        self.color = color 
    
    def infos(self):
        print(f"size:  {self.size}")
        print(f"color: {self.color}")
        print(f"name:  {self.name}")
        print(f"price: {self.price}")

    def __str__(self):
        return f"{self.name} - {self.color} - Size {self.size} - ${self.price}"

class Shirt(ClothingItem):
    def infos(self):
        print("-" * 25)
        print("shirt")
        super().infos()

class Pants(ClothingItem):
    def infos(self):
        print("-" * 25)
        print("pants")
        super().infos()

class Shorts(ClothingItem):
    def infos(self):
        print("-" * 25)
        print("shorts")
        super().infos()

# Exemplo de uso:
shirt1 = Shirt("G", "storm", 145, "pillowhite")
shirt1.infos()

pants1 = Pants(45, "storm", 265, "greeneva")
pants1.infos()

shorts1 = Shorts(15, "airfreedom", 89, "blackout")
shorts1.infos()

# Para imprimir a instância de forma mais amigável:
print(shirt1)
print(pants1)