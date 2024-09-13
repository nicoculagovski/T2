import random
import os
from parametros import *

def cargar_archivo(nombre_jardin):
    archivo_jardines = os.path.join("data", "jardines.txt")

    with open(archivo_jardines, 'r') as f_jardines:
        jardines_data = f_jardines.readlines()
    
    for linea in jardines_data:    
        nombre, layout_str = linea.strip().split('!') #en este caso, cada linea es un nombre + jardín
        if nombre_jardin == nombre: #elijo el jardin que el usuario me dieron
            layout = [fila.split(',') for fila in layout_str.split(';')] #formato [['X', 'X', 'X'], ...]
            for i, fila in enumerate(layout): #i crece 0, 1, etc y la fila de forma ['X', 'X', 'X']
                for j, celda in enumerate(fila): #j 0, 1, etc y la celda de forma 'X'
                    layout[i][j] = Jardin.crear_plantas(celda)
            return nombre, layout #aca nombre es nombre y layout es tablero (los que se reciben en init)
    print("Ese jardín no existe...")
    exit()

class Plantas():
    def __init__(self, tipo, vida_max, vida, resistencia, resistencia_termica, congelacion, altura):
        self.tipo = tipo
        self.vida_max = vida_max
        self._vida = vida
        self.resistencia = resistencia
        self.resistencia_termica = resistencia_termica
        self.congelacion = congelacion
        self.altura = altura

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if 0 <= valor <= self.vida_max:
            self._vida = valor
        else: 
            self._vida = max(0, min(valor, self.vida_max))
    
    def regar_planta(self, planta):
        cantidad = random.choice([RIEGO_1, RIEGO_2])
        planta.vida = min(self.vida + cantidad, self.vida_max)

class Solaretillo(Plantas):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = 'Solaretillo'
        self.potencial = random.uniform(POTENCIAL_SOLARETILLO_MIN, POTENCIAL_SOLARETILLO_MAX)
    
    def generar_soles(self, temperatura):
        produccion_soles = round(CONSTANTE_SOLES * self.potencial * (temperatura / 25) * (self.altura / 30))
        if self.congelacion:
            produccion_soles = 0
        return max(0, produccion_soles)

class Defensauce(Plantas):
    #Acá agrego armadura ya que no viene del padre y que no es algo interno random (como potencial)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = 'Defensauce'
        self.armadura = ARMADURA_DEFENSAUCE

    def recibir_dano(self,dano):
        if self.armadura > 0:
            if dano >= self.armadura:
                dano -= self.armadura 
                self.armadura = 0
            else:
                self.armadura -= dano
            dano = 0
        #Obligando 0 al final me aseguro de que la vida no reciba daño a pesar de lo grande del ataque
        else: 
            self.vida = max(0, self.vida - dano) 

class Potencilantro(Plantas):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nombre = 'Potencilantro'
        self.nutriente = AUMENTO_NUTRIENTE 

    def potenciar_area(self, jardin, x, y):
        celdas_adyacentes = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) != (x,y): #no se potencia a si mismo
                    celdas_adyacentes.append((i, j))
        for i, j in adyacentes:
            #recordar que i en python es vertical y vice versa con j (creo)
            if (0 <= i < len(jardin.tablero) and 0 <= j < len(jardin.tablero[0])):
                planta = self.tablero[i][j]
                if isinstance(planta, Solarentillo):
                    planta.potencial *= (1 + self.nutriente / 100)

class Aresauce(Solaretillo, Defensauce):
    def __init__(self, **kwargs):
        Solaretillo.__init__(self, **kwargs)
        Defensauce.__init__(self, **kwargs)
        self.nombre = 'Aresauce'
        self.armadura = ARMADURA_ARESAUCE
        self.anti_robo = ANTI_ROBO

    def reducir_robo(self, robo):
        robo_reducido = robo * (1 - self.anti_robo)
        return robo_reducido

