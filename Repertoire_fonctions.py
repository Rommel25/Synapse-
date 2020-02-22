import tkinter as tk

"""
Fichier qui rencense toute les fonctions utilisées dans les différents fichier python du code
Voire le fichier excel avec la liste des fonctions et variables pour avoir leur descritption
"""
def creation_fenetre_graphique(titre_fenetre, taille):
    win = tk.Tk()
    win.title(titre_fenetre)
    win.geometry(taille) #Taille de la fenêtre sous la forme "LargeurxHauteur"
    
    return win

def import_image(nom_image):
    place = "Images/" + nom_image #NE PAS OUBLIER D'AJOUTER L'EXTENSION AVEC LE NOM DE L'IMAGE!!!
    image = tk.PhotoImage(file = place)
    
    return image

def creation_objet(main_frame, type_objet, objet, x, y, taille = 18,
                   couleur = "#000000"):
    
    if type_objet == "texte":
        objet_cree = main_frame.create_text(x, y, text = objet,
                              font = ("Minecraft", taille), fill = couleur)
        
    elif type_objet == "image":
        objet_cree = main_frame.create_image(x, y, image = objet)
        
    return objet_cree
    
def creation_plateau(canvas):
    global nb_joueur #Nombre de joueur qui jouent
    l_c = 2*nb_joueur #Nombre de lignes et de colonnes sur le plateau
    l_offset = 286+36 #Largeur à partir du bord de la fenêtre
    h_offset = 42 #Hauteur à partir du bord de la fenêtre
    for i in range(1,l_c):
        #Création des lignes
        canvas.create_line(l_offset, h_offset+632-(632/l_c)*i,
                           l_offset+636, h_offset+632-(632/l_c)*i,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330") #Couleur pour le plateau_1
        #Création des colonnes
        canvas.create_line(l_offset+632-(632/l_c)*i, h_offset,
                           l_offset+632-(632/l_c)*i, h_offset+636,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")
