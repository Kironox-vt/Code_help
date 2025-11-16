import pygame

class MouvementsDeBase:
    # Soit la variable position une liste [x, y] où x, la position horizontale et y, la position verticale.
    def __init__(self, vitesse=5):
        self.vitesse = vitesse

    def deplacer_haut(self, position):
        position[1] = position[1] - self.vitesse
        return position
    
    def deplacer_bas(self, position):
        position[1] = position[1] + self.vitesse
        return position
    
    def deplacer_gauche(self, position):
        position[0] = position[0] - self.vitesse
        return position

    def deplacer_droite(self, position):
        position[0] = position[0] + self.vitesse
        return position

    