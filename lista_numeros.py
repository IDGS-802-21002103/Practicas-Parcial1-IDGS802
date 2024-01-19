'''Practica 1'''
class Ordenar:
    '''Clase que ordena una lista de números'''
    lista = []

    def __init__(self, lista):
        self.lista = lista

    def ordenar_menor_mayor(self):
        '''Ordena los números de menor a mayor'''
        lista_ordenada = []
        for numero in self.lista:
            try:
                lista_ordenada.index(numero)
            except ValueError:
                lista_ordenada.append(numero)
        return sorted(lista_ordenada)

    def ordenar_pares(self):
        '''Ordena los números pares de la lista'''
        lista_pares = []
        for numero in self.lista:
            if numero % 2 == 0:
                try:
                    en_lista = lista_pares.index(numero)
                    if en_lista == -1:
                        lista_pares.append(numero)
                except ValueError:
                    lista_pares.append(numero)
        return sorted(lista_pares)

    def ordenar_impares(self):
        '''Ordena los números impares de la lista'''
        lista_impares = []
        for numero in self.lista:
            if numero % 2 != 0:
                try:
                    en_lista = lista_impares.index(numero)
                    if en_lista == -1:
                        lista_impares.append(numero)
                except ValueError:
                    lista_impares.append(numero)
        return sorted(lista_impares)

def main():
    '''Función principal'''
    cantidad_numeros = int(input("Ingrese la cantidad de números: "))
    lista_numeros = []
    contador = 0
    while contador < cantidad_numeros:
        numero = int(input("Ingrese el número: "))
        lista_numeros.append(numero)
        contador += 1
    print(lista_numeros)
    ordenar = Ordenar(lista_numeros)

    print("Ordenados")
    print(ordenar.ordenar_menor_mayor())
    print("Pares")
    print(ordenar.ordenar_pares())
    print("Impares")
    print(ordenar.ordenar_impares())

if __name__ == '__main__':
    main()
