**Punto 3: Programa Radio**

`PROGRAMA<radio, año, programa, conductor, gerente, frecuencia_radio>`

1. **Restricciones**
    1. Una radio se transmite por una única frecuencia (frecuencia_radio) en un año
determinado, y puede cambiarla en años diferentes.
    2. Cada radio tiene un único gerente por año, pero el mismo gerente puede repetirse en la
misma radio en diferentes años. Y la misma persona puede ser gerente de diferentes
radios durante el mismo año.
    3. Un mismo programa puede transmitirse por varias radios y en diferentes años.
    4. Un programa transmitido en una radio en un año determinado tiene un solo conductor

### Paso 1: Determinar las dependecnias Funcionales

A partir del esquema y las restricciones dadas, podemos determinar las siguientes dependencias funcionales:

1. **radio, año -> frecuencia_radio**: Una radio es transmitida en una unica frecuencia en un determinado año, por lo tanto el atributo `frecuencia_radio` depende funcionalmente de `radio` y de `año`.
2. **radio, año -> gerente**: Cada radio tiene un gerente por año, esto implica que `gerente` depende de `radio` y de `año`.
3. **programa, radio, año -> conductor**: un programa transmitido en una radio en un determinado año tiene un solo conductor, asi que `conductor` depende de `programa`, `radio` y `año`.

### Paso 2: Determinar las Claves Candidatas
- La combinacion de **`radio`, `programa`, `año`**, permite identificar de forma única cada fila en la tabla `PROGRAMA`:
    - `año`: representa al año.
    - `radio`: representa a la radio.
    - `programa`: representa al programa que se transmite en la radio.

Esto se debe a que en la restriccion ***iii*** dice que un mismo programa se puede transmitir por varias radios y en diferentes años. A partir de esto, con las columnas de radio y año solamente no podemos diferenciar cada registro en la tabla, ya que en la misma radio y mismo año puede haber mas de un programa.

Por lo tanto la clave candidata es: (`radio`, `programa`, `año`) ya que la combinacion de estos 3 atributos daría como resultado una única fila.

### Paso 3: Diseño en Tercera Forma Normal

El nuevo diseño en 3FN sería el siguiente:

1. **Tabla `Radio`**

    - `radio`
    - `año`
    - `frecuencia_radio`
    - `gerente`
    - Clave Primaria Compuesta: (`radio`, `año`)


2. **Tabla `PROGRAMA`**

    - `radio`(clave foranea que referencia a `Radio`)
    - `programa`
    - `año` (clave foranea que referencia a `Radio`)
    - `conductor`
    - Clave Primaria Compuesta: (`radio`, `programa`, `año`)