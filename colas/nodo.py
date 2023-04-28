class Nodo:
    _elem: int
    _sig: 'Nodo'

    def __init__(self, elem: int = 0) -> None:
        self._elem = elem
        self._sig = None
