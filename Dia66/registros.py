import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Definir la base de datos en la carpeta 'instance'
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'cafes.db')
if not os.path.exists(os.path.dirname(db_path)):
    os.makedirs(os.path.dirname(db_path))

# Configurar SQLAlchemy para usar esta ruta
Base = declarative_base()

class Cafe(Base):
    __tablename__ = 'cafes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    map_url = Column(String(500), nullable=False)
    img_url = Column(String(500), nullable=False)
    location = Column(String(250), nullable=False)
    seats = Column(String(250), nullable=False)
    has_toilet = Column(Boolean, nullable=False)
    has_wifi = Column(Boolean, nullable=False)
    has_sockets = Column(Boolean, nullable=False)
    can_take_calls = Column(Boolean, nullable=False)
    coffee_price = Column(String(250), nullable=True)

# Configuración de la base de datos
engine = create_engine(f'sqlite:///{db_path}')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Datos de ejemplo
cafes = [
    Cafe(name="Cafe A", map_url="http://map_a.com", img_url="http://img_a.com", location="Location A", seats="10", has_toilet=True, has_wifi=True, has_sockets=True, can_take_calls=True, coffee_price="$3"),
    Cafe(name="Cafe B", map_url="http://map_b.com", img_url="http://img_b.com", location="Location B", seats="20", has_toilet=False, has_wifi=True, has_sockets=True, can_take_calls=False, coffee_price="$2.5"),
    Cafe(name="Cafe C", map_url="http://map_c.com", img_url="http://img_c.com", location="Location C", seats="15", has_toilet=True, has_wifi=False, has_sockets=True, can_take_calls=True, coffee_price="$4"),
    Cafe(name="Cafe D", map_url="http://map_d.com", img_url="http://img_d.com", location="Location D", seats="25", has_toilet=True, has_wifi=True, has_sockets=False, can_take_calls=True, coffee_price="$3.5"),
    Cafe(name="Cafe E", map_url="http://map_e.com", img_url="http://img_e.com", location="Location E", seats="30", has_toilet=False, has_wifi=True, has_sockets=True, can_take_calls=False, coffee_price="$5"),
    Cafe(name="Cafe F", map_url="http://map_f.com", img_url="http://img_f.com", location="Location F", seats="12", has_toilet=True, has_wifi=False, has_sockets=False, can_take_calls=True, coffee_price="$3.2"),
    Cafe(name="Cafe G", map_url="http://map_g.com", img_url="http://img_g.com", location="Location G", seats="18", has_toilet=True, has_wifi=True, has_sockets=True, can_take_calls=False, coffee_price="$2.8"),
    Cafe(name="Cafe H", map_url="http://map_h.com", img_url="http://img_h.com", location="Location H", seats="22", has_toilet=False, has_wifi=True, has_sockets=True, can_take_calls=True, coffee_price="$3.6"),
    Cafe(name="Cafe I", map_url="http://map_i.com", img_url="http://img_i.com", location="Location I", seats="10", has_toilet=True, has_wifi=False, has_sockets=True, can_take_calls=True, coffee_price="$4.5"),
    Cafe(name="Cafe J", map_url="http://map_j.com", img_url="http://img_j.com", location="Location J", seats="35", has_toilet=True, has_wifi=True, has_sockets=False, can_take_calls=True, coffee_price="$5.5")
]

# Agregar registros a la sesión y confirmar la transacción
session.add_all(cafes)
session.commit()

# Cerrar la sesión
session.close()
