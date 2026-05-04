import sqlite3
import requests

BASE_URL = "http://127.0.0.1:5000"


def registrar():

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    response = requests.post(
        f"{BASE_URL}/registro",
        json=datos
    )

    print(response.json())


def login():

    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=datos
    )

    print(response.json())

def ver_usuarios():

    response = requests.get(f"{BASE_URL}/usuarios")

    if response.status_code == 200:
        usuarios = response.json()
        print("\n=== USUARIOS EN DB ===")
        for usuario in usuarios:
            print(usuario)
    else:
        print("Error al obtener usuarios:", response.text)


while True:

    print("\n=== SISTEMA ===")
    print("1. Registrar usuario")
    print("2. Login")
    print("3. Ver usuarios")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar()

    elif opcion == "2":
        login()

    elif opcion == "3":
        ver_usuarios()

    elif opcion == "4":
        break

    else:
        print("Opción inválida")