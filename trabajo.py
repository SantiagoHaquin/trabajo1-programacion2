class Libro:
    def __init__(self, codigo, titulo, autor, ejemplares_disponibles, ejemplares_prestados):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles
        self.ejemplares_prestados = ejemplares_prestados
        
        
libros = []

libro_registrado = Libro(codigo=1, titulo="Python para principiantes", autor="John Doe", ejemplares_disponibles=5, ejemplares_prestados=0)

libros = [libro_registrado]

def buscar_libro_por_codigo(codigo):
    for libro in libros:
        if libro.codigo == codigo:
            return libro
    return None

def gestionar_prestamo():
    codigo = input("Ingrese el código del libro: ")
    libro = buscar_libro_por_codigo(int(codigo))
    if libro:
        if libro.ejemplares_disponibles > 0:
            print(f"Autor: {libro.autor}")
            print(f"Título: {libro.titulo}")
            print(f"Ejemplares disponibles: {libro.ejemplares_disponibles}")
            confirmar = input("¿Desea confirmar el préstamo? (S/N): ").strip().lower()
            if confirmar == 's':
                libro.ejemplares_disponibles -= 1
                libro.ejemplares_prestados += 1
                print("Préstamo confirmado.")
            else:
                print("Préstamo cancelado.")
        else:
            print("No quedan ejemplares disponibles para prestar.")
    else:
        print("Error: El libro no existe.")

def gestionar_devolucion():
    codigo = input("Ingrese el código del libro: ")
    libro = buscar_libro_por_codigo(int(codigo))
    if libro:
        if libro.ejemplares_prestados > 0:
            print(f"Confirmar devolución de '{libro.titulo}'")
            confirmar = input("¿Desea confirmar la devolución? (S/N): ").strip().lower()
            if confirmar == 's':
                libro.ejemplares_prestados -= 1
                libro.ejemplares_disponibles += 1
                print("Devolución confirmada.")
            else:
                print("Devolución cancelada.")
        else:
            print("Error: El libro no tiene ejemplares prestados.")
    else:
        print("Error: El libro no existe.")


def registrar_nuevo_libro():
    titulo = input("Ingrese el título del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    ejemplares_disponibles = int(input("Ingrese la cantidad de ejemplares disponibles: "))
    codigo = len(libros) + 1
    libro = Libro(codigo, titulo, autor, ejemplares_disponibles, 0)
    libros.append(libro)
    print(f"Libro registrado con éxito. Código: {codigo}")

def eliminar_ejemplar():
    codigo = input("Ingrese el código del libro: ")
    libro = buscar_libro_por_codigo(int(codigo))
    if libro:
        cantidad = int(input(f"Ingrese la cantidad de ejemplares a eliminar de '{libro.titulo}': "))
        if cantidad > 0 and cantidad <= libro.ejemplares_disponibles:
            libro.ejemplares_disponibles -= cantidad
            print("Ejemplares eliminados con éxito.")
        else:
            print("Error: Cantidad inválida o excede la cantidad de ejemplares disponibles.")
    else:
        print("Error: El libro no existe.")

def mostrar_ejemplares_prestados():
    for libro in libros:
        if libro.ejemplares_prestados > 0:
            print(f"'{libro.titulo}': {libro.ejemplares_prestados} ejemplar(es) prestado(s).")
        else:print("No hay ejemplares prestados.")

while True:
    print("\nMenú:")
    print("1) Gestionar Préstamo")
    print("2) Gestionar Devolución")
    print("3) Registrar Nuevo Libro")
    print("4) Eliminar Ejemplar")
    print("5) Mostrar Ejemplares Prestados")
    print("6) Salida")

    opcion = input("Seleccione una opción (1-6): ").strip()

    if opcion == '1':
        gestionar_prestamo()
    elif opcion == '2':
        gestionar_devolucion()
    elif opcion == '3':
        registrar_nuevo_libro()
    elif opcion == '4':
        eliminar_ejemplar()
    elif opcion == '5':
        mostrar_ejemplares_prestados()
    elif opcion == '6':
        print("--------------- Gracias por utilizar el sistema. ¡Hasta luego! ---------------")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1-6).")
