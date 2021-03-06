import tkinter as tk

###############################################################################
#Variables
l_jeu = 1280
h_jeu = 720
res_jeu = str(l_jeu) + "x" + str(h_jeu)
nom_fenetre = "SYNAPSE 2 Joueurs"
nb_joueur = 2 #Nombre de joueur qui jouent
l_c = 2*nb_joueur #Nombre de lignes et de colonnes sur le plateau
nb_cases = l_c**2

grille_de_jeu = [] #Grille qui sauvegarde les informations du plateau
liste_piece = [] #Liste qui stocke les pieces
liste_image_piece = [] #Liste qui stocke les nom des images des pieces

nb_pieces_restantes = int(nb_cases * 25 / 16)
numero_tour = 1
gagnant = 0 #Numero de joueur du gagnant

nom = ["Paul", "Anthony", "Enzo"] #Liste qui contient le nom de chaque joueur
score = [3, 5, 4] #Liste qui contient le score de chaque joueur

ligne = 0 #Ligne actuelle de la sélection du plateau
colonne = 0 #Colonne actuelle de la sélection du plateau
axe_X = 0
axe_Y = 0
nb_pieces_jouees = 0 #Nombre de pieces jouees
orientation_pieces = "NON-DETERMINEE" #Orientation de la piece jouees
tour_valide = False #Tour du joeur valide
espace_vide = nb_cases

l_offset = 286+36 #Largeur entre le bord de la fenetre et le plateau
h_offset = 42 #Hauteur entre le bord de la fenetre et le plateau

#Ces variables permettent de placer les images des fleches et chiffres
pad1 = 5 #Petit espace entre les boutons
pad2 = 40 #Grand espace entre les boutons
c_img = 55 #Longeur des cotes des images des boutons
padH = int(h_jeu*6.3/10-pad2+50-2*pad1-2.5*c_img) #Hauteur de la fleche du haut
padB = int(h_jeu*6.3/10-pad2+50-0.5*c_img) #Hauteur de la fleche du bas
padG = int(l_jeu-2*pad2-2.5*c_img) #Cote de la fleche gauche
padD = int(l_jeu-pad2-0.5*c_img) #Cote de la fleche droite

padH2 = int(padH-2.1*pad2) #Hauteur des chiffres
padB2 = int(padB+2.2*pad2) #Hauteur du bouton de validation

###############################################################################
#Fonctions
def reinitialisation_variables():
    global nb_pieces_restantes
    global numero_tour
    global gagnant
    global nb_pieces_jouees
    global orientation_pieces
    global tour_valide
    global espace_vide
    global grille_de_jeu
    global liste_piece
    global liste_image_piece
    global ligne
    global colonne
    global axe_X
    global axe_Y

    nb_pieces_restantes = int(nb_cases * 25 / 16)
    numero_tour = 1
    gagnant = 0 #Numero de joueur du gagnant

    nb_pieces_jouees = 0 #Nombre de pieces jouees
    orientation_pieces = "NON-DETERMINEE" #Orientation de la piece jouees
    tour_valide = False #Tour du joeur valide
    espace_vide = nb_cases

    grille_de_jeu = [] #Grille qui sauvegarde les informations du plateau
    liste_piece = [] #Liste qui stocke les pièces
    liste_image_piece = [] #Liste qui stocke les nom des images des pieces
    ligne = 0 #Ligne actuelle de la sélection du plateau
    colonne = 0 #Colonne actuelle de la sélection du plateau
    axe_X = 0
    axe_Y = 0


def creation_fenetre_graphique(titre_fenetre, taille):
    win = tk.Tk()
    win.title(titre_fenetre)
    win.geometry(taille)

    return win

def import_image(nom_image):
    place = "Images/" + nom_image
    image = tk.PhotoImage(file = place)

    return image

def creation_objet(main_frame, type_objet, objet, x, y, taille = 16,
                   couleur = "#000000"):

    if type_objet == "texte":
        objet_cree = main_frame.create_text(x, y, text = objet, 
            font = ("Minecraft", taille), fill = couleur, width = 286-2*5)

    elif type_objet == "image":
        objet_cree = main_frame.create_image(x, y, image = objet)

    return objet_cree

