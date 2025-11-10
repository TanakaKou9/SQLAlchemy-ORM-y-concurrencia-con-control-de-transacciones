from pathlib import Path
from sqlalchemy import create_engine, Column, Integer,ForeignKey, String, Float
from sqlalchemy.orm import declarative_base, relationship,  sessionmaker

Base = declarative_base()

DATA_DIR = Path("datos")

DATA_DIR.mkdir(exist_ok=True)
DB_URL = f"sqlite:///{(DATA_DIR / 'libros.db').as_posix()}"

engine = create_engine(DB_URL, echo=True, future=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

class Libro(Base):
    __tablename__= "libros"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categoria = relationship("Categoria", back_populates="libros")

    def __repr__(self) -> str:
        return f"<Libro id={self.id} titulo='{self.titulo}' autor='{self.autor}' precio={self.precio:.2f} categoria_id={self.categoria_id}>"
Base.metadata.create_all(engine)