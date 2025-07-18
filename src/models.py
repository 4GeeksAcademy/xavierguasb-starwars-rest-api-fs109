from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    fecha_de_subscripcion: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_de_subscripcion": self.fecha_de_subscripcion,
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    clima: Mapped[str] = mapped_column(nullable=False)
    diametro: Mapped[int] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(nullable=False)
    poblacion: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "diametro": self.diametro,
            "terreno": self.terreno,
            "poblacion": self.poblacion,
        }
    
class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    planet_id: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }

class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    color_de_pelo: Mapped[str] = mapped_column(nullable=False)
    altura: Mapped[int] = mapped_column(nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "color_de_pelo": self.color_de_pelo,
            "altura": self.altura,
            "color_de_ojos": self.color_de_ojos,
        }

class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    character_id: Mapped[int] = mapped_column(nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "haracter_id": self.haracter_id,
        }