def matrice(nb_lignes_colonnes):
    grille = []
    for i in range(nb_lignes_colonnes):
        grille.append([])
        for j in range(nb_lignes_colonnes):
            grille[i].append("-")

    return grille

def creation_plateau(canvas):
    global nb_joueur
    global grille_de_jeu
    global l_offset
    global h_offset
    global l_c

    couleur = "#7A4330"

    for i in range(1,l_c):
        #Création des lignes
        canvas.create_line(l_offset, h_offset+632-(632//l_c)*i,
                           l_offset+636, h_offset+632-(632//l_c)*i,
                           width = 10-(nb_joueur-2)*2, fill = couleur)
        #Création des colonnes
        canvas.create_line(l_offset+632-(632//l_c)*i, h_offset,
                           l_offset+632-(632//l_c)*i, h_offset+636,
                           width = 10-(nb_joueur-2)*2, fill = couleur)

def affichage_joueur(nb_joueur, nom_joueur, score_joueur):
    global txt_score

    for j in range (nb_joueur):
        #nom_joueur.append("Joueur " + str(j+1))
        creation_objet(c, "texte", str(nom_joueur[j]), 286//2, ((h_jeu*j)//nb_joueur)+30, 24)
        creation_objet(c, "texte", "Parties gagnées : ", 286//2, ((h_jeu*j)//nb_joueur)+80, 16)
        c.itemconfigure(txt_score[j], text = str(score_joueur[j]))



def localisation_grille(pos_X, pos_Y):
    global nb_joueur
    global l_offset
    global h_offset
    global l_c

    lin = (pos_Y // (632//l_c))
    col = ((pos_X-l_offset) // (632//l_c))

    return lin, col

def choix_nb_pieces(pos_X, pos_Y):
    global padH2
    global padD
    global padG
    global orientation_pieces

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

    if orientation_pieces == "NON-DETERMINEE":
        c.itemconfigure(instruction, text = "Sélectionnez l'orientation des pièces à placer")
    else:
        c.itemconfigure(instruction, text = "Validez le tour")

    return pieces

def choix_orientation_pieces(pos_X, pos_Y):
    global padH
    global padB
    global padD
    global padG
    global nb_pieces_jouees

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
        orientation = "H"
        axe_X = 0
        axe_Y = -1

    elif pos_X in intervalle_X_Bas and pos_Y in intervalle_Y_Bas:
        orientation = "B"
        axe_X = 0
        axe_Y = 1

    elif pos_X in intervalle_X_Gauche and pos_Y in intervalle_Y_Gauche:
        orientation = "G"
        axe_X = -1
        axe_Y = 0

    elif pos_X in intervalle_X_Droite and pos_Y in intervalle_Y_Droite:
        orientation = "D"
        axe_X = 1
        axe_Y = 0

    if nb_pieces_jouees == 0:
        c.itemconfigure(instruction, text = "Sélectionnez le nombre de pièce à placer")
    else:
        c.itemconfigure(instruction, text = "Validez le tour")


    return orientation, axe_X, axe_Y

def verification_nb_pieces(pieces_jouees):
    global nb_pieces_restantes

    if nb_pieces_restantes < pieces_jouees:
        choix = False
        c.itemconfigure(instruction, text = "Choisissez moins de pièces !")
    elif pieces_jouees == 0:
        choix = False
        c.itemconfigure(instruction, text = "Choisissez un nombre de pièces !")
    else:
        choix = True
 
    return choix

def verification_orientation(orientation):
    if orientation == "NON-DETERMINEE":
        choix = False
        c.itemconfigure(instruction, text = "Choisissez une orientation pour vos pièces !")
    else:
        choix = True

    return choix

def verification_plateau(ligne, colonne):
    global l_c
    global grille_de_jeu
    global nb_pieces_restantes
    global nb_pieces_jouees
    #Verification par rapport à la grille du plateau
    if (ligne + 1) > l_c or (ligne) < 0:
        choix = False
        c.itemconfigure(instruction, text = "Votre choix n'est pas valide, les pièces seraient en dehors du plateau !")
    elif (colonne + 1) > l_c or (colonne) < 0:
        choix = False
        c.itemconfigure(instruction, text = "Votre choix n'est pas valide, les pièces seraient en dehors du plateau !")
    elif grille_de_jeu[ligne][colonne] != '-' and nb_pieces_restantes > nb_pieces_jouees:
        choix = False
        c.itemconfigure(instruction, text = "Votre choix n'est pas valide, les pièces se chevauchent !")
    else:
        choix = True

    return choix

def verification(pieces_jouees, orientation, ligne, colonne):
    choix_orientation = verification_orientation(orientation)
    choix_nb_pieces = verification_nb_pieces(pieces_jouees)
    choix_plateau = verification_plateau(ligne, colonne)

    if choix_nb_pieces and choix_orientation and choix_plateau:
        choix = True    
    else:
        choix = False

    return choix

def clic(event):
    global nb_joueur
    global nb_pieces_restantes
    global numero_tour
    global nb_pieces_jouees
    global espace_vide
    global l_c
    global orientation_pieces
    global ligne
    global colonne
    global tour_valide
    global grille_de_jeu
    global numero_joueur
    global joueur
    global axe_X
    global axe_Y
    global liste_image_piece

    X = event.x
    Y = event.y
    lettre = event.char
    #print("Position clic X : ", X, ", Position clic Y : ", Y)

    #Interrvalle dans laquelle le joueur peut cliquer sur le plateau
    intervalle_X_plateau = list(range(l_offset, l_offset+632))
    intervalle_Y_plateau = list(range(h_offset, h_offset+632))

    #Intervalle dans laquelle le joueur choisi le nombre de pieces qu'il veut placer
    intervalle_X_chiffre = list(range(padG-55//2, padD+55//2))
    intervalle_Y_chiffre = list(range(padH2-55//2, padH2+55//2))

    #Intervalle dans laquelle le joueur choisi l'orientation des pieces qu'il veut placer
    intervalle_X_orientation = list(range(padG-55//2, padD+55//2))
    intervalle_Y_orientation = list(range(padH-55//2, padB+55//2))

    #Intervalle dans laquelle le joueur valide son tour
    intervalle_X_validation = list(range(padG-55//2, padD+55//2))
    intervalle_Y_validation = list(range(padB2-55//2, padB2+55//2))

    #Intervalle dans laquelle le joueur quitte la partie
    intervalle_X_quitter = list(range((140-116)//2, (140+116)//2))
    intervalle_Y_quitter = list(range(h_jeu-(50+35)//2, h_jeu-(50-35)//2))

    if X in intervalle_X_plateau and Y in intervalle_Y_plateau and numero_tour == 1:
        (ligne, colonne) = localisation_grille(X, Y)
        #print("Ligne : ", ligne, ", Colonne : ", colonne)
        c.itemconfigure(instruction, text = "Sélectionnez le nombre ou l'orientation des pièces")

    if X in intervalle_X_chiffre and Y in intervalle_Y_chiffre:
        nb_pieces_jouees = choix_nb_pieces(X, Y)
        #print("Nombre jouée : ", nb_pieces_jouees)

    if X in intervalle_X_orientation and Y in intervalle_Y_orientation:
        (orientation_pieces, axe_X, axe_Y) = choix_orientation_pieces(X, Y)
        #print("Orientation X : ", axe_X, ", Orientation Y : ", axe_Y)
    
    if X in intervalle_X_validation and Y in intervalle_Y_validation:
        ligne_suiv = ligne + nb_pieces_jouees * axe_Y
        colonne_suiv = colonne + nb_pieces_jouees * axe_X
        #print("Prochaine ligne : ", ligne_suiv,", Prochaine colonne : ",  colonne_suiv)
        tour_valide = verification(nb_pieces_jouees, orientation_pieces, ligne_suiv, colonne_suiv)
        
    if X in intervalle_X_quitter and Y in intervalle_Y_quitter:
        win.destroy()

    if lettre == "q":
        win.destroy()


    #print(nb_pieces_jouees, orientation_pieces, tour_valide)

    #Si le choix du nombre et de l'orientation des pieces par rapport au plateau est valide, alors on met à jour les textes et la fenêtre
    if tour_valide:
        numero_tour += 1
        nb_pieces_restantes -= nb_pieces_jouees
        espace_vide -= 1
        (numero_joueur, joueur) = joueur_actuel(numero_tour, nb_joueur)


        liste_image_piece.append(import_image("Piece_" + str(nb_pieces_jouees) + orientation_pieces + ".png"))
        mise_a_jour_grille()

        grille_de_jeu [ligne][colonne] = str(nb_pieces_jouees*orientation_pieces)
        print("Tour : ", numero_tour-1)
        for i in range(2*nb_joueur):
            print(grille_de_jeu[i])

        c.itemconfigure(tour_joueur, text = "Tour de " + str(joueur))
        c.itemconfigure(instruction, text = "Sélectionnez le nombre ou l'orientation des pièces")
        c.itemconfigure(piece_restante, text = str(nb_pieces_restantes))

        nb_pieces_jouees = 0 #Nombre de pieces jouees
        orientation_pieces = "NON-DETERMINEE" #Orientation de la piece jouees
        tour_valide = False #Tour du joeur valide
        ligne = ligne_suiv
        colonne = colonne_suiv


    win.update()

def mise_a_jour_grille():
    global nb_pieces_jouees
    global orientation_pieces
    global ligne
    global colonne
    global numero_tour
    global liste_piece
    global liste_image_piece
    global l_offset
    global h_offset
    global l_c
 
    pos_X = l_offset + int((632//l_c)*(colonne+1/2))
    pos_Y = h_offset + int((632//l_c)*(ligne+1/2))

    #print("Position piece X : ", pos_X, ", Position piece Y : ", pos_Y)
    #print(liste_image_piece[numero_tour-2])

    image = creation_objet(c, "image", liste_image_piece[numero_tour-2], pos_X, pos_Y)
    liste_piece.append(image)


def quit(event):
    global fond_gagnant
    global message

    X = event.x
    Y = event.y
    letter = event.char

    #Intervalle dans laquelle le joueur quitte la partie
    intervalle_X_quitter = list(range((140-116)//2, (140+116)//2))
    intervalle_Y_quitter = list(range(h_jeu-(50+35)//2, h_jeu-(50-35)//2))

    intervalle_X_validation = list(range(padG-55//2, padD+55//2))
    intervalle_Y_validation = list(range(padB2-55//2, padB2+55//2))
    
    if X in intervalle_X_validation and Y in intervalle_Y_validation:
        c.event_delete("<<Quitter>>", "<Button-1>", "<KeyRelease-q>")
        c.itemconfigure(fond_gagnant, state = "hidden")
        c.itemconfigure(message, state = "hidden")
        partie_en_cours()

    if X in intervalle_X_quitter and Y in intervalle_Y_quitter:
        win.destroy()

    if letter == "q":
        win.destroy()


#Temporaire : aide dans le code pour directement acceder a la fin de la partie
def fin(event):
    global nb_pieces_restantes
    nb_pieces_restantes = 0
    c.focus_force()


def joueur_actuel(tour, total_joueur):
    global nom

    joueur_actu = numero_tour % total_joueur
    if joueur_actu == 0:
        joueur_actu = total_joueur

    nom_joueur = nom[joueur_actu-1]

    return joueur_actu, nom_joueur


def partie_en_cours():
    global matrice
    global l_c
    global grille_de_jeu
    global numero_tour
    global nb_joueur
    global joueur
    global nb_pieces_restantes
    global espace_vide

    print("")
    print("##################################################################")
    print("NOUVELLE PARTIE")
    print("")
    reinitialisation_variables()
    #Creation de la matrice qui va sauvegarder toutes informations du plateau
    grille_de_jeu = matrice(l_c)
    (numero_joueur, joueur) = joueur_actuel(numero_tour, nb_joueur)

    c.itemconfigure(tour_joueur, text = "Tour de " + str(joueur))
    c.itemconfigure(instruction, text = "Cliquez sur une des cases du plateau afin de placer vos pièces")
    c.itemconfigure(validation, text = "Valider")
    c.itemconfigure(piece_restante, text = str(nb_pieces_restantes))

    win.event_add("<<Fin_partie>>", "<KeyRelease-f>")
    c.event_add("<<choix_pieces>>", "<Button-1>", "<KeyRelease-q>")
    c.focus_force()

    while nb_pieces_restantes > 0 and espace_vide > 1:
        c.bind("<<choix_pieces>>", clic)
        win.bind("<<Fin_partie>>", fin)
        win.update()

    c.event_delete("<<choix_pieces>>")
    fin_partie()

def fin_partie():
    global l_jeu
    global numero_tour
    global nb_joueur
    global score
    global fond_gagnant
    global message
    global liste_piece
    global liste_image_piece

    c.event_add("<<Quitter>>", "<Button-1>", "<KeyRelease-q>")
    c.bind("<<Quitter>>", quit)

    c.itemconfigure(tour_joueur, text = "Fin de la partie")
    c.itemconfigure(instruction, text = "Cliquez sur le bouton de validation pour continuer à jouer ou sur quitter pour arrêter ")
    c.itemconfigure(validation, text = "Recommencer", font = ("Minecraft", 16))

    #print(liste_piece, liste_image_piece)
    del(liste_piece)
    del(liste_image_piece)


    numero_tour += 1
    (numero_gagnant, gagnant) = joueur_actuel(numero_tour, nb_joueur)
    score[numero_gagnant-1] += 1

    affichage_joueur(nb_joueur, nom, score)

    c.itemconfigure(fond_gagnant, state = "normal")
    c.itemconfigure(message, text = "Le gagnant de la partie est " + str(gagnant), state = "normal")
   

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
img_quitter = import_image("Fond_quitter.png")
###############################################################################
#Panneau de jeu central
#Placement des images
fond = creation_objet(c, "image", img_fond, l_jeu//2, h_jeu//2)
plateau = creation_objet(c, "image", img_plateau, l_jeu//2, h_jeu//2)
creation_plateau(c)

fond_gagnant = c.create_rectangle(280,720//4, l_jeu-280, 3*720//4, fill = "lightgrey", outline = "red3", width = 10, state = "hidden")

message = creation_objet(c, "texte", "Le gagnant de la partie est " + str(gagnant),
        l_jeu//2, h_jeu//2, 50, "red3")
c.itemconfigure(message, justify = "center", width = 700, state = "hidden")


###############################################################################

###############################################################################
#Panneau de jeu droite
#Affichage du joueur sur le tour actuel
joueur = joueur_actuel(1, nb_joueur)
tour_joueur = creation_objet(c, "texte", "Tour de " + str(joueur), (padG+padD)//2, 45, 24)

#Instruction au joueur pour le tour actuel
instruction = creation_objet(c, "texte", "Cliquez sur une des cases du plateau afin de placer vos pièces", (padG+padD)//2, 135)
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
validation = creation_objet(c, "texte", "Valider", (padD+padG)//2, padB2, 20, "#CEAF91")
c.itemconfigure(validation, justify = "center")

#Affichage du nombre de pièce restante
txt_piece_restante = creation_objet(c, "texte", "Nombre de pièces restantes :",
    (padG+padD)//2, 504 + 96)
c.itemconfigure(txt_piece_restante, justify = "center")

piece_restante = creation_objet(c, "texte", str(nb_pieces_restantes), 
    (padG+padD)//2, 504 + 76 + 90, 44)
###############################################################################

###############################################################################
#Panneau de jeu gauche
txt_score = []
for j in range(nb_joueur):
    texte = creation_objet(c, "texte", str(score[j]), 286//2, ((h_jeu*j)//nb_joueur)+150, 40)
    txt_score.append(texte)

affichage_joueur(nb_joueur, nom, score)

#Bouton quitter
fond_quitter = creation_objet(c, "image", img_quitter, 140//2, h_jeu-50//2)
quitter = creation_objet(c, "texte", "Quitter", 140//2, h_jeu-50//2, 14, "#CEAF91")
c.itemconfigure(validation, justify = "center")

###############################################################################

partie_en_cours()

win.mainloop()
