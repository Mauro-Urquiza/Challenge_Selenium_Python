from selenium import webdriver
import time

class Trabajar_en_Amazon():
    def __init__(self,myDriver):
        self.driver = myDriver
        
    def trabajar_Amazon(self):
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(),'Trabajar en Amazon')]").click()
        time.sleep(3)
    def idioma(self):
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element_by_xpath("//body/div[2]/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//body/div[2]/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/a[5]").click()
        time.sleep(3)
    def buscador(self, puesto):
        buscador = self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
        buscador.send_keys(puesto)
        self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
        print("Puesto buscado: "+ puesto)
        time.sleep(4)
    def ordenado_por_relevante(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Ordenado por: Más relevantes')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@id='relevant']").click()
    def filtro_pais_ver_mas(self):
        ver_mas = self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/fieldset[1]/button[1]")
        ver_mas.click()
        time.sleep(2)
        ver_mas.click()
    def filtro_pais_españa(self):
        self.driver.find_element_by_xpath("//body/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/content[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/fieldset[1]/div[1]/button[15]/div[1]").click()
        time.sleep(5)