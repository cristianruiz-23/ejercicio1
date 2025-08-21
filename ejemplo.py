def taller_mecanico():
    print("=== Mini sistema experto  ===")

    arranca = input("¿El auto arranca? (si/no): ").strip().lower()
    luces = input("¿Las luces del tablero están encendidas? (si/no): ").strip().lower()
    humo_negro = input("¿El auto tiene humo negro? (si/no): ").strip().lower()
    humo_blanco = input("¿El auto tiene humo blanco ? (si/no): ").strip().lower()
    se_apaga = input("¿El auto arrancana pero se apaga a la hora de arrancar? (si/no): ").strip().lower()

    
    if arranca == "no" and luces == "no":
        print("\nPosible causa: Batería descargada.")
    elif arranca == "no" and luces == "si":
        print("\nPosible causa: Fallo en el motor de arranque.")
    elif arranca == "si" and se_apaga == "si":
        print("\nPosible causa: Problema por falta de combustible.")
    elif humo_negro == "si":
        print("\nPosible causa: Mezcla rica de combustible.")
    elif humo_blanco == "si":
        print("\nPosible causa: Falla en la  culata.")
    else:
        print("\nNo hay diagnóstico claro con daños dados.")


if __name__ == "__main__":
    taller_mecanico()
