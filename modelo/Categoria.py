from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from pathlib import Path


Base = declarative_base()

DATA_DIR = Path("datos")

DATA_DIR.mkdir(exist_ok=True)
DB_URL = f"sqlite:///{(DATA_DIR / 'libros.db').as_posix()}"

engine = create_engine(DB_URL, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


class Categoria(Base):
    


    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)

    libros = relationship("Libro", back_populates="categoria", cascade="all, delete")

    def __repr__(self) -> str:
        return f"<Categoria id={self.id} nombre='{self.nombre}'>"



Base.metadata.create_all(engine)
