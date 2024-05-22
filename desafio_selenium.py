import pandas as pd
from IPython.display import display
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

#Lendo o arquivo do excel
tabela = pd.read_excel("challenge.xlsx")

#URL do site acessado
url = "https://www.rpachallenge.com/"
driver = Firefox()
driver.implicitly_wait(20)
driver.get(url)

#identificar e clicar no botao iniciar
botao_start = driver.find_element(By.CSS_SELECTOR, 'button.waves-effect').click()

for indice, linha in tabela.iterrows():
    #pegando os campos dentro do arquivo
    first_name = tabela.loc[indice, "First Name"]
    last_name = tabela.loc[indice, "Last Name "]
    company_name = tabela.loc[indice, "Company Name"]
    role_company = tabela.loc[indice, "Role in Company"]
    adress = tabela.loc[indice, "Address"]
    email = tabela.loc[indice, "Email"]
    phone_number = tabela.loc[indice, "Phone Number"]
        
    #Identifcar os campos no navegador
    input_elements = driver.find_elements(By.XPATH, '//input[@ng-reflect-name="labelAddress"]')
    if len(input_elements) >0:
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]').send_keys(adress)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelRole"]').send_keys(role_company)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]').send_keys(last_name)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]').send_keys(first_name)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]').send_keys(company_name)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelEmail"]').send_keys(email)
        driver.find_element(By.XPATH, '//input[@ng-reflect-name="labelPhone"]').send_keys(str(phone_number))
        input_submit = driver.find_element(By.XPATH, '//input[@class="btn uiColorButton" and @type="submit"]')
        input_submit.click()
        

    