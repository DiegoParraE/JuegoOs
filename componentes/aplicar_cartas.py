import random

def aplicar_cartas(sistema, cartas):
    """
    Aplica las cartas seleccionadas al sistema operativo escogido y retorna los atributos del jugador.
    """
    jugador = {
        "nombre": f"Jugador ({sistema})",
        "ataque": random.randint(5, 10),
        "defensa": random.randint(5, 10),
        "vida": 100
    }

    # Modificar atributos con cartas
    for carta in cartas:
        if carta == "antivirus":
            jugador["defensa"] += 3
        elif carta == "troyano":
            jugador["ataque"] += 5
        elif carta == "firewall":
            jugador["defensa"] += 2
        elif carta == "botiquín":
            jugador["vida"] += 20
        elif carta == "phishing":
            jugador["ataque"] += 2
            jugador["defensa"] -= 1
        # Agrega más cartas según tu lógica

    return jugador
