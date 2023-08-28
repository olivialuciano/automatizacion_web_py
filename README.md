# Automatización y Web Scraping en Supermercados de la ciudad de Messi (Rosario).

¡Bienvenido al proyecto de Automatización y Web Scraping en Supermercados! Este script, desarrollado en Python utilizando las bibliotecas Selenium y Helium, te permite buscar productos en diferentes supermercados, obtener sus nombres y precios, y guardarlos en un archivo JSON para una rápida referencia.

### ¡Automatizá la búsqueda de precios y ahorra dinero en tus compras diarias!

## Características

- **Tecnologías Utilizadas:** Python, Selenium, Helium
- **Métodos de Búsqueda:** CSS Selectors, XPath
- **Funcionalidad Principal:** Búsqueda de productos en supermercados, obtención de nombres de productos y sus precios, almacenamiento en un archivo JSON y su eliminación posterior.

## Cómo Funciona

1. **Iniciar el Script:** Al ejecutar el script, te hará una serie de preguntas como, por ejemplo, en qué zona de rosario querés buscar para discriminar los supermercados que te quedan lejos. También, te pedirá que ingreses el nombre del producto que deseas buscar.

2. **Búsqueda en Supermercados:** Utilizando web scraping, el script buscará el producto en varias páginas web de supermercados. Esto es mediante la combinación de clases CSS y rutas XPath.

3. **Extracción de Datos:** Una vez que se encuentran los resultados, el script extraerá los nombres y precios de los productos en cada supermercado.

4. **Almacenamiento en JSON:** Los datos obtenidos se organizarán en un formato JSON fácilmente legible para que puedas comparar precios tranquilamente.

5. **Eliminación:** Para no ocupar espacio, al finalizar de leer el archivo, puedes eliminar el archivo JSON presionando "Enter".

## Por qué esto

La idea surgió de la necesidad de encontrar rápidamente los precios más bajos para productos cotidianos. Por ejemplo, la yerba mate playadito. La yerba no es un producto muy barato entonces se me ocurrió automatizar un poco la tradicional búsqueda manual de precios. Con este script, podés:

- **Ahorrá Tiempo:** Evitá la molestia de buscar manualmente en varios sitios web de supermercados.
- **Tomá Decisiones Informadas:** Compará rápidamente los precios y tomá decisiones de compra más inteligentes.

## Requisitos y Uso

Para utilizar este script, asegúrate de tener instaladas las bibliotecas de Python: Selenium y Helium. También se requiere tener google chrome.

1. Instalá las bibliotecas requeridas usando: `pip install selenium helium`
2. Descargá google chrome si no lo tenés.
3. Ejecutá el script y seguí las instrucciones para buscar productos y obtener los precios.

