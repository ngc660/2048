import pygame.draw
class Square():
    wight = 0
    height = 0
    character = {
        2 : [60,10,10],
        4 : [1,1,1],
        8 : [2,2,2],
        16 : [3,3,3],
        32 : [4,4,4],
        64 : [5,5,5],
        128: [6,6,6],
        256 : [7,7,7],
        512 : [8,8,8],
        1024 : [9,9,9],
        2048 : [10,10,10]
    }
    # font = pygame.font.SysFont("arial",12)
    moving_value = 5
    value = 0
    def __init__(self):
        self.pos_row = -1
        self.pos_column = -1
        self.pos_x = 10
        self.pos_y = 10

        pass
    def __del__(self):
        pass
    def drawing(self,surf,x,y,v):
        w = Square.wight
        h = Square.height
        v = Square.value
        if v > 0:
            pygame.draw.rect(surf,Square.character[v],(x,y,w,h))
            # text = Square.font.render(surf,str(v),(200,200,200))
            # text.blit(surf,x,y)
        # print(Square.character.get(2))
        pass
    def updating(self):

        pass
    pass