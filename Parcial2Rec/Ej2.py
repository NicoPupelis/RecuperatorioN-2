from grafoparcial import Grafo
GrafoStarWars=Grafo(dirigido=False)

GrafoStarWars.insert_vertice("Darth Vader")
GrafoStarWars.insert_vertice("Leia")
GrafoStarWars.insert_vertice("BB-8")
GrafoStarWars.insert_vertice("Chewbacca")
GrafoStarWars.insert_vertice("Han")
GrafoStarWars.insert_vertice("Luke Skywalker")
GrafoStarWars.insert_vertice("Yoda")
GrafoStarWars.insert_vertice("C-3PO")
GrafoStarWars.insert_vertice("Kylo Ren")
GrafoStarWars.insert_vertice("Boba Fett")
GrafoStarWars.insert_vertice("R2-D2")
GrafoStarWars.insert_vertice("Rey")

GrafoStarWars.insert_arist("C-3PO","Leia Organa",4)
GrafoStarWars.insert_arist("Luke Skywalker","Han",6)
GrafoStarWars.insert_arist("Chewbacca","Han",9)
GrafoStarWars.insert_arist("Darth Vader","Han",5)
GrafoStarWars.insert_arist("Boba Fett","Rey",13)
GrafoStarWars.insert_arist("C-3PO","R2-D2",18)
GrafoStarWars.insert_arist("Leia","BB-8",10)
GrafoStarWars.insert_arist("Han","Rey",7)
GrafoStarWars.insert_arist("Yoda","Chewbacca",7)
GrafoStarWars.insert_arist("Rey","Chewbacca",7)

GrafoStarWars.barrido()

# B) 

bosque,encontrado = GrafoStarWars.kruskal_yoda()

for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

if encontrado == True:
    print('Se encontro a Yoda')
else:
    print('No se encontro a Yoda')

print ('')
# C) 
print('Numero max episodios')
GrafoStarWars.MaxEpBarrido1()


# D) Encontrar el camino más corto de Yoda a Rey
ori = 'Yoda'
des = 'Rey'

print('Este es el camino mas corto')
origen = GrafoStarWars.search_vertice(ori)
destino = GrafoStarWars.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(GrafoStarWars.has_path(ori, des)):
        camino_mas_corto = GrafoStarWars.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value[2]

