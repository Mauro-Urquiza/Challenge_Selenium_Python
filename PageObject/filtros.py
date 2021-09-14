import time
import unittest
from selenium.webdriver.common.by import By

class Filtro():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.todosLosDepartamentos = "//select[@id='searchDropdownBox']"
        self.boton_buscador = "//input[@id='nav-search-submit-button']"
    def buscador(self):
        self.driver.find_element_by_xpath(self.boton_buscador).click()

    def filtro_marca_hyperx(self):
        checkbox = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[5]/ul[1]/li[5]/span[1]/a[1]/div[1]/label[1]/i[1]")
        checkbox.is_selected()
        time.sleep(4)
    def filtro_precio(self):
        checkbox = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[6]/ul[1]/li[5]/span[1]/a[1]/div[1]/label[1]/i[1]")
        checkbox.is_selected()
        time.sleep(5)
    def form_portatil_ultrab(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[2]/div[1]/div[1]/div[8]/ul[1]/li[2]/span[1]/a[1]/div[1]/label[1]/i[1]").click()
    def tam_pantalla_15(self):
        self.driver.find_element_by_xpath("//li[@id='p_n_style_browse-bin/949808031']").click()
        time.sleep(3)
    def tipo_proc_I7(self):
        self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[6]/ul[4]/li[3]/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        time.sleep(3)
    def marca_asus(self):
        self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/div[4]/ul[1]/li[5]/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        time.sleep(3)
    def oferta(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[2]/div[1]/div[1]/div[15]/ul[1]/li[1]/span[1]/a[1]/div[1]/label[1]/i[1]").click()
        time.sleep(5)
    def videojuegos(self):
        self.driver.find_element_by_xpath(self.todosLosDepartamentos).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//option[contains(text(),'Videojuegos')]").click()
        time.sleep(3)
    def los_mas_vendidos(self):
        self.driver.find_element_by_xpath("//*[@id='nav-subnav']/a[2]/span").click()
        time.sleep(3)
    

