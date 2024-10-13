import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time
import sys

# Regex para capturar números de telefone, URLs (sites) e Instagram
phone_regex = re.compile(r'\(\d{2}\) \d{4,5}-\d{4}')
url_regex = re.compile(r'https?://[^\s]+|[^\s]+\.(com|br|org|net|gov|edu)')
instagram_regex = re.compile(r'instagram\.com')

# Obtendo argumentos de entrada
palavrachave = sys.argv[1] if len(sys.argv) > 1 else input("Qual nicho deseja pesquisar? ")
qtd = int(sys.argv[2]) if len(sys.argv) > 2 else int(input("Quantas buscas deseja fazer? "))

navegador = webdriver.Chrome()
action = ActionChains(navegador)

navegador.get(f"https://www.google.com.br/maps/search/{palavrachave}/")
time.sleep(3)

# Lista para armazenar os dados
dados_empresas = []

div = 3
for i in range(qtd):
    print(f"Tentando encontrar o elemento DIV XPATH: {div}")

    elemento_encontrado = False
    tentativas_de_scroll = 0

    while not elemento_encontrado and tentativas_de_scroll < 20:
        try:
            # Tenta encontrar o elemento clicável
            element = WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{div}]/div/a'))
            )
            element.click()
            elemento_encontrado = True
        except (NoSuchElementException, TimeoutException, ElementClickInterceptedException):
            print(f"Elemento {div} não encontrado ou não clicável, rolando a página para baixo...")
            action.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)  # Pausa para garantir que novos resultados sejam carregados
            tentativas_de_scroll += 1

    if not elemento_encontrado:
        print(f"Elemento {div} não encontrado após várias tentativas. Pulando para o próximo...")
        div += 2
        continue

    time.sleep(5)

    try:
        # Tenta pegar o nome e endereço
        nome_empresa = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "DUwDvf"))
        ).text
        endereco = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Io6YTe"))
        ).text
        
        # Busca todos os elementos com a classe Io6YTe
        elementos = navegador.find_elements(By.CLASS_NAME, "Io6YTe")
        instagram_elementos = navegador.find_elements(By.CLASS_NAME, "CIdPsb")  # Classe para Instagram
        
        numero_telefone = None
        site = None
        instagram = None

        for elemento in elementos:
            texto_elemento = elemento.text
            # Verifica se o texto corresponde ao formato de um número de telefone
            if phone_regex.match(texto_elemento):
                numero_telefone = texto_elemento
            # Verifica se o texto corresponde a um site (URL)
            elif url_regex.match(texto_elemento):
                site = texto_elemento

        # Procura links do Instagram
        for ig_elemento in instagram_elementos:
            texto_ig = ig_elemento.text
            if instagram_regex.search(texto_ig):
                instagram = texto_ig
                break
        
        # Armazenar dados em uma lista
        dados_empresas.append({
            "Nome": nome_empresa,
            "Endereço": endereco,
            "Telefone": numero_telefone if numero_telefone else 'Não encontrado',
            "Site": site if site else 'Não encontrado',
            "Instagram": instagram if instagram else 'Não encontrado'
        })

        print(f"\nNome: {nome_empresa}\n")
        print(f"Endereço: {endereco}\n")
        print(f"Telefone: {numero_telefone if numero_telefone else 'Telefone não encontrado'}\n")
        print(f"Site: {site if site else 'Site não encontrado'}\n")
        print(f"Instagram: {instagram if instagram else 'Instagram não encontrado'}\n")

    except (NoSuchElementException, TimeoutException):
        print("Erro ao buscar nome, endereço, telefone, site ou Instagram.")
    
    div += 2

# Criar um DataFrame e salvar como Excel
df = pd.DataFrame(dados_empresas)
nome_arquivo = f"{palavrachave}.xlsx"
df.to_excel(nome_arquivo, index=False)

print(f"Dados salvos em {nome_arquivo}")

input("Pressione Enter para fechar o navegador...")
