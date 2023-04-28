from colas import Cola

def main():
    cola = Cola([2,3,4,5])
    print(cola)
    cola.push(3)
    print(cola)
    cola.push([5,6])
    print(cola)
    val_eliminado = cola.pop()
    print(f'{cola}, valor eliminado: {val_eliminado}')
    val_eliminado = cola.pop(4)
    print(f'{cola}, valores eliminados: {val_eliminado}')
    cola.push([10,11,12])
    print(cola)

if __name__ == '__main__':
    main()
