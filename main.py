import sys
from entidades import Jardin
from entidades import Plantas
from entidades import cargar_archivo
from parametros import *

nombre_jardin = sys.argv[1] #si le pongo 0 me dice que el jardín no existe
dificultad = sys.argv[2]
nombre_jardin, layout = cargar_archivo(nombre_jardin)
jardin = Jardin(nombre_jardin, layout)

total_soles = SOLES_INICIO
if dificultad != "facil" and dificultad != "medio" and dificultad != "dificil":
    print("Ingresa una dificultad permitida (facil, medio o dificl)...")
    exit()

def mostrar_menu_inicio():
    print("\n")
    print("-" * 29)
    titulo = "Menú de inicio"
    print(" " * 7 + titulo)
    print("-" * 29)
    print(f"\nSoles Disponibles: {total_soles}")
    print(f"Temperatura: {jardin.temperatura} °C")
    print(f"Día Actual: {jardin.dia_actual}")
    print("\n[1] Menu Jardín")
    print("[2] Laboratorio")
    print("[3] Pasar Día")
    print("\n[0] Salir del programa")
    opcion = input("\nOpción: ")
    print("-" * 29)
    return opcion

def mostrar_menu_jardin():
    print("\n")
    print("-" * 29)
    titulo = "Jardín"
    print(" " * 11 + titulo)
    print("-" * 29)
    jardin.mostrar_jardin()
    print("\n[1] Intercambiar")
    print("[2] Cultivar")
    print("[3] Regar")
    print("\n[0] Volver al menú de inicio")
    opcion = input("\nOpción: ")
    print("-" * 29)
    return opcion

def mostrar_menu_laboratorio():
    print("\n")
    print("-" * 50)
    titulo = "Laboratorio"
    print(" " * 19 + titulo)
    print("-" * 50)
    guia = "|Guía|"
    tienes = "|Tienes|"
    mutaciones = "|Mutaciones|"
    print("\n")
    print(" " * 21 + guia)
    print("\nSolaretillo + Defensauce = Aresauce")
    print("Solaretillo + Potencilantro = Cilantrillo")
    print("Defensauce + Potencilantro = Fensaulantro")
    print("\n")
    print(" " * 20 + tienes)
    print(f"\nSolaretillo: {jardin.inventario_plantas.count('S')}" 
    + " " * 3 + f"Defensauce: {jardin.inventario_plantas.count('D')}" 
    + " " * 3 + f"Potencilantro: {jardin.inventario_plantas.count('P')}"
    )
    print("\n")
    print(" " * 19 + mutaciones)
    print("\n[1] Aaresauce" 
    + " " * 3 + "[2] Cilantrillo" 
    + " " * 3 + "[3] Fensaulantro"
    )
    print("\n[0] Volver al menú de inicio")
    opcion = int(input("\nIndique su mutación a crear: "))
    print("-" * 30)
    return opcion

def mostrar_menu_cultivar():
    print("\n")
    print("\nPlantas Disponibles:")
    print(f"[1] Solarentillo: {jardin.inventario_plantas.count('S')}")
    print(f"[2] Defensauce: {jardin.inventario_plantas.count('D')}")
    print(f"[3] Potencilantro: {jardin.inventario_plantas.count('P')}")
    print(f"[4] Aresuace: {jardin.inventario_plantas.count('A')}")
    print(f"[5] Cilantrillo: {jardin.inventario_plantas.count('C')}")
    print(f"[6] Fensaulantro: {jardin.inventario_plantas.count('F')}")
    print("\n[0] Volver al menú de jardín")
    
    numero = input("\nElige la planta que quieres usar: ")
    #Esto arregla mal numero de planta y error de formato de planta
    if not numero.isnumeric() or not (0 <= int(numero) <= 6): 
        print("Por favor, ingresa un número válido entre 0 y 6.")
        return None
    numero = int(numero)
    if numero == 0:
        return -1
    #Quiero que si el usuario pone 0 que no se le pregunte posicion, sino que altiro se vaya a inicio
    
    posicion_usar = input("Elige donde la quieres cultivar (forma x,y): ")
    if ',' not in posicion_usar: #Esto ve que efectivamente se esten metiendo coordenadas
        print("Formato incorrecto. Por favor ingresa las coordenadas en la forma x,y.")
        return None

    #No logré arreglar una entrada como "2,2;ho,la"
    coordenadas = posicion_usar.split(',')

    #Esto hace que si metio algo como 0,a o si puso algo mas largo devuelva error
    if len(coordenadas) != 2 or not coordenadas[0].isnumeric() or not coordenadas[1].isnumeric():
        print("Formato incorrecto. Por favor ingresa las coordenadas en la forma x,y.")
        return None

    x, y = int(coordenadas[0]), int(coordenadas[1])

    if not (0 <= x < len(jardin.tablero[0]) and 0 <= y < len(jardin.tablero)): 
        print("Coordenadas fuera del rango del jardín. Por favor, intenta nuevamente.")
        return None

    return [numero, [x,y]]

