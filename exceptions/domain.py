# ================================================
# Excepciones personalizadas del dominio.
# Sirven para manejar errores de negocio y evitar
# usar mensajes genéricos del sistema.
# ================================================

class ItinerarioError(Exception):
    # Clase base para todas las excepciones del itinerario.
    pass

class ContinuidadError(ItinerarioError):
    # Error que se lanza cuando se rompe la secuencia de continuidad
    # (ejemplo: insertar o eliminar una ruta que rompe el enlace entre destinos).
    pass

class IndiceFueraDeRangoError(ItinerarioError):
    # Error cuando el usuario intenta acceder o eliminar
    # una conexión con un índice inexistente.
    pass

class EntradaInvalidaError(ItinerarioError):
    # Error cuando se ingresa un tipo de dato incorrecto
    # o un valor fuera de rango (ejemplo: texto en lugar de número).
    pass