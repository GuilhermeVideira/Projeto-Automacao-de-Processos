#!/usr/bin/env python
# coding: utf-8

# In[55]:


# pyautogui.click --> Clicar com o mouse
# pyautogui.write --> Escrever um texto
# pyautogui.press --> Apertar uma tecla
# pyautogui.hotkey --> Aperta uma combinação de teclas

import pyautogui
import time

pyautogui.PAUSE = 0.7

# 1 - Acessar o sistema
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

# 2 - Realizar o login
pyautogui.click(x=584, y=344)
pyautogui.write("Guilherme Videira")

pyautogui.click(x=706, y=401)
pyautogui.write("Senha123#")

pyautogui.click(x=669, y=497)

time.sleep(5)

# 3 - Baixar a base de dados
# Propriedades: button="right": Aperta o botão direito do mouse // clicks=2: Realizar duplo click
pyautogui.click(x=435, y=515, button="right")

pyautogui.click(x=595, y=585)

time.sleep(5)


# In[58]:


# 4 - Calcular os indicadores
import pandas as pd

# Importar a base de dados
tabela = pd.read_csv(r"C:\Users\PHPM\Downloads\Compras.csv", sep=";") #Adicionar o "r" quando for caminho
display(tabela)

# Calculo dos indicadores
# Total gasto: Soma dos valores da última coluna
total_gasto = tabela["ValorFinal"].sum()

# Quantidade: Somar a coluna quantidade
quantidade = tabela["Quantidade"].sum()

# Valor médio: Total gasto / Quantidade
media = total_gasto / quantidade

print(total_gasto)


# In[71]:


# 5 - Enviar um email
import pyperclip

# Acessar o email
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/1/#inbox")
pyautogui.press("enter")

time.sleep(15)

# Clicar escrever
pyautogui.click(x=116, y=159)

# Preecher o email
pyautogui.write("guifvideira@gmail.com")
pyautogui.press("tab") #Selecionar email

pyautogui.press("tab") # Ir para a linha de baixo
pyperclip.copy("Relatório de Compras")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # Ir para a linha de baixo

texto = f"""
Olá!

Envio o relatório semanal de compras:

- Total Gasto: R${total_gasto:,.2f}
- Quantidade de produtos: {quantidade:,}
- Valor médio: R${media:,.2f}

Qualquer dúvida é só entrar em contato!

Grato, 

Guilherme Videira. 

"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

pyautogui.hotkey("ctrl", "enter")


# In[ ]:


#Instalações
get_ipython().system('pip install pandas')
get_ipython().system('pip install pyautogui')


# In[61]:


#Tempo de localizar lugar da tela
time.sleep(5)
print(pyautogui.position())

