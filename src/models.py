import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

    # class Person(Base):
    #     __tablename__ = 'person'
    #     # Here we define columns for the table person
    #     # Notice that each column is also a normal Python instance attribute.
    #     id = Column(Integer, primary_key=True)
    #     name = Column(String(250), nullable=False)

    # class Address(Base):
    #     __tablename__ = 'address'
    #     # Here we define columns for the table address.
    #     # Notice that each column is also a normal Python instance attribute.
    #     id = Column(Integer, primary_key=True)
    #     street_name = Column(String(250))
    #     street_number = Column(String(250))
    #     post_code = Column(String(250), nullable=False)
    #     person_id = Column(Integer, ForeignKey('person.id'))
    #     person = relationship(Person)

    #     def to_dict(self):
    #         return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    gender = Column(String(250))
    height = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    gravity = Column(String(250))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    class_type = Column(String(250))
    passenger = Column(Integer)
    model = Column(String(250))

class Planet_favorite(Base):
    __tablename__ = 'planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Character_favorite(Base):
    __tablename__ = 'character_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

class Vehicle_favorite(Base):
    __tablename__ = 'vehicle_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')