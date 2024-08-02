import pyautogui, time

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://sp.senai.br/unidade/jundiai/")
pyautogui.prees("enter")
time.sleep(2)
cursos = pyautogui.locateOnScreeen('cursos.png')
posi_cursos = pyautogui.center(cursos)
pyautogui.click(posi_cursos.x, posi_cursos.y)
