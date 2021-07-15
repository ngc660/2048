import pygame
pygame.init()
back = pygame.image.load("Sprites/Background.png")
sc_start = pygame.Surface((100,50))
color1_sc_start = (100,120,120)
color2_sc_start = (120,140,140)
sc_start.fill(color1_sc_start)
sc_records = pygame.Surface((100,50))
color1_sc_records = (120,200,90)
color2_sc_records = (140,220,110)
sc_records.fill((color1_sc_records))
open_records = False
isStart = False
key_up = False
key_space = False
choice = 0

font = pygame.font.SysFont("arial",18)
def draw(surf,W,H):
    surf.blit(back,(0,0))
    surf.blit(sc_start,(W/2,H/2-40))
    surf.blit(sc_records,(W/2,H/2+40))

    text_start = font.render("Начать игру", 1, (0, 200, 0), color1_sc_start)
    text_records = font.render("Рекорды",1,(0,200,0),color1_sc_records)
    surf.blit(text_start,(W/2+10,H/2-20))
    surf.blit(text_records,(W/2+10,H/2+60))
    if choice == 1:
        text_start = font.render("Начать игру",1,(0,200,0),color2_sc_start)
        sc_start.fill(color2_sc_start)
        text_records = font.render("Рекорды", 1, (0, 200, 0), color1_sc_records)
        sc_records.fill(color1_sc_records)
    elif choice == 2:
        text_start = font.render("Начать игру", 1, (0, 200, 0), color1_sc_start)
        sc_start.fill(color1_sc_start)
        text_records = font.render("Рекорды", 1, (0, 200, 0), color2_sc_records)
        sc_records.fill(color2_sc_records)
    pass

def start():
    return True
def update():
    global key_up
    global choice
    global key_space
    global isStart
    if key_up:
        if choice == 0:
            choice = 1
        elif choice == 1:
            choice = 2
        elif choice == 2:
            choice = 1
        key_up = False
    elif key_space:
        if choice == 1:
            isStart = start()
        key_space = False
    pass
