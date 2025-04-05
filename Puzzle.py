#Cargar imagen y dividirla en un puzzle de 3x3 o 4x4

import pygame #Interfar de el puzzle
import random #Para barajar el puzzle

class Puzzle:
    def cargar_imagen(self, imagen, filas: int, columnas: int):
        ancho = imagen.get.width() // filas  #Width(): utilizamos para obtener el ancho, //: division entera
        alto = imagen.get.height() // columnas #Height(): utilizamos para obtener el alto
        piezas = [] #Guardamos las piezas del puzzle

        for fil in range(filas):
            for col in range(columnas):
                rect = pygame.Rect(fil * ancho, col * alto, ) #Pygame.rect: generar un rectangle en la interfaz
                pieza = imagen.subsurface() #Subsurface: para crear el recorte



from PIL import Image
from fpdf import FPDF


