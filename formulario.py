from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from colorama import init, Fore
init(autoreset=True)

#start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium\ChromeTestProfile"
#https://formspree.io/register

def iniciar_navegador(com_debugging_remoto=True):
    chrome_driver_path = ChromeDriverManager().install()
    chrome_driver_executable = os.path.join(os.path.dirname(chrome_driver_path), 'chromedriver.exe')
    
    if not os.path.isfile(chrome_driver_executable):
        raise FileNotFoundError(f"O ChromeDriver não foi encontrado em {chrome_driver_executable}")

    service = Service(executable_path=chrome_driver_executable)
    
    chrome_options = Options()
    if com_debugging_remoto:
        remote_debugging_port = 9222
        chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")
    
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    return navegador

def formulario():
    navegador = iniciar_navegador(com_debugging_remoto=True)
    
    first_name = navegador.find_element('xpath', '//*[@id=":r0:"]')
    last_name = navegador.find_element('xpath', '//*[@id=":r1:"]')
    email = navegador.find_element('xpath', '//*[@id=":r2:"]')
    password = navegador.find_element('xpath', '//*[@id=":r3:"]')
    botao_terms = navegador.find_element('xpath', '//*[@id=":r4:"]')
    registrar = navegador.find_element('xpath', '//*[@id="body"]/section/main/div[2]/div/form/button')

    first_name.click()
    first_name.send_keys('Gabriel')
    time.sleep(0.5)

    last_name.click()
    last_name.send_keys('Alvise')
    time.sleep(0.5)

    print(Fore.GREEN + 'Gabriel Alvise OK')

    email.click()
    email.send_keys('schenorberger123@gmail.com')
    time.sleep(0.5)

    print(Fore.GREEN + 'Email OK')

    password.click()
    password.send_keys('Alvise123?')
    time.sleep(1)

    botao_terms.click()
    time.sleep(0.5)

    registrar.click()
    print(Fore.GREEN + 'Conta registrada com sucesso!')

formulario()
