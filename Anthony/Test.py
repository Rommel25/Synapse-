import tkinter

def touche(evt0):
  texte0.config(text=evt0.char)

racine0=tkinter.Tk()

texte0=tkinter.Label(racine0, text="...", font="Arial 64", width=3)
texte0.pack()
racine0.bind("<KeyRelease>", touche)

racine0.mainloop()