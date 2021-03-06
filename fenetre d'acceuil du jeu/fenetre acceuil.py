from tkinter import *
import pygame
import webbrowser

#Variables

Text = ("Minecraft", 13)
Texttitre = ("Minecraft", 40)
fenetre = Tk()
fenetre.geometry("854x580")
var = IntVar()
pygame.init()
url = "https://github.com/Rommel25/Synapse-"



#Fenetre options et ses options

def fenetre_options():
    root = Toplevel()
    def liste():
        liste1 = Listbox(root,font=Text,height=3,width=20)
        liste1.insert(1, "francais")
        liste1.insert(2, "english")
        liste1.place(x=550,y=350)
    def musique_options():
        pygame.mixer.music.load("musique1.mp3")  # Loading File Into Mixer
        pygame.mixer.music.play()  # Playing It In The Whole Device
    def rules():
        fichier = open("C:\\Users\\Utilisateur\\Desktop\\prog\\calculatrice(pbjs)\\regles.txt", "r")
        contenu = fichier.read()
        print(contenu)
    def openweb():
        webbrowser.open(url, new=1)
    root.configure(background = "#4a2210")
    Titre3 = "Options"
    Label(root, text=Titre3, font=Texttitre).pack()
    c = Checkbutton(root, text="Musique ?", command=musique_options, font=Text, height=2, width=10)
    c.place(x=160, y=150)
    btn_quit = Button(root, text="Quit", command=root.destroy, font=Text, height=2, width=20)
    btn_quit.place(x=300, y=350)
    btn_site = Button(root, text="Lien du Github", font=Text, command=openweb,height=2,width=20)
    btn_site.place(x=120, y=250)
    btn_regles = Button(root, text="regles", command=rules, height=2, width=20, font=Text)
    btn_regles.place(x=500, y=150)
    btn_langue = Button(root,text="Langue",command=liste,font=Text,height=2,width=20)
    btn_langue.place(x=500,y=250)
    root.geometry("854x580")




#fenetre d'accueil principale

def fenetre_principale():
    Titre1 = "Synapse"
    Titre1 = Label(fenetre, text=Titre1, font=Texttitre)
    Titre1.place(x=288, y=10)
    jouer = Button(fenetre, text="Jouer", command=fenetre_jouer_menu, font=Text, width=30, height=2)
    jouer.place(x=240, y=150)
    Quit = Button(fenetre, text="Quitter", command=fenetre.destroy, font=Text, width=30, height=2)
    Quit.place(x=240, y=260)
    opt = Button(fenetre, text="Options", command=fenetre_options, font=Text, width=20, height=2)
    opt.place(x=550, y=480)
    fenetre.configure(background="#4a2210")
    return fenetre_principale



#fenetre de la section jouer

def fenetre_jouer_menu():
    win = Toplevel()
    def d11():
        f11 = Toplevel()
        f11.geometry("1200x800")
    def d111():
        f111 = Toplevel()
        f111.geometry("1200x800")
    def d1o():
        f1o = Toplevel()
        f1o.geometry("1200x800")
    Titre2 = "Synapse"
    Label(win, text=Titre2, font=Texttitre).pack()
    quit = Button(win, text="Quitter", font=Text, command=win.destroy,height=2,width=20)
    quit.place(x=300,y=350)
    b11 = Button(win,text="1 Vs 1",command=d11,font=Text,height=2,width=20)
    b11.place(x=120,y=150)
    b111 = Button(win,text="1 vs 1 vs 1",command=d111,font=Text,height=2,width=20)
    b111.place(x=500,y=150)
    b1o = Button(win,text="Contre l'ordinateur",command=d1o,font=Text,height=2,width=20)
    b1o.place(x=300,y=250)
    win.geometry("854x580")
    win.configure(background="#4a2210")


fenetre_principale()

fenetre.mainloop()
