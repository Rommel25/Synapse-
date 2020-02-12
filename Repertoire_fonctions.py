"""
Fichier qui rencense toute les fonctions utilisées dans les différents fichier python du code
Voire le fichier excel avec la liste des fonctions et variables pour avoir leur descritption
"""
def creation_objet(main_frame, type_objet, objet_a_creer):
    if type_objet == "texte":
        objet = tkinter.Label(main_frame, text = objet_a_creer,
                                          font = ("Comic Sans MS", 16))

    elif type_objet == "image":
            objet = tkinter.Label(main_frame, image = objet_a_creer)
    
    return objet

def placement(objet, ligne, colonne, fusion_ligne = 1, fusion_colonne = 1):
    espace = 7
    objet.grid(row = ligne, column = colonne,
                rowspan = fusion_ligne, columnspan = fusion_colonne,
                padx = espace, pady = espace)