def menu_inicio():
    while True: #esto me lo mantiene abierto
        opcion = mostrar_menu_inicio()

        #jardin
        if opcion == '1':
            print("\n-> Accediendo al Menú Jardín")
            menu_jardin()

        #lab
        elif opcion == '2':
            print("\n-> Accediendo al Labroatorio")
            menu_laboratorio()

        #pasar día
        elif opcion == '3': 
            simular_dia()

        #salir
        elif opcion == '0':
            print("\nSaliste de DCCampesino, supongo que vas a seguir tu camino...")
            print("Gracias por ayudar a Hernán a combatir los zombies!!")
            break

        #incorrecto
        else: 
            print("Opcion no válida. Saliendo del programa...")
            break
            
def menu_jardin():
    while True: 
        opcion = mostrar_menu_jardin()

        #intercambiar
        if opcion == '1':
            while True: 
                coords = str(
                    input("Indica las coordenadas de los espacios que quieres intercambiar (de la forma a,b;x,y): ")
                    )
                #Esto me quita tanto todo lo que no sea de forma a,b;x,y y todo lo que se pase de argumentos (ej a,b;x,y;m,n)
                if ';' not in coords or len(coords.split(';')) != 2:
                    print("\nError: Entrada inválida. Asegúrate de usar el formato correcto: a,b;x,y.")
                    break
                coord1, coord2 = coords.split(';') #esto me deja el input como "a,b", "x,y"
                #Esto me evita que se puedan poner cosas como 2,2;hola
                if not (coord1.count(',') == 1 and coord2.count(',') == 1): 
                    print("\nError: Entrada inválida. Asegúrate de usar el formato correcto: a,b;x,y.")
                    break
                x1 = int(coord1.split(',')[0])
                y1 = int(coord1.split(',')[1])
                x2 = int(coord2.split(',')[0])
                y2 = int(coord2.split(',')[1])
                if not (0 <= x1 <= len(jardin.tablero) or 0 <= y1 <= len(jardin.tablero)):
                    print(f"\nCoordenadas {coord1} fuera del rango del tablero.")
                    break
                if not (0 <= x2 <= len(jardin.tablero) or 0 <= y2 <= len(jardin.tablero)):
                    print(f"\nCoordenadas {coord2} fuera del rango del tablero.")
                    break
                coord1 = (x1,y1)
                coord2 = (x2,y2)
                jardin.intercambiar(coord1, coord2)
                print(f"\nExito! El intercambio entre {coord1} y en {coord2} resulto bien")
                break
        
        #cultivar
        elif opcion == '2':
            resultado = mostrar_menu_cultivar()
            if resultado is None:
                continue
            if resultado == -1:
                print("Volviendo al menú de jardín")
                continue
            numero, coordenadas = resultado
            #diccionario para asociar el numero recibidio con la planta
            tipo_planta = {
                1: 'S',  
                2: 'D', 
                3: 'P',  
                4: 'A',  
                5: 'C',  
                6: 'F'   
            }.get(numero)
            if tipo_planta in jardin.inventario_plantas:
                jardin.cultivar_plantas(tipo_planta, coordenadas)
                jardin.inventario_plantas.remove(tipo_planta) #si la planté, no puede seguir en el inventario
            else:
                instancia_planta = jardin.crear_plantas(tipo_planta)
                print(f"No puedes plantar ya que no tienes de esa planta")

        #regar
        elif opcion == '3': 
            vidas_antiguas = []
            for fila in jardin.tablero:
                for celda in fila:
                    if isinstance(celda, Plantas):
                        vida_antigua = celda.vida
                        vidas_antiguas.append(vida_antigua)
            jardin.regar_plantas()
            indice = 0
            print("\n")
            print("-" * 30)
            print("Se han regado tus plantas")
            print("-" * 30)
            for i, fila in enumerate(jardin.tablero):
                for j, celda in enumerate(fila):
                    if isinstance(celda, Plantas):
                        coords = (j,i)
                        vida_nueva = celda.vida
                        print(
                            f"Un {celda.nombre} en {coords} ha subido su salud de {vidas_antiguas[indice]} a {vida_nueva}"
                            )
                        indice += 1
            print("\n")

        #vovler al inicio
        elif opcion == '0':
            print("Volviendo al menú de inicio")
            break

        #incorrecta
        else: 
            print("Opcion no válida. Volviendo el menú de inicio")
            break

def menu_laboratorio():
    while True: 
        opcion = mostrar_menu_laboratorio()
        if opcion == 1:
            jardin.mutar('S', 'D', 'A')
        elif opcion == 2:
            jardin.mutar('S', 'P', 'C')
        elif opcion == 3:
            jardin.mutar('D', 'P', 'F')
        elif opcion == 0: 
            print("Volviendo al menú de inicio")
            break
        else:
            print("Opcion no válida. Volviendo el menú de inicio")
            break

def simular_dia():
    global total_soles
    jardin.actualizar_temperatura()
    jardin.actualizar_dia()
    evento = jardin.inicar_evento(dificultad)
    jardin.descongelar_plantas()
    if evento == 1:
        print("¡Oleada de zombies activada!")
        jardin.activar_zombies(dificultad)
    elif evento == 2:
        print("¡Helada activada!")
        jardin.activar_helada()
    elif evento == 3:
        print("Día tranquilo")
    print("\n")
    soles_producidos = jardin.calcular_soles()
    jardin.soles += soles_producidos
    total_soles = jardin.soles
    print("\n")
    jardin.llegada_plantas()
    print("\n")
    jardin.presentarse()

#Partir todo
menu_inicio()