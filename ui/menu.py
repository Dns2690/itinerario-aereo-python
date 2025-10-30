# ================================================
# Interfaz de usuario por consola
# Presenta el menú principal y controla las opciones.
# Se comunica con la clase Itinerario.
# ================================================

from core.itinerario import Itinerario

def loop_menu():
    # Bucle principal del programa.
    # Muestra las opciones y espera la selección del usuario.
    # 1) Añadir conexión
    # 2) Ver itinerario completo
    # 3) Eliminar conexión
    # 4) Salir
    # Llama a los manejadores específicos según la opción.
    pass

def manejador_insertar(itinerario: Itinerario):
    # Pide al usuario:
    # - Origen
    # - Destino
    # - Duración
    # Valida las entradas usando utils.validators.
    # Llama a insertar_al_final() del itinerario.
    # Muestra un mensaje de éxito o error.
    pass

def manejador_mostrar(itinerario: Itinerario):
    # Llama a mostrar_itinerario().
    # Si hay rutas, imprime cada conexión y la duración total.
    # Si está vacío, muestra mensaje "No hay conexiones registradas".
    pass

def manejador_eliminar(itinerario: Itinerario):
    # Pide el índice al usuario (1, 2, 3...).
    # Valida la entrada y llama a eliminar_por_indice().
    # Muestra un mensaje de confirmación o error si no existe el índice.
    pass