class Cilantrillo(Solaretillo, Potencilantro):
    def __init__(self, **kwargs):
        Solaretillo.__init__(self, **kwargs)
        Potencilantro.__init__(self, **kwargs)
        self.nombre = 'Cilantrillo'
        self.potencial *= 1 + AUM_POT_CIL
        self.nutriente *= 1 + AUM_AUM_CIL

    def potenciar_area(self, jardin, x, y):
        celdas_adyacentes = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                    celdas_adyacentes.append((i, j))
        for i, j in adyacentes:
            if (0 <= i < len(jardin.tablero) and 0 <= j < len(jardin.tablero[0])):
                planta = self.tablero[i][j]
                if isinstance(planta, Solarentillo):
                    planta.potencial *= (1 + self.nutriente / 100)

class Fensaulantro(Defensauce, Potencilantro):
    def __init__(self, **kwargs):
        Potencilantro.__init__(self, **kwargs)
        Defensauce.__init__(self, **kwargs)
        self.nombre = 'Fensaulantro'
        self.armadura = 15
        self.red_atq = RED_ATQ

    def aumentar_solaretillo(self, solaretillo):
        super().aumentar_solaretillo(solaretillo)

    def reducir_ataque(self, ataque):
        ataque_reducido = ataque * (1 - self.red_atq)
        return ataque_reducido

