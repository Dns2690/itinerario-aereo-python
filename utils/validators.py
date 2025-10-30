# ================================================
# Funciones de validación de entrada
# Aseguran que los datos ingresados por el usuario
# sean del tipo y formato correcto antes de operar.
# ================================================

def to_non_empty_str(texto: str):
    # Valida que el texto no esté vacío ni contenga solo espacios.
    # Retorna el texto limpio (strip) o lanza error/mensaje si está vacío.
    pass

def to_positive_float(valor: str):
    # Intenta convertir el texto a número decimal (float).
    # Si falla, lanza error o muestra mensaje.
    # Además valida que el valor sea mayor a cero.
    pass

def to_positive_int(valor: str):
    # Intenta convertir el texto a entero.
    # Si falla o es menor que 1, lanza error o muestra mensaje.
    pass