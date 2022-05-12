from datetime import datetime
import time

import pyautogui as pygui

pygui.failSafeCheck
pygui.PAUSE = 2


def abrirSap(pswd):  # Abrir SAP - Transacao SP02
    # pygui.hotkey('win', 'd')
    pygui.click(x=25, y=609, clicks=2)
    time.sleep(2)
    pygui.write(pswd)
    pygui.press('enter')
    # time.sleep(3)


def configVisual():  # Configurações...
    pygui.sleep(1)
    pygui.hotkey('ctrl', 'shift', 'f10')
    pygui.press('tab', presses=3)
    pygui.press('delete')
    pygui.press('enter')


def dir_format(slp1, slp2):
    pygui.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pygui.press('down')  # Texto com tabuladores
    pygui.press('enter')
    time.sleep(slp1)
    pygui.hotkey('shift', 'tab')
    pygui.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pygui.click(x=539, y=329)  # Salvar Pasta Parametros
    time.sleep(slp2)


def dir_nformat(slp1, slp2):
    pygui.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pygui.press('enter')
    print('Aguardando para selecionar Parametros')
    time.sleep(slp1)
    pygui.hotkey('shift', 'tab')
    pygui.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pygui.click(x=539, y=329)  # Seleciona Pasta Parametros
    print('Parametros selecionado, aguadardando para mover arquivo')
    time.sleep(slp2)


def move_arquivo(a, b, slp3):  # Move arquivo para bkp
    pygui.moveTo(a, b)  # Seleciona arquivo
    pygui.mouseDown()
    pygui.moveTo(x=215, y=310)  # Move para bkp
    pygui.mouseUp()
    pygui.click(x=670, y=366)  # Confima mover arquivo
    time.sleep(5)
    pygui.click(x=692, y=606)  # Salvar Arquivo
    time.sleep(5)
    pygui.click(x=420, y=390)  # Gerar
    pygui.sleep(slp3)
    pygui.press('f3')  # Voltar para Lista ABAP


def zmmQualif(x, y, slp1, slp2, slp3):  # ZMM_Qualificação
    pygui.click(x, y)  # seleciona relatorio
    time.sleep(3)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 520, slp3)


def ydv1(x, y, slp1, slp2, slp3):  # YDV1
    pygui.click(x, y)  # seleciona relatorio
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 460, slp3)


def zmmforn(x, y, slp1, slp2, slp3):  # ZMM_FORNECEDORES
    pygui.click(x, y)  # seleciona relatorio
    print('Aguardando carregar relatorio ZMM_Forncedores')
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 500, slp3)


def me3l(x, y, slp1, slp2, slp3):  # ME3L
    pygui.click(x, y)  # seleciona relatorio
    print('Aguardando carregar relatorio ME3L')
    time.sleep(210)
    dir_nformat(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 420, slp3)


def zmmcont(x, y, slp1, slp2, slp3):  # ZMM_CONTRATO
    pygui.click(x, y)  # seleciona relatorio
    print('Aguardando carregar relatorio ME3L')
    time.sleep(100)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 480, slp3)


def acomp(x, y, slp1, slp2, slp3):  # ACOMP_PEDIDO
    pygui.click(x, y)  # seleciona relatorio
    time.sleep(20)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 325, slp3)


def pocont(x, y, slp1, slp2, slp3):  # POCONTRATO
    pygui.click(x, y)  # seleciona relatorio
    time.sleep(22)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 440, slp3)


# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pygui.alert('Olá, sou seu robo assistente. \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo! \
    \nVou avisar assim que terminar!!!')

pswd = pygui.password('Digite sua senha', 'Login SAP', mask='*')

dt = datetime.now()
print('Extração Iniciada: ', dt.strftime(
    '%d-%m-%Y, %H:%M:%S'))  # Extração iniciada

# Abrir SAP - SP02
abrirSap(pswd)

# Configura Visualização
configVisual()

# Salvando Relatorios
me3l(130, 253, 100, 40, 100)
ydv1(130, 301, 5, 5, 5)
zmmQualif(130, 285, 3, 3, 3)
zmmforn(130, 268, 8, 8, 8)
zmmcont(130, 237, 145, 30, 30)
acomp(130, 220, 30, 30, 30)
pocont(130, 205, 30, 30, 30)

dt = datetime.now()
# Extração finalizada.
print('Extração Finalizada: ', dt.strftime('%d-%m-%Y, %H:%M:%S'))

# AVISO AO USUARIO - PROCESSO FINALIZADO
pygui.alert('PRONTO! Terminei! \nPode continuar seu trabalho!')
