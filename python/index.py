class Clothes:
    def __init__(self, id, size, price, color):
        self.id = id
        self.size = size
        self.price = price
        self.color = color

    def display_info(self):
        print("ID:", self.id)
        print("Size:", self.size)
        print("Price:", self.price)
        print("Color:", self.color)

cuts = {'pants': 1, 'shirts': 2, 'shorts': 3, 'hoodie': 4, 'dress': 5, 'underpants': 6}
colors = {'black': 0, 'red': 1, 'green': 2, 'white': 3, 'yellow': 4, 'gray': 5}

def generate_id(cut, color):
    return str(cuts[cut]) + str(colors[color])

newpant = Clothes(generate_id('pants', 'black'), "XX", 485, 'black')

# Função para mostrar informações da peça de roupa
def show_clothes_info(clothes):
    clothes.display_info()

# Chamar a função para mostrar informações da peça de roupa
show_clothes_info(newpant)