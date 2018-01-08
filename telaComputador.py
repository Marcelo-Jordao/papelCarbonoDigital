#   python = 3.6
#   criador marcelo ramos jordao

from tkinter import *


class Pintura:
    # ********************** variaveis *********************** #

    # estado do cursor
    estadoCursor = "up"

    # posicao X e Y do pincel
    posX, posY = None, None

    def left_but_down(self, event=None):
        self.estadoCursor = "down"

    # ************ captura de estado do cursor *************** #

    def left_but_up(self, event=None):
        self.estadoCursor = "up"

        # reseta a
        self.posX = None
        self.posY = None

    # ************* execucao do pincel na tela **************** #

    def motion(self, event=None):

        self.pencil_draw(event)

    # ******************** controle do pincel ***************** #

    def pencil_draw(self, event=None):
        if self.estadoCursor == "down":

            # verificar se posX e posY tem valor numerico
            if self.posX is not None and self.posY is not None:
                event.widget.create_line(self.posX, self.posY, event.x, event.y, smooth=TRUE)

            self.posX = event.x
            self.posY = event.y

    # ****************** execucao da tela ********************* #

    def __init__(self, tela):
        drawing_area = Canvas(tela)
        drawing_area.pack()
        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


tela = Tk()

pintura = Pintura(tela)

tela.mainloop()
