# TACO122-037-electronica2025
repositorio del curso Electrónica Digital: del Dato al Objeto del Departamento de Artes Visuales de la Universidad de Chile

## Planificación

| clase | día     | clase                                                                                               |
|-------|---------|---------------------------------------------------------------------------------------------------- |
|     1 |   7 ago |  bitácora, lista de materiales, programa, introducción github, preguntar por compu, referentes      |
|     2 |  14 ago | Intro programación en processing: variables, funciones, strings, print                              |
|     3 |  21 ago | Intro programación en arduino, señal digital, morse                                                  |
|     4 |  28 ago | Señales analógicas de entrada y salida                                                              |
|     5 |  4 sept | display 7 segmentos, cátodo común, números binarios                                                |
|     6 | 11 sept | i2c y pantallas (16x2? OLED? 8x8?). EVALUACIÓN NOTA 1                                                                  |
| x     | 18 sept | feriado                                                                                            |
|     7 | 25 sept | processing, texto, cámara                                                                          |
|     8 |   2 oct | guardar datos en tarjeta SD (spi)                                                                  |
|     9 |   9 oct | teclado experimental con encoder y sensor capacitivo                                               |
|    10 |  16 oct | mouse experimental con acelerómetro y giroscopio                                                   |
|    11 |  23 oct | intro sonic pi                                                                                     |
|    12 |  30 oct | controlador midi                                                                                   |
|    13 |   6 nov | proyecto individual                                                                                |
|    14 |  13 nov | proyecto individual                                                                                |
|    15 |  20 nov | proyecto individual                                                                                |
|    16 |  27 nov | proyecto individual                                                                                |
|    17 |   4 dic | exámenes                                                                                           |
|    18 |  11 dic | exámenes                                                                                           |

## Bitácoras de estudiantes

| estudiante | enlace |
|--------------|------|
| estudiante02 | [link](https://github.com/koydfripp/No-se-usar-github-ayuda.git) |
| estudiante03 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante04 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante05 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante06 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante07 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante08 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante09 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante10 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante11 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante12 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante13 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |
| estudiante14 | [link](https://github.com/misaaaaaa/TACO122-037-electronica2025#) |

## Evaluaciones

- Nota 1
    - Un proyecto de resolución de problema interconexión de un sensor y un actuador (50%) 
    - Procesos de bitácora de ejercicios dados clase a clase hasta ese punto
- Nota 2
    - Anteproyecto artístico
    - Procesos de bitácora
- Nota 3
    - Avance de proyecto final en última clse del semestre
    - Documentación en bitácora

La nota final está compuesta de la ponderación de la nota de presentación y la nota de examen. git sLa nota de presentación será el promedio de las 3 notas anteriores, y conformará el 60% de la nota final del curso. El otro 40% corresponde al examen.

### Nota para el profesor

Para trabajar con submódulos:

- Crear carpeta para recibir cada bitácora e ir a ella

```
cd bitacoras
```

- Para agregar submódulo

```
git submodule add <enlace-repo-bitácora> bitacora1   
```

- Si clonas un repositorio que tiene submódulos es necesario incluirlos luego de clonarlos

```
git submodule init
git submodule update
```

- Para que Git incluya automáticamente los submódulos en ciertos comandos sin que tengas que poner la opción --recurse-submodules cada vez

```
git config submodule.recurse true
```



- Utilizar este comando para hacer un pull que incluya los submódulos

```
git pull --recurse-submodules && git submodule update --remote --merge --recursive
```

- Se puede configurar un alias para que haga todo esto más rápido

```
git config --global alias.pullall '!git pull --recurse-submodules && git submodule update --remote --merge --recursive'
```
