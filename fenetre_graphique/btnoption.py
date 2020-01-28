from tkinter import *

Text = ("helvetic", 10)
def nouvelle_fenetre():
    win = Toplevel()
    message = "But du jeu: \n" \
              "Le but du jeu est d’amener son adversaire à ne plus pouvoir jouer. \n" \
              "Déroulement d’une partie: \n" \
              "Le 1 er joueur est tiré au sort. Il peut placer sur la case qu’il veut 1, 2 ou 3 pièces (placée dans le" \
              "même sens)\n qui vont indiquer l’endroit où le joueur suivant doit jouer. Si le joueur 1 choisi : \n" \
              "⮚ 1pièce : le joueur 2 jouera sur la 1 ère case dans le sens indiqué par la pièce ;\n" \
              "⮚ 2 pièces : le joueur 2 jouera sur la 2 ème case dans le sens indiqué par les pièces ;\n" \
              "⮚ 3 pièces : le joueur 2 jouera sur la 3 ème case dans le sens indiqué par les pièces. \n" \
              "Puis les joueurs jouent à tour de rôle tout en suivant cette règle."
    Label(win, text=message, font=Text).pack()
    Button(win,text="ok",command=win.destroy).pack()
    win.geometry("650x650")


fenetre = Tk()
fenetre.geometry("500x500")
Button(fenetre, text="Règles du jeu", command=nouvelle_fenetre).pack()
fenetre.mainloop()