class Jardin():
    def __init__(self, nombre, tablero):
        self.nombre = nombre
        self.tablero = tablero 
        self.inventario_plantas = [] 
        self.soles = SOLES_INICIO 
        self.temperatura = TEMP_INICIAL 
        self.dia_actual = 0

    @staticmethod
    def crear_plantas(tipo): 
        archivo_plantas = os.path.join("data", "plantas.txt")
        with open(archivo_plantas, 'r') as f_plantas:
            plantas_data = f_plantas.readlines()
        for linea in plantas_data:
            tipo_planta, vida_max, vida, resistencia, resistencia_termica, congelacion, altura = linea.strip().split(';')
            if (len(tipo_planta) == 1 and 0 < int(vida_max) < 100 and 0 < int(vida) < int(vida_max) 
                and 0 < int(resistencia) < 40 and -5 < int(resistencia_termica) < 25 
                and (congelacion == '0' or congelacion == '1') and 0 < int(altura) < 30):
                if tipo == tipo_planta:
                    kwargs = {
                        "tipo": tipo_planta,
                        "vida_max": int(vida_max),
                        "vida": int(vida),
                        "resistencia": int(resistencia),
                        "resistencia_termica": int(resistencia_termica),
                        "congelacion": bool(congelacion == "True"),
                        "altura": int(altura)
                    }
                    if tipo == 'S':
                        return Solaretillo(**kwargs)
                    elif tipo == 'D':
                        return Defensauce(**kwargs)
                    elif tipo == 'P':
                        return Potencilantro(**kwargs)
                    elif tipo == 'A':
                        return Aresauce(**kwargs)
                    elif tipo == 'C':
                        return Cilantrillo(**kwargs)
                    elif tipo == 'F':
                        return Fensaulantro(**kwargs)
        return 'X'
    
    def regar_plantas(self):
        for fila in self.tablero:
            for celda in fila:
                if isinstance(celda, Plantas):
                    celda.regar_planta(celda)

    def cultivar_plantas(self, planta, coordenadas: list):
        x, y = coordenadas
        instancia_planta = self.crear_plantas(planta)
        if isinstance(instancia_planta, Plantas): #esta linea quizás sobra
            self.tablero[y][x] = instancia_planta
            print(f"Plantada {instancia_planta.nombre} en coordenadas ({x}, {y})")

    def intercambiar(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        if (0 <= x1 < len(self.tablero) and 0 <= y1 < len(self.tablero) and
            0 <= x2 < len(self.tablero) and 0 <= y2 < len(self.tablero)): #verifica coordenadas
            self.tablero[y1][x1], self.tablero[y2][x2] = self.tablero[y2][x2], self.tablero[y1][x1] 
            #Al principio tenía esto en 2 lineas distintas pero si hacía eso una de las 2 se sobrescribia mal
            
    def mutar(self, tipo1, tipo2, tipo_mutacion):
        if self.inventario_plantas.count(tipo1) > 0 and self.inventario_plantas.count(tipo2) > 0:
                self.inventario_plantas.remove(tipo1)
                self.inventario_plantas.remove(tipo2)
                self.inventario_plantas.append(tipo_mutacion)
                if tipo_mutacion == 'A':
                    print(f"¡Mutación exitosa! Ahora tienes un Aresauce")
                elif tipo_mutacion == 'C':
                    print(f"¡Mutación exitosa! Ahora tienes un Cilantrillo")
                if tipo_mutacion == 'F':
                    print(f"¡Mutación exitosa! Ahora tienes un Fensaulantro")
        else:
            print("No tienes suficientes plantas para hacer esta mutación")

    def actualizar_temperatura(self):
        self.temperatura = random.randint(TEMP_MIN_JARDIN, TEMP_MAX_JARDIN)
    
    def actualizar_dia(self):
        if self.dia_actual <= DURACION:
            self.dia_actual += 1
        else:
            print(f"Se acabó el juego... Grcias por ayudar a defender el jardín, !espero hayas disfrutado!")
            print("Así quedo tu jardín:")
            print("\n")
            self.presentarse_final()
            print("\n")
            exit()
    
    def inicar_evento(self, dificultad):
        archivo_eventos = os.path.join("data", "eventos.txt")
        with open(archivo_eventos) as archivo:
            for linea in archivo:
                evento, prob_facil, prob_medio, prob_dificil = linea.strip().split(';')
                if evento == "Z":
                    if dificultad == "facil":
                        prob_zombies = float(prob_facil)
                    elif dificultad == "medio":
                        prob_zombies = float(prob_medio)
                    elif dificultad == "dificil":
                        prob_zombies = float(prob_dificil)
                elif evento == "H":
                    if dificultad == "facil":
                        prob_hel = float(prob_facil)
                    elif dificultad == "medio":
                        prob_hel = float(prob_medio)
                    elif dificultad == "dificil":
                        prob_hel = float(prob_dificil)
        
        if random.random() < prob_zombies:
            return 1
        elif random.random() < prob_hel:
            return 2
        else: 
            return 3

    def calcular_soles(self):
        total_soles = 0
        for i, fila in enumerate(self.tablero):
            for j, celda in enumerate(fila):
                if isinstance(celda, Solaretillo): #esto revisa si es o solaretillo o una de sus subclases
                    soles_producidos = celda.generar_soles(self.temperatura)
                    print(f"Un {celda.nombre} en {j, i} ha producido {soles_producidos} soles")
                    total_soles += soles_producidos
        soles_cielo = random.randint(MIN_SOLES, MAX_SOLES)
        total_soles += soles_cielo
        print(f"Se han obtenido {soles_cielo} soles del cielo")
        print(f"En total se han recolcetado {total_soles} soles durante del día")  
        return total_soles         

    def llegada_plantas(self):
        cant_llegadas = random.randint(NUM_MIN_PLANTA, NUM_MAX_PLANTA)
        for planta in range(cant_llegadas):
            tipo = random.randint(1, 3)
            if tipo == 1:
                tipo = 'S'
            elif tipo == 2: 
                tipo = 'D'
            elif tipo == 3:
                tipo = 'P'
            instancia_planta = self.crear_plantas(tipo)
            if isinstance(instancia_planta, Plantas): 
                self.inventario_plantas.append(tipo)
        print(f"** Ha(n) llegado {cant_llegadas} planta(s) a tu inventario **")
    
    def mostrar_jardin(self):
        for fila in self.tablero:
            lista_jardin = []
            for celda in fila:
                if isinstance(celda, Plantas):
                    if celda.congelacion == True:
                        lista_jardin.append(f"*{celda.tipo}*") 
                    else: 
                        lista_jardin.append(f"{celda.tipo}") 
                else: 
                    lista_jardin.append(f"{celda}")
            print(lista_jardin)

    def presentarse(self):
        print("*** Esté es tu jardín actual ***")
        print(f"Temperatura : {self.temperatura} °C")
        print("\n")
        self.mostrar_jardin()
        print("\nTe quedan en el inventario:")
        print(f"{self.inventario_plantas.count('S')} Solarentillo")
        print(f"{self.inventario_plantas.count('D')} Defensauce")
        print(f"{self.inventario_plantas.count('P')} Potencilantro")
        print(f"{self.inventario_plantas.count('A')} Aresuace")
        print(f"{self.inventario_plantas.count('C')} Cilantrillo")
        print(f"{self.inventario_plantas.count('F')} Fensaulantro")

    def presentarse_final(self):
        self.mostrar_jardin()
        print("\nTe quedaron en el inventario:")
        print(f"{self.inventario_plantas.count('S')} Solarentillo")
        print(f"{self.inventario_plantas.count('D')} Defensauce")
        print(f"{self.inventario_plantas.count('P')} Potencilantro")
        print(f"{self.inventario_plantas.count('A')} Aresuace")
        print(f"{self.inventario_plantas.count('C')} Cilantrillo")
        print(f"{self.inventario_plantas.count('F')} Fensaulantro")

    def activar_helada(self):
        self.temperatura = random.randint(TEMP_MIN_HELADA, TEMP_MAX_HELADA)
        for i, fila in enumerate(self.tablero):
            for j, celda in enumerate(fila):
                if isinstance(celda, Plantas):
                    if celda.resistencia_termica > self.temperatura:
                        celda.congelacion = True
                    else:
                        celda.congelacion = False
                        if isinstance(celda, Solaretillo):
                            celda.generar_soles(self.temperatura + SOLES_EXTRA_HELADA) 
    def descongelar_plantas(self):
        for fila in self.tablero:
            for celda in fila:
                if isinstance(celda, Plantas):
                    celda.congelacion = False
    def hay_planta(self, tipo_planta):
        for fila in self.tablero:
            for celda in fila:
                if isinstance(celda, tipo_planta):
                    return True

    def activar_zombies(self, dificultad):
        ataques_realizados = 0
        soles_robados = 0
        if dificultad == "facil":
            cant_zombies = ZOMBIES_FACIL
        elif dificultad == "medio":
            cant_zombies = ZOMBIES_MEDIO
        elif dificultad == "dificil":
            cant_zombies = ZOMBIES_DIFICIL

        print("-" * 30)
        print(f"Durante la noche pasaron {cant_zombies} zombies")
        print("-" * 30)

        hay_aresauce = self.hay_planta(Aresauce)
        hay_fensaulantro = self.hay_planta(Fensaulantro)
        if hay_aresauce:
            reduccion_robo = (1 - ANTI_ROBO)
        else:
            reduccion_robo = 1
        if hay_fensaulantro:
            reduccion_ataque = (1 - RED_ATQ)
        else:
            reduccion_ataque = 1
        
        #por lo que entendí el zombie atacá de forma random y una casilla puede ser atacada mas de una vez
        for zombie in range(cant_zombies):
            x = random.randint(0, len(self.tablero[0]) - 1)
            y = random.randint(0, len(self.tablero) - 1)
            if self.tablero[y][x] == 'X':
                print(f"¡Un zombie intentó atacar a la posición ({x}, {y}) pero estaba vacía!")
            elif isinstance(self.tablero[y][x], Plantas):
                planta = self.tablero[y][x]
                ataque = random.randint(Z_DANO_MIN, Z_DANO_MAX)
                ataque_reducido = ataque * reduccion_ataque
                dano = max(1, round(ataque * (40-planta.resistencia)/40))
                planta.vida -= dano
                if planta.vida > 0:
                    print(f"La planta {planta.nombre} en ({x}, {y}) ha perdido {dano} puntos de vida")
                else:
                    print(f"La planta de {planta.nombre} en ({x}, {y}) ha perdido {dano} puntos de vida, lo que ha acabado con su vida :(")
                    self.tablero[y][x] = 'X'
                ataques_realizados += 1
                soles_robados += SOLES_ROBADOS * reduccion_robo
        self.soles = max(0, self.soles - soles_robados)
        if ataques_realizados > 0:
            print(f"Los zombies lograron atacar {ataques_realizados} casillas, robando {soles_robados} soles.")
        else:
            print("¡Ninguna de tus plantas fue atacada! No has sufrido robos de soles.")