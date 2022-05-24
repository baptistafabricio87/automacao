import pyautogui as pg
import pyscreeze as ps


pg.PAUSE = 2


pg.sleep(2)
# im1 = pg.screenshot('myscreenshot.png')
sz = pg.locateCenterOnScreen(r'img//txt_zmm_qualif.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_zmm_forn.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_zmm_contrato.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_ydv1.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_me3l.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_acomp.png')
print(sz)
sz = pg.locateCenterOnScreen(r'img//txt_po_contrato.png')
print(sz)


# img_rel = 'img\\txt_zmm_forn.png'
# pg.sleep(2)
# rel_position = pg.locateCenterOnScreen(img_rel)
# pg.sleep(2)
# print(rel_position)
# pg.click(rel_position)
# pg.press('f6')


# pyautogui.alert("POSICIONE O MOUSE PARA CAPTURA")
# # time.sleep(2)
# # print(pyautogui.position())
# for i in range(0, 7) :
#     time.sleep(2)
#     print(pyautogui.position())
# pyautogui.alert("POSICAO CAPTURADA")


# KEYBOARD_KEYS
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
#  '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b',
#  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept',
#  'add', 'alt', 'altleft', 'altright', 'appg', 'backspace', 'browserback',
#  'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh',
#  'browsersearch', 'browserstop', 'capglock', 'clear', 'convert', 'ctrl',
#  'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down',
#  'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12',
#  'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22',
#  'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn',
#  'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana',
#  'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect',
#  'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1',
#  'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock',
#  'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack',
#  'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right',
#  'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright',
#  'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute',
#  'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option',
#  'optionleft', 'optionright']
