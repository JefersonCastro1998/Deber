''''''''''#elegir las opciones
jugador1: input('jugador1,elige: piedra, papel, tijera:')
jugador2: input('jugador2,elige: piedra, papel, tijera:')

#comparacion

if jugador1==jugador2:
    print('empate')
elif (jugador1=='piedra' and jugador2=='tijera') or\
     (jugador1=='papel' and jugador2=='piedra') or\
     (jugador1=='tijera' and jugador2=='papel'):
    print('jugador1 gana')
else: ('jugador2 gana')'''







# Elegir las opciones 
valid_choices = ['piedra', 'papel', 'tijera']

jugador1 = input('jugador1: elige: piedra, papel, tijera: ')
while jugador1 not in valid_choices:
    jugador1 = input('Entrada no válida. jugador1: elige: piedra, papel, tijera: ')

jugador2 = input('jugador2: elige: piedra, papel, tijera: ')
while jugador2 not in valid_choices:
    jugador2 = input('Entrada no válida. jugador2: elige: piedra, papel, tijera: ')

# Comparación
if jugador1 == jugador2:
    print('empate')
elif (jugador1 == 'piedra' and jugador2 == 'tijera') or\
     (jugador1 == 'papel' and jugador2 == 'piedra') or\
     (jugador1 == 'tijera' and jugador2 == 'papel'):
    print('jugador1 gana')
else:
    print('jugador2 gana')
