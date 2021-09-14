import time
import unittest
from selenium.webdriver.common.by import By

class Asserts ():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.nombre_play = "//span[@id='productTitle']"

    def nombrePlay(self):
        string_nombre_play = self.driver.find_element_by_xpath(self.nombre_play).text
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_nombre_play, "Sony Consola PS5 & Ratchet & Clank - Una Dimensión Aparte")
        print("Assert: " + string_nombre_play)
        time.sleep(4)
    def enviar_a(self):
        self.pais = "Angola"
        string_enviar_a = self.driver.find_element_by_xpath("//span[@id='glow-ingress-line2']").text
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_enviar_a, self.pais)
        print("Assert Enviar a: " + string_enviar_a)
        time.sleep(4)
    def juegos_accesorios_pc(self):
        self.titulo = "Juegos y Accesorios para PC"
        string_jue_acc_pc = self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[1]/div[1]/h1[1]/span[1]").text
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_jue_acc_pc, self.titulo)
        print("Assert Titulo: " + string_jue_acc_pc)
        time.sleep(3)

    def assert_tam_pantalla_15(self):
        check = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[6]/ul[1]/li[4]/span[1]/a[1]/div[1]/label[1]/i[1]").get_attribute("checked")
        if check is not None:
            print("Element checked Pantalla 15' - ", check)
        else: 
            print("Element checked - false")
    def assert_tipo_proc_I7(self):
        check = self.driver.find_element_by_xpath("//li[@id='p_n_feature_fifteen_browse-bin/8178957031']").get_attribute("checked")
        if check is not None:
            print("Element checked Proc Core I7 - ", check)
        else: 
            print("Element checked Proc Core I7 - false")
    def juegos_mas_vendidos(self):
        #self.url = self.driver.current_url
        #self.titulin = self.url.title 
        self.titulin = "Amazon.es Los más vendidos: Los productos más populares en Videojuegos"
        string_titulo = self.driver.find_element_by_xpath("//body/div[@id='a-page']/meta[1]").get_attribute("content")
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_titulo, self.titulin)
        print("Assert titulo pagina: " + string_titulo)
    
    




    



    