# Passo a passo do projeto

# entrar no sistema
        #  https://dlp.hashtagtreinamentos.com/python/intensivao/login
# fazer login
# importar base de dados
# cadastrar um produto
# repetir até acabar os produtos

# Importando bibliotecas em Python

import pyautogui
import time
import pandas as pd

# pyautogui - RPA - automação
# Clicar - pyautogui.click
# Escrever - pyautogui.write
# Apertar uma tecla - oyautogui.press
# apertar - pyautogui.hotkey("ctrl", "c")
# scroll - pyautogui.scroll()

# Pausar um segundo por tarefa
#pyautogui.PAUSE = 1

# Abrir o google:

pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
time.sleep(0.5)

# Passo 1: Entrar no sistema

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(1)

# Pausar em determinado momento

#time.sleep(1)

# Passo 2: Fazer login

#pyautogui.press("tab")
pyautogui.click(x=756, y=408)

# digitar o email

pyautogui.write("testegui@guimail.com")
#time.sleep(1)
# prox.

pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

# Passo 3: Importar a base de dados

tabela = pd.read_csv("produtos.csv")
#print(tabela)

for linha in tabela.index:

    # Passo 4: Cadastrar um produto

    pyautogui.click(x=748, y=294)
    #codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
    
    #Passo 5: Repetir até acabar os produtos