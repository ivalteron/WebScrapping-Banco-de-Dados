# WebScrapping-Banco-de-Dados
O projeto se trata de um Webscraping simples afim de aprender um pouco sobre Python e banco de dados.

# Descrição
Esse código de Webscraping tem a função de retirar informações de um determinado link, usando um HTML simples, e usar essas informações para realizar calculos de lucro afim de indicar através do envio de um email se o lucro está no valor determinado. Aproveitando essa funcionalidade também utilizei um banco de dados MYSQL para armazenar as váriaveis desejadas para realizar posteriormente uma análise desses dados.

# Começando

# Pré requesitos
Editor de código
Instalação das bibliotecas utilizadas
Conhecimento básico de Python, MYSQL e HTML
Driver do Google Chrome para conseguir realizar a extração dos dados (O driver está junto do anexo do código, mas pesquise antes a versão do seu Chrome instalado e verifique se é igual. Se não for pode baixar o driver com a versão correspondente nesse link https://chromedriver.chromium.org/downloads).

# Bibliotecas utilizadas
    from ast import parse
    from dataclasses import replace
    from http import server
    from time import sleep
    from tracemalloc import stop
    import requests
    import re
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import mysql.connector
    import pyodbc
    
# Sistema utilizado
Windows 10 Home edition

# Execução do código
O código pode ser executado diretamente no editor de código ou se preferir transforma-lo em um arquivo .EXE
Para transformar em .EXE utilizei o pyinstaller.

# Instalação do Pyinstaller
No cmd do editor de código digite pip install pyinstaller

# Transformando em .EXE
Em seguida vamos utilizar o seguinte código no terminal: pyinstaller –onefile NomeDoArquivo.py

Enfim, é isso... Espero que possa ajudar alguém.

Muito Obrigado!
