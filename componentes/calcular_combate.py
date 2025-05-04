def calcular_combate(jugador, cpu):
    """
    Simula un combate por turnos entre el jugador y la CPU.
    Retorna: jugador_final, cpu_final, daño_jugador, daño_cpu
    """
    vida_jugador = jugador["vida"]
    vida_cpu = cpu["vida"]
    daño_jugador_total = 0
    daño_cpu_total = 0

    while vida_jugador > 0 and vida_cpu > 0:
        # Daño recibido por turno (con defensa)
        daño_cpu = max(jugador["ataque"] - cpu["defensa"], 1)
        daño_jugador = max(cpu["ataque"] - jugador["defensa"], 1)

        vida_cpu -= daño_cpu
        vida_jugador -= daño_jugador

        daño_jugador_total += daño_jugador
        daño_cpu_total += daño_cpu

    jugador["vida"] = max(vida_jugador, 0)
    cpu["vida"] = max(vida_cpu, 0)

    return jugador, cpu, daño_jugador_total, daño_cpu_total
