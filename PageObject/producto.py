import time
import unittest
from selenium.webdriver.common.by import By

class Producto():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.campo_busqueda = "//input[@id='twotabsearchtextbox']"
        self.boton_buscar = "//input[@id='nav-search-submit-button']"

    def play_station_5(self):
        search = self.driver.find_element_by_xpath(self.campo_busqueda)
        search.send_keys("play station 5")
        print("Producto seleccionado: PlayStation 5")
        self.driver.find_element_by_xpath(self.boton_buscar).click()
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='search']/div[1]/div[1]/div[1]/span[3]/div[2]/div[3]/div[1]/span[1]/div[1]/div[1]/span[1]/a[1]/div[1]/img[1]").click()
    def alexa_carrusel(self):
        #time.sleep(1)
        #self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='pageContent']/div[@id='desktop-banner']/div[@id='gw-desktop-herotator']/div[1]/div[1]/div[1]/div[3]/a[1]/i[1]").click()
        #time.sleep(3)
        #self.driver.find_element_by_xpath("//*[@id='OuxVZ10-p1Cvsj5uNtQCLQ']/a/div/img").click()
        time.sleep(3)
        self.driver.get("https://www.amazon.es/b/?ie=UTF8&node=15862673031&ref_=gw_es_desk_h1_aucc_brwcroatn_fc_kifjuly&pf_rd_r=YB09PYM6547BK0NHWFGQ&pf_rd_p=87099d04-af89-4741-b396-07458cd51086&pd_rd_r=a656ce7d-9951-41c3-a453-46b253099e56&pd_rd_w=lbKQF&pd_rd_wg=RQJgw")
    def alexa(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ol[1]/li[2]/div[1]/div[1]/a[1]/img[1]").click()
        time.sleep(3)
    def alexa_color_cant(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='dp']/div[@id='dp-container']/div[@id='ppd']/div[@id='centerCol']/div[@id='twister_feature_div']/div[@id='twisterContainer']/div[1]/form[1]/div[1]/ul[1]/li[2]/span[1]/div[1]/span[1]/span[1]/span[1]/button[1]/div[1]/div[1]/img[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//select[@id='quantity']").click()
        self.driver.find_element_by_xpath("//option[contains(text(),'3')]").click()
        time.sleep(4)
    def juegos_pc(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/span[6]/li[1]/span[1]/div[1]/a[1]/div[1]/div[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/span[1]/li[1]/span[1]/div[1]/a[1]/div[1]/div[1]").click()
        time.sleep(4)