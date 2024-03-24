from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

sleep(3)

full_name = driver.find_element(By.XPATH, "//label[text()='Full Name:']/following-sibling::input")
full_name = driver.find_element(By.ID, "fullName")

full_name.send_keys("Fernanda Abbud")

email = driver.find_element(By.XPATH, "//label[text()='Email:']/following-sibling::input")
email.send_keys("fabbud@gmail.com")

phone_number = driver.find_element(By.XPATH, "//label[text()='Phone Number:']/following-sibling::input")
phone_number.send_keys("123456789")

Select(driver.find_element(By.XPATH, "//select[@name='desiredPosition']")).select_by_visible_text("Designer")

remote = driver.find_element(By.XPATH, "//label[text()='Remote']/preceding-sibling::input")
remote.click()

years = driver.find_element(By.XPATH, "//label[text()='Years of Experience:']/following-sibling::input")
years.send_keys("3")

html = driver.find_element(By.XPATH, "//label[text()='HTML']/preceding-sibling::input")
html.click()

css = driver.find_element(By.XPATH, "//label[text()='CSS']/preceding-sibling::input")
css.click()

js = driver.find_element(By.XPATH, "//label[text()='JavaScript']/preceding-sibling::input")
js.click()

button = driver.find_element(By.XPATH, "//button[text()='Submit Application']")
button.click()

message = driver.find_element(By.XPATH, "//span[@id='successMessage']").text

sleep(1)

assert "Submission successful!" == message

sleep(2)

driver.quit()
