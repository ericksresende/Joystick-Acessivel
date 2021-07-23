import serial
import time
import pyautogui

ser = serial.Serial('COM10', 9600)
time.sleep(1)
while 1:
    leitura = str(ser.readline().decode().strip('\r\n'))
    if (leitura=='up'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.keyDown("up")
        pyautogui.keyUp("up")
    if (leitura=='left'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.keyDown("left")
        pyautogui.keyUp("left")
    if (leitura=='right'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.keyDown("right")
        pyautogui.keyUp("right")
    if (leitura=='down'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.keyDown("down")
        pyautogui.keyUp("down")
    if (leitura=='pause'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.press('enter')
    if (leitura=='end'):
        pyautogui.moveTo(200, 200)
        pyautogui.click()
        pyautogui.press('esc')


