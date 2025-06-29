import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, date


class Equipos(db.Base):
    __tablename__ = 'equipos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    fecha = Column(String)
    matricula = Column(String)
    roma = Column(Integer)
    modelo = Column(String)
    marca = Column(String)
    serie = Column(String)
    tipo = Column(String)

    def __init__(self, nombre, fecha, matricula, roma, modelo, marca, serie, tipo):
        self.nombre = nombre
        self.fecha = fecha
        self.matricula = matricula
        self.roma = roma
        self.modelo=modelo
        self.marca= marca
        self.serie= serie
        self.tipo= tipo

class Infraestructura(db.Base):
    __tablename__ = 'infraestructura'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    poblacion = Column(String)
    ciudad = Column(Integer)
    pais = Column(String)
    local = Column(String)

    def __init__(self, nombre, direccion, poblacion, ciudad, pais, local):
        self.nombre = nombre
        self.direccion = direccion
        self.poblacion = poblacion
        self.ciudad = ciudad
        self.pais= pais
        self.local = local

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
    nombre = Column(String)
    apellido = Column(String)
    nif = Column(String)
    direccion = Column(String)
    poblacion = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    movil = Column(Integer)
    correo = Column(String)
    carnet = Column(String)
    rol = Column(String)

    def __init__(self, nombre, apellido, nif, direccion, poblacion, ciudad, pais, movil, correo, carnet, rol):
        self.nombre = nombre
        self.apellido= apellido
        self.nif = nif
        self.direccion= direccion
        self.poblacion = poblacion
        self.ciudad= ciudad
        self.pais= pais
        self.movil = movil
        self.correo = correo
        self.carnet = carnet
        self.rol = rol

class Crear(db.Base):
    __tablename__= 'parcelas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    comunidad= Column(String)
    provincia = Column(String)
    nombre = Column(String)
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
    producto= Column(String )
    registro= Column(String)
    abono= Column(String)
    descripcion= Column(String)
    fabricante= Column(String)
    ingrediente= Column(String)
    autorizado= Column(String)
    caducidad= Column(String)

    costos = relationship("Costos", back_populates="inventario", uselist=False)

    def __init__(self, tipo_producto, producto, registro, abono, descripcion, fabricante, ingrediente, autorizado, caducidad):
        self.tipo_producto= tipo_producto
        self.producto= producto
        self.registro= registro
        self.abono= abono
        self.descripcion= descripcion
        self.fabricante= fabricante
        self.ingrediente= ingrediente
        self.autorizado= autorizado
        self.caducidad= caducidad

class Tareas(db.Base):
    __tablename__ = 'tareas'

    id= Column(Integer, primary_key=True, autoincrement=True)
    parcela_tratar= Column(String)
    unidades_tratar= Column(String )
    tipo_labor= Column(String)
    labores= Column(String)
    fertilizar= Column(String)
    tratar= Column(String)
    prioridad= Column(String)
    personal= Column(String)
    equipos= Column(String)
    productos= Column(String)
    fecha= Column(String)

    def __init__(self, parcela_tratar, unidades_tratar, tipo_labor, labores, fertilizar, tratar, prioridad, personal, equipos, productos, fecha):
        self.parcela_tratar= parcela_tratar
        self.unidades_tratar= unidades_tratar
        self. tipo_labor= tipo_labor
        self.labores= labores
        self. fertilizar= fertilizar
        self.tratar= tratar
        self.prioridad=prioridad
        self.equipos= equipos
        self.personal= personal
        self.productos= productos
        self.fecha= fecha


class Ugestion(db.Base):
    __tablename__='unidades de gestion'

    id= Column(Integer, primary_key=True, autoincrement=True)
    nombre= Column(String)
    parcela=Column(String)
    fecha= Column(String)

    def __init__(self, nombre, parcela, fecha):
        self.nombre= nombre
        self.parcela= parcela
        self.fecha = fecha

