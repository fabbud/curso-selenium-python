# Criar um script com os seguintes passos:
#  ■ Abra o site
#  ■ Maximize a janela do browser
#  ■ Localize 3 elementos na página
#  ■ Obtenha o título da página
#  ■ Imprima o título da página no console
#  ■ Feche o browser
#  ○ Criar 6 scripts, um para cada tipo de locator (id, name, className, linkText, partialLinkText, 
# tagName)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# Amazon
# browser.get("https://www.amazon.es/")
# browser.maximize_window()
# sleep(3)

# cookies = browser.find_element(By.ID, "sp-cc-accept")
# cookies.click()
# sleep(1)

# #By ID
# greeting_byID = browser.find_element(By.ID, "nav-link-accountList-nav-line-1")

# #By CLASS_NAME
# search = browser.find_element(By.CLASS_NAME, "nav-input nav-progressive-attribute")

# #By NAME
# search = browser.find_element(By.NAME, "field-keywords")

# #By LINK_TEXT
# link1 = browser.find_element(By.LINK_TEXT, "Torne-se um afiliado")

# #By PARTIAL_LINK_TEXT
# link2 = browser.find_element(By.PARTIAL_LINK_TEXT, "Conversor de moedas")

# #By TAG_NAME
# browser.find_elements(By.TAG_NAME, "body")


# SauceLabs
browser.get("https://accounts.saucelabs.com/am/XUI/#login/")
browser.maximize_window()
sleep(3)

cookies = browser.find_element(By.ID, "onetrust-accept-btn-handler")
cookies.click()
sleep(2)

#By ID
browser.find_element(By.ID, "content")

#By CLASS_NAME
browser.find_element(By.CLASS_NAME, "login-wrapper")

#By NAME
password = browser.find_element(By.NAME, "callback_1")

#By LINK_TEXT
link1 = browser.find_element(By.LINK_TEXT, "Try for free")

#By PARTIAL_LINK_TEXT
link2 = browser.find_element(By.PARTIAL_LINK_TEXT, "my password")

#By TAG_NAME
browser.find_elements(By.TAG_NAME, "header")

title = browser.title
print(title)
