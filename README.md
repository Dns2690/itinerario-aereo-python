Objetivo General
Desarrollar una aplicación de consola interactiva en Python que permita gestionar una secuencia dinámica de conexiones aéreas (rutas), utilizando la Lista Doblemente Enlazada como estructura de datos fundamental para la manipulación y optimización del itinerario.
Estructura de Datos Obligatoria
1.	Clase NodoRuta: Cada nodo debe representar una conexión aérea (un segmento de la ruta) y contener:
o	origen: El código o nombre de la ciudad de salida (string).
o	destino: El código o nombre de la ciudad de llegada (string).
o	duracion: Duración del vuelo en horas (float o int).
o	siguiente: Puntero al siguiente nodo (conexión) en la lista.
o	anterior: Puntero al nodo anterior (conexión) en la lista.
2.	Clase Itinerario: Debe gestionar la lista completa de conexiones, incluyendo referencias a la cabeza y la cola si es necesario, y contener todos los métodos de manipulación.
Requisitos Funcionales (Menú de Opciones)
La aplicación debe presentar al usuario un menú de consola con las siguientes opciones.
1.	Añadir Conexión:
o	Pide al usuario Origen, Destino y Duración del vuelo.
o	La nueva conexión se inserta al final del itinerario.
2.	Ver Itinerario Completo:
o	Recorre la lista de inicio a fin.
o	Muestra el índice (secuencia del vuelo 1, 2, 3...), el Origen, el Destino y la Duración.
o	Calcula y muestra la Duración Total del itinerario.
o	Si la lista está vacía, muestra un mensaje apropiado.
3.	Eliminar Conexión (Modificación):
o	Pide al usuario el número de índice de la conexión a eliminar.
o	El sistema debe buscar y eliminar el nodo de la lista, simulando la cancelación de ese segmento de vuelo.
o	Se debe manejar el caso en que el índice no exista.
4.	Salir:
o	Termina la ejecución del programa.
Consideraciones Adicionales
•	Manejo de Errores: La aplicación debe manejar entradas inválidas (texto donde se espera un número, opciones de menú inexistentes).
•	Comentarios: El código debe estar exhaustivamente comentado para explicar la lógica de la Lista Doble y cada función.

 
Estructuras Fundamentales de la Lista Doblemente Enlazada 
El proyecto se basa en dos clases principales que conforman la Lista Doble:
1. Clase NodoRuta
Este es el ladrillo fundamental de la estructura de datos. Cada instancia de esta clase representa un segmento de vuelo (una conexión) dentro del itinerario.
Atributo	Propósito	Desafío para el Estudiante
origen, destino, duracion	Almacenan los datos del vuelo.	El manejo de la conversión a float para la duración debe incluir manejo de errores (try/except).
siguiente	Puntero hacia el próximo vuelo en la secuencia (hacia la cola).	Es esencial para el recorrido y el re-enlazado.
anterior	Puntero hacia el vuelo previo en la secuencia (hacia la cabeza).	Permite el movimiento hacia atrás (optimización 'Arriba') y simplifica la eliminación.
2. Clase Itinerario
Esta clase administra el conjunto de NodoRuta. Es el contenedor lógico que implementa todas las operaciones.
Atributo	Propósito	Concepto de Lista Doble
cabeza (head)	Referencia al primer nodo del itinerario.	Define el inicio de la ruta.
cola (tail)	Referencia al último nodo del itinerario.	Define el final de la ruta y es clave para la inserción rápida (Opción 1).
longitud	Contador que rastrea la cantidad de conexiones.	Útil para validar índices (obtener_nodo_por_indice) y mostrar mensajes de lista vacía.
 
Explicación Detallada de las Opciones del Menú
Las opciones del menú representan las manipulaciones que los estudiantes deben implementar en la Lista Doble, además de la crucial validación de continuidad de la ruta aérea (la lógica del negocio).
Opción 1: Añadir Conexión (Método insertar_al_final)
Lógica de la Lista Doble	Lógica de Negocio
El nuevo nodo siempre se conecta después de la cola actual. Se actualizan los punteros de la antigua cola (siguiente) y del nuevo nodo (anterior). El nuevo nodo pasa a ser la nueva cola de la lista.	Validación Crítica: Se debe verificar que el origen del nuevo nodo sea exactamente igual al destino de la cola actual. Si no coinciden (ej: BOG  MIA, pero se intenta añadir GDL  JFK), la inserción debe ser rechazada.



Opción 2: Ver Itinerario Completo (Método mostrar_itinerario)
Lógica de la Lista Doble	Lógica de Negocio
Implementa un simple recorrido (traversal). Comienza en la cabeza y avanza hasta que el puntero actual es None.	Se utiliza un acumulador para calcular la Duración Total del viaje mientras se recorre la lista. También se muestra el índice secuencial de cada vuelo (1, 2, 3...) al usuario.

Opción 3: Eliminar Conexión (Método eliminar_conexion)
Lógica de la Lista Doble	Lógica de Negocio 
Implica tres casos: eliminar la cabeza, la cola, o un nodo intermedio. En el caso intermedio, es necesario re-enlazar los punteros: el anterior.siguiente debe apuntar al siguiente, y el siguiente.anterior debe apuntar al anterior.	Validación de Continuidad: A->B->C Antes de eliminar el nodo 'B', se debe revisar si su vecino anterior 'A' se conecta correctamente con su vecino siguiente 'C'. Es decir, si A.destino coincide con C.origen. Si la eliminación de 'B' rompe esta conexión, la eliminación se rechaza para mantener un itinerario funcional.
 

<img width="468" height="590" alt="image" src="https://github.com/user-attachments/assets/a0db275d-8a30-441e-a84d-64a35479c58c" />
