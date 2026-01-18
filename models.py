import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime, date

ugestion_parcela = Table(
    "ugestion_parcela",
    db.Base.metadata,
    Column("ugestion_id", Integer, ForeignKey("unidades_gestion.id"), primary_key=True),
    Column("parcela_id", Integer, ForeignKey("parcelas.id"), primary_key=True)
)


class Equipos(db.Base):
    __tablename__ = 'equipos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(String)
    matricula = Column(String)
    tipo = Column(String, unique=True)
    costo = Column(Integer)

    tareas = relationship("Tareas", back_populates="equipos")

    def __init__(self, fecha, matricula, tipo, costo):
        self.fecha = fecha
        self.matricula = matricula
        self.tipo= tipo
        self.costo = costo

class Infraestructura(db.Base):
    __tablename__ = 'infraestructura'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    local = Column(String)
    costo = Column(Integer)

    def __init__(self, nombre, direccion, local, costo):
        self.nombre = nombre
        self.direccion = direccion
        self.local = local
        self.costo = costo

class Costos(db.Base):
    __tablename__ = 'costos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_inventario= Column(Integer,ForeignKey('inventario.id'))
    costo = Column(Integer)
    unidades = Column(String)
    unidades_c = Column(String)
    cantidad = Column(String)

    inventario = relationship("Inventario", back_populates="costos")


    def __init__(self, costo, unidades, cantidad, unidades_c, id_inventario):
        self.costo = costo
        self.unidades = unidades
        self.cantidad = cantidad
        self.unidades_c = unidades_c
        self.id_inventario = id_inventario


class Personal(db.Base):
    __tablename__ = 'personal'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, unique=True)
    nif = Column(String)
    direccion = Column(String)
    movil = Column(Integer)
    carnet = Column(String)
    rol = Column(String)
    costo = Column(Integer)

    tareas = relationship("Tareas", back_populates="personal")

    def __init__(self, nombre, nif, direccion, movil, carnet, rol, costo):
        self.nombre = nombre
        self.nif = nif
        self.direccion= direccion
        self.movil = movil
        self.carnet = carnet
        self.rol = rol
        self.costo = costo

class Crear(db.Base):
    __tablename__= 'parcelas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    comunidad= Column(String)
    provincia = Column(String)
    nombre = Column(String, unique=True)
    municipio = Column(String)
    poligono = Column(Integer)
    parcela = Column(Integer)
    recinto = Column(Integer)
    especie = Column(String)
    variedad = Column(String)
    edad = Column(Integer)
    estado = Column(String)
    superficie = Column(Integer)
    plantas = Column(Integer)
    secano = Column(String)
    aire_libre = Column(String)

    tareas = relationship("Tareas", back_populates="parcela")
    unidades = relationship(
        "Ugestion",
        secondary=ugestion_parcela,
        back_populates="parcelas"
    )

    def __init__(self,nombre, comunidad, provincia,municipio,poligono,parcela,recinto,especie,variedad,edad,estado,superficie,plantas,secano,aire_libre):
        self.nombre=nombre
        self.comunidad= comunidad
        self.provincia= provincia
        self.municipio= municipio
        self.poligono=poligono
        self.parcela=parcela
        self.recinto=recinto
        self.especie=especie
        self.variedad=variedad
        self.edad=edad
        self.estado=estado
        self.superficie=superficie
        self.plantas=plantas
        self.secano=secano
        self.aire_libre=aire_libre


class Inventario(db.Base):
    __tablename__ = 'inventario'

    id= Column(Integer, primary_key=True, autoincrement=True)
    tipo_producto= Column(String)
    producto= Column(String, unique=True )
    abono= Column(String)
    ingrediente= Column(String)
    autorizado= Column(String)
    caducidad= Column(String)

    costos = relationship("Costos", back_populates="inventario", uselist=False)
    tareas = relationship("Tareas", back_populates="inventario")

    def __init__(self, tipo_producto, producto, abono, ingrediente, autorizado, caducidad):
        self.tipo_producto= tipo_producto
        self.producto= producto
        self.abono= abono
        self.ingrediente= ingrediente
        self.autorizado= autorizado
        self.caducidad= caducidad

class Tareas(db.Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True, autoincrement=True)

    parcela_tratar = Column(String, ForeignKey('parcelas.nombre'))
    personal_nombre = Column(String, ForeignKey('personal.nombre'))
    equipo_tipo = Column(String, ForeignKey('equipos.tipo'))
    productos = Column(String, ForeignKey('inventario.producto'))
    cantidad = Column(Integer)

    unidades_tratar = Column(String)
    tipo_labor = Column(String)
    labores = Column(String)
    fertilizar = Column(String)
    tratar = Column(String)
    prioridad = Column(String)
    fecha = Column(String)
    costo = Column(Integer)

    equipos = relationship("Equipos", back_populates="tareas")
    personal = relationship("Personal", back_populates="tareas")
    inventario = relationship("Inventario", back_populates="tareas")
    parcela = relationship("Crear", back_populates="tareas")


    def __init__(self, parcela_tratar, unidades_tratar, tipo_labor, labores, fertilizar, tratar, prioridad, personal_nombre, equipo_tipo, productos, fecha, costo, cantidad):
        self.parcela_tratar= parcela_tratar
        self.unidades_tratar= unidades_tratar
        self. tipo_labor= tipo_labor
        self.labores= labores
        self. fertilizar= fertilizar
        self.tratar= tratar
        self.prioridad=prioridad
        self.equipo_tipo= equipo_tipo
        self.personal_nombre= personal_nombre
        self.productos= productos
        self.fecha= fecha
        self.costo = costo
        self.cantidad = cantidad


class Ugestion(db.Base):
    __tablename__='unidades_gestion'

    id= Column(Integer, primary_key=True, autoincrement=True)
    nombre= Column(String)
    fecha= Column(String)

    parcelas = relationship(
        "Crear",
        secondary=ugestion_parcela,
        back_populates="unidades"
    )

    def __init__(self, nombre, fecha):
        self.nombre= nombre
        self.fecha = fecha



