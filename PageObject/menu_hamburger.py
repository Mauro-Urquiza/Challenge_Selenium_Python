from selenium import webdriver
import time

class Menu():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.menu_hamburguesa = "//a[@id='nav-hamburger-menu']"
    
    def menu_hamburger(self):
        self.driver.find_element_by_xpath(self.menu_hamburguesa).click()
        time.sleep(3)
    def videoJuegos(self):
        self.driver.find_element_by_xpath("//body/div[@id='hmenu-container']/div[@id='hmenu-canvas']/div[@id='hmenu-content']/ul[1]/li[22]/a[1]/i[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//body/div[@id='hmenu-container']/div[@id='hmenu-canvas']/div[@id='hmenu-content']/ul[1]/ul[1]/li[2]/a[1]").click()
        time.sleep(3)
    def juegos_para_pc(self):
        self.driver.find_element_by_xpath("//body/div[@id='hmenu-container']/div[@id='hmenu-canvas']/div[@id='hmenu-content']/ul[15]/li[5]/a[1]").click()
        time.sleep(3)