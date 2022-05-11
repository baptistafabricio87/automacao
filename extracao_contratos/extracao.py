import time
import pyautogui as pygui

pygui.failSafeCheck
pygui.PAUSE = 1


def abrirSap(pswd):  # Abrir SAP - Transacao SP02
    pygui.hotkey("win", "d")
    pygui.click(x=25, y=609, clicks=2)
    time.sleep(2)
    pygui.write(pswd)
    pygui.press("enter")
    time.sleep(3)


def configVisual():  # Configurações...
    pygui.click(x=354, y=121)
    time.sleep(1)
    pygui.press("tab", presses=3)
    pygui.press("delete")
    pygui.press("enter")
    time.sleep(2)


def dirParametro():
    pygui.click(x=863, y=117)  # Gravar em file local...
    pygui.click(x=531, y=458)  # Texto com tabuladores
    pygui.press("enter")
    time.sleep(3)
    pygui.click(x=539, y=351)  # Salvar como...
    time.sleep(2)
    pygui.click(x=129, y=310)  # Acesso rapido...
    pygui.click(x=258, y=433, clicks=2)  # Pasta Parametros


def moverArquivo(a, b):
    pygui.moveTo(a, b)  # Seleciona arquivo
    pygui.mouseDown()
    pygui.moveTo(x=215, y=310)  # Move arquivo para bkp
    pygui.mouseUp()
    pygui.click(x=670, y=366)  # Confima mover arquivo
    time.sleep(2)
    pygui.click(x=692, y=606)  # Salvar Arquivo
    time.sleep(2)
    pygui.click(x=420, y=390)  # Gerar
    pygui.sleep(1)
    pygui.press("f3")  # Voltar para Lista ABAP


def zmmQualif(x, y):  # ZMM_Qualificação
    pygui.click(x=129, y=300)
    time.sleep(3)
    # Configura Visualização
    configVisual()
    dirParametro()
    # Mover arquivo
    moverArquivo(x, y)


def ydv1(x, y):  # YDV1
    pygui.click(x=131, y=283)
    time.sleep(5)
    # Configura Visualização
    dirParametro()
    # Mover arquivo
    moverArquivo(x, y)


def me3l(x, y):  # ME3L
    pygui.click(x=131, y=283)
    time.sleep(5)
    # Configura Visualização
    dirParametro()
    # Mover arquivo
    moverArquivo(x, y)


def pocontrato(x, y):  # POCONTRATO
    pygui.click(x=131, y=283)
    time.sleep(5)
    # Configura Visualização
    dirParametro()
    # Mover arquivo
    moverArquivo(x, y)


def acomp_pedido(x, y):  # ACOMP_PEDIDO
    pygui.click(x=131, y=283)
    time.sleep(5)
    # Configura Visualização
    dirParametro()
    # Mover arquivo
    moverArquivo(x, y)


# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pygui.alert("Olá, sou seu robo assistente.  \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo!\
    \nVou avisar assim que terminar!!!")

pswd = pygui.password('Digite sua senha', 'Login SAP', mask='*')

# Abrir SAP - SP02
abrirSap(pswd)

# Salvando Relatorios
zmmQualif(220, 514)
ydv1(220, 462)

# AVISO AO USUARIO - PROCESSO FINALIZADO
pygui.alert("PRONTO! Terminei! \nPode continuar seu trabalho!")
