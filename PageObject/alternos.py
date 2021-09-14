import time
import unittest
from selenium.webdriver.common.by import By

class Alternos():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.campo_busqueda = "//input[@id='twotabsearchtextbox']"
        self.boton_buscar = "//input[@id='nav-search-submit-button']"
    
    def enviar_a(self):
        self.pais = "Angola"
        string_enviar_a = self.driver.find_element_by_xpath("//span[@id='glow-ingress-line2']").text
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_enviar_a, self.pais)
        print("Assert Enviar a: " + string_enviar_a)
        time.sleep(4)
    def cambiar_lugar(self):
        self.driver.find_element_by_xpath("//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/span[1]/span[1]/span[1]/span[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@id='GLUXCountryList_17']").click()
        time.sleep(4)
    def monitores_marca_hp(self):
        check_hp = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[4]/ul[1]/li[1]/span[1]/a[1]/span[1]")
        check_hp.click()
        time.sleep(3)
    def asser_motinores_asus(self):
        self.asus = "ASUS"
        string_check_hp = self.driver.find_element_by_xpath("//li[@id='p_89/HP']").get_attribute("aria-label")
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_check_hp, self.asus)
        print("Assert ok: " + string_check_hp)
        time.sleep(3)
    def filtro_marca_corsair(self):
        checkbox_marca_corsair = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[5]/ul[1]/li[3]/span[1]/a[1]/span[1]")
        checkbox_marca_corsair.is_selected()
        time.sleep(4)
    def asser_marca_hyperx(self):
        self.marca = "HyperX"
        string_marca_corsair = self.driver.find_element_by_xpath("//li[@id='p_89/Corsair']").get_attribute("aria-label")
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_marca_corsair, self.marca)
        print("Assert ok: " + string_marca_corsair)
        time.sleep(3)
    def play_station(self):
        search = self.driver.find_element_by_xpath(self.campo_busqueda)
        search.send_keys("play station")
        print("Producto seleccionado: PlayStation")
        self.driver.find_element_by_xpath(self.boton_buscar).click()
        #self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[3]/div[1]/span[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
    def asser_play_station(self):
        self.producto = "PlayStation 5"
        string_campo_busqueda = self.driver.find_element_by_xpath(self.campo_busqueda).get_attribute("value")
        tc = unittest.TestCase('__init__')
        tc.assertEqual(string_campo_busqueda, self.producto)
        print("Assert ok: " + string_campo_busqueda)
        time.sleep(3)