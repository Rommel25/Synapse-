import tkinter as tk

###############################################################################
#Variables
l_jeu = 1280
h_jeu = 720
res_jeu = str(l_jeu) + "x" + str(h_jeu)
nom_fenetre = "SYNAPSE 2 Joueurs"
nb_joueur = 2
nb_cases = (nb_joueur*2)**2

nb_pieces_restantes = int(nb_cases * 25 / 16)
numero_tour = 1
gagnant = 0 #Numero de joueur du gagnant

nom = ["Paul", "Anthony", "Enzo"] #Liste qui contient le nom de chaque joueur
score = [3, 5, 4] #Liste qui contient le score de chaque joueur
tour_valide = False #Tour du joeur valide

#Ces variables permettent de placer les images des fleches et chiffres
pad1 = 10 #Petit espace entre les boutons
pad2 = 40 #Grand espace entre les boutons
c_img = 55 #Longeur des cotes des images des boutons
padH = int(h_jeu*6/10-pad2+50-2*pad1-2.5*c_img) #Hauteur de la fleche du haut
padB = int(h_jeu*6/10-pad2+50-0.5*c_img) #Hauteur de la fleche du bas
padG = int(l_jeu-2*pad2-2.5*c_img) #Cote de la fleche gauche
padD = int(l_jeu-pad2-0.5*c_img) #Cote de la fleche droite

padH2 = int(padH-2.5*pad2) #Hauteur des chiffres
padB2 = int(padB+2.5*pad2)

###############################################################################
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
            font = ("Minecraft", taille), fill = couleur, width = 286-2*10)

    elif type_objet == "image":
        objet_cree = main_frame.create_image(x, y, image = objet)

    return objet_cree

