from selenium import webdriver
import time

class Ordenado_por():
    def __init__(self,myDriver):
        self.driver = myDriver

    def ordenado_por(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[16]/div[1]/div[1]/div[1]/div[1]/p[1]/span[1]/span[1]/span[1]/span[1]").click()
        time.sleep(2)
    def precio_menor_mayor(self):
        self.driver.find_element_by_xpath("//a[@id='sorting_dropdown0_3']").click()
        time.sleep(4)
        