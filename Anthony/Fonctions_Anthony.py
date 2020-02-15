import tkinter

#Variables
l_jeu = 1280
h_jeu = 720
res_jeu = str(l_jeu) + "x" + str(h_jeu)
nom_fenetre = "SYNAPSE 2 Joueurs"
cote = 700
espace = 2

#Fonctions
def import_image(nom_image):
    place = "images/" + nom_image + ".gif"
    image = tkinter.PhotoImage(file = place)
    return image

def creation_objet(main_frame, type_objet, objet_a_creer = " "):
    if type_objet == "texte":
        objet = tkinter.Label(main_frame, text = objet_a_creer,
                                          font = ("Comic Sans MS", 16))

    elif type_objet == "image":
        objet = tkinter.Label(main_frame, image = objet_a_creer)

    return objet

def creation_frame(main_frame, largeur, hauteur, couleur = ""):
    objet = tkinter.Frame(main_frame, width = largeur, height = hauteur,
                          bg = couleur)

    return objet


def placement(objet, ligne, colonne, fusion_ligne = 1, fusion_colonne = 1):
    global espace
    objet.grid(row = ligne, column = colonne,
                rowspan = fusion_ligne, columnspan = fusion_colonne,
                padx = espace, pady = espace)

def creation_fenetre_graphique(titre_fenetre, taille):
    win = tkinter.Tk()
    win.title(titre_fenetre)
    win.geometry(taille)
    
    return win

#Fenetre graphique
win2 = creation_fenetre_graphique(nom_fenetre, res_jeu)


plateau_frame = creation_frame(win2, h_jeu-2*espace, h_jeu-2*espace)
placement(plateau_frame, 0, 1, 10, 1)

score_P1_frame = creation_frame(win2, (l_jeu-h_jeu)/2-2*espace, h_jeu/2-2*espace, "green")
placement(score_P1_frame, 0, 0, 5, 1)

score_P2_frame = creation_frame(win2, (l_jeu-h_jeu)/2-2*espace, (h_jeu/2)-2*espace, "blue")
placement(score_P2_frame, 5, 0, 5, 1)


commande_frame = creation_frame(win2, (l_jeu-h_jeu)/2-2*espace, (7*h_jeu/10)-2*espace, "green")
placement(commande_frame, 0, 2, 7, 1)

piece_frame = creation_frame(win2, (l_jeu-h_jeu)/2-2*espace, (3*h_jeu/10)-2*espace, "blue")
placement(piece_frame, 7, 2, 3, 1)

"""
plateau2 = creation_objet(plateau_frame, "image", import_image("plateau"))
placement(rien, 0,0)

plateau2 = tkinter.Canvas(plateau_frame, width = cote, height = cote)
placement(plateau2, 0, 0) 

#Colonnes du plateau
plateau2.create_line(2, 2, 2, cote)
plateau2.create_line((cote/4), 0, (cote/4), cote)
plateau2.create_line((cote/2), 0, (cote/2), cote)
plateau2.create_line((cote*3/4), 0, (cote*3/4), cote)
plateau2.create_line(cote, 0, cote, cote)

#Lignes du plateau
plateau2.create_line(2, 2, cote, 2)
plateau2.create_line(0, (cote/4), cote, (cote/4))
plateau2.create_line(0, (cote/2), cote, (cote/2))
plateau2.create_line(0, (cote*3/4), cote, (cote*3/4))
plateau2.create_line(0, cote, cote, cote)
"""

win2.mainloop()

