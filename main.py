from personaje import Personaje
import random

print('¡Bienvenido a Gran Fantasía!')
nombre = input('Por favor indique nombre de su personaje: \n')

p = Personaje(nombre)
o = Personaje("Orco")

print(p.estado)
print('¡Oh no!, ¡Ha aparecido un Orco!')

probalidad_de_ganar = p.mostrar_probabilidad(o)

op_vs_orco = Personaje.mostrar_dialogo(probalidad_de_ganar)

while op_vs_orco == 1:
    resultado = "G" if random.uniform(0,1) < probalidad_de_ganar else "P"
    if resultado == "G":
        print('''
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
''')
        p.estado = 50
        o.estado = -30
    
    else:
        print('''
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!           
''')
        p.estado = -30
        o.estado = 50
        
    print(p.estado)
    print(o.estado)
    probalidad_de_ganar = p.mostrar_probabilidad(o)
    op_vs_orco = Personaje.mostrar_dialogo(probalidad_de_ganar)

print("¡Has huido! El orco ha quedado atrás.")