def creation_plateau(canvas):
    global nb_joueur #Nombre de joueur qui jouent
    l_c = 2*nb_joueur #Nombre de lignes et de colonnes sur le plateau
    l_offset = 286+36 #Largeur à partir du bord de la fenetre
    h_offset = 42 #Hauteur à partir du bord de la fenetre
    for i in range(1,l_c):
        #Création des lignes
        canvas.create_line(l_offset, h_offset+632-(632//l_c)*i,
                           l_offset+636, h_offset+632-(632//l_c)*i,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")
        #Création des colonnes
        canvas.create_line(l_offset+632-(632//l_c)*i, h_offset,
                           l_offset+632-(632//l_c)*i, h_offset+636,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")

def choix_valide_pieces(pieces_jouees):
    global nb_pieces_restantes
    if (nb_pieces_restantes - pieces_jouees) < 0:
        choix = False
        c.itemconfigure(instruction, text = "Choisissez moins de pièces !")

    else:
        choix = True

    return choix

def choix_nb_pieces(pos_X, pos_Y):
    global padH2
    global padD
    global padG

    intervalle_X_C1 = list(range(padG-55//2, padG+55//2))
    intervalle_Y_C1 = list(range(padH2-55//2, padH2+55//2))
    intervalle_X_C2 = list(range((padD+padG-55)//2, (padD+padG+55)//2))
    intervalle_Y_C2 = list(range(padH2-55//2, padH2+55//2))
    intervalle_X_C3 = list(range(padD-55//2, padD+55//2))
    intervalle_Y_C3 = list(range(padH2-55//2, padH2+55//2))

    pieces = 0
    if pos_X in intervalle_X_C1 and pos_Y in intervalle_Y_C1:
        pieces = 1

    elif pos_X in intervalle_X_C2 and pos_Y in intervalle_Y_C2:
        pieces = 2

    elif pos_X in intervalle_X_C3 and pos_Y in intervalle_Y_C3:
        pieces = 3

    return pieces

def joueur_actuel(tour, total_joueur):
    joueur_actu = numero_tour % total_joueur
    if joueur_actu == 0:
    	joueur_actu = total_joueur

    return joueur_actu


def choix_orientation_pieces(pos_X, pos_Y):
    global padH
    global padB
    global padD
    global padG

    intervalle_X_Haut = list(range((padD+padG-55)//2, (padD+padG+55)//2))
    intervalle_Y_Haut = list(range(padH-55//2, padH+55//2))
    intervalle_X_Bas = list(range((padD+padG-55)//2, (padD+padG+55)//2))
    intervalle_Y_Bas = list(range(padB-55//2, padB+55//2))
    intervalle_X_Gauche = list(range(padG-55//2, padG+55//2))
    intervalle_Y_Gauche = list(range((padH+padB-55)//2, (padH+padB+55)//2))
    intervalle_X_Droite = list(range(padD-55//2, padD+55//2))
    intervalle_Y_Droite = list(range((padH+padB-55)//2, (padH+padB+55)//2))

    orientation = "NON-DETERMINEE"
    if pos_X in intervalle_X_Haut and pos_Y in intervalle_Y_Haut:
        orientation = "Haut"

    elif pos_X in intervalle_X_Bas and pos_Y in intervalle_Y_Bas:
        orientation = "Bas"

    elif pos_X in intervalle_X_Gauche and pos_Y in intervalle_Y_Gauche:
        orientation = "Gauche"

    elif pos_X in intervalle_X_Droite and pos_Y in intervalle_Y_Droite:
        orientation = "Droite"

    return orientation

def verification(pieces_jouees, orientation):
    global nb_pieces_restantes
    if (nb_pieces_restantes - pieces_jouees) < 0:
        choix = False
        c.itemconfigure(instruction, text = "Choisissez moins de pièces !")

    else:
        choix = True

    return choix

def clic(event):
    global padH
    global padH2
    global padD
    global padG
    global padB
    global nb_pieces_restantes
    global numero_tour
    global tour_valide

    X = event.x
    Y = event.y

    #if grille est cliquee
    #c.itemconfigure(instruction, text = "Sélectionnez le nombre de pièce que vous voulez placer")

    #Definition de l'intervalle dans laquelle le joueur choisi le nombre de pieces qu'il veut placer
    intervalle_X_chiffre = list(range(padG-55//2, padD+55//2))
    intervalle_Y_chiffre = list(range(padH2-55//2, padH2+55//2))
    nb_pieces_jouees = 0
    if X in intervalle_X_chiffre and Y in intervalle_Y_chiffre:
        nb_pieces_jouees = choix_nb_pieces(X, Y)
        tour_valide = True

    #Definition de l'intervalle dans laquelle le joueur choisi l'orientation des pieces qu'il veut placer
    intervalle_X_orientation = list(range(padG-55//2, padD+55//2))
    intervalle_Y_orientation = list(range(padH-55//2, padB+55//2))
    orientation_pieces = "NON-DETERMINEE"
    if X in intervalle_X_orientation and Y in intervalle_Y_orientation:
        orientation_pieces = choix_orientation_pieces(X, Y)
        tour_valide = True

    #Definition de l'intervalle dans laquelle le joueur valide son tour
    intervalle_X_validation = list(range(padG-55//2, padD+55//2))
    intervalle_Y_validation = list(range(padB2-55//2, padB2+55//2))
    if X in intervalle_X_validation and Y in intervalle_Y_validation:
        if numero_tour == 1:
            c.event_delete("<<choix_pieces>>")
            win.destroy()
        else:
            tour_valide = verification(nb_pieces_jouees, orientation_pieces)

    #Si le choix du nombre et de l'orientation des pieces est valide, alors on met à jour les textes et la fenêtre
    if tour_valide:
        numero_tour += 1
        nb_pieces_restantes -= nb_pieces_jouees
        joueur = joueur_actuel(numero_tour, nb_joueur)

        c.itemconfigure(instruction, text = "Tour du joueur " + str(joueur))   
        c.itemconfigure(piece_restante, text = str(nb_pieces_restantes))

    win.update()





###############################################################################
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
img_validation = import_image("Fond_validation.png")

###############################################################################
#Panneau de jeu central
#Placement des images
fond = creation_objet(c, "image", img_fond, l_jeu//2, h_jeu//2)
plateau = creation_objet(c, "image", img_plateau, l_jeu//2, h_jeu//2)
creation_plateau(c)
###############################################################################

###############################################################################
#Panneau de jeu droite
#Instruction au joueur pour le tour actuel
instruction = creation_objet(c, "texte", "Cliquez sur une des cases du plateau afin de placer vos pièces", (padG+padD)//2, 70)
c.itemconfigure(instruction, justify = "center")

#Fond des chiffres
chiffre_1 = creation_objet(c, "image", img_chiffre, padG, padH2)
chiffre_2 = creation_objet(c, "image", img_chiffre, (padG+padD)/2, padH2)
chiffre_3 = creation_objet(c, "image", img_chiffre, padD, padH2)
#Chiffres
taille_chiffre = 22
C1 = creation_objet(c, "texte", "1", padG, padH2, taille_chiffre, "#CEAF91")
C2 = creation_objet(c, "texte", "2", (padG+padD)//2, padH2, taille_chiffre, "#CEAF91")
C3 = creation_objet(c, "texte", "3", padD, padH2, taille_chiffre, "#CEAF91")

#Flèches
FH = creation_objet(c, "image", img_FH, (padD+padG)//2, padH)
FB = creation_objet(c, "image", img_FB, (padD+padG)//2, padB)
FD = creation_objet(c, "image", img_FD, padD, (padH+padB)//2)
FG = creation_objet(c, "image", img_FG, padG, (padH+padB)//2)

#Champ de validation du tour
fond_validation = creation_objet(c, "image", img_validation, (padD+padG)//2, padB2)
validation = creation_objet(c, "texte", "Quitter", (padD+padG)//2, padB2, 20, "#CEAF91")
c.itemconfigure(validation, justify = "center")

#Affichage du nombre de pièce restante
txt_piece_restante = creation_objet(c, "texte", "Nombre de pièces restantes :",
    (padG+padD)//2, 504 + 86)
c.itemconfigure(txt_piece_restante, justify = "center")

piece_restante = creation_objet(c, "texte", str(nb_pieces_restantes), 
    (padG+padD)//2, 504 + 76 + 90, 44)
###############################################################################

###############################################################################
#Panneau de jeu gauche
for j in range (0,nb_joueur):
    #nom.append("Joueur " + str(j+1))
    creation_objet(c, "texte", str(nom[j]), 286//2, ((h_jeu*j)//nb_joueur)+30, 24)
    creation_objet(c, "texte", "Parties gagnées : ", 286//2, ((h_jeu*j)//nb_joueur)+80, 16)
    creation_objet(c, "texte", str(score[j]), 286//2, ((h_jeu*j)//nb_joueur)+150, 40)


###############################################################################
c.event_add("<<choix_pieces>>", "<Button-1>")


while nb_pieces_restantes > 0:
    win.update()
    c.bind("<<choix_pieces>>", clic)


c.event_delete("<<choix_pieces>>")

c.itemconfigure(instruction, text = "Fin de la partie")

c.create_rectangle(280,720//4, l_jeu-280, 3*720//4, fill = "lightgrey",
        outline = "red3", width = 10)

if gagnant == 0:
    message = creation_objet(c, "texte", "Le gagnant de la partie est le joueur 2 !",
        l_jeu//2, h_jeu//2, 50, "red")
    c.itemconfigure(message, justify = "center", width = 700)

elif gagnant == 1:
    message = creation_objet(c, "texte", "Le gagnant de la partie est le joueur 1 !",
        l_jeu//2, h_jeu//2, 50, "red3")
    c.itemconfigure(message, justify = "center", width = 700)

win.mainloop()
