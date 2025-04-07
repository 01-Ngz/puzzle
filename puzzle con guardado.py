import random
import pygame



class puzzle:
    def __init__(self, imagen, filas: int, columnas : int):
        self.filas : int = filas
        self.columnas: int = columnas
    def cargar_imagen(self, imagen, filas: int, columnas : int):

        ancho = imagen.get_width() // filas
        alto = imagen.get_height() // columnas
        piezas = []

        for fil in range(filas):
            for col in range (columnas):
                x = col * ancho
                y= fil * alto
                rect = pygame.rect(x,y, ancho, alto)
                pieza = imagen.subsurface(). copy()
                piezas.append(pieza)
            return piezas
    def mover_teclado(columnas: int):
        pygame.init()
        pantalla = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Mover con teclado")
        reloj = pygame.time.Clock()
        ejecutando = True

        while ejecutando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                        mover("up")
                    elif evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                        mover("down")
                    elif evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                        mover("left")
                    elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                        mover("right")

            # Aquí podrías dibujar el tablero actualizado con las piezas
            pantalla.fill((30, 30, 30))  # Color de fondo
            # Ejemplo de renderizado básico
            font = pygame.font.Font(None, 36)
            for i, pieza in enumerate(piezas):
                x = (i % columnas) * 100
                y = (i // columnas) * 100
                if pieza != 0:  # 0 representa vacío
                    texto = font.render(str(pieza), True, (255, 255, 255))
                    pantalla.blit(texto, (x + 30, y + 30))

            pygame.display.flip()
            reloj.tick(30)

        pygame.quit()
        sys.exit()


from PIL import Image
from fpdf import FPDF
from docx import Document

class Tipos_de_imagenes:
    def __init__(self, JPG: bool, PNG: bool, PDF: bool, WORD: bool):
        self.JPG: bool = JPG
        self.PNG: bool = PNG
        self.PDF: bool = PDF
        self.WORD: bool = WORD

    def guardar_imagen(self, JPG, PNG, PDF, WORD, imagen=None):
        imagen.convert("RBG").save("Puzzle_done.jpg")
        imagen.save("Puzzle_done.png")


        pdf = FPDF()
        pdf.add_page()
        pdf.image(JPG, 10, 10, 210, 297)
        pdf.output("Puzzle_done .pdf")

        doc = Document ()
        doc.add_heading('Puzzle_done', 0)
        doc.add_picture(width=Inches(5))
        doc.save("Imagen_puzzle")