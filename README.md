# Automatización y Web Scraping en Supermercados de la ciudad de Rosario.

¡Bienvenido al proyecto de Automatización y Web Scraping en Supermercados! Este script, desarrollado en Python utilizando las bibliotecas Selenium y Helium, te permite buscar productos en diferentes supermercados, obtener sus nombres y precios, y guardarlos en un archivo JSON para una rápida referencia.

### ¡Automatizá la búsqueda de precios y ahorrá dinero en tus compras diarias!

## Características

- **Tecnologías Utilizadas:** Python, Selenium, Helium
- **Métodos de Búsqueda:** CSS Selectors, XPath
- **Funcionalidad Principal:** Búsqueda de productos en supermercados, obtención de nombres de productos y sus precios, almacenamiento en un archivo JSON y su eliminación posterior. Además, tenés la opción de ver un video receta de youtube sobre el producto consultado.

## Cómo Funciona

1. **Iniciar el Script:** Al ejecutar el script, te hará una serie de preguntas como, por ejemplo, en qué zona de rosario querés buscar para discriminar los supermercados que te quedan lejos. También, te pedirá que ingreses el nombre del producto que deseas buscar.

2. **Búsqueda en Supermercados:** Utilizando web scraping, el script buscará el producto en varias páginas web de supermercados. Esto es mediante la combinación de clases CSS y rutas XPath.

3. **Extracción de Datos:** Una vez que se encuentran los resultados, el script extraerá los nombres y precios de los productos en cada supermercado.

4. **Almacenamiento en JSON:** Los datos obtenidos se organizarán en un formato JSON fácilmente legible para que puedas comparar precios tranquilamente.

5. **Eliminación:** Para no ocupar espacio, al finalizar de leer el archivo, puedes eliminar el archivo JSON presionando "Enter".

6. **Video receta:** Una vez eliminado el archivo puedes optar por ver un video receta del producto buscado.

## Por qué esto

La idea surgió de la necesidad de encontrar rápidamente los precios más bajos para productos cotidianos. Por ejemplo, la yerba mate playadito. La yerba no es un producto muy barato entonces se me ocurrió automatizar un poco la tradicional búsqueda manual de precios. Con este script, podés:

- **Ahorrá Tiempo:** Evitá la molestia de buscar manualmente en varios sitios web de supermercados.
- **Tomá Decisiones Informadas:** Compará rápidamente los precios y tomá decisiones de compra más inteligentes.
- **Encontrar una buena receta:** Sin siquiera hacer un click vas a acceder a una excelente receta de youtube sobre el producto que buscaste.

## Requisitos y Uso

1. Si no tenés Python instalado en la compu, podés descargarlo mediante este link: https://www.python.org/downloads/ e instalarlo.
2. Descargá Selenium: pip install selenium
3. Descargá google chrome si no lo tenés.
4. Ejecutá el script.
