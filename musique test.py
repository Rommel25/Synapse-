import pygame
from tkinter import *
root = Tk()
pygame.init()
def play():
    pygame.mixer.music.load("Musique/musique1.mp3") #Loading File Into Mixer
    pygame.mixer.music.play() #Playing It In The Whole Device
Button(root,text="Play",command=play).pack()
root.mainloop()
#voir pour mettre la musique dès l'ouverture du jeu
#Quand la musique ce termine son état est 0
#if musique == 1:
    #pygame.mixer.music.play()
#if musique == 0:
    #musique = 1