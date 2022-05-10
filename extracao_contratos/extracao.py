import time
import pyautogui

pyautogui.PAUSE = 1


def abrirSap():  # Abrir SAP - Transacao SP02
    pyautogui.hotkey("win", "d")
    pyautogui.click(x=25, y=609, clicks=2)
    time.sleep(2)
    pyautogui.write(r"Fbc@354663")
    pyautogui.press("enter")
    time.sleep(3)


def configVisual():  # Configurações...
    pyautogui.click(x=354, y=121)
    time.sleep(1)
    pyautogui.press("tab", presses=3)
    pyautogui.press("delete")
    pyautogui.press("enter")
    time.sleep(2)


def zmmQualif():  # ZMM_Qualificação
    pyautogui.click(x=129, y=301)
    time.sleep(3)


def dirParametro():
    pyautogui.click(x=863, y=117)  # Gravar em file local...
    pyautogui.click(x=531, y=458)  # Texto com tabuladores
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=539, y=351)  # Salvar como...
    time.sleep(2)
    pyautogui.click(x=129, y=310)  # Acesso rapido...
    pyautogui.click(x=258, y=433, clicks=2)  # Pasta Parametros


def moverArquivo(a, b):
    pyautogui.moveTo(a, b)  # Seleciona arquivo
    pyautogui.mouseDown()
    pyautogui.moveTo(x=215, y=310)  # Move arquivo para bkp
    pyautogui.mouseUp()
    pyautogui.click(x=670, y=366)  # Confima mover arquivo
    time.sleep(2)
    pyautogui.click(x=692, y=606)  # Salvar Arquivo
    time.sleep(2)
    pyautogui.click(x=420, y=390)  # Gerar


# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pyautogui.alert("Olá, sou seu robo assistente.  \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo!\
    \nVou avisar assim que terminar!!!")

# Abrir SAP - SP02
abrirSap()

# Salvando Relatorios
zmmQualif()

# Configura Visualização
configVisual()
dirParametro()

# Mover arquivo
moverArquivo(220, 514)

# AVISO AO USUARIO - PROCESSO FINALIZADO
pyautogui.alert("PRONTO! Terminei! \nPode continuar seu trabalho!")
