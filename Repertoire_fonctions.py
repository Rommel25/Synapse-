"""
Fichier qui rencense toute les fonctions utilisées dans les différents fichier python du code
Voire le fichier excel avec la liste des fonctions et variables pour avoir leur descritption
"""
def creation_objet(main_frame, type_objet, objet_a_creer = " "):
    global l_jeu
    global h_jeu
    if type_objet == "texte":
        objet = tkinter.Label(main_frame, text = objet_a_creer,
                                          font = ("Comic Sans MS", 16))

    elif type_objet == "image":
        objet = tkinter.Label(main_frame, image = objet_a_creer)

    elif type_objet == "frame":
        objet = tkinter.Frame(main_frame, width = l_jeu, height = h_jeu)
    
    return objet

def placement(objet, ligne, colonne, fusion_ligne = 1, fusion_colonne = 1):
    espace = 7
    objet.grid(row = ligne, column = colonne,
                rowspan = fusion_ligne, columnspan = fusion_colonne,
                padx = espace, pady = espace)

def creation_plateau():
    global ligne_colonne
    pas=0
    inc=int(700/ligne_colonne)-1
    for pas in range(2,700,inc):
        plateau3.create_line(pas,2,pas,700)
        plateau3.create_line(2,pas,700,pas)