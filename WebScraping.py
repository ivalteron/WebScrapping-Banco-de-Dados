# Dado fictício para gerar um loop infinito até a ordem de stop
valor_fictcio = 100
while valor_fictcio == 100:

    #Importação das bibliotecas
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

    # Importação das opções da pagina web
    from selenium.webdriver.chrome.options import Options

    # Importação das bibliotecas para enviar email
    import smtplib
    import email.message

    # Opções de definição do Chrome
    options = Options()
    ## Não abre o chrome mas está rodando
    options.add_argument('--headless')
    ## Argumento para definir o tamanho da pagina gerada
    options.add_argument('window-size=400,800')

    # Chamada de funcionamento do Chrome para a Hidra/Draco
    navegador = webdriver.Chrome(options=options)
    navegador.get('https://www.mir4draco.com/price')

    # Chamada de funcionamento do Chrome para a Hidra/Draco
    navegador3 = webdriver.Chrome(options=options)
    navegador3.get('https://www.mir4draco.com/draco')

    # Chamada de funcionamento do Chrome para a Real/Dolar
    navegador2 = webdriver.Chrome(options=options)
    navegador2.get('https://www.google.com/search?q=dolar&rlz=1C1ISCS_pt-PTBR993BR993&biw=1365&bih=924&ei=274TYuPsAu2y5OUP4L-Z2AY&ved=0ahUKEwijxufXnJH2AhVtGbkGHeBfBms4ChDh1QMIDg&uact=5&oq=dolar&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwEyBwgAEIAEEAoyBQgAEIAEMggIABCABBCxAzIECAAQQzILCAAQgAQQsQMQgwE6CggAELEDEIMBEEM6DQgAEIAEELEDEIMBEApKBAhBGABKBAhGGABQAFi9AmC-A2gAcAB4AIABpQGIAfgEkgEDMC40mAEAoAEBwAEB&sclient=gws-wiz')

    # Tempo de carregamento da página (A pagina precisa de tempo suficiente para carregar as informações)
    sleep(5)

    # Chamando o BeautifulSoup para Hidra/Draco
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    dados = []

    # Chamando o BeautifulSoup para Draco
    sitedraco = BeautifulSoup(navegador3.page_source, 'html.parser')
    dados = []

    ## Busca todas as strings na página HTML que contém 'span'
    valor_hidra_draco = site.findAll('span', attrs={'class': 'amount'})
    valor_hidra_draco_qnt = site.find('span', attrs={'class': 'amount draco'})
    valor_hidra_draco_seprtaria_qnt = site.find('span', attrs={'class': 'amount septaria'})
    valor_draco_draco = sitedraco.find('div', attrs={'class': 'coin__volume'})
    valor_draco_draco1 = valor_draco_draco.find('span', attrs={'class': 'amount'})
    
    # Chamando o BeautifulSoup para Real/Dolar
    site2 = BeautifulSoup(navegador2.page_source, 'html.parser')
    dados1 = []
    ## Busca todas as strings na página HTML que contém 'div, após filtra por 'span'
    valor_dolar_real = site2.find('div', attrs={'class': 'b1hJbf'})
    preco_dolar_real = valor_dolar_real.findAll('span')

    # Código referente ao Real/Dolar (Selecionando o terceiro elemento[2] 'span' da página HTML)
    preco_dolar_real_final = preco_dolar_real[2].text
    ## Remover caracteres indesejados
    preco_dolar_real_final1 = preco_dolar_real_final.replace(",", ".")
    ## Transformar o valor de string para float(numeros decimais)
    preco_dolar_real_final2 = float(preco_dolar_real_final1)

    # Código referente a moeda Hidra (Selecionando o segundo elemento[1] 'span' da página HTML)
    valorhidra = valor_hidra_draco[1].text
    ## Remover caracteres indesejados
    valorhidrafinal = valorhidra.replace("$", "")
    valorhidrafinal1 = valorhidrafinal.replace(",", ".")
    ## Transformar o valor de string para float(numeros decimais)
    valorhidra1 = float(valorhidrafinal1)
    valor_hidra_str = str(valorhidra1)

    # Código referente a moeda Draco (Selecionando o sexto elemento[5] 'span' da página HTML)
    valordraco = valor_draco_draco1.text
    ## Remover caracteres indesejados
    valordracofinal = valordraco.replace("$", "")
    valordracofinal1 = valordracofinal.replace(",", ".")
    ## Transformar o valor de string para float(numeros decimais)
    valordraco1 = float(valordracofinal1)

    # Código referente as Quantidades (Selecionando o terceiro e quarto elementos[2][3] 'span' da página HTML)
    qntdraco = valor_hidra_draco_qnt.text
    qntdraco1 = int(qntdraco)
    qntseptaria = valor_hidra_draco_seprtaria_qnt.text
    ## Remover caracteres indesejados
    qntseptariafinal = re.sub('[^0-9]', '', qntseptaria)
    ## Transformar o valor de string para int(numeros inteiros)
    qntseptariafinal1 = int(qntseptariafinal)

    ##Comando para mostrar o print no formato HTML
    #print(valorhidra.prettify())

    # # Calculo do Custo e impressão (Utilizando os valores Decimais e Inteiros[float/int])
    Custo = valordraco1 * qntdraco1
    Custo_final = valorhidra1 - Custo
    lucro = Custo_final * preco_dolar_real_final2
    lucro_final = str(lucro)

    navegador.quit()
    navegador3.quit()
    navegador2.quit()

    #Impressão dos códigos
    print('Lucro: ' + lucro_final)
    print('Dolar: ' + preco_dolar_real_final1)
    print('Hidra: ' + valorhidra) 
    print('Draco: ' + valordraco)
    print('Qnt Draco: ' + qntdraco)
    print('Qnt Septaria: ' + qntseptariafinal)

    # Código para enviar o email se a opção for satisfeita
    def send_email_lucro():
        ## Mensagem do email
        email_content = 'Lucro: ' + lucro_final
        msg = email.message.Message()
        ## Titulo do email
        msg['Subject'] = 'Hora de negociar'
        ## Credenciais
        msg['From'] = ''
        msg['To'] = ''
        ## Senha do email emissor
        password = ''
        ## Configurações do email
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())

        print('sucesso ao enviar email')

    # Opção para ativar o envio do email
    if (lucro) >= 10:    
        send_email_lucro()

    # Código para enviar o email se a opção for satisfeita
    def send_email_hidra():
        ## Mensagem do email
        email_content = 'Hidra: ' + valor_hidra_str
        msg = email.message.Message()
        ## Titulo do email
        msg['Subject'] = 'Atenção no Valor da Hidra'
        ## Credenciais
        msg['From'] = ''
        msg['To'] = ''
        ## Senha do email emissor
        password = ''
        ## Configurações do email
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())

        print('sucesso ao enviar email')

    # Opção para ativar o envio do email
    if (valorhidra1) < 12 or (valorhidra1) > 25:    
        send_email_hidra()

    # Salvar os valores em um banco de dados MySQL
    # User = Usuário do banco de dados(no meu caso é o root, o meu próprio pc) Password = A senha do usuário root do Banco de dados, Host = Ip do Banco de dados, no meu caso é o ip padrão do meu pc, Database = A database que você criou quando criou o seu banco de dados.
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='')
    # Comando para utilizar a conexão criada
    cursor = cnx.cursor()
    # Comando para ser usado no banco de dados, no caso a liguagem MYSQL, dentro das chaves as variáveis as quais eu desejo armazenar.
    comando = f"""INSERT INTO valor_hidra(hidra, dolar, lucro) VALUES({valorhidra1}, {preco_dolar_real_final2}, {lucro});"""
    # Comando para executar a ação e atualizar o Banco de Dados.
    cursor.execute(comando)
    cnx.commit()

    # Tempo para refazer toda a operação
    sleep(35)

# Ordem de parar o Loop quando a condição for satisfeita
    if lucro  >= 10 or valorhidra1 <= 12 or valorhidra1 >= 25:
        break
print('Parar de enviar Email')