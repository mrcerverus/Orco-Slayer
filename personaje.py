class Personaje():
    
    def __init__(self , nombre:str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
    
    @property #getter
    def estado(self):
        return f'''
            Nombre: {self.nombre}
            Nivel: {self.nivel}
            Exp: {self.experiencia}
                '''
    
    @estado.setter #setter
    def estado(self, exp : int):
        temp_exp = self.experiencia + exp
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -= 100
        
        while temp_exp < 0:
            if self.nivel > 1:
                temp_exp = 100 + temp_exp
                self.nivel -= 1
            else:
                temp_exp = 0
        
        self.experiencia = temp_exp
    
    #sobrecargas
    def __lt__(self, other): # menor que
        return self.nivel < other.nivel
    def __gt__(self, other): # mayor que
        return self.nivel > other.nivel
    def __eq__(self, other): # iguales
        return self.nivel == other.nivel
    
    def mostrar_probabilidad(self, other):
        if self < other:
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.50
    
    @staticmethod
    def mostrar_dialogo(prob_ganar):
        print(f"Con tu nivel actual, tienes {prob_ganar*100}% de probabilidades de ganarle al Orco.")
        return int(input(f'''
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
    1. Atacar
    2. Huir
            '''))