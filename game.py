import pyxel

class Jeu:
    """
    La classe du jeu
    """
    def __init__(self, width=256, height=512):
        self.w = width
        self.h = height
        self.vaisseau = Vaisseau(self)
        pyxel.init(self.w, self.h, title="Jeu d'arcade")
        # chargement des images
        pyxel.load("images.pyxres")
        pyxel.run(self.update, self.draw)

    # =====================================================
    # == UPDATE
    # =====================================================
    def update(self):
        """
        mise à jour des variables (30 fois par seconde)
        """
        self.vaisseau.update()

    # =====================================================
    # == DRAW
    # =====================================================
    def draw(self):
        """création et positionnement des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)
        self.vaisseau.draw()

class Vaisseau:
    """
    La classe du vaisseau
    """
    def __init__(self, jeu, width=16, height=16):
        self.jeu = jeu
        self.w = width
        self.h = height
        self.x = self.jeu.w//2
        self.y = self.jeu.h - self.h

    def draw(self):
        """
        Affiche le vaisseau
        """
        #pyxel.rect(self.x, self.y, self.w, self.h, 1)
        if pyxel.frame_count%10 < 5:
            pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 16, self.w, 16+self.h)


    def update(self):
        self.deplacement()

    def deplacement(self) :
        """
        déplacement avec les touches de directions
        """
        if pyxel.btn(pyxel.KEY_RIGHT) and (self.x < self.jeu.w-self.w) :
            self.x += 4
        if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
            self.x += -4
        if pyxel.btn(pyxel.KEY_DOWN) and self.y<self.jeu.h-self.w:
            self.y += 4
        if pyxel.btn(pyxel.KEY_UP) and self.y>0:
            self.y += -4


Jeu()