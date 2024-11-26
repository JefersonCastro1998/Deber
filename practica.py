#elegir las opciones
jugador1: input('jugador1,elige: piedra, papel, tijera:')
jugador2: input('jugador2,elige: piedra, papel, tijera:')

#comparacion
if jugador1==jugador2:
    print('empate')
elif (jugador1=='piedra' and jugador2=='tijeras') or\
     (jugador1=='papel' and jugador2=='piedra') or\
     (jugador1=='tijera' and jugador2=='papel'):
    print('jugador1 gana')
else: ('jugador2 gana')