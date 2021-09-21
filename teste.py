from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# PASSO 1: Entrar em: http://127.0.0.1:8000/
driver.get("http://127.0.0.1:8000/")

# PASSO 2: Clicar em Criar Conta
element = driver.find_element_by_xpath('//*[@id="criar"]')
driver.execute_script("arguments[0].click();", element)

# # PASSO 3: Preencher as informações do usuário
email = driver.find_element_by_xpath('//*[@id="id_email"]')
email.clear()
email.send_keys("testesistemas@gmail.com")
email.send_keys(Keys.RETURN)

usuar = driver.find_element_by_xpath('//*[@id="id_username"]')
usuar.clear()
usuar.send_keys("TesteSistemas")
usuar.send_keys(Keys.RETURN)

senha = driver.find_element_by_xpath('//*[@id="id_password1"]')
senha.clear()
senha.send_keys("atividadesistemas123456")
senha.send_keys(Keys.RETURN)

senhatwo = driver.find_element_by_xpath('//*[@id="id_password2"]')
senhatwo.clear()
senhatwo.send_keys("atividadesistemas123456")
senhatwo.send_keys(Keys.RETURN)


# # PASSO 4: Clicar em cadastrar
cadastro = driver.find_element_by_xpath('/html/body/div/form/button')
driver.execute_script("arguments[0].click();", cadastro)

# # PASSO 5: Preencher as informações de login
usuari = driver.find_element_by_xpath('//*[@id="id_username"]')
usuari.clear()
usuari.send_keys("testesistemas@gmail.com")
usuari.send_keys(Keys.RETURN)

senhalogin = driver.find_element_by_xpath('//*[@id="id_password"]')
senhalogin.clear()
senhalogin.send_keys("atividadesistemas123456")
senhalogin.send_keys(Keys.RETURN)

# # PASSO 6: Clicar em Entrar
logar = driver.find_element_by_xpath('//*[@id="logar"]')
driver.execute_script("arguments[0].click();", logar)