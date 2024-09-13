# Tarea 2: DCCampesino 🌻🧟

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### Programación Orientada a Objetos: 16 pts (10%)
##### 🟠 Definición de clases, herencia y *properties*: Por lo que pude ver debería estar todo funcionando correctamente. EL único problema sería la clase abstracta, no entendí como se usaba así que no incluí ninguna, pero las plantas funcionan bien y estan heredando correctamente.

#### Preparación del programa: 6 pts (4%)
##### ✅ Inicio de la partida: Funciona correctamente. Además, si el usuario elige un tablero o dificultad no valida se le pedirá de nuevo.

#### Entidades: 64 pts (39%)
##### Jardín: Quiero especificar cada funcionamiento del jardín.
##### ✅ 1. Modelo correcto del jardín: Acá me costo bastante y tomo mucha busqueda entender que la opción classmethod para cargar el archivo y que se creara el jardín era lo mejor para este caso y que funcionará como yo quería. Luego de eso puedo decir que esta funcionando correctamente, el jardín se crea con todos sus atributos y si no existe el nombre en jardines.txt no lo crea. 
##### ✅ 2. Método cultivar: Funciona correctamente.
##### ✅ 3. Método regar: Funciona correctamente.
##### ✅ 4. Método mutar: Funciona correctamente.
##### ✅ 5. Método presentarse: Acá esto lo dividí en 2. Esta presentarse, que hace tal cual lo que pide el enunciado, pero además está mostrar_jardin(), que solo muestra el tablero con las plantas presentes, esto lo hice para poder usar mostrar_jardin en el menu de jardin y esa la implemente dentro de presentarse().

##### Plantas: Quiero especificar cada funcionamiento de las plantas.
##### ✅🟠 1. Modelar cada planta: Pongo ambos emojis por que creo haber entendido y aplicado herencia de forma correcta.
##### ✅ 2. Modelar atributos de la planta: Funciona correctamente.
##### ✅ 3. Metodo regarse: Funciona correctamente.
##### ✅ 4. Potencial y producción de soles del Solaretillo: Funciona correctamente.
##### ✅ 5. Armadura del Defensuace: Funciona correctamente.
####  🟠 6. Aumento del Potencilantro: Quizás es por como definí los parámetros pero no note un aumento significativo con y sin la presencia del potencilantro, pero creo que si funciona bien y es un tema de parámetros.
##### 🟠 7. Funcionalidades adicionales del Aresauce: Mismo tema que el potencilantro pero el reducir robo.
##### 🟠 8. Funcionalidades adicionales del Cilantrillo: Mismo tema que el potencilantro.
##### 🟠 9. Funcionalidades adicionales del Fensaulantro: Mismo tema que el potencilantro pero el reducir ataque.

#### Flujo del programa: 40 pts (24%)
##### ✅ Menú de Inicio: Funciona correctamente.
##### ✅ Menú Jardín: Funciona correctamente.
##### ✅ Laboratorio: Funciona correctamente.
##### ✅ Fin del juego: Funciona correctamente.
##### 🟠 Robustez: Con la cantidad de menus e inputs posibles en esta tarea estoy seguro que algun input erroneo no debo estar pudiendo captar y responder a el adecuadamente. Si considero que está bastamte robusto pero algo puede faltar.

#### Simular día: 23 pts (14%)
##### ✅ Temperatura: Funciona correctamente.
##### ✅ Eventos: Funciona correctamente.
##### ✅ Calcular soles: Funciona correctamente.
##### ✅ Llegada de plantas: Funciona correctamente.
##### ✅ Presentación: Funciona correctamente.

#### Archivos: 15 pts (9%)
##### ✅ Archivos.txt: Implementado correctamente.
##### ✅ parametros.py: Implementado correctamente.


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```entidades.py``` en ```la misma carpeta```
2. ```parametros.py``` en ```la misma carpeta```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```os.path.join / entidades.py```
2. ```sys```: ```sys.argv / main.py```
3. ```random```: ```random.randint y random.random / entidades.py```

### Librerías propias
No use librerias propias.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <La mayoría del programa es trabajado  y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>
1. \<https://www.geeksforgeeks.org/enumerate-in-python/>: este hace \<for x, y in enumerate()> y está implementado en el archivo <main.py y entidades.py> en las líneas <215, 216 y 144, 145, 261, 262, 326, 327, respectivamente> y hace <para los for _ in range, ayuda a iterar sobre 2 parametros, uno que solo va contando y otro que recorre los elementos de la lista u objeto sobre el cual itero>.

2. \<https://www.dataquest.io/blog/basic-statistics-in-python-probability/>: este hace \<random.random()> y está implementado en el archivo <entidades.py> en las líneas <252 y 254> y hace <genera, aleatoriamente, un número entre 0 y 1. Esto me fue útil para ver lo de las probabilidades de oleadas de zombies y heladas. Vi el ejemplo en el link donde usaba random.random para activar una probabilidad de 0.5 e hice lo mismo.>

3. \< https://www.w3schools.com/python/ref_func_isinstance.asp>: este hace \<if isinstance (x,y)> y está implementado en el archivo <main.py y entidades.py> en las líneas <74, 105, 187, 193, 263, 284, 292, 328, 333, 339, 345, 378 y 206, 217, respectivamente> y hace <revisa si lo que le entregaste (primer parámetro) es una instancia del segundo parámetro. Esto me sirvió mucho para funciones donde revisaba todo el tablero y tenía que hacer distintas cosas si es que en la celda había una planta o estaba vacío (X)>

4. \<https://www.w3schools.com/python/ref_string_isnumeric.asp>: este hace \<x.isnumeric()> y está implementado en el archivo <main.py> en las líneas <89 y 104> y hace <revisa si lo que le entregas tiene solo caracteres numéricos y retorna true de ser el caso. Me ayudo para captar errores en el menu cultivar.>

5. \<https://www.eumus.edu.uy/eme/ensenanza/electivas/python/2020/clase_08a.html#:~:text=La%20funci%C3%B3n%20sys.,se%20los%20llama%20argumentos%20posicionales>: este hace \<sys.argv[x]> y está implementado en el archivo <main.py> en las líneas <6 y 7> y hace <hace que pueda pedirle al usuario 2 inputs que vayan junto a la inicialización del programa. Luego toma esos 2 inputs y se los entrega al programa para que este pueda trabajar con el nombre del jardín y la dificultad seleccionada por el usuario.>

6. \<https://www.w3schools.com/python/python_variables_global.asp>: este hace \<global x> y está implementado en el archivo <main.py> en la línea <251> y hace <hace que la variable total_soles. Esto lo implemente ya que antes de tenerlo la terminal me entregaba lo siguiente: ... cannot access local variable total_soles .... Entonces busque como podía solucionar eso y encontre que si antes de empezar el proceso en la función llamaba a la variable global, la podía usar sin problemas.>

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/main/Tareas/Bases%20Generales%20de%20Tareas%20-%20IIC2233.pdf).