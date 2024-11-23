***Sistema de ventas en Linea***

El sistema está compuesto por las siguientes entidades:
1. **Clientes** (entidad fuerte)
2. **Productos** (entidad fuerte)
3. **Ordenes** (entidad debil)
4. **Categorias** (entidad debil)


El diseño en 3FN sería el siguiente:

1. **Tabla `Categorias`**
    - `id_categoria` (clave primaria)
    - `nombre_categoria`
    La clave primaria `id_categoria` identifica de manera única a cada categoria, a su vez que `nombre_categoria` depende de `id_categoria`.
.
2. **Tabla `Productos`**
    - `id_producto` (clave primaria)
    - `nombre_producto`
    - `precio`
    - `id_categoria` (clave foranea que referencia a `Categorias`)
    - `cantidad_stock`
    La clave primaria `id_producto` identifica de manera única a cada producto de la tabla `Productos`
    La clave foranea `id_categoria` referencia a una única categoria de la tabla `Categorias`, además de que los demas atributos dependen unicamente de `id_producto`.
.
3. **Tabla `Clientes`**
    - `id_cliente` (clave primaria)
    - `nombre_cliente`
    - `apellido_cliente`
    - `direccion`
    La clave primaria `id_cliente` identifica de manera única a cada cliente de la tabla `Clientes`, además de que los demas atributos dependen unicamente de `id_cliente`.
.
4. **Tabla `Ordenes`**
    - `id_orden` (clave primaria)
    - `id_producto` (clave foranea que referencia a `Productos`)
    - `id_cliente` (clave foranea que referencia a `Clientes`)
    - `fecha`
    - `cantidad_unidades`
    La clave primaria `id_cliente` identifica cada cliente de la tabla `Clientes`, además de que los demas atributos dependen unicamente de `id_orden` y no hay dependencias funcionales transitivas.
