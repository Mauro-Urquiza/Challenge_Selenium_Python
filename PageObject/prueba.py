from selenium import webdriver 
  
driver = webdriver.Chrome(executable_path=r"/home/mauro/Escritorio/chromedriver")
driver.find_element_by_css_selector
  
url = "https://www.amazon.es/"
  
driver.get(url) 
  
get_title = driver.title 
  
print(get_title) 