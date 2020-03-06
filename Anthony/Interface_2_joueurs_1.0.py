import tkinter as tk
  
#Variables
l_jeu = 1280
h_jeu = 720
res_jeu = str(l_jeu) + "x" + str(h_jeu)
nom_fenetre = "SYNAPSE 2 Joueurs"
nb_joueur = 2
nb_cases = (nb_joueur*2)**2
nb_pieces = int(nb_cases * 25 / 16)
numero_tour = 0
clic_valide = False
gagnant = 0

#Ces variables permettent de placer les images des flèches et chiffres
pad1 = 10
pad2 = 40
c_img = 55
padH = int(h_jeu*7/10-pad2+50-2*pad1-2.5*c_img)
padH2 = int(padH-3*pad2)
padB = int(h_jeu*7/10-pad2+50-0.5*c_img)
padD = int(l_jeu-pad2-0.5*c_img)
padG = int(l_jeu-2*pad2-2.5*c_img)

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
    l_offset = 286+36 #Largeur à partir du bord de la fenêtre
    h_offset = 42 #Hauteur à partir du bord de la fenêtre
    for i in range(1,l_c):
        #Création des lignes
        canvas.create_line(l_offset, h_offset+632-(632//l_c)*i,
                           l_offset+636, h_offset+632-(632//l_c)*i,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")
        #Création des colonnes
        canvas.create_line(l_offset+632-(632//l_c)*i, h_offset,
                           l_offset+632-(632//l_c)*i, h_offset+636,
                           width = 10-(nb_joueur-2)*2, fill = "#7A4330")

def clic(event):
    global padH
    global padH2
    global padB
    global padD
    global padG
    global nb_pieces
    global numero_tour
    global clic_valide

    X = event.x
    Y = event.y

    intervalle_X_C1 = list(range(padG-55//2, padG+55//2))
    intervalle_Y_C1 = list(range(padH2-55//2, padH2+55//2))
    intervalle_X_C2 = list(range((padD+padG-55)//2, (padD+padG+55)//2))
    intervalle_Y_C2 = list(range(padH2-55//2, padH2+55//2))
    intervalle_X_C3 = list(range(padD-55//2, padD+55//2))
    intervalle_Y_C3 = list(range(padH2-55//2, padH2+55//2))

    #if grille est cliquée
    #c.itemconfigure(instruction, text = "Sélectionnez le nombre de pièce que vous voulez placer")

    if X in intervalle_X_C1 and Y in intervalle_Y_C1:
        if nb_pieces >=1:
            numero_tour+=1
            nb_pieces -= 1
            clic_valide = True
        elif nb_pieces < 0 :
            clic_valide = False
              
    elif X in intervalle_X_C2 and Y in intervalle_Y_C2:
        if nb_pieces >= 2:
            numero_tour += 1
            nb_pieces -= 2
            clic_valide = True
        elif nb_pieces > 0 :
            c.itemconfigure(instruction, text = "Choisissez moins de pièces !")
            clic_valide = False
        
    elif X in intervalle_X_C3 and Y in intervalle_Y_C3:
        if nb_pieces >= 3:
            numero_tour += 1
            nb_pieces -= 3
            clic_valide = True
        elif nb_pieces > 0 :
            c.itemconfigure(instruction, text = "Choisissez moins de pièces !")
            clic_valide = False

    c.itemconfigure(piece_restante, text = str(nb_pieces))
    win.update()


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
fond = creation_objet(c, "image", img_fond, l_jeu//2, h_jeu//2)
plateau = creation_objet(c, "image", img_plateau, l_jeu//2, h_jeu//2)
creation_plateau(c)

###############################################################################
#Panneau de jeu gauche
#Instruction au joueur pour le tour actuel
instruction = creation_objet(c, "texte", "Cliquez sur une des cases du plateau afin de placer vos pièces", (padG+padD)//2, 80)
c.itemconfigure(instruction, justify = "center")

#Fond des chiffres
chiffre_1 = creation_objet(c, "image", img_chiffre, padG, padH2)
chiffre_2 = creation_objet(c, "image", img_chiffre, (padG+padD)/2, padH2)
chiffre_3 = creation_objet(c, "image", img_chiffre, padD, padH2)
#Chiffres
C1 = creation_objet(c, "texte", "1", padG, padH2, 22, "#CEAF91")
C2 = creation_objet(c, "texte", "2", (padG+padD)//2, padH2, 22, "#CEAF91")
C3 = creation_objet(c, "texte", "3", padD, padH2, 22, "#CEAF91")

#Flèches
FH = creation_objet(c, "image", img_FH, (padD+padG)//2, padH)
FB = creation_objet(c, "image", img_FB, (padD+padG)//2, padB)
FD = creation_objet(c, "image", img_FD, padD, (padH+padB)//2)
FG = creation_objet(c, "image", img_FG, padG, (padH+padB)//2)

#Affichage du nombre de pièce restante
txt_piece_restante = creation_objet(c, "texte", "Nombre de pièces restantes :",
    (padG+padD)//2, 504 + 76)
c.itemconfigure(txt_piece_restante, justify = "center")

piece_restante = creation_objet(c, "texte", str(nb_pieces), 
    (padG+padD)//2, 504 + 66 + 90, 44)
###############################################################################

while nb_pieces >= 0:
    if numero_tour%2 == 0 and numero_tour > 0 and clic_valide == True:
        c.itemconfigure(instruction, text = "Au tour du joueur 1")

    elif numero_tour > 0 and clic_valide == True:
        c.itemconfigure(instruction, text = "Au tour du joueur 2")

    if nb_pieces <= 0:
        #print("PLUS DE PIECE")
        gagnant = 1-numero_tour%2
        break
    else:
        win.update()
        c.bind("<Button-1>", clic)

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
