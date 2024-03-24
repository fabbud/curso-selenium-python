from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.uol.com.br')
driver.maximize_window()
sleep(5)

titulo = driver.title
print(titulo)
driver.quit()
