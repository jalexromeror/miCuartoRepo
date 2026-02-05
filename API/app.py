import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]
    return rows

@app.get("/LOTRWarriors")
def get_lotr_warriors():
    rows = ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Gollum", "El anillo"]
    return rows

@app.get("/starwarsWarriors")
def get_starwars_warriors():
    rows = ['Luke', 'Leia', 'Han', 'Chewbacca', 'C-3PO', 'R2-D2', 'Dart Vader']
    return rows

@app.get("/warriorsGOT")
def get_warriors_got():
    rows = ["Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Bran Stark", "Sansa Stark"]
    return rows

@app.get("/cursosplatzi")
def get_cursos():
    rows = ["Docker", "Bash", "Linux", "Inglés", "Python" , "Javascript", "Azure", "DevOps"]
    return rows