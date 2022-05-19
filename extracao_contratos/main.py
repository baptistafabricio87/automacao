from datetime import datetime as dt

import pyautogui as pg

import extracao as ext

# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pg.alert('Olá, sou seu robo assistente. \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo! \
    \nVou avisar assim que terminar!!!')

# Abrir SAP - SP02
ext.abrir_sap()

# Configura Visualização
ext.config_visual()

# Extração iniciada
print('\nExtração Iniciada: ', dt.now().strftime('%d-%m-%Y, %H:%M:%S \n'))

# Extraindo Relatorios
ext.me3l(300, 150, 60, 240)
ext.zmm_cont(110, 180, 30, 60)
ext.acomp(40, 30, 30, 30)
ext.po_cont(30, 30, 30, 30)
ext.zmm_forn(8, 8, 8, 8)
ext.ydv1(5, 5, 5, 5)
ext.zmm_qualif(3, 3, 3, 3)

# Extração finalizada.
print('\nExtração Finalizada: ', dt.now().strftime('%d-%m-%Y, %H:%M:%S'))

# AVISO AO USUARIO - PROCESSO FINALIZADO
pg.alert('PRONTO! Terminei! \nPode continuar seu trabalho!')
