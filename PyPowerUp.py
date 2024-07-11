#1 entra no sistema da empresa
#   numero: (21) 96721-8715    
#   link https://dlp.hashtagtreinamentos.com/python/intensivao/login
#2 Fazer o login
#3 Importar a base de dados
#4 Cadastrar um produto
#5 Repetir o passo 4 até o ultimo produto

#pyautogui.click 
#pyautogui.write 
#pyautogui.press 
#pyautogui.hotkey

#Bibliotecas

import pyautogui
import time
import pandas

#1 
pyautogui.PAUSE = 0.25

pyautogui.press('win')

pyautogui.write('Chrome')

pyautogui.press('Enter')
time.sleep(1)
pyautogui.press('tab')

pyautogui.press('Enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('Enter')

time.sleep(1)

#2

pyautogui.click(x=153, y=369)
pyautogui.write('loginzin')

time.sleep(1)

pyautogui.click(x=174, y=446)
pyautogui.write('senhahaha')

pyautogui.click(x=351, y=496)

time.sleep(1)
pyautogui.click(x=124, y=294)

#3
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:        
    pyautogui.click(x=113, y=259)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)

    pyautogui.press('tab')
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)

    pyautogui.press('tab')
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)

    pyautogui.press('tab')
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)

    pyautogui.press('tab')
    observacao = str(tabela.loc[linha,"obs"])
    if observacao != "nan":    
        pyautogui.write(observacao)

    pyautogui.press('tab')
    pyautogui.press('Enter')

    time.sleep(1)

    pyautogui.scroll(5000)