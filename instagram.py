from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import wget

driver = webdriver.Chrome()
driver.maximize_window()#deixa o tamanho da tela proporcional a tela usada 
driver.get('http://instagram.com')

#(driver, 10-tempo de espera para começar a executar os proximos comandos )
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#send_keys registra o que fica regitrado dentro da variavel
username.send_keys("digite seu login")#precisa digitar seu login
password.send_keys("digite sua senha ")#digite sua senha 

submit = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

#.click() executa  comando ENTER
submit.click()


not_now = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

#.click() executa  comando ENTER
not_now.click()

not_now1 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

#.click() executa  comando ENTER
not_now1.click()

searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

keyword = "<digite AQUI a conta do insta que deseja baixar as fotos >"

searchbox.send_keys(keyword)

element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id = "react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')))

#.click() executa  comando ENTER
element.click()

sleep(3)

#executa o comando de rolagem até o final da pagina 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#extrai todas as fotos usando a tag IMG
images = driver.find_elements_by_tag_name('img')

images = [image.get_attribute('src') for image in images]

#importando a biblioteca OS ele cria uma pasta para adicionar as foto da conta do usuario
path = os.getcwd()
path = os.path.join(path, keyword)

os.mkdir(path)

counter = 0

#Faz um laço de repetição até pegar todas as fotos 
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
