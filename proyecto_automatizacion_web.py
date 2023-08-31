from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
chromedriver_autoinstaller.install()
import subprocess
import os
import json

# ARRANCAR
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()
while start != 'S' and start != 'N':
    print("Respuesta inválida. Le preguntaremos de nuevo.")
    start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()

if start == 'S':
    # LOCACIÓN
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) ")).upper()
    while location != "Q" and location != "C" and location != "S" and location != "O" and location != "F" and location != "N" :
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) ")).upper()
    # PRODUCTO
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    product = str(input("Ingrese el producto a buscar: "))
    print("Buscando el producto ", product, "... (te aviso que va a demorar bastante)")

    products_data_la_gallega = []
    products_data_la_reina = []
    products_data_coto = []
    products_data_carrefour = []
    products_data_jumbo = []

    #### 1 LA GALLEGA
    def la_gallega_1(product):
        print("estamos buscando en La Gallega...")
        he.start_chrome("https://www.lagallega.com.ar/login.asp")
        time.sleep(6)
        search_box1 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box1.exists)
        he.click(search_box1)
        search_box12 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box12.exists)
        he.write(product, into=search_box12)
        he.press(he.ENTER)
        time.sleep(4)
        #list_of_cards = he.find_all(he.S(".cuadProd"))
        for i in range (1, 3) :
            try:
                product_name = (he.find_all(he.S(".desc"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".izq"))[i-1]).web_element.text
                products_data_la_gallega.append(("producto: " + product_name, "precio: " + product_price))
            except:
                print(f"No hemos encontrado el artículo {i}.")
                products_data_la_gallega.append(f"Artículo {i} no encontrado")
        he.kill_browser()

    #### 2 LA REINA 
    def la_reina_2(product):
        print("estamos buscando en La Reina...")
        he.start_chrome("https://www.lareinaonline.com.ar/")
        time.sleep(6)
        search_box2 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box2.exists)
        he.click(search_box2)
        search_box22 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box22.exists)
        he.write(product, into=search_box22)
        he.press(he.ENTER)
        time.sleep(4)
        #list_of_cards = he.find_all(he.S(".cuadProd"))
        for i in range (1, 3) :
            try:
                product_name = (he.find_all(he.S(".desc"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".izq"))[i-1]).web_element.text
                products_data_la_reina.append(("producto: " + product_name, "precio: " + product_price))
            except:
                print(f"No hemos encontrado el artículo {i}.")
                products_data_la_reina.append(f"Artículo {i} no encontrado")
        he.kill_browser()

    #### 3 COTO
    def coto_3(product):
        print("estamos buscando en Coto...")
        he.start_chrome("https://www.cotodigital3.com.ar/sitios/cdigi/")
        time.sleep(8)
        search_box3 = he.find_all(he.S("#atg_store_searchInput"))[0]
        he.wait_until(search_box3.exists)
        he.write(product, into=search_box3)
        he.press(he.ENTER)
        time.sleep(7)
        #list_of_cards = he.find_all(he.S(".clearfix"))
        for i in range (1, 3) :
            try:
                product_name = (he.find_all(he.S(f"//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[{i}]/div[1]/div/a/span[2]/div/span/div"))[0]).web_element.text
                product_price = (he.find_all(he.S(f"//html/body/div[5]/div[2]/div/div/div[3]/div/div[1]/ul/li[{i}]/div[2]/div[1]/div[1]/span/span"))[0]).web_element.text
                products_data_coto.append(("producto: " + product_name, "precio: " + product_price))
            except:
                print(f"No hemos encontrado el artículo {i}.")
                products_data_coto.append(f"Artículo {i} no encontrado")
        he.kill_browser()

    #### 4 CARREFOUR
    def carrefour_4(product):
        print("estamos buscando en Carrefour...")
        he.start_chrome("https://www.carrefour.com.ar/")
        time.sleep(10)
        search_box4 = he.find_all(he.S(".vtex-styleguide-9-x-input"))[0]
        he.wait_until(search_box4.exists)
        he.write(product, into=search_box4) 
        he.press(he.ENTER)
        time.sleep(8)
        #list_of_cards = he.find_all(he.S(".valtech-carrefourar-product-summary-status-0-x-container"))
        for i in range (1, 3) :
            try:
                product_name = (he.find_all(he.S(".vtex-product-summary-2-x-productNameContainer"))[i-1]).web_element.text
                product_price_all = (he.find_all(he.S(".valtech-carrefourar-product-price-0-x-sellingPriceValue"))[i-1]).web_element.text
                products_data_carrefour.append(("producto: " + product_name, "precio: "+ product_price_all))
            except:
                print(f"No hemos encontrado el artículo {i}.")
                products_data_carrefour.append(f"Artículo {i} no encontrado")
        he.kill_browser()

    #### 5 JUMBO 
    def jumbo_5(product):
        print("estamos buscando en Jumbo...")
        he.start_chrome("https://www.jumbo.com.ar/")
        time.sleep(7)
        search_box5 = he.find_all(he.S(".vtex-styleguide-9-x-input"))[0]
        he.wait_until(search_box5.exists)
        time.sleep(3)
        he.write(product, into=search_box5)
        he.press(he.ENTER)
        time.sleep(6)
        #list_of_cards = he.find_all(he.S(".vtex-search-result-3-x-galleryItem"))
        for i in range (1, 3) :
            try:
                product_name = (he.find_all(he.S(".vtex-product-summary-2-x-productBrand"))[i-1]).web_element.text
                product_price = (he.find_all(he.S(".productPrice"))[i-1]).web_element.text
                products_data_jumbo.append(("producto: " + product_name, "precio: " + product_price))
            except:
                print(f"No hemos encontrado el artículo {i}.")
                products_data_jumbo.append(f"Artículo {i} no encontrado")
        he.kill_browser()

    # ZONAS
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

    ###### archivo agregar data ########
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
        open_file = str(input("desea ahora abrir el archivo para ver los productos y precios? s/n ")).upper()
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
    
    #BUSCAR POR YOUTUBE
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    yt_video = str(input("¿Desea buscar por youtube una receta del producto que buscó? s/n ")).upper()
    while yt_video != 'S' and yt_video != 'N':
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        yt_video = str(input("¿Desea buscar por youtube una receta del producto que buscó? s/n ")).upper()

    if yt_video == "S":    
        print("Buscando el video...")
        he.start_chrome("https://www.youtube.com/@enricorapalin/videos")
        time.sleep(6)
        counter = 0
        try:
            while counter < 100:
                video_title = (he.find_all(he.S("#video-title"))[counter]).web_element
                if product.upper() in (video_title.text).upper():
                    video_title.click()
                    print("Reproduciendo la receta...")
                    break
                else:
                    he.scroll_down(50)
                    he.scroll_down(50)
                    he.scroll_down(50)
                    counter += 1
        except:
            print("No se ha encontrado nungun video receta del producto que buscó.")
    print("---------------------------------")
    print("Espero que te hayamos ayudado <3")
    print("---------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
else:
    print("---------------------------------")
    print("Bueno, gracias por elegirnos(?")
    print("---------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
