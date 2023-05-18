import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favourite = relationship('Favourite', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Favourite

class Favourite(Base):
    __tablename__ = 'favourite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False) # Define la columna user_id como clave foránea relacionada con la tabla 'user'
    starships = relationship('Starships', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Starships
    planets = relationship('Planets', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Planets
    character = relationship('Character', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Character

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    starships = relationship('Starships', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Starships
    character = relationship('Character', backref='user', lazy=True) # Establece una relación uno a muchos con la clase Character
    favourite_id = Column(Integer, ForeignKey('favourite.id'),
        nullable=True)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    mglt = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'),
        nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'),
        nullable=True)
    favourite_id = Column(Integer, ForeignKey('favourite.id'),
        nullable=True)
    
class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    planet =  Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'),
        nullable=True)
    films = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starships = relationship("Starships", backref="character", uselist=False) # Establece una relación uno a muchos con la clase Starships
    vehicles = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    favourite_id = Column(Integer, ForeignKey('favourite.id'),
        nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
