from time import sleep
from datetime import datetime as dt

import pyautogui as pg

pg.failSafeCheck
pg.PAUSE = 2


def abrir_sap(pswd):  # Abrir SAP - Transacao SP02
    # pg.hotkey('win', 'd')
    img_rel = 'img\spool_ydv1.png' # Define caminho da imagem
    rel_position = pg.locateCenterOnScreen(img_rel)
    pg.click(rel_position, clicks=2)
    sleep(2)
    pg.write(pswd)
    pg.press('enter')
    sleep(1)

# Configura visualização dos relatorios
def configVisual():  
    pg.click(x=511, y=464) # clica na janela para manter ativa.
    pg.hotkey('ctrl', 'shift', 'f10')
    pg.press('tab', presses=3)
    pg.press('delete')
    pg.press('enter')


def dir_format(slp1, slp2):
    # dt = datetime.now()
    print('Gravar em file local...', dt.now().strftime('%H:%M:%S'))
    pg.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pg.press('down')  # Texto com tabuladores
    pg.press('enter')
    # dt.now() = datetime.now()
    print('Aguardando para selecionar pasta Parametros', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    pg.hotkey('shift', 'tab')
    pg.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pg.click(x=539, y=329)  # Salvar Pasta Parametros
    # dt = datetime.now()
    print('Parametros OK, aguardando p/ mover arquivo p/ bkp', dt.now().strftime('%H:%M:%S'))
    sleep(slp2)


def dir_nformat(slp1, slp2):
    # dt = datetime.now()
    print('Gravar em file local...', dt.now().strftime('%H:%M:%S'))
    pg.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pg.press('enter')
    # dt.now() = datetime.now()
    print('Aguardando para selecionar Parametros', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    pg.hotkey('shift', 'tab')
    pg.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    pg.click(x=539, y=329)  # Seleciona Pasta Parametros
    # dt.now() = datetime.now()
    print('Parametros OK, aguadardando p/ mover arquivo p/ bkp',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp2)


def move_arquivo(a, b, slp3):  # Move arquivo para bkp
    pg.moveTo(a, b)  # Seleciona arquivo
    pg.mouseDown()
    pg.moveTo(x=215, y=310)  # Move para bkp
    pg.mouseUp()
    pg.click(x=670, y=366)  # Confima mover arquivo
    sleep(5)
    pg.click(x=692, y=606)  # Clica em Salvar
    sleep(5)
    pg.click(x=420, y=390)  # Clica em Gerar
    pg.sleep(slp3)
    pg.press('f3')  # Voltar para Lista ABAP Spool


def zmm_qualif(x, y, slp1, slp2, slp3):  # ZMM_Qualificação
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Qualificacao',
          dt.now().strftime('%H:%M:%S'))
    sleep(3)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 540, slp3)
    print('\n Relatorio ZMM_Qualificacao finalizado.', dt.now().strftime('%H:%M:%S'))


def zmm_forn(x, y, slp1, slp2, slp3):  # ZMM_FORNECEDORES
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Forncedores',
          dt.now().strftime('%H:%M:%S'))
    sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 520, slp3)
    print('\n Relatorio ZMM_Fornecedores finalizado.', dt.now().strftime('%H:%M:%S'))


def zmm_cont(x, y, slp1, slp2, slp3):  # ZMM_CONTRATO
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio ZMM_Contrato', dt.now().strftime('%H:%M:%S'))
    sleep(100)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 500, slp3)
    print('\n Relatorio ZMM_Contrato finalizado.', dt.now().strftime('%H:%M:%S'))


def ydv1(x, y, slp1, slp2, slp3):  # YDV1
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio YDV1', dt.now().strftime('%H:%M:%S'))
    sleep(5)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 480, slp3)
    print('\n Relatorio YDV1 finalizado.', dt.now().strftime('%H:%M:%S'))


def po_cont(x, y, slp1, slp2, slp3):  # POCONTRATO
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio POContrato', dt.now().strftime('%H:%M:%S'))
    sleep(22)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 460, slp3)
    print('\n Relatorio POContrato finalizado.', dt.now().strftime('%H:%M:%S'))


def me3l(x, y, slp1, slp2, slp3):  # ME3L
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio ME3L', dt.now().strftime('%H:%M:%S'))
    sleep(300)
    dir_nformat(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 440, slp3)
    print('\n Relatorio ME3L finalizado.', dt.now().strftime('%H:%M:%S'))


def acomp(x, y, slp1, slp2, slp3):  # ACOMP_PEDIDO
    pg.click(x, y)  # seleciona relatorio
    # dt.now() = datetime.now()
    print('\n Aguardando carregar relatorio Acomp_Pedido', dt.now().strftime('%H:%M:%S'))
    sleep(40)
    dir_format(slp1, slp2)
    # Mover arquivo
    move_arquivo(220, 325, slp3)
    print('\n Relatorio Acomp_pedido finalizado.', dt.now().strftime('%H:%M:%S'))
