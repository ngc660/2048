import pygame

pygame.init()
DISP_W = 800
DISP_H = 600
activiti = True
disp = pygame.display.set_mode((800,600))
pygame.display.set_caption("2048")
frame = 50

def drawing():
    disp.fill((0,60,190))
    pass
def updating():
    pass
while activiti:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            activiti = False
    updating()
    drawing()
    pygame.display.flip()
    pygame.time.delay(frame)
    pass
pygame.quit()