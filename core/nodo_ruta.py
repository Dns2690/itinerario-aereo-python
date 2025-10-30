# ================================================
# Clase NodoRuta
# Representa una conexión aérea dentro del itinerario.
# Cada nodo tiene referencias al anterior y siguiente,
# lo que permite recorrer la lista en ambos sentidos.
# ================================================

class NodoRuta:
    def __init__(self, origen: str, destino: str, duracion: float):
        # Inicializa los atributos de la ruta:
        # - origen: ciudad de salida
        # - destino: ciudad de llegada
        # - duracion: duración del vuelo en horas
        # - siguiente: referencia al siguiente nodo (None por defecto)
        # - anterior: referencia al nodo anterior (None por defecto)
        pass

    def __repr__(self):
        # Retorna una representación legible del nodo (por ejemplo "SJO->LAX (5h)")
        # Solo para propósitos de depuración o impresión.
        pass