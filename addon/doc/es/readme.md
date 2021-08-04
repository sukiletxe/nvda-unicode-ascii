# Unicode ASCII (convierte caracteres Unicode en ASCII)

## Introducción

Este complemento intenta resolver el problema con caracteres matemáticos alfanuméricos que, entre otras cosas, ahora se usan con propósito decorativo porque se ven bien en las redes sociales, además de utilizarse con el uso en que fueron pensados. El complemento convierte los caracteres que se le pasan a una representación cercana en ASCII, así que también se puede utilizar para convertir cualquier otro símbolo. Desgraciadamente, los resultados no siempre son perfectos ni buenos porque a veces los caracteres decorativos se utilizan por similitud con el caracter que se quiere escribir, y no por su significado.

Nota: Este complemento puede no transliterar japonés o chino (entre otros) correctamente, ya que la librería que utiliza no tiene ninguna forma para adivinar el idioma del texto. Además, si no puede transliterar un caracter lo dejará sin tocar, por lo cual el resultado puede no ser siempre ASCII.

## Modo de uso

* Pulsa NVDA+Ctrl+N para decodificar el texto seleccionado. Si lo pulsas dos veces el resultado se copiará al portapapeles.
* Pulsa CTRL+Shift+NVDA+N para decodificar el texto del portapapeles. Si lo pulsas dos veces el resultado se copiará.

Estos gestos se pueden cambiar en el diálogo de gestos de entrada, en la categoría unicodeAscii.

## Qué hacer cuando la transliteración falla

Puedes usar [el complemento información del caracter][charinfo] para obtener más información sobre un caracter, y si quieres, añadirlo al diálogo de pronunciación de puntuación y símbolos o al diccionario por defecto.

## Registro de cambios

### 1.0.1

* Ahora el texto que no se pueda convertir se mantendrá en lugar de reemplazarse por signos de interrogación.

### 1.0

* Versión inicial.

## Agradecimientos


* A Jesús Pavón por la idea.
* Javi Domínguez por [FEN Reader][FEN]. La mayoría del código de este complemento está basado en el suyo.
* Sean M. Burke por `Text::Unidecode` y Tomaž Šolc por [Unidecode].
* [Nikola] por ser genial y utilizar Unidecode (ahí supe de su existencia).

[FEN]: https://github.com/javidominguez/FenReader/
[Unidecode]: https://github.com/avian2/unidecode
[Nikola]: https://getnikola.com/avian2/unidecode
[charinfo]: https://addons.nvda-project.org/addons/charInfo.es.html
