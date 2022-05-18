from datetime import datetime as dt

import pyautogui as pg

import extracao as ext

# AVISO AO USUÁRIO - INICIANDO PROCESSO!
pg.alert('Olá, sou seu robo assistente. \
    \nPreciso que não interfira no processo OK? \
    \nPara isso não mexa no pc até eu finalizar o processo! \
    \nVou avisar assim que terminar!!!')

pswd = pg.password('Digite sua senha', 'Login SAP', mask='*')

# Abrir SAP - SP02
ext.abrir_sap(pswd)

dt = datetime.now()
print('Extração Iniciada: ', dt.now().strftime(
    '%d-%m-%Y, %H:%M:%S'))  # Extração iniciada

# Configura Visualização
ext.configVisual()

# Salvando Relatorios
ext.me3l(130, 252, 150, 60, 240)
ext.ydv1(130, 285, 5, 5, 5)
ext.zmm_qualif(130, 264, 3, 3, 3)
ext.zmm_forn(130, 301, 8, 8, 8)
ext.zmm_cont(130, 235, 180, 30, 50)
ext.acomp(130, 218, 30, 30, 30)
ext.po_cont(130, 205, 30, 30, 30)

dt = datetime.now()
# Extração finalizada.
print('\n Extração Finalizada: ', dt.now().strftime('%d-%m-%Y, %H:%M:%S'))

# AVISO AO USUARIO - PROCESSO FINALIZADO
pg.alert('PRONTO! Terminei! \nPode continuar seu trabalho!')
