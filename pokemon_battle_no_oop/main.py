'''
Simulación de batalla Pokémon SIN OOP.
Los Pokémon son diccionarios y la lógica vive en funciones.
'''

from random import sample
from time import sleep


# Utils
def esperar():
    print('\n...')
    sleep(0.7)


# Pokémon
def crear_pokemon(nombre, tipo, hp, ad):
    return {
        'nombre': nombre.capitalize(),
        'tipo': tipo,
        'hp': hp,
        'ad': ad
    }


def Pokemon_disponibles():
    return [
        crear_pokemon('pikachu', 'electrico', 60, 15),
        crear_pokemon('chikorita', 'planta', 45, 10),
        crear_pokemon('charmander', 'fuego', 40, 10),
        crear_pokemon('froakie', 'agua', 40, 20),
    ]


def esta_vivo(pokemon):
    return pokemon['hp'] > 0


def nombre_ataque(pokemon):
    if pokemon['tipo'] == 'electrico':
        return 'Impactrueno'
    elif pokemon['tipo'] == 'planta':
        return 'Hoja navaja'
    elif pokemon['tipo'] == 'fuego':
        return 'Llamarada'
    else:
        return 'Cañon de agua'


def mostrar_estado(pokemon):
    print(f'{pokemon["nombre"]} | HP: {pokemon["hp"]}')


# Combate
def recibir_dañio(pokemon, daño):
    pokemon['hp'] = pokemon['hp'] - daño

    if pokemon['hp'] < 0:
        pokemon['hp'] = 0


def atacar(atacante, rival):
    recibir_dañio(rival, atacante['ad'])
    print(f'\n({atacante["nombre"]}) Ataca con {nombre_ataque(atacante)} | -{atacante["ad"]}')


def batalla(poke_1, poke_2):
    print('\n ------ POKEMON SELECCIONADOS ------')
    esperar()
    print(f'\nPokemon 1: {poke_1["nombre"]} (HP: {poke_1["hp"]} | AD: {poke_1["ad"]})')
    print(f'Pokemon 2: {poke_2["nombre"]} (HP: {poke_2["hp"]} | AD: {poke_2["ad"]})')

    # Ciclo de turnos hasta que uno pierda
    while True:
        # Turno poke_1
        esperar()
        atacar(poke_1, poke_2)

        if not esta_vivo(poke_2):
            print(f'\nGAME OVER: {poke_1["nombre"]} venció a {poke_2["nombre"]}')
            break

        # Turno poke_2
        esperar()
        atacar(poke_2, poke_1)

        if not esta_vivo(poke_1):
            print(f'\nGAME OVER: {poke_2["nombre"]} venció a {poke_1["nombre"]}')
            break

        # Vidas restantes
        esperar()
        print('\nHPs restantes')
        mostrar_estado(poke_1)
        mostrar_estado(poke_2)


def iniciar_batalla():
    # Se crea un catalogo nuevo en cada batalla para que las vidas vuelvan a empezar
    poke_1, poke_2 = sample(Pokemon_disponibles(), 2)
    batalla(poke_1, poke_2)


def ver_pokemon():
    print('\n ------ POKEMON DISPONIBLES ------\n')

    for pokemon in Pokemon_disponibles():
        print(f'{pokemon["nombre"]} ({pokemon["tipo"]}) | HP: {pokemon["hp"]} | AD: {pokemon["ad"]}')


# Menú
def mostrar_menu():
    print('\n===== BATALLA POKÉMON SIN OOP =====\n')
    print('1. Iniciar batalla')
    print('2. Ver Pokémon disponibles')
    print('3. Salir')


def main():
    while True:
        mostrar_menu()

        try:
            opcion = input('\nElige una opción: ').strip()
        except EOFError:
            break

        if opcion == '1':
            iniciar_batalla()
        elif opcion == '2':
            ver_pokemon()
        elif opcion == '3':
            print('\nAdiós hermos@')
            break
        else:
            print('\nOpción inválida, intenta de nuevo.')


main()