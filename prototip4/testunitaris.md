# TEST UNITARIS

### ¿Qué son los test unitarios?

Las pruebas unitarias son el proceso en el que se prueba la unidad funcional de código más pequeña. Las pruebas de software ayudan a garantizar la calidad del código y son una parte integral del desarrollo de software. Una práctica recomendada en el desarrollo de software es escribir el software como unidades pequeñas y funcionales, y luego escribir una prueba unitaria para cada unidad de código.

Una prueba unitaria es un bloque de código que verifica la precisión de un bloque más pequeño y aislado de código de aplicación, normalmente una función o un método. La prueba unitaria está diseñada para verificar que el bloque de código se ejecuta según lo esperado, de acuerdo con la lógica teórica del desarrollador. La prueba unitaria solo interactúa con el bloque de código a través de entradas y salidas (verdaderas o falsas) capturadas afirmadas. 

### ¿Cómo funciona específicamente la librería unittest de Python?

Unittest es una librería estándar del lenguaje de programación Python. Gracias a los módulos y herramientas que posee, se puede ejecutar un test para comprobar las funciones de tu código, encontrar errores y facilitar el desarrollo del programa.
Con la librería Unittest en Python podrás comprobar todos los casos cada vez que se hace una prueba y, por lo tanto, es menos probable que el programa falle por errores del inicio o por casos específicos, si se testan mucho más tarde en la programación.
Podrás ir resolviendo los fallos mientras se desarrolla en lugar de volver a empezar.

### Lista de 'assertions' más importantes

Las assertions son métodos utilizados para verificar que el resultado real sea el esperado. Algunas de las más importantes son:

assertEqual(a, b): Comprueba que a y b sean iguales.

assertNotEqual(a, b): Comprueba que a y b no sean iguales.

assertTrue(x): Comprueba que x sea verdadero (True).

assertFalse(x): Comprueba que x sea falso (False).

assertIsNone(x): Comprueba que x sea None.

assertIsNotNone(x): Comprueba que x no sea None.

assertRaises(exception, func, *args, kwargs): Comprueba que se lance una excepción cuando se llama a la función func con los argumentos especificados.

Estas assertions son esenciales para garantizar que el comportamiento del código sea el deseado en todos los casos de prueba.