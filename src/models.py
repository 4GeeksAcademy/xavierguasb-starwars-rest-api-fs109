from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    favorite_planet = relationship("FavoritePlanet", back_populates="user")
    favorite_characters = relationship("FavoriteCharacter", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_de_subscripcion": self.fecha_de_subscripcion,
        }

    def __str__(self):
        return self.nickname


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    clima: Mapped[str] = mapped_column(nullable=False)
    diametro: Mapped[int] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(nullable=False)
    poblacion: Mapped[int] = mapped_column(nullable=False)

    characters = relationship("Character", back_populates="planet")
    favorite_planet = relationship("FavoritePlanet", back_populates="planet")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "clima": self.clima,
            "diametro": self.diametro,
            "terreno": self.terreno,
            "poblacion": self.poblacion,
        }

    def __str__(self):
        return self.nombre


class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite_planet")

    planet_id = mapped_column(ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates="favorite_planet")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }

    def __str__(self):
        return str(self.planet)


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=False)
    color_de_pelo: Mapped[str] = mapped_column(nullable=False)
    altura: Mapped[int] = mapped_column(nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(nullable=False)

    planet_id = mapped_column(ForeignKey("planet.id"))
    planet = relationship("Planet", back_populates="characters")

    favorite_characters = relationship("FavoriteCharacter", back_populates="character")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "genero": self.genero,
            "color_de_pelo": self.color_de_pelo,
            "altura": self.altura,
            "color_de_ojos": self.color_de_ojos,
        }

    def __str__(self):
        return self.nombre


class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="favorite_characters")

    character_id = mapped_column(ForeignKey("character.id"))  # ✅ corregit
    character = relationship("Character", back_populates="favorite_characters")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }

    def __str__(self):
        return str(self.character)
