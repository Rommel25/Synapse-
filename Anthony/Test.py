import tkinter, time

def temps():
  global tps0
  heure=time.strftime("%Y.%m.%d - %H:%M:%S")
  texte0.config(text=heure)
  tps0=racine0.after(2000, temps)

def stop():
  global tps0
  racine0.after_cancel(tps0)

racine0=tkinter.Tk()

texte0=tkinter.Label(racine0, text="")
texte0.pack()

bouton0=tkinter.Button(racine0, text="Stop", command=stop)
bouton0.pack()
temps()

racine0.mainloop()