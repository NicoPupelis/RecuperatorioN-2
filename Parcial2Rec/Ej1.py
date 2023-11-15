
from arbol_binario import BinaryTree

class pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre=nombre
        self.numero=numero
        self.tipo=tipo
        
    def __str__(self):
        return f'{self.nombre} {self.numero} {self.tipo}'

arbolnombre=BinaryTree()
arbolnumero=BinaryTree()
arboltipo=BinaryTree()


pk1 = pokemon("Magnemite", 986, "Eléctrico")
pk2 = pokemon("Metapod", 876, "Planta")
pk3 = pokemon("Ponyta", 512, "Fuego")
pk4 = pokemon("Squirtle", 14, "Agua")
pk5 = pokemon("Jigglypuff", 534, "Normal")
pk6 = pokemon("Golduck", 134, "Agua")
pk7 = pokemon("Mewtwo", 150, "Psíquico")
pk8 = pokemon("Gyarados", 654, "Agua")
pk9 = pokemon("Jolteon", 432, "Eléctrico")
pk10 = pokemon("Lycanroc", 543, "Roca")
pk11 = pokemon("Tyrantrum",321, "Dragón")
pk12 = pokemon("Bulbasur" ,325, "Planta")

pk = [pk1,pk2,pk3,pk4,pk5,pk6,pk7,pk8,pk9,pk10,pk11,pk12]

for i in pk:
    arbolnombre.insert_node(i.nombre,(i.numero,i.tipo))
    arbolnumero.insert_node(i.numero,(i.nombre,i.tipo))
    arboltipo.insert_node(i.tipo,(i.nombre,i.numero))



# B)

pos1=arbolnumero.search(150)

if pos1 is not None:
     print(pos1.value,pos1.other_values)

arbolnombre.search_by_coincidence("Bul")


# C)

Listatosostipos= ['Agua','Fuego','Planta','Eléctrico']

for i in Listatosostipos:
    poke=arboltipo.search(i)
    print(poke.other_values,i)



# D)

print('Ascendente')

arbolnombre.inorden()

print('-----------------')

arbolnumero.inorden()

print('-----------------')

print('Por por nivel')

arbolnombre.by_level()

# E) 

J=arbolnombre.search('Jolteon')
print(J.value,J.other_values)
L=arbolnombre.search('Lycanroc')
print(L.value,L.other_values)
T=arbolnombre.search('Tyrantrum')
print(T.value,T.other_values)


# F) 
print('Electricos hay un total de:')
print(arboltipo.contar('Eléctrico'))

print('Acero hay un total de:')
print(arboltipo.contar('Acero'))



    
