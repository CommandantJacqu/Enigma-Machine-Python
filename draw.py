# Créé par Eleve, le 16/11/2024 en Python 3.7
import pygame

def draw(enigma, path, screen, width, height, margins, gap, font):

    # width and height components
    w = (width - margins["left"] - margins["right"] - 5*gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # path coordinates.
    y = [margins["top"]+(signal+1)*h/27  for signal in path]
    x = [width-margins["right"]-w/2] # keyboard.
    for i in [4,3,2,1,0]: # forward pass.
        x.append(margins["left"]+i*(w+gap)+w*3/4)
        x.append(margins["left"]+i*(w+gap)+w*1/4)
    x.append(margins["left"]+w*3/4) # reflect.

    for i in [1,2,3,4]: # backward pass.
        x.append(margins["left"]+i*(w+gap)+w*1/4)
        x.append(margins["left"]+i*(w+gap)+w*3/4)
    x.append(width-margins["right"]-w/2) # lampboard.

    # draw the path.
    if len(path) > 0:
        for i in range(1,21):
            if i < 10:
                color = "green"
            elif i < 12:
                color = "orange"
            else:
                color = "red"
            start = (x[i-1],y[i-1])
            end = (x[i],y[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # base coordinate.
    x = margins["left"]
    y = margins["top"]

    # draw enigma components.
    for component in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:


        component.draw(screen, x, y, w, h, font)

        x += w + gap





