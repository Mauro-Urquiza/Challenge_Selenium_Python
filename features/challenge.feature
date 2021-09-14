@feature
Feature: 10 test Challenge
Challenge usando la pag de Amazon

@testCase1
Scenario: Agregar PlayStation 5 a la lista de deseos
    Given Que el usuario se encuentra en el la pagina principal 
        And El usuario ingreso play station 5 en el buscador
    When El usuario accede al producto encontrado
    Then El usuario podra agredar el producto a la lista de deseos

@testCase2
Scenario: Cambiar de lugar envio a Angola
    Given Que el usuario se encuentra en la pagina principal
    When El usuario selecciona la opcion Enviar a
    Then El usuario podra cambiar su lugar de envio
        And Se debe corroborar el lugar de envio solicitado

@testCase3
Scenario: Visualizar todo los Juegos para PC
    Given Que el usuario se encuentra en la pagina principal de Amazon
    When El usuario selecciona el menu hamburguesa
        And en la seccion Buscar por departamento selecciona videojuegos
        And en la seccion Videojuegos selecciona Juegos para PC
    Then El usuario podra visualizar Juegos y Accesorios para PC       

@testCase4
Scenario: Visualizar todos los auriculares gaming de la marca HyperX de mas de 50 euros
    Given Que el usuario se encuentra en la pagina de Amazon
    When El usuario ingresa en el buscador auriculares gaming
        And en el filtro de marca selecciona HyperX
    Then El usuario podra visualizar todos los auriculares gaming HyperX de mas de 50 euros

@testCase5
Scenario: Buscar trabajo como QA en Amazon España 
    Given Usuario se encuentra en la pagina de Amazon
    When Usuario selecciona, en la seccion Conocenos, Trabajar en Amazon
        And el usuario cambia de idioma la pagina
        And en el buscador ingresa QA
    Then El usuario podra visualizar todos avisos de trabajo como QA
        And en el filtro pais podra seleccionar España 

@testCase6
Scenario: Visualizar todas las ultrabook de 15 puldagas y con procesador Intel Core I7 
    Given El usuario se encuentra en la pagina de Amazon
    When Usuario selecciona como categoria Informatica
        And selecciona el filtro formato del portatil en ultrabook 
        And selecciona los filtros tamaño de pantalla en 15 pulgadas, tipo de procesador en intel Core I7
    Then El usuario podra visualizar todos productos con dichas caracteristicas
    

@testCase7
Scenario: Visualizar todos los Monitores ASUS de oferta  
    Given El usuario se encuentra en la pagina principal de Amazon
    When El usuario selecciona como categoria Monitores
        And selecciona los filtros marca ASUS, ofertas 
    Then El usuario podra visualizar todos los Monitores ASUS de oferta  

@testCase8
Scenario: Visualizar todas las ofertas de hoy para coche y moto en orden de precio de menor a mayor   
    Given El usuario se encuentra posicionado en la pagina principal de Amazon
    When El usuario selecciona como categoria ofertas 
        And selecciona la categoria Coche y moto  
    Then El usuario, al ordenar por precio de menor a mayor, podra visualizar todos los productos que cumplan con dichos requisitos.     

@testCase9
Scenario: Desde el carrusel seleccionar Alexa y agregar a la cesta 3 unidades en color blanco 
    Given Usuario se encuentra posicionado en la pagina principal de Amazon
    When El usuario selecciona Alexa en el carrusel 
        And selecciona un producto de tipo Echo Dot 4ta gen
        And selecciona el color blanco, ademas de las 3 unidades  
    Then El usuario podra agregar las 3 unidades de Alexa a la cesta   

@testCase10
Scenario: Visualizar todos los juegos para PC mas vendidos   
    Given A que el usuario se encuentra posicionado en la pagina principal de Amazon
    When El usuario busca por medio de la categoria Videojuegos 
        And en la seccion de PC selecciona juegos, ademas en categorias Los Mas Vendidos  
    Then El usuario podra visualizar todos los Videojuegos mas vendidos para PC
        And podra visualizar todas las paginas disponibles       

@testCaseAlterno1
Scenario: Cambiar de lugar envio a Angola 
    Given Que el usuario se encuentra en la pagina principall
    When El usuario selecciona la opcion Enviar a Argentina 
    Then El usuario no podra cambiar su lugar de envio 

@testCaseAlterno2
Scenario: Visualizar todos los Monitores ASUS de oferta  
    Given El usuario se encuentra en la pagina principal de Amazonn
    When El usuario selecciona como categoria Monitoress
        And selecciona los filtros marca HP, ofertas 
    Then El usuario no podra visualizar todos los Monitores ASUS de oferta  

@testCaseAlterno3
Scenario: Visualizar todos los auriculares gaming de la marca HyperX de mas de 50 euros
    Given Que el usuario se encuentra en la pagina de Amazonn
    When El usuario ingresa en el buscador auriculares gamingg
        And en el filtro de marca selecciona Sony
    Then El usuario no podra visualizar todos los auriculares gaming HyperX de mas de 50 euros

@testCaseAlterno4
Scenario: Agregar PlayStation 5 a la lista de deseos
    Given Que el usuario se encuentra en el la pagina principall 
        And El usuario ingreso play station en el buscador
    When El usuario accede al primer producto encontrado
    Then El usuario no podra agredar el producto a la lista de deseos