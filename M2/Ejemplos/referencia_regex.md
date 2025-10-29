| Símbolo | Significado                                      | Ejemplo         | Qué coincide                     |     |              |
| ------- | ------------------------------------------------ | --------------- | -------------------------------- | --- | ------------ |
| `^`     | Inicio de la cadena                              | `^Hola`         | Coincide si empieza con “Hola”   |     |              |
| `$`     | Final de la cadena                               | `fin$`          | Coincide si termina con “fin”    |     |              |
| `.`     | Cualquier carácter excepto salto de línea        | `a.c`           | "abc", "a-c", "a_c"...           |     |              |
| `\d`    | Un dígito (0-9)                                  | `\d\d`          | "12", "34"                       |     |              |
| `\w`    | Carácter alfanumérico (letras, números o `_`)    | `\w+`           | "hola123", "A_B"                 |     |              |
| `\s`    | Espacio en blanco (incluye tab y salto de línea) | `\s+`           | "  " o "\t"                      |     |              |
| `{n}`   | Repite n veces                                   | `\d{3}`         | "123"                            |     |              |
| `{n,m}` | Entre n y m repeticiones                         | `\d{2,4}`       | "12", "123", "1234"              |     |              |
| `[ ]`   | Clase de caracteres (uno de estos)               | `[aeiou]`       | “a”, “e”, “u”…                   |     |              |
| `[^ ]`  | Negación dentro de clase                         | `[^0-9]`        | Cualquier cosa que NO sea dígito |     |              |
| `( )`   | Grupo de captura                                 | `(\d{3})-\d{3}` | Permite extraer el grupo         |     |              |
| `       | `                                                | OR (o)          | `com                             | es` | “com” o “es” |
| `+`     | 1 o más repeticiones                             | `\d+`           | "1", "25", "999"                 |     |              |
| `*`     | 0 o más repeticiones                             | `\w*`           | "", "a", "hola"                  |     |              |
| `?`     | Opcional (0 o 1)                                 | `https?`        | "http" o "https"                 |     |              |
| `\\`    | Escape (para usar símbolos literales)            | `\.`            | Un punto real “.”                |     |              |
