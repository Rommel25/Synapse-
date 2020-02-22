import tkinter as tk
  
#Variables
l_jeu = 1280
h_jeu = 720
res_jeu = str(l_jeu) + "x" + str(h_jeu)
nom_fenetre = "SYNAPSE 2 Joueurs"
nb_joueur = 2

pad1 = 10
pad2 = 20
pad3 = 40
c_img = 55
padH = h_jeu*7/10-pad2-2*pad1-2.5*c_img
padH2 = padH-6*pad2
padB = h_jeu*7/10-pad2-0.5*c_img
padD = l_jeu-pad3-0.5*c_img
padG = l_jeu-pad3-pad2-2.5*c_img


#Fonctions
def creation_fenetre_graphique(titre_fenetre, taille):
    win = tk.Tk()
    win.title(titre_fenetre)
    win.geometry(taille)
    return win

def import_image(nom_image):
    place = "Images/" + nom_image
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
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")
        #Création des colonnes
        canvas.create_line(l_offset+632-(632/l_c)*i, h_offset,
                           l_offset+632-(632/l_c)*i, h_offset+636,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")
        


    

#Fenetre graphique
win = creation_fenetre_graphique(nom_fenetre, res_jeu)
c = tk.Canvas(win, width = l_jeu, height = h_jeu)
c.pack() #Placement du canvas au milieu de la fenêtre

#Importation des images
img_fond = import_image("Bois_brut_tres_clair.png") #Background du jeu
img_plateau = import_image("Plateau_1.png")
img_FH = import_image("Fleche_haut_1.png")
img_FB = import_image("Fleche_bas_1.png")
img_FD = import_image("Fleche_droite_1.png")
img_FG = import_image("Fleche_gauche_1.png")
img_chiffre = import_image("Chiffre_1.png") #Fond des chiffres du tableau de bord


#Placement des images
fond = creation_objet(c, "image", img_fond, l_jeu/2, h_jeu/2)
plateau = creation_objet(c, "image", img_plateau, l_jeu/2, h_jeu/2)
creation_plateau(c)

chiffre_1 = creation_objet(c, "image", img_chiffre, padG, padH2)
chiffre_2 = creation_objet(c, "image", img_chiffre, (padG+padD)/2, padH2)
chiffre_3 = creation_objet(c, "image", img_chiffre, padD, padH2)

FH = creation_objet(c, "image", img_FH, (padD+padG)/2, padH)
FB = creation_objet(c, "image", img_FB, (padD+padG)/2, padB)
FD = creation_objet(c, "image", img_FD, padD, (padH+padB)/2)
FG = creation_objet(c, "image", img_FG, padG, (padH+padB)/2)

#Chiffres
C1 = creation_objet(c, "texte", "1", padG, padH2, 22, "#CEAF91")
C2 = creation_objet(c, "texte", "2", (padG+padD)/2, padH2, 22, "#CEAF91")
C3 = creation_objet(c, "texte", "3", padD, padH2, 22, "#CEAF91")


win.mainloop()
