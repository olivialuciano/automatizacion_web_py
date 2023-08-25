from selenium import webdriver
import chromedriver_autoinstaller
import time
import helium as he
chromedriver_autoinstaller.install()


# ARRANCAR
start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()
while start != 'S' and start != 'N':
    print("Respuesta inválida. Le preguntaremos de nuevo.")
    start = str(input("¿Desea buscar y comparar los precios de un producto en especifico de diferentes supermercados de la ciudad de rosario? s/n ")).upper()

if start == 'S':
    # ARCHIVO
    file = str(input("¿En donde desea crear el archivo del listado de productos? Por favor ingrese la ruta ")) ## CREAR ARCHIVO TEMPORAL

    # LOCACIÓN
    location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) ")).upper()
    while location != "Q" and location != "C" and location != "S" and location != "O" and location != "F" and location != "N" :
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        location = str(input("¿En qué zona desea que se ubique el supermercado? (cualquiera: Q, centro: C, sur: S, oeste: O, fisherton: F, norte: N) "))
    # PRODUCTO
    product = str(input("Ingrese el producto a buscar: "))
    print("Buscando ", product, " (te aviso que va a demorar bastante)")

    # ############### 1 LA GALLEGA #################################

    def la_gallega_1(product):
        he.start_chrome("https://www.lagallega.com.ar/login.asp")
        time.sleep(5)
        search_box1 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box1.exists)
        he.click(search_box1)
        search_box1 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box1.exists)
        he.write(product, into=search_box1)
        he.press(he.ENTER)
        time.sleep(10)
        he.kill_browser()

    # ############### 2 LA REINA ###################################
    def la_reina_2(product):
        he.start_chrome("https://www.lareinaonline.com.ar/")
        time.sleep(5)
        search_box2 = he.find_all(he.S("#CabeBusca"))[0]
        he.wait_until(search_box2.exists)
        he.click(search_box2)
        search_box2 = he.find_all(he.S("#cpoBuscarMovil"))[0]
        he.wait_until(search_box2.exists)
        he.write(product, into=search_box2)
        he.press(he.ENTER)
        time.sleep(10)
        he.kill_browser()

    # ############### 3 COTO #######################################
    def coto_3(product):
        he.start_chrome("https://www.cotodigital3.com.ar/sitios/cdigi/")
        time.sleep(5)
        search_box3 = he.find_all(he.S("#atg_store_searchInput"))[0]
        he.wait_until(search_box3.exists)
        he.write(product, into=search_box3)
        he.press(he.ENTER)
        time.sleep(10)
        he.kill_browser()

    # ############### 4 CARREFOUR ##################################
    def carrefour_4(product):
        he.start_chrome("https://www.carrefour.com.ar/")
        time.sleep(5)
        search_box3 = he.find_all(he.S("#downshift-1-input"))[0]
        he.wait_until(search_box3.exists)
        he.write(product, into=search_box3) 
        he.press(he.ENTER) #tarda bastante en buscar la zanahoria y aparece abajo todo desubicado
        time.sleep(20)
        he.kill_browser()

    ############### 5 JUMBO ######################################
    def jumbo_5(product):
        he.start_chrome("https://www.jumbo.com.ar/")
        time.sleep(5)
        search_box5 = he.find_all(he.S(".vtex-styleguide-9-x-input"))[0]
        time.sleep(2)
        he.write(product, into=search_box5)
        he.press(he.ENTER)
        time.sleep(5)
        input()
        he.kill_browser()

    ## llamo a las funciones supermercados dependiendo la zona en la que hay
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

    # ABRIR ARCHIVO
    open_file = str(input("desea ahora abrir el archivo para ver los productos y precios? s/n "))
    while open_file != 's' and open_file != 'S' and open_file != 'n' and open_file != 'N':
        print("Respuesta inválida. Le preguntaremos de nuevo.")
        open_file = str(input("desea ahora abrir el archivo para ver los productos y precios? s/n "))
    
    # BORRAR ARCHIVO
    delete_file = str(input("Cuando presione ENTER, el archivo será eliminado."))
     ##y que ahi elimine el archivo

    print("Espero haberte ayudado <3 ")

else:
    print("Bueno, gracias por elegirnos(?")