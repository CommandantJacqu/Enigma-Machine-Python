# Créé par Eleve, le 15/11/2024 en Python 3.7
"""
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A => X
"""
import pygame

from Keyboard import Keyboard
from Plug import Plugboard
from Rotor import Rotor
from Reflect import Reflect
from Enigma_clas import Enigma
from draw import draw

# setup pygame.
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulator")

# create font.
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# globals variables.
WIDTH = 1310
HEIGHT = 645
screen = pygame.display.set_mode((WIDTH,HEIGHT))
MARGINS = {"top":90, "bottom":50, "left":100, "right":100}
GAP = 100
INPUT = ""
OUTPUT = ""
PATH = []


# historical enigma rotors and reflect.
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflect("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflect("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflect("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard.
KB = Keyboard()
PB = Plugboard(["AB", "CD", "EF"])

# define enigma machine.
ENIGMA = Enigma(B,I,II,III,PB,KB)

# set the rings.
ENIGMA.set_rings((1,1,1))

# set message key
ENIGMA.set_key("BBC")

running  = True

while running:

    # backround.
    screen.fill("#333333")

    # text input.
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/2))
    screen.blit(text, text_box)

        # text output.
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2,MARGINS["top"]/2+35))
    screen.blit(text, text_box)

    # draw enigma machine.
    draw(ENIGMA, PATH, screen, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen.
    pygame.display.flip()

    # track user input.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                III.rotate()
            elif event.key == pygame.K_2:
                II.rotate()
            elif event.key == pygame.K_1:
                I.rotate()
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    print(PATH)
                    OUTPUT = OUTPUT + cipher
            if event.key == pygame.K_LEFT:
                INPUT = ""
                OUTPUT = ""
            if event.key == pygame.K_SPACE:
                INPUT = INPUT + " "