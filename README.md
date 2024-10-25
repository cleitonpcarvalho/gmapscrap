# Automação de Coleta de Dados no Google Maps

Este projeto em Python é uma automação para a coleta de dados de empresas a partir de pesquisas no Google Maps. Com a integração de Selenium e Tkinter, a aplicação permite ao usuário inserir uma palavra-chave e definir a quantidade de resultados a serem coletados. Os dados coletados incluem nome da empresa, endereço, telefone, site e Instagram, e são salvos em um arquivo Excel.

[![Assista ao vídeo](https://img.youtube.com/vi/2NUPKAootOA/0.jpg)](https://youtu.be/2NUPKAootOA?si=E6OtG4RdVwsTTtQr)

## Funcionalidades

- Interface gráfica com `Tkinter` e `Kivy` para fácil uso.
- Coleta automatizada de informações de empresas, incluindo:
  - Nome
  - Endereço
  - Telefone
  - Site
  - Instagram
- Armazenamento dos dados em um arquivo Excel para fácil manipulação.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `selenium`
  - `pandas`
  - `tkinter`
  - `kivy`
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Google Chrome

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>

Instale as dependências:

pip install selenium pandas kivy

Baixe o ChromeDriver e adicione-o ao PATH do sistema.

Execute o arquivo app.py para abrir a interface gráfica:
python app.py

Insira uma palavra-chave para pesquisa e a quantidade de buscas desejadas.
Clique em Iniciar Busca para que a automação colete as informações.
Ao final da execução, escolha onde deseja salvar o arquivo Excel.
Vídeo de Demonstração
Assista ao vídeo de demonstração aqui.

Estrutura do Código

app.py: Interface gráfica construída com Tkinter e Kivy, e integração com script.py.
script.py: Script responsável pela coleta de dados no Google Maps com Selenium.
Observações
Este projeto requer conexão com a internet e um navegador Google Chrome atualizado.

Contribuição

Se desejar contribuir, por favor, abra um pull request com suas alterações ou sugestões.
