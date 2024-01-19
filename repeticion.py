'''Practica 1'''
class Asteriscos:
    '''Clase que imprime asteriscos'''
    numero_lineas = 0

    def __init__(self, cantidad):
        self.numero_lineas = cantidad

    def imprimir(self):
        '''Imprime asteriscos'''
        for i in range(1, self.numero_lineas + 1):
            cadena = ""
            for j in range(i):
                cadena += "*"
            print(cadena)

def main():
    '''Función principal'''
    num_lineas = int(input("Ingrese el número de líneas: "))
    asteriscos = Asteriscos(num_lineas)
    asteriscos.imprimir()

if __name__ == '__main__':
    main()
