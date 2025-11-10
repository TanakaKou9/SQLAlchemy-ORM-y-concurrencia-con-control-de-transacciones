from typing import Iterable
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, update, delete
from modelo.Libro import Libro, SessionLocal
from modelo.Categoria import Categoria



def agregar_categoria(nombre: str) -> None:
    """Inserta una nueva categoría."""
    session = SessionLocal()
    try:
        nueva = Categoria(nombre=nombre)
        session.add(nueva)
        session.commit()
        print(f"Categoría agregada: {nueva}")
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al agregar categoría. Rollback ejecutado.")
        print("Detalle:", e)
    finally:
        session.close()


def listar_categorias() -> Iterable[Categoria]:
 
    session = SessionLocal()
    try:
        stmt = select(Categoria).order_by(Categoria.id.asc())
        return session.scalars(stmt).all()
    finally:
        session.close()


def eliminar_categoria(nombre: str) -> int:
    """Elimina una categoría (y sus libros asociados por cascada)."""
    session = SessionLocal()
    try:
        stmt = delete(Categoria).where(Categoria.nombre == nombre)
        result = session.execute(stmt)
        session.commit()
        if result.rowcount:
            print(f"Categoría '{nombre}' eliminada correctamente.")
        else:
            print(f"No se encontró la categoría '{nombre}'.")
        return result.rowcount or 0
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al eliminar categoría. Rollback ejecutado.")
        print("Detalle:", e)
        return 0
    finally:
        session.close()

# ====================================================

def agregar_libro(titulo: str, autor: str, precio: float, categoria_id: int) -> None:
    """Inserta un nuevo libro asociado a una categoría."""
    session = SessionLocal()
    try:
        nuevo = Libro(titulo=titulo, autor=autor, precio=precio, categoria_id=categoria_id)
        session.add(nuevo)
        session.commit()
        print(f"Libro agregado: {nuevo}")
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al agregar libro. Rollback ejecutado.")
        print("Detalle:", e)
    finally:
        session.close()


def listar_libros() -> Iterable[Libro]:
    """Lista todos los libros disponibles."""
    session = SessionLocal()
    try:
        stmt = select(Libro).order_by(Libro.id.asc())
        return session.scalars(stmt).all()
    finally:
        session.close()


def buscar_por_categoria(nombre_categoria: str) -> Iterable[Libro]:
    """Busca libros pertenecientes a una categoría específica."""
    session = SessionLocal()
    try:
        stmt = (
            select(Libro)
            .join(Categoria)
            .where(Categoria.nombre == nombre_categoria)
            .order_by(Libro.titulo.asc())
        )
        return session.scalars(stmt).all()
    finally:
        session.close()


def actualizar_precio(titulo: str, nuevo_precio: float) -> bool:
    """Actualiza el precio de un libro específico."""
    session = SessionLocal()
    try:
        stmt = update(Libro).where(Libro.titulo == titulo).values(precio=nuevo_precio)
        result = session.execute(stmt)
        session.commit()
        if result.rowcount:
            print(f"Precio actualizado para '{titulo}'.")
        else:
            print(f"No se encontró el libro '{titulo}'.")
        return result.rowcount > 0
    except SQLAlchemyError as e:
        session.rollback()
        print("Error al actualizar precio. Rollback ejecutado.")
        print("Detalle:", e)
        return False
    finally:
        session.close()


def eliminar_libro(titulo: str) -> int:
    """Elimina un libro por título."""
    session = SessionLocal()
    try:
        stmt = delete(Libro).where(Libro.titulo == titulo)
        result = session.execute(stmt)
        session.commit()
        if result.rowcount:
            print(f"Libro '{titulo}' eliminado.")
        else:
            print(f"No se encontró el libro '{titulo}'.")
        return result.rowcount or 0
    except SQLAlchemyError as e:
        session.rollback()
        print("Error en eliminación. Rollback ejecutado.")
        print("Detalle:", e)
        return 0
    finally:
        session.close()

