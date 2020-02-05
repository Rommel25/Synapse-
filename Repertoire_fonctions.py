def placement(objet, ligne, colonne, fusion_ligne = 1, fusion_colonne = 1):
    espace = 7
    objet.grid(row = ligne, column = colonne,
                rowspan = fusion_ligne, columnspan = fusion_colonne,
                padx = espace, pady = espace)
