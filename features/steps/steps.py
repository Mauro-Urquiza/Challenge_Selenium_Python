from behave import given
from behave import when
from behave import then 
from PageObject.home import *
from PageObject.producto import *
from PageObject.asserts import *
from PageObject.menu_hamburger import *
from PageObject.filtros import *
from PageObject.trabajar_en_amazon import *
from PageObject.ofertas import *
from PageObject.ordenado_por import *
from PageObject.alternos import *
from selenium.webdriver.common.by import By

#Primer Caso de prueba
@given(u'Que el usuario se encuentra en el la pagina principal')
def implement(context):
    print("---------Inicio Test 1 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
    time.sleep(4)

@given(u'El usuario ingreso play station 5 en el buscador')
def implement(context):
    context.prod = Producto(context.driver)
    context.prod.play_station_5()

@when('El usuario accede al producto encontrado')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.nombrePlay()
    
@then('El usuario podra agredar el producto a la lista de deseos')
def implement(context):
    context.anadir_lista_deseos = Home(context.driver) 
    context.anadir_lista_deseos.boton_anadir_lista_deseos()
    context.home.cerrar_navegador()
    print("---------Fin Test 1 --------")

#Segundo Caso de prueba
@given(u'Que el usuario se encuentra en la pagina principal')
def implement(context):
    print("---------Inicio Test 2 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona la opcion Enviar a')
def implement(context):
    context.home.enviar_a()
@then('El usuario podra cambiar su lugar de envio')
def implement(context):
    context.home.cambiar_lugar()
@then('Se debe corroborar el lugar de envio solicitado')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.enviar_a()
    context.home.cerrar_navegador()
    print("---------Fin Test 2 --------")

#Tercer Caso de prueba
@given(u'Que el usuario se encuentra en la pagina principal de Amazon')
def implement(context):
    print("---------Inicio Test 3 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona el menu hamburguesa')
def implement(context):
    context.menu = Menu(context.driver)
    context.menu.menu_hamburger()

@when('en la seccion Buscar por departamento selecciona videojuegos')
def implement(context):
    context.menu.videoJuegos()

@when('en la seccion Videojuegos selecciona Juegos para PC')
def implement(context):
    context.menu.juegos_para_pc()

@then('El usuario podra visualizar Juegos y Accesorios para PC')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.juegos_accesorios_pc()
    context.home.ver_todos_los_productos()
    context.home.cerrar_navegador()
    print("---------Fin Test 3 --------")

#Cuarto Caso de prueba
@given(u'Que el usuario se encuentra en la pagina de Amazon')
def implement(context):
    print("---------Inicio Test 4 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()

@when('El usuario ingresa en el buscador auriculares gaming')
def implement(context):
    context.home.buscador("auriculares gaming")

@when('en el filtro de marca selecciona HyperX')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.filtro_marca_hyperx()

@then('El usuario podra visualizar todos los auriculares gaming HyperX de mas de 50 euros')
def implement(context):
    context.filtro.filtro_precio()
    context.home.cerrar_navegador()
    print("---------Fin Test 4 --------")

#Quinto Caso de prueba
@given(u'Usuario se encuentra en la pagina de Amazon')
def implement(context):
    print("---------Inicio Test 5 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()

@when('Usuario selecciona, en la seccion Conocenos, Trabajar en Amazon')
def implement(context):
    context.trabajar_en_Amazon = Trabajar_en_Amazon(context.driver)
    context.trabajar_en_Amazon.trabajar_Amazon()
@when('el usuario cambia de idioma la pagina')
def implement(context):
    context.trabajar_en_Amazon.idioma()
@when('en el buscador ingresa QA')
def implement(context):
    context.trabajar_en_Amazon.buscador("QA")

@then('El usuario podra visualizar todos avisos de trabajo como QA')
def implement(context):
    context.trabajar_en_Amazon.ordenado_por_relevante()
@then('en el filtro pais podra seleccionar España')
def implement(context):
    context.trabajar_en_Amazon.filtro_pais_ver_mas()
    context.home.cerrar_navegador()
    print("---------Fin Test 5 --------")

#Sexto Caso de prueba
@given(u'El usuario se encuentra en la pagina de Amazon')
def implement(context):
    print("---------Inicio Test 6 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()

@when('Usuario selecciona como categoria Informatica')
def implement(context):
    context.home.informatica_portatiles()

@when('selecciona el filtro formato del portatil en ultrabook')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.form_portatil_ultrab()

@when('selecciona los filtros tamaño de pantalla en 15 pulgadas, tipo de procesador en intel Core I7')
def implement(context):
    context.filtro.tam_pantalla_15()
    context.filtro.tipo_proc_I7()

@then('El usuario podra visualizar todos productos con dichas caracteristicas')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.assert_tam_pantalla_15()
    context.afirmacion.assert_tipo_proc_I7()
    context.home.cerrar_navegador()
    print("---------Fin Test 6 --------")

#Septimo Caso de prueba
@given(u'El usuario se encuentra en la pagina principal de Amazon')
def implement(context):
    print("---------Inicio Test 7 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona como categoria Monitores')
def implement(context):
    context.home.informatica_monitores()

@when('selecciona los filtros marca ASUS, ofertas')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.oferta()
    context.filtro.marca_asus()

@then('El usuario podra visualizar todos los Monitores ASUS de oferta')
def implement(context):
    context.home.cerrar_navegador()
    print("---------Fin Test 7 --------")


#Octavo Caso de prueba
@given(u'El usuario se encuentra posicionado en la pagina principal de Amazon')
def implement(context):
    print("---------Inicio Test 8 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona como categoria ofertas')
def implement(context):
    context.ofertas = Ofertas(context.driver)
    context.ofertas.boton_ofertas()

@when('selecciona la categoria Coche y moto')
def implement(context):
    context.ofertas.cat_coche_moto()

@then('El usuario, al ordenar por precio de menor a mayor, podra visualizar todos los productos que cumplan con dichos requisitos.')
def implement(context):
    context.ordenadoPor = Ordenado_por(context.driver)
    context.ordenadoPor.ordenado_por()
    context.ordenadoPor.precio_menor_mayor()
    context.home.cerrar_navegador()
    print("---------Fin Test 8 --------")

#Noveno Caso de prueba
@given(u'Usuario se encuentra posicionado en la pagina principal de Amazon')
def implement(context):
    print("---------Inicio Test 9 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona Alexa en el carrusel')
def implement(context):
    context.prod = Producto(context.driver)
    context.prod.alexa_carrusel()

@when('selecciona un producto de tipo Echo Dot 4ta gen')
def implement(context):
    context.prod.alexa()

@when('selecciona el color blanco, ademas de las 3 unidades')
def implement(context):
    context.prod.alexa_color_cant()
@then('El usuario podra agregar las 3 unidades de Alexa a la cesta')
def implement(context):
    context.home.anadir_cesta()
    context.home.cerrar_navegador()
    print("---------Fin Test 9 --------")


#Decimo Caso de prueba
@given(u'A que el usuario se encuentra posicionado en la pagina principal de Amazon')
def implement(context):
    print("---------Inicio Test 10 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()

@when('El usuario busca por medio de la categoria Videojuegos')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.videojuegos()
    context.filtro.buscador()

@when('en la seccion de PC selecciona juegos, ademas en categorias Los Mas Vendidos')
def implement(context):
    context.producto = Producto(context.driver)
    context.producto.juegos_pc()
    context.filtro.los_mas_vendidos()

@then('El usuario podra visualizar todos los Videojuegos mas vendidos para PC')
def implement(context):
    context.home = Home(context.driver)
    context.home.scroll_abajo()
    context.home.siguiente_pag()

@then('podra visualizar todas las paginas disponibles')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.juegos_mas_vendidos()
    context.home.cerrar_navegador()
    print("---------Fin Test 10 --------")


#Primer Caso de prueba alterno
@given(u'Que el usuario se encuentra en la pagina principall')
def implement(context):
    print("---------Inicio Test Alterno 1 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona la opcion Enviar a Argentina')
def implement(context):
    context.home.enviar_a()
@then('El usuario no podra cambiar su lugar de envio')
def implement(context):
    context.alterno = Alternos(context.driver)
    context.alterno.cambiar_lugar()
    context.alterno.enviar_a()
    context.home.cerrar_navegador()
    print("---------Fin Test alterno 1 --------")

#Segundo Caso de prueba alterno
@given(u'El usuario se encuentra en la pagina principal de Amazonn')
def implement(context):
    print("---------Inicio Test alterno 2 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
@when('El usuario selecciona como categoria Monitoress')
def implement(context):
    context.home.informatica_monitores()

@when('selecciona los filtros marca HP, ofertas')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.oferta()
    context.alterno = Alternos(context.driver)
    context.alterno.monitores_marca_hp()
    context.alterno.asser_motinores_asus()

@then('El usuario no podra visualizar todos los Monitores ASUS de oferta')
def implement(context):
    context.home.cerrar_navegador()
    print("---------Fin Test alterno 2 --------")

#Tercer Caso de prueba alternativo
@given(u'Que el usuario se encuentra en la pagina de Amazonn')
def implement(context):
    print("---------Inicio Test alterno 3 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()

@when('El usuario ingresa en el buscador auriculares gamingg')
def implement(context):
    context.home.buscador("auriculares gaming")

@when('en el filtro de marca selecciona Sony')
def implement(context):
    context.alterno = Alternos(context.driver)
    context.alterno.filtro_marca_corsair();
    context.alterno.asser_marca_hyperx()

@then('El usuario no podra visualizar todos los auriculares gaming HyperX de mas de 50 euros')
def implement(context):
    context.filtro = Filtro(context.driver)
    context.filtro.filtro_precio()
    context.home.cerrar_navegador()
    print("---------Fin Test alterno 3 --------")

#Cuarto Caso de prueba alterno 
@given(u'Que el usuario se encuentra en el la pagina principall')
def implement(context):
    print("---------Inicio Test alterno 4 --------")
    context.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    context.home = Home(context.driver)
    context.home.page()
    time.sleep(4)

@given(u'El usuario ingreso play station en el buscador')
def implement(context):
    context.alterno = Alternos(context.driver)
    context.alterno.play_station()
    context.alterno.asser_play_station()

@when('El usuario accede al primer producto encontrado')
def implement(context):
    context.afirmacion = Asserts(context.driver)
    context.afirmacion.nombrePlay()
    
@then('El usuario no podra agredar el producto a la lista de deseos')
def implement(context):
    context.anadir_lista_deseos = Home(context.driver) 
    context.anadir_lista_deseos.boton_anadir_lista_deseos()
    context.home.cerrar_navegador()
    print("---------Fin Test alterno 4 --------")