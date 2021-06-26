from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

#make class containing all coordinates

class Cordinates():
    replayBtn=(700,341)
    dinosaur=(450,360)


def restartGame():
    pyautogui.click(Cordinates.replayBtn)  # restarts the game
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def grabImg():
    box = (Cordinates.dinosaur[0] + 60, Cordinates.dinosaur[1],
           Cordinates.dinosaur[0] + 100, Cordinates.dinosaur[1] + 30)
    img = ImageGrab.grab(box)
    grayImg = ImageOps.grayscale(img)  # get the gray scale
    a = array(grayImg.getcolors())
    return (a.sum())


def main():
    restartGame()
    while True:
        if (grabImg() != 1447):
            pressSpace()
            time.sleep(0.1)


main()
