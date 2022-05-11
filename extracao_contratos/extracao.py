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
    pygui.click(x=130, y=300)
    time.sleep(3)
    # Configura Visualização
    configVisual()
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def ydv1(x, y, slp1, slp2, slp3):  # YDV1
    pygui.click(x=130, y=285)
    time.sleep(5)
    # Configura Visualização
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def zmmforn(x, y, slp1, slp2, slp3):  # ZMM_FORNECEDORES
    pygui.click(x=130, y=270)
    time.sleep(5)
    # Configura Visualização
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def me3l(x, y, slp1, slp2, slp3):  # ME3L
    pygui.click(x=130, y=255)
    time.sleep(220)
    # Configura Visualização
    dir_nformat(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def zmmcont(x, y, slp1, slp2, slp3):  # ZMM_CONTRATO
    pygui.click(x=130, y=240)
    time.sleep(100)
    # Configura Visualização
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def acomp(x, y, slp1, slp2, slp3):  # ACOMP_PEDIDO
    pygui.click(x=130, y=225)
    time.sleep(20)
    # Configura Visualização
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


def pocont(x, y, slp1, slp2, slp3):  # POCONTRATO
    pygui.click(x=130, y=210)
    time.sleep(22)
    # Configura Visualização
    dir_format(slp1, slp2)
    # Mover arquivo
    moverArquivo(x, y, slp3)


# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pygui.alert("Olá, sou seu robo assistente.  \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo!\
    \nVou avisar assim que terminar!!!")

pswd = pygui.password('Digite sua senha', 'Login SAP', mask='*')

# Abrir SAP - SP02
abrirSap(pswd)

# Salvando Relatorios
zmmQualif(220, 514, 3, 3)
# ydv1(220, 462, 5, 5)
# zmmforn(220, 501, 5, 5)
# zmmcont(220, 479, 145, 30)
# acomp(220, 327, 18, 8)
# pocont(220, 441)
me3l(220, 422, 100, 140)


# AVISO AO USUARIO - PROCESSO FINALIZADO
pygui.alert("PRONTO! Terminei! \nPode continuar seu trabalho!")
