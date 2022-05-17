import pyautogui
import time
"""
                                 TESTE DE AUTOMAÇÃO 2
             TESTE EXEMPLO PASSANDO ARQUIVOS DE UMA PASTA PARA A OUTRA  
"""

pyautogui.alert ("Sou uma IA e vou começar a fazer a automação! Não mexa em nada! Teste automação2")
pyautogui.PAUSE = 0.8
#abrir a area de trabalho
pyautogui.hotkey('winleft','d')
#selecionar a pasta chave

pyautogui.moveTo (856,277)
pyautogui.doubleClick (856,277)

#Copiar a chave com o lado direito do mouse

pyautogui.moveTo (790,278)
pyautogui.rightClick (790,278)
pyautogui.moveTo (878,532)
pyautogui.leftClick (878,532)
#arrastar a pasta Chave para a pasta Porta
pyautogui.moveTo (400,286)
pyautogui.rightClick (400,286)

#clicando com lado direito para a porta
pyautogui.moveTo (474,559)
pyautogui.leftClick (474,559)

pyautogui.alert ("TESTE FINALIZADO!!")