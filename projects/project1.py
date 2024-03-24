import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(3)
    yield driver
    driver.quit()

# Logar no site com o usuário standard
def test_login(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.XPATH, "//input[@type='submit']")
    button.click()
    sleep(3)

    # Adicionar os todos os produtos no carrinho
    product_elements = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name ']")
    product_list = [product.text for product in product_elements]

    for i in product_list:
        add_to_cart_button = driver.find_element(By.XPATH, f"//div[text()='{i}']/ancestor::div[@class='inventory_item_description']//div[@class='pricebar']/button")
        add_to_cart_button.click()
        sleep(1)

    # Conferir que no carrinho tem a badge com todos produtos
    product_count = len(product_list)
    cart_number = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    assert product_count == int(cart_number)

    # Entrar no carrinho
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()

    # Remover um dos produtos do carrinho
    remove_button = driver.find_element(By.XPATH, "(//button[text()='Remove'])[1]")
    remove_button.click()
    sleep(1)

    # Conferir que no carrinho tem a badge com 5 produtos
    continue_shopping_button = driver.find_element(By.XPATH, "//button[text()='Continue Shopping']")
    continue_shopping_button.click()
    sleep(1)

    cart_number = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    assert (product_count - 1) == int(cart_number)

    # Clicar no botão Checkout
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    checkout_button = driver.find_element(By.XPATH, "//button[text()='Checkout']")
    checkout_button.click()
    sleep(1)

    # Preencher os dados solicitados e clicar em Continue
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Fernanda")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Abbud")
    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("1600-606")
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    sleep(1)

    # Clicar no botão Finish
    finish_button = driver.find_element(By.XPATH, "//button[text()='Finish']")
    finish_button.click()
    sleep(1)

    # Conferir a mensagem “Thank you for your order!”
    message_headline = driver.find_element(By.TAG_NAME, "h2").text
    assert "Thank you for your order!" ==  message_headline
    message_body = driver.find_element(By.CLASS_NAME, "complete-text").text
    assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" ==  message_body
