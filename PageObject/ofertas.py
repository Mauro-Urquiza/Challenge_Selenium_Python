from selenium import webdriver
import time

class Ofertas():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.oferta = "//a[contains(text(),'Ofertas')]"
        self.flechita_der = "//body/div[@id='a-page']/div[16]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]"
        self.cat_coche_y_moto = "//body/div[@id='a-page']/div[16]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[26]/div[1]/span[1]/img[1]"
    def boton_ofertas(self):
        self.driver.find_element_by_xpath(self.oferta).click()
        time.sleep(3)
    def cat_coche_moto(self):
        clic_flechita_der = self.driver.find_element_by_xpath(self.flechita_der)
        clic_flechita_der.click()
        time.sleep(2)
        clic_flechita_der.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.cat_coche_y_moto).click()
        time.sleep(2)


