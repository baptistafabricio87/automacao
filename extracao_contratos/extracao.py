from time import sleep
from datetime import datetime as dt

import pyautogui as pg

pg.failSafeCheck()
pg.PAUSE = 2


def abrir_sap():  # Abrir SAP - Transacao SP02
    pswd = pg.password('Digite sua senha', 'Login SAP', mask='*')
    pg.hotkey('win', 'd')
    # Define caminho da imagem a ser reconhecida
    img_rel = 'img\\atalho_sap_sp02.png'
    # Função de reconhecimento de imagem e posição
    rel_position = pg.locateCenterOnScreen(img_rel)
    pg.moveTo(rel_position)  # Move cursor até local da imagem reconhecida
    pg.doubleClick()
    sleep(2)
    pg.write(pswd)
    pg.press('enter')


def config_visual():  # Configura visualização dos relatorios
    sleep(2)  # Aguarda abertura do aplicativo
    pg.click(x=511, y=464)  # Click na janela para manter ativa.
    # Abre janela de configuração de visualização
    pg.hotkey('ctrl', 'shift', 'f10')
    pg.press('tab', presses=3)
    pg.press('delete')
    pg.press('enter')


def exp_format(slp1, slp2):  # Exportar relatorio em file local com formatação
    print('Gravar em file local...', dt.now().strftime('%H:%M:%S'))
    pg.click(x=511, y=464)  # Click na janela para manter ativa.
    pg.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pg.press('down')  # Altera para Texto com tabuladores
    pg.press('enter')
    print('Aguardando para selecionar pasta Parametros',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    pg.hotkey('shift', 'tab')
    pg.write(r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    img_rel = 'img\\btn_abrir_diretorio.png'
    rel_position = pg.locateCenterOnScreen(
        img_rel)  # localiza botao abrir pasta
    pg.click(rel_position)  # Abrir pasta Parametros
    print('Parametros OK, aguadardando p/ mover arquivo p/ bkp',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp2)


def exp_nformat(slp1, slp2):  # Exportar relatorio em file local sem formatação
    print('Gravar em file local...', dt.now().strftime('%H:%M:%S'))
    pg.click(x=511, y=464)  # Click na janela para manter ativa.
    pg.hotkey('ctrl', 'shift', 'f12')  # Gravar em file local...
    pg.press('enter')  # Confirma - Texto sem tabuladores
    print('Aguardando para selecionar Parametros',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    pg.hotkey('shift', 'tab')
    pg.write(
        r'P:\Central_Abastecimento\Automações\Projeto de Contratos\Parametros')
    img_rel = 'img\\btn_abrir_diretorio.png'
    rel_position = pg.locateCenterOnScreen(
        img_rel)  # localiza botao abrir pasta
    pg.click(rel_position)  # Abrir pasta Parametros
    print('Parametros OK, aguadardando p/ mover arquivo p/ bkp',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp2)


def move_arquivo(txt_local, slp3):  # Move arquivo para bkp
    pg.moveTo(txt_local)  # Seleciona arquivo
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


def zmm_qualif(slp1, slp2, slp3, slp4):  # ZMM_QUALIF_FOR_REL
    img_rel = 'img\\spool_zmm_qualif.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio ZMM_Qualificacao',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    # locilizar TXT
    img_rel = 'img\\txt_zmm_qualif.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio ZMM_Qualificacao finalizado.',
          dt.now().strftime('%H:%M:%S'))


def zmm_forn(slp1, slp2, slp3, slp4):  # ZMM_FORNECEDORES
    img_rel = 'img\\spool_zmm_forn.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio ZMM_Qualificacao',
          dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    # locilizar TXT
    img_rel = 'img\\txt_zmm_forn.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio ZMM_Fornecedores finalizado.',
          dt.now().strftime('%H:%M:%S'))


def zmm_cont(slp1, slp2, slp3, slp4):  # ZMM_CONTRATO
    img_rel = 'img\\spool_zmm_contrato.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    img_rel = 'img\\txt_zmm_contrato.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio finalizado.',
          dt.now().strftime('%H:%M:%S'))


def ydv1(slp1, slp2, slp3, slp4):  # YDV1
    img_rel = 'img\\spool_zmm_ydv1.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    img_rel = 'img\\txt_zmm_ydv1.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio finalizado.', dt.now().strftime('%H:%M:%S'))


def po_cont(slp1, slp2, slp3, slp4):  # POCONTRATO
    img_rel = 'img\\spool_ydv1.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    img_rel = 'img\\txt_ydv1.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio finalizado.', dt.now().strftime('%H:%M:%S'))


def me3l(slp1, slp2, slp3, slp4):  # ME3L
    img_rel = 'img\\spool_me3l.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    img_rel = 'img\\txt_me3l.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio finalizado.', dt.now().strftime('%H:%M:%S'))


def acomp(slp1, slp2, slp3, slp4):  # ACOMP_PEDIDO
    img_rel = 'img\\spool_acomp_pedido.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza relatorio
    pg.click(rel_position)  # Seleciona relatorio para extração
    pg.press('f6')
    print('\n Aguardando carregar relatorio', dt.now().strftime('%H:%M:%S'))
    sleep(slp1)
    exp_format(slp2, slp3)  # Exportar relatorio
    img_rel = 'img\\txt_acomp_pedido.png'
    rel_position = pg.locateCenterOnScreen(img_rel)  # Localiza txt
    move_arquivo(rel_position, slp4)  # Move e Salva arquivo
    print('\n Relatorio finalizado.', dt.now().strftime('%H:%M:%S'))
