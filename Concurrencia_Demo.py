"""
Demostración de concurrencia segura con SQLAlchemy y Lock.
Cada hilo agrega libros a la base de datos al mismo tiempo,
usando sesiones independientes y bloqueo del tramo crítico.
"""

import threading
from time import sleep
from random import uniform
from threading import Lock
from sqlalchemy.exc import SQLAlchemyError
from modelo.Libro import Libro, SessionLocal

lock = Lock()  # protege add + commit


def agregar_concurrente(titulo: str, autor: str, precio: float, categoria_id: int, pausa: float = 0.1) -> None:
    """
    Inserta un libro usando un Lock global para evitar colisiones.
    Cada hilo usa su propia sesión independiente.
    """
    session = SessionLocal()
    try:
        with lock:
            nuevo = Libro(titulo=titulo, autor=autor, precio=precio, categoria_id=categoria_id)
            session.add(nuevo)
            session.commit()
            print(f"[{threading.current_thread().name}] Agregado: {nuevo}")
            sleep(pausa)  # simula carga de trabajo
    except SQLAlchemyError as e:
        session.rollback()
        print(f"[{threading.current_thread().name}] Error. Rollback ejecutado.")
        print("Detalle:", e)
    finally:
        session.close()


if __name__ == "__main__":
    # Datos de prueba (puedes cambiarlos)
    datos = [
        ("Refactoring", "Martin Fowler", 50.0, 1),
        ("Clean Architecture", "Robert C. Martin", 48.0, 1),
        ("Design Patterns", "GoF", 60.0, 1),
        ("The Pragmatic Programmer", "Hunt & Thomas", 44.0, 1),
        ("Effective Python", "Brett Slatkin", 42.0, 1),
    ]

    hilos = []

    for i, (titulo, autor, precio, categoria_id) in enumerate(datos, start=1):
        pausa = round(uniform(0.05, 0.2), 3)
        hilo = threading.Thread(
            target=agregar_concurrente,
            name=f"Hilo-{i}",
            args=(titulo, autor, precio, categoria_id, pausa)
        )
        hilos.append(hilo)
        hilo.start()

    for h in hilos:
        h.join()

    print("\nInserciones concurrentes completadas.")
