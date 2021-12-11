from peewee import *

db = SqliteDatabase('crud/db/peliculas.db')

class Peliculas(Model):
    Titulo = CharField()
    Fecha = CharField()
    Comentario = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Peliculas])