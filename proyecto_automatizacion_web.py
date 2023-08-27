from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
chromedriver_autoinstaller.install()
import subprocess
import os
import json
####### VER EL TEMA DE LOS PRECIOS CUANDO TIENEN DESCUENTO
####### NO SÉ SI ESTAS PÁGINAS SON DINÁMICAS
######## CARREFOUR CORREGIR PRECIOS CON MIL
######## VER DE AGREGAR SECCION EJ ALMACEN, FREEZADOS

# ARRANCAR
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()
while start != 'S' and start != 'N':
    print("Respuesta inválida. Le preguntaremos de nuevo.")
    start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()

if start == 'S':
    # ARCHIVO
    #file = str(input("¿En donde desea crear el archivo del listado de productos? Por favor ingrese la ruta ")) ## CREAR ARCHIVO TEMPORAL

    # LOCACIÓN
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) ")).upper()
    while location != "Q" and location != "C" and location != "S" and location != "O" and location != "F" and location != "N" :
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) "))
    # PRODUCTO
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    product = str(input("Ingrese el producto a buscar: "))
    print("Buscando el producto ", product, "... (te aviso que va a demorar bastante)")

    products_data_la_gallega = []
    products_data_la_reina = []
    products_data_coto = []
    products_data_carrefour = []
    products_data_jumbo = []

    # ############### 1 LA GALLEGA #################################

    def la_gallega_1(product):
        he.start_chrome("https://www.lagallega.com.ar/login.asp")
        print("estamos buscando en La Gallega...")
        #time.sleep(5)
        search_box1 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box1.exists)
        he.click(search_box1)
        search_box12 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box12.exists)
        he.write(product, into=search_box12)
        he.press(he.ENTER)
        time.sleep(2)
        #list_of_cards = he.find_all(he.S(".cuadProd"))
        #he.wait_until(list_of_cards.exists)
        #len(list_of_cards)+1
        try:
            for i in range (1, 3) :
                product_name = (he.find_all(he.S(".desc"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".izq"))[i-1]).web_element.text
                products_data_la_gallega.append((product_name, product_price))
        except:
            print("No hemos encontrado el artículo.")
            products_data_la_gallega.append("Artículo no encontrado")
        he.kill_browser()

    # # ############### 2 LA REINA ###################################
    def la_reina_2(product):
        he.start_chrome("https://www.lareinaonline.com.ar/")
        print("estamos buscando en La Reina...")
        #time.sleep(5)
        search_box2 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box2.exists)
        he.click(search_box2)
        search_box22 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box22.exists)
        he.write(product, into=search_box22)
        he.press(he.ENTER)
        time.sleep(2)
        #list_of_cards = he.find_all(he.S(".cuadProd"))
        try:
            for i in range (1, 3) :
                product_name = (he.find_all(he.S(".desc"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".izq"))[i-1]).web_element.text
                products_data_la_reina.append((product_name, product_price))
            #print(products_data_la_reina)
        except:
            print("No hemos encontrado el artículo.")
            products_data_la_reina.append("Artículo no encontrado")
        #acorto los productos a 2 porque hay productos cuyo precio esta en descuento y entonces cambia la clase css :( HAY QUE ARREGLAR
        he.kill_browser()

    ############### 3 COTO #######################################    #NO PUDE EXTRAER EL NOMBRE DE LOS PRODUCTOS
    def coto_3(product):
        he.start_chrome("https://www.cotodigital3.com.ar/sitios/cdigi/")
        time.sleep(4)
        search_box3 = he.find_all(he.S("#atg_store_searchInput"))[0]
        he.wait_until(search_box3.exists)
        he.write(product, into=search_box3)
        he.press(he.ENTER)
        time.sleep(6)
    
        # xPath porque coto hace imposible buscar un elemento porque todos los ids de ccs los hace distintos
        # x_path_product_name = "//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[3]/div[1]/div/a/span[2]/div/span/div/div[1]"
        # x_path_product_price = "//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[1]/div[2]/div[1]/div[1]/span/span"
        # /html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[2]/div[2]/div[1]/div[1]/span/span
        # /html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[3]/div[2]/div[1]/div[1]/span/span
        # /html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[1]/div[2]/div[1]/div[1]/span/span

        # "//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[{i}]/div[1]/div/a/span[2]/div/span/div"
        # /html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[2]/div[1]/div/a/span[2]/div/span/div
        # /html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[3]/div[1]/div/a/span[2]/div/span/div/div[1]


        #list_of_cards = he.find_all(he.S(".clearfix"))
        try:
            for i in range (1, 3) :
                product_name = (he.find_all(he.S(f"//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[{i}]/div[1]/div/a/span[2]/div/span/div"))[0]).web_element.text
                product_price = (he.find_all(he.S(f"//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[{i}]/div[2]/div[1]/div[1]/span/span"))[0]).web_element.text
                products_data_coto.append((product_name, product_price))
        except:
            print("No hemos encontrado el artículo.")
            products_data_coto.append("Artículo no encontrado")
        he.kill_browser()

    # ############### 4 CARREFOUR ##################################  #downshift-1-input ##VER TEMA PRECIOS QUE APARECEN MAL
    def carrefour_4(product):
        he.start_chrome("https://www.carrefour.com.ar/")
        print("estamos buscando en Carrefour...")
        time.sleep(8)
        search_box3 = he.find_all(he.S(".vtex-styleguide-9-x-input"))[0]
        he.wait_until(search_box3.exists)
        he.write(product, into=search_box3) 
        he.press(he.ENTER) #tarda bastante en buscar la zanahoria y aparece abajo todo desubicado
        time.sleep(6)
        #list_of_cards = he.find_all(he.S(".valtech-carrefourar-product-summary-status-0-x-container"))
        #len(list_of_cards)+1
        try:
            for i in range (1, 3) :
                product_name = (he.find_all(he.S(".vtex-product-summary-2-x-productNameContainer"))[i-1]).web_element.text
                product_price_int = (he.find_all(he.S(".valtech-carrefourar-product-price-0-x-currencyInteger"))[i-1]).web_element.text
                product_price_frac = (he.find_all(he.S(".valtech-carrefourar-product-price-0-x-currencyFraction"))[i-1]).web_element.text
                products_data_carrefour.append((product_name, ("$ "+ product_price_int+ ","+ product_price_frac)))
        except:
            print("No hemos encontrado el artículo.")
            products_data_carrefour.append("Artículo no encontrado")

        he.kill_browser()

    # ############### 5 JUMBO ######################################
    def jumbo_5(product):
        he.start_chrome("https://www.jumbo.com.ar/")
        print("estamos buscando en Jumbo...")
        time.sleep(2)
        search_box5 = he.find_all(he.S(".vtex-styleguide-9-x-input"))[0]
        he.wait_until(search_box5.exists)
        time.sleep(3)
        he.write(product, into=search_box5)
        he.press(he.ENTER)
        time.sleep(5)
        #list_of_cards = he.find_all(he.S(".vtex-search-result-3-x-galleryItem"))
        try:
            for i in range (1, 3) :
                product_name = (he.find_all(he.S(".vtex-product-summary-2-x-productBrand"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".productPrice"))[i-1]).web_element.text
                products_data_jumbo.append((product_name, product_price))
        except:
            print("No hemos encontrado el artículo.")
            products_data_jumbo.append("Artículo no encontrado")
        he.kill_browser()


    # DEPENDIENDO ZONA, CUALES FUNCIONES
    if location == 'Q':
        la_gallega_1(product)
        la_reina_2(product)
        coto_3(product)
        carrefour_4(product)
        jumbo_5(product)
    elif location == 'C' or location == 'F':
        la_gallega_1(product)
        coto_3(product)
    elif location == 'S':
        la_reina_2(product)
    elif location == 'O':
        coto_3(product)
        carrefour_4(product)
    elif location == 'N':
        la_gallega_1(product)
        coto_3(product)
        jumbo_5(product)

################## archivo agregar data #############################

    file_name = "informacion_productos_precios.json"

    data = {
        "Supermercados": {
            "La Gallega": products_data_la_gallega,
            "La Reina": products_data_la_reina,
            "Coto": products_data_coto,
            "Carrefour": products_data_carrefour,
            "Jumbo": products_data_jumbo
        }
    }
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    # ABRIR ARCHIVO
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    open_file = str(input("desea ahora abrir el archivo para ver los productos y precios? s/n ")).upper()
    while open_file != 'S' and open_file != 'N':
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        open_file = str(input("desea ahora abrir el archivo para ver los productos y precios? s/n "))
    if open_file == 'S':
        try:
            subprocess.Popen(['notepad', file_name], shell=True)
        except:
            print("Ocurrió un error al abrir el archivo.")
    else:
        print("Bueno, no se va a abrir.")

    # BORRAR ARCHIVO
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    delete_file = str(input("Cuando presione ENTER, el archivo será eliminado."))

    try:
        os.remove(file_name)
        print("El archivo se eliminó correctamente.")
    except:
        print("Ocurrió un error y no se eliminó el archivo.")
    print("---------------------------------")
    print("Espero que te hayamos ayudado <3")
    print("---------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    print("---------------------------------")
    print("Bueno, gracias por elegirnos(?")
    print("---------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
