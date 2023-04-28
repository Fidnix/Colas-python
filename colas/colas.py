from typing import Union
from colas.nodo import Nodo

class Cola:
    _size: int
    _cabeza: Nodo
    _cola: Nodo

    def __init__(self, elems: Union[int, tuple[int]] = None) -> None:
        if(elems == None):
            self._size = 0
            self._cabeza = None
            self._cola = None
            return
        if(type(elems) == int):
            elems = list([elems])
        self._cabeza = Nodo(elems[0])
        current_node = self._cabeza
        for elem in elems[1:]:
            current_node._sig = Nodo(elem)
            current_node = current_node._sig
        self._cola = current_node
        self._size = len(elems)

    def empty_queue(self) -> bool:
        return self._size == 0
    
    def push(self, elems: Union[int, tuple[int]] = 0) -> None:
        if(self.empty_queue()):
            self._size = 1
            self._cabeza = Nodo(elems)
            self._cola = self._cabeza
            return
        if(type(elems) == int):
            elems = list([elems])
        current_node = self._cola
        for elem in elems:
            current_node._sig = Nodo(elem)
            current_node = current_node._sig
        self._cola = current_node
        self._size += len(elems)
    
    def pop(self, n: int = 1) -> tuple[int]:
        if(self.empty_queue()):
            return
        if(n < 1 or n > self._size):
            raise Exception('Error: Nmms')
        aux_list: list[int] = []
        current_node = self._cabeza
        for _ in range(0, n):
            aux_list += [current_node._elem]
            current_node = current_node._sig
        self._cabeza = current_node
        if(n == self._size):
            self._cola = None
        self._size -= n
        return tuple(aux_list)

    def __str__(self):
        output = ''
        current_node = self._cabeza
        for _ in range(0, self._size):
            output += f'{current_node._elem} '
            current_node = current_node._sig
        return output