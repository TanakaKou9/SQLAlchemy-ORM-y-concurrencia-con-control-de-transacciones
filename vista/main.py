from controlador.operaciones import agregar_libro, listar_libros
import controlador.operaciones as operaciones

def mostrar_menu():
    print("\n=== GESTOR DE LIBROS Y CATEGORÍAS ===")
    print("1. Listar categorías")
    print("2. Agregar categoría")
    print("3. Eliminar categoría")
    print("4. Listar libros")
    print("5. Agregar libro")
    print("6. Buscar libros por categoría")
    print("7. Actualizar precio de un libro")
    print("8. Eliminar libro")
    print("9. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            categorias = operaciones.listar_categorias()
            if not categorias:
                print("No hay categorías registradas.")
            else:
                for c in categorias:
                    print(c)

        elif opcion == "2":
            nombre = input("Nombre de la categoría: ")
            operaciones.agregar_categoria(nombre)

        elif opcion == "3":
            nombre = input("Nombre de la categoría a eliminar: ")
            operaciones.eliminar_categoria(nombre)

        elif opcion == "4":
            libros = operaciones.listar_libros()
            if not libros:
                print("No hay libros registrados.")
            else:
                for l in libros:
                    print(l)

        elif opcion == "5":
            categorias = operaciones.listar_categorias()
            if not categorias:
                print("Primero debe registrar una categoría.")
                continue
            for c in categorias:
                print(f"{c.id} - {c.nombre}")

            try:
                categoria_id = int(input("ID de la categoría: "))
                titulo = input("Título del libro: ")
                autor = input("Autor: ")
                precio = float(input("Precio: "))
                operaciones.agregar_libro(titulo, autor, precio, categoria_id)
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

        elif opcion == "6":
            nombre_cat = input("Nombre de la categoría: ")
            libros = operaciones.buscar_por_categoria(nombre_cat)
            if not libros:
                print("No hay libros en esa categoría.")
            else:
                for l in libros:
                    print(l)

        elif opcion == "7":
            titulo = input("Título del libro: ")
            try:
                nuevo_precio = float(input("Nuevo precio: "))
                operaciones.actualizar_precio(titulo, nuevo_precio)
            except ValueError:
                print("Precio inválido.")

        elif opcion == "8":
            titulo = input("Título del libro a eliminar: ")
            operaciones.eliminar_libro(titulo)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main()
