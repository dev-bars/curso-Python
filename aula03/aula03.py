import pyautogui as py
py.press("win")
py.write("chrome")
py.press("enter")
py.sleep(2)
py.write("Senai Americana")
py.press("enter")
py.sleep(2)
#print(py.position()) este comando serve para descobrir a posição do mouse na tela
py.click(190, 465,button="left")
py.sleep(3)
#print(py.position())
py.click(1514, 775,button="left")
print(py.position())
py.sleep(3)
#py.click(1514, 775,button="left")



#Info: "Esta biblioteca PYAUTOGUI é utilizada para automação de tarefas de teclado 
# e mouse, permite simular cliques, digitação e acessos. Utilizo para
# realizar tarefas rotineiras de forma automática"