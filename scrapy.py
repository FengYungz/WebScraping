from selenium import webdriver
import time


driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get('https://sorteia-quiz.vercel.app/')

mode = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-hKwDye.fNiswD > div > div.sc-eCImPb.kKCenc > div > span'
dificuldade = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-hKwDye.fNiswD > div > div.handleDifficulty > span'
sortear = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-gsDKAQ.giCzBE > div > div.sc-dkPtRN.coZBdQ > button:nth-child(1)'
limpar = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-gsDKAQ.giCzBE > div > div.sc-dkPtRN.coZBdQ > button:nth-child(2)'
responde = '#alt'
salvar = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-gsDKAQ.giCzBE > div > button'
textoo = '#root > div.sc-jRQBWg.bwYaOL > div.sc-bdvvtL.lkYwdo > div.sc-gsDKAQ.giCzBE > div > div.pega > span'

#identifica e retorna os elementos
sortear_element = driver.find_element_by_css_selector(sortear)
responde_element = driver.find_element_by_css_selector(responde)
salvar_element = driver.find_element_by_css_selector(salvar)
limpar_element = driver.find_element_by_css_selector(limpar)

"""
#Acionando botao
    sortear_element.click()
    limpar_element.click()
    salvar_element.click()
"""
#instrucoes_element.click()


"""
Inserindo resposta
    responde_element.send_keys('(C)')
"""

#Tempo para jogador responder a Pergunta
#time.sleep(15)

verificaMode = 0

#loop para aguardar o Jogador escolher o modo de jogo
while verificaMode == 0:
    mode_element = driver.find_element_by_css_selector(mode).text
    if mode_element == 'showDoMilhao' or mode_element == 'highScore':
        print(f"*************************O modo de jogo escolhido foi {mode_element}*************************")
        verificaMode = 1


verificaDificuldade = 0

#Loop para aguardar o Jogador escolher a dificuldade
while  verificaDificuldade == 0:
    #Pegando nivel de dificuldade
    dificuldade_element = driver.find_element_by_css_selector(dificuldade).text
    #Verificando a resposta
    if dificuldade_element == 'Easy' or dificuldade_element == 'Medium' or dificuldade_element == 'Hard':
        print(f"*************************Dificuldade inserida foi: {dificuldade_element}*************************")
        verificaDificuldade = 1


cont = 0
if mode_element == 'highScore':
    while cont < 16:
        cont += 1
        if dificuldade_element == 'Easy':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(2) #40
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
            if pegatexto == '2':
                print("2 do pega texto nao e int e sim std")
        elif dificuldade_element == 'Medium':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(7)#30
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
        elif dificuldade_element == 'Hard':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(7)#20
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
elif  mode_element == 'showDoMilhao':
     while cont < 20:
        cont += 1
        if dificuldade_element == 'Easy':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(7) #40
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
        elif dificuldade_element == 'Medium':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(7)#30
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
        elif dificuldade_element == 'Hard':
            limpar_element.click()
            time.sleep(0.5)
            sortear_element.click()
            time.sleep(7)#20
            # Pegando resposta da Pergunta
            pegatexto = driver.find_element_by_css_selector(textoo).text
            print(f"*************************Resposta inserida foi: {pegatexto}*************************")
