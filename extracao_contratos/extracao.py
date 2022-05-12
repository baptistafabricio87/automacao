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
    pygui.sleep(2)
    pygui.hotkey('ctrl', 'shift', 'f10')
    time.sleep(2)
    pygui.press("tab", presses=3)
    pygui.press("delete")
    pygui.press("enter")
    time.sleep(2)


def dir_format(slp1, slp2):
    pygui.click(x=863, y=117)  # Gravar em file local...
    pygui.click(x=531, y=458)  # Texto com tabuladores
    pygui.press("enter")
    time.sleep(slp1)
    pygui.click(x=539, y=351)  # Salvar como...
    time.sleep(slp2)
    pygui.click(x=129, y=310)  # Acesso rapido...
    pygui.click(x=258, y=433, clicks=2)  # Pasta Parametros


def dir_nformat(slp1, slp2):
    pygui.click(x=863, y=117)  # Gravar em file local...
    pygui.click(x=531, y=436)  # Texto com tabuladores
    pygui.press("enter")
    time.sleep(slp1)
    pygui.click(x=539, y=351)  # Salvar como...
    time.sleep(slp2)
    pygui.click(x=129, y=310)  # Acesso rapido...
    pygui.click(x=258, y=433, clicks=2)  # Pasta Parametros


def moverArquivo(a, b, slp3):
    pygui.moveTo(a, b)  # Seleciona arquivo
    pygui.mouseDown()
    pygui.moveTo(x=215, y=310)  # Move arquivo para bkp
    pygui.mouseUp()
    pygui.click(x=670, y=366)  # Confima mover arquivo
    time.sleep(5)
    pygui.click(x=692, y=606)  # Salvar Arquivo
    time.sleep(5)
    pygui.click(x=420, y=390)  # Gerar
    pygui.sleep(slp3)
    pygui.press("f3")  # Voltar para Lista ABAP


def zmmQualif(x, y, slp1, slp2, slp3):  # ZMM_Qualificação
    pygui.click(x, y)
    time.sleep(3)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 520, slp3)


def ydv1(x, y, slp1, slp2, slp3):  # YDV1
    pygui.click(x, y)
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 460, slp3)


def zmmforn(x, y, slp1, slp2, slp3):  # ZMM_FORNECEDORES
    pygui.click(x, y)
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 500, slp3)


def me3l(x, y, slp1, slp2, slp3):  # ME3L
    pygui.click(x, y)
    time.sleep(220)
    dir_nformat(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 420, slp3)


def zmmcont(x, y, slp1, slp2, slp3):  # ZMM_CONTRATO
    pygui.click(x, y)
    time.sleep(100)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 480, slp3)


def acomp(x, y, slp1, slp2, slp3):  # ACOMP_PEDIDO
    pygui.click(x, y)
    time.sleep(20)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 325, slp3)


def pocont(x, y, slp1, slp2, slp3):  # POCONTRATO
    pygui.click(x, y)
    time.sleep(22)
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(220, 440, slp3)


# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pygui.alert("Olá, sou seu robo assistente. \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo! \
    \nVou avisar assim que terminar!!!")

pswd = pygui.password('Digite sua senha', 'Login SAP', mask='*')

# Abrir SAP - SP02
abrirSap(pswd)

# Configura Visualização
configVisual()

# Salvando Relatorios
ydv1(130, 301, 5, 5, 5)
zmmQualif(130, 285, 3, 3, 3)
zmmforn(130, 268, 8, 8, 8)
me3l(130, 253, 140, 60, 140)
zmmcont(130, 237, 145, 30, 30)
acomp(130, 222, 30, 30, 30)
pocont(130, 205, 30, 30, 30)

# AVISO AO USUARIO - PROCESSO FINALIZADO
pygui.alert("PRONTO! Terminei! \nPode continuar seu trabalho!")
