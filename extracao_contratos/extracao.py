import time
from datetime import datetime

import pyautogui as pygui

pygui.failSafeCheck
pygui.PAUSE = 2


def abrir_sap(pswd):  # Abrir SAP - Transacao SP02
    # pygui.hotkey('win', 'd')
    pygui.click(x=25, y=609, clicks=2)
    time.sleep(2)
    pygui.write(pswd)
    pygui.press('enter')
    time.sleep(1)


def configVisual():  # Configurações...
    pygui.click(x=511, y=464)
    pygui.sleep(1)
    pygui.hotkey('ctrl', 'shift', 'f10')
    pygui.press('tab', presses=3)
    pygui.press('delete')
    pygui.press('enter')


def dir_format(slp1, slp2):
    dt = datetime.now()
    print('Gravar em file local...', dt.strftime('%H:%M:%S'))
    pygui.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pygui.press('down')  # Texto com tabuladores
    pygui.press('enter')
    dt = datetime.now()
    print('Aguardando para selecionar pasta Parametros', dt.strftime('%H:%M:%S'))
    time.sleep(slp1)
    pygui.hotkey('shift', 'tab')
    pygui.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pygui.click(x=539, y=329)  # Salvar Pasta Parametros
    dt = datetime.now()
    print('Parametros OK, aguardando p/ mover arquivo p/ bkp',
          dt.strftime('%H:%M:%S'))
    time.sleep(slp2)


def dir_nformat(slp1, slp2):
    dt = datetime.now()
    print('Gravar em file local...', dt.strftime('%H:%M:%S'))
    pygui.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pygui.press('enter')
    dt = datetime.now()
    print('Aguardando para selecionar Parametros', dt.strftime('%H:%M:%S'))
    time.sleep(slp1)
    pygui.hotkey('shift', 'tab')
    pygui.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pygui.click(x=539, y=329)  # Seleciona Pasta Parametros
    dt = datetime.now()
    print('Parametros OK, aguadardando p/ mover arquivo p/ bkp',
          dt.strftime('%H:%M:%S'))
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


def zmm_qualif(x, y, slp1, slp2, slp3):  # ZMM_Qualificação
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Qualificacao',
          dt.strftime('%H:%M:%S'))
    time.sleep(3)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 540, slp3)
    print('\n Relatorio ZMM_Qualificacao finalizado.', dt.strftime('%H:%M:%S'))


def zmm_forn(x, y, slp1, slp2, slp3):  # ZMM_FORNECEDORES
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Forncedores',
          dt.strftime('%H:%M:%S'))
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 520, slp3)
    print('\n Relatorio ZMM_Fornecedores finalizado.', dt.strftime('%H:%M:%S'))


def zmm_cont(x, y, slp1, slp2, slp3):  # ZMM_CONTRATO
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Contrato', dt.strftime('%H:%M:%S'))
    time.sleep(100)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 500, slp3)
    print('\n Relatorio ZMM_Contrato finalizado.', dt.strftime('%H:%M:%S'))


def ydv1(x, y, slp1, slp2, slp3):  # YDV1
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio YDV1', dt.strftime('%H:%M:%S'))
    time.sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 480, slp3)
    print('\n Relatorio YDV1 finalizado.', dt.strftime('%H:%M:%S'))


def po_cont(x, y, slp1, slp2, slp3):  # POCONTRATO
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio POContrato', dt.strftime('%H:%M:%S'))
    time.sleep(22)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 460, slp3)
    print('\n Relatorio POContrato finalizado.', dt.strftime('%H:%M:%S'))


def me3l(x, y, slp1, slp2, slp3):  # ME3L
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio ME3L', dt.strftime('%H:%M:%S'))
    time.sleep(300)
    dir_nformat(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 440, slp3)
    print('\n Relatorio ME3L finalizado.', dt.strftime('%H:%M:%S'))


def acomp(x, y, slp1, slp2, slp3):  # ACOMP_PEDIDO
    pygui.click(x, y)  # seleciona relatorio
    dt = datetime.now()
    print('\n Aguardando carregar relatorio Acomp_Pedido', dt.strftime('%H:%M:%S'))
    time.sleep(40)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 325, slp3)
    print('\n Relatorio Acomp_pedido finalizado.', dt.strftime('%H:%M:%S'))
