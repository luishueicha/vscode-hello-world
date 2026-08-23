#!/usr/bin/env python3
"""Script de saludo personalizado para el issue #2."""

from datetime import datetime


def main():
    nombre = input("Cual es tu nombre? ").strip()
    if not nombre:
        nombre = "Invitado"
    print(f"Hola {nombre}, bienvenido a GitHub!")
    ahora = datetime.now()
    print(f"Hoy es {ahora.strftime('%d/%m/%Y')} y son las {ahora.strftime('%H:%M:%S')}")


if __name__ == "__main__":
    main()
