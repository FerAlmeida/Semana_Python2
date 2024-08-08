import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker("PETR4.SA").history(start="2020-01-01", end="2020-12-31")
fechamento = dados.Close

maxima = fechamento.max()
minima = fechamento.min()
valor_medio = fechamento.mean()

destinatario = "___________________@gmail.com"
assunto = "Análises do Projeto 2020"

mensagem = f""" 
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R$ {maxima}
Cotação mínima: R$ {minima}
Valor médio:    R$ {valor_medio}

Qualquer dúvida, estou á disposição!

Atte.
"""
# abrir o navegador e ir ao e-mail desejado
webbrowser.open("www.gmail.com")

# abaixo vamos colocar um time para que o PYTHON ajuste o tempo de carregamento do e-mail, essa função irá auxiliar nas próximas configurações do projeto
time.sleep(4)

# Para não correr o riso do pyautogui sair disparado escrevendo desorientadamente devemos adicionar a ele um comando de pausa para que se execute com calma
pyautogui.PAUSE = 3

# Para clicar no botão escrever,o ponteiro do mouse tem uma coordenada no eixo X e eixo Y, esses pontos que determinarão a coordenada a ser clicada
# Para descobrir essas coordenadas, PRIMEIRO vamos utilizamos o comando pyautogui.position() e onde o mouse for parado será a coordenada a ser adicionada
# Então ao abrir na sequência o e-mail, já apontamos o mouse para o local onde está o botão escrever e teremos a coordenada do botão "escrever"
pyautogui.click(x=74, y=213)

# digitar o e-mail do destinátario e teclar TAB -> copia o e-mail de destino, cola o e-mail de destino e da o TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do e-mail
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem do e-mail
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=1303, y=991)
