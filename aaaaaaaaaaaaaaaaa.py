import random

figus_total = 12
repeticiones = 1000
tengo_figus = 45

def cuantas_figus(figuritas):
    album = [0]*figuritas
    contador = 0
    while sum(album)<figuritas:
        figu = random.randint(0,figuritas-1)
        contador = contador+1
        album[figu] = 1
    return(contador)

def lista_repes(repes,figuritas): 
    lista=[]
    while len(lista)<repes:
        album_completo = cuantas_figus(figuritas)
        lista.append(album_completo)
    return lista

def promedio_lista(lista,repes):
    promedio = sum(lista)/repes
    return promedio

lista1 = lista_repes(repeticiones, figus_total)
promedio1 = promedio_lista(lista1,repeticiones)
print("El promedio de figuritas necesarias para completar un álbum de " + str(figus_total) + " figuritas es: " + str(promedio1))

def chances_completar_album(lista, puedo_comprar):
    contador_2 = 0
    vale_11 = 0
    while contador_2 < len(lista):
        if lista[contador_2] <= puedo_comprar:
            vale_11 = vale_11 + 1
        contador_2 = contador_2 +1
    return vale_11

chances = chances_completar_album(lista1, tengo_figus)/len(lista1)
print("Tengo " + str(chances) + " chances de completar un álbum de " + str(figus_total) + " figuritas comprando " + str(tengo_figus) + " figuritas.")
