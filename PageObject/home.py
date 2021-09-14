from selenium import webdriver
import time

class Home():
    def __init__(self,myDriver):
        self.driver = myDriver
        self.cat_informatica = "//a[contains(text(),'Informática')]"
        self.ofertas = "//a[contains(text(),'Ofertas')]"
    def scroll_abajo(self):
        self.driver.execute_script("window.scroll(0,document.body.scrollHeight)")
        time.sleep(3)

    def page(self):
        self.driver.get("https://www.amazon.es/")
        print ("Pagina visitada: https://www.amazon.es/")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='sp-cc-accept']").click()
        time.sleep(4)
    def cerrar_navegador(self):
        self.driver.quit()
    
    def browser(self):
        self.driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
    def boton_anadir_lista_deseos(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Añadir a la Lista de deseos')]").click()
    def enviar_a(self):
        self.driver.find_element_by_xpath("//a[@id='nav-global-location-popover-link']").click()
        time.sleep(4)
    def cambiar_lugar(self):
        self.driver.find_element_by_xpath("//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[4]/span[1]/span[1]/span[1]/span[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@id='GLUXCountryList_11']").click()
        time.sleep(4)
    def ver_todos_los_productos(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Ver todos los resultados')]").click()
        time.sleep(4)
    def buscador(self, producto):
        campo_buscador = self.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
        campo_buscador.send_keys(producto)
        self.driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()
        print("Producto buscado: " + producto)
        time.sleep(4)

    def informatica_portatiles(self):
        self.driver.find_element_by_xpath(self.cat_informatica).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/ul[1]/span[10]/li[1]/span[1]/div[1]/a[1]/div[1]/div[1]").click()
        time.sleep(3)
    def informatica_monitores(self):
        self.driver.find_element_by_xpath(self.cat_informatica).click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/ul[1]/span[8]/li[1]/span[1]/div[1]/a[1]/div[1]/div[1]").click()
        time.sleep(3)
    def anadir_cesta(self):
        self.driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()
        time.sleep(5)
    def siguiente_pag(self):
        self.driver.find_element_by_xpath("//body/div[@id='a-page']/div[@id='zg']/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]").click()
        time.sleep(5)
    
    
    
    


    