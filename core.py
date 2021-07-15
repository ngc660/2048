import pygame
import squares
import random
pygame.init()
DISP_W = 600
DISP_H = 600
GFW = 400   #Game Field Widht
GFH = 400   # Height
Ceil_W = GFW/4 - 20
Ceil_H = GFH/4 - 20
activiti = True
disp = pygame.display.set_mode((DISP_W,DISP_H))
pygame.display.set_caption("2048")
frame = 50

squares.Square.height = Ceil_H
squares.Square.wight = Ceil_W

#colors
color_back = (70,60,190)
color_field_info = (130,160,130,30)
color_field = (0,0,0)
color_line = (130,130,130,20)
color_game_field = (90,90,90)
color_empty_ceil = (145,145,145)

grid = list()
for i in range(0,4):
    row = list()
    for j in range(0,4):
        row.append(0)
    grid.append(row)

game_field = pygame.Surface((GFW,GFH))
game_field.fill(color_game_field)

up = False
down = False
right = False
left = False

gen_ceils = 2
def gen_grid(): # функция добавляющая элемент в начале игры и в за каждый ход
    global gen_ceils
    stop = False
    while gen_ceils > 0 and not(stop):
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if gen_ceils == 0:
                    stop = True
                    break
                if grid[i][j] == 0:
                    rand = random.randint(1,20)
                    if rand == 2:
                        # print(True)
                        grid[i][j] = 2
                        gen_ceils -= 1
                        print(gen_ceils)
                    elif rand == 7:
                        # print(False)
                        grid[i][j] = 4
                        gen_ceils -= 1

    pass
def show_grid(): #функция для отображения работы матрицы
    print("new gen")
    for i in grid:

        print(i)
    pass

end_score=0
END = False

@staticmethod
def gameOver(matrix): #функция отвечающая за окончание игры
        testmatrix = matrix.copy()
        a,b = testmatrix.shape
        for i in range(a):
            for j in range(b-1):
                if testmatrix[i][j] == testmatrix[i][j+1]:                    # Если в каждой строке два соседних номера, игра не окончена
                    print("Игра не окончена")
                    return False
        for i in range(b):
            for j in range(a-1):
                if testmatrix[j][i] == testmatrix[j+1][i]:
                    print("Игра не окончена")
                    return False
        print("игра закончена")
        return True
 
    pass

  def combineList(self,rowlist): #Функция текущего счета
        start_num = 0
        end_num = Size-rowlist.count(0)-1
        while start_num < end_num:
            if rowlist[start_num] == rowlist[start_num+1]:
                rowlist[start_num] *= 2
                self.score += int(rowlist[start_num])                      # Возвращать накопленный счет каждый раз
                rowlist[start_num+1:] = rowlist[start_num+2:]
                rowlist.append(0)
            start_num += 1
        return rowlist

    def removeZero(self,rowlist): #Функция обнуления счета
        while True:
            mid = rowlist[:]                      
            try:
                rowlist.remove(0)
                rowlist.append(0)
            except:
                pass
            if rowlist == mid:
                break;
        return self.combineList(rowlist)

def drawing():
    disp.fill(color_back)
    pygame.draw.rect(disp, color_field_info, (5,5,DISP_W-10,DISP_H/4), 0, 3)
    pygame.draw.line(disp, color_line, (0,DISP_H/4+2+5), (DISP_W,DISP_H/4+2+5))
    disp.blit(game_field,((DISP_W-GFW)/2, DISP_H/4+2+25))
    for r in range(0,len(grid)):
        for c in range(0,len(grid[r])):
            pygame.draw.rect(game_field,color_empty_ceil, (25+10*c + Ceil_W*c, 25+10*r + Ceil_H*r, Ceil_W, Ceil_H), 0,3)

            pass
    for k in range(0, len(grid)):
        for c in range(0,len(grid[k])):

            pass
def updating():
    global down
    global up
    global left
    global right
    global gen_ceils
    global end_score
    if down:
        # end_score = 0
        # print("условие сработало")
        up = False
        down = False
        for r in range(len(grid)-1,0,-1):
            for c in range(0, len(grid[r])):
                if grid[r-1][c] != 0 and r != len(grid):
                    if grid[r][c] == 0:
                        grid[r][c] = grid[r-1][c]
                        grid[r-1][c] = 0
                    elif grid[r][c] == grid[r-1][c]:
                        grid[r][c] += grid[r-1][c]
                        grid[r-1][c] = 0
                        pass
                    pass
        gen_ceils += 1
        gen_grid()
        show_grid()
        # print(end_score)
    if up:
        up = False
        down = False
        for r in range(1,len(grid)):
            for c in range(0,len(grid[r])):
                if grid[r][c] != 0:
                    if grid[r-1][c] == 0:
                        grid[r-1][c] = grid[r][c]
                        grid[r][c] = 0
                    elif grid[r-1][c] == grid[r][c]:
                        grid[r-1][c] += grid[r][c]
                        grid[r][c] = 0
        gen_ceils += 1
        gen_grid()
        show_grid()
    if left:
        left = False
        for r in range(0,len(grid)):
            for c in range(1,len(grid[r])):
                if grid[r][c] != 0:
                    if grid[r][c-1] == 0:
                        grid[r][c-1] = grid[r][c]
                        grid[r][c] = 0
                    elif grid[r][c-1] == grid[r][c]:
                        grid[r][c-1] += grid[r][c]
                        grid[r][c] = 0

        gen_ceils += 1
        gen_grid()
        show_grid()
    if right:
        for r in range(0,len(grid)):
            for c in range(len(grid[r])-1,0,-1):
                if grid[r][c-1] != 0:
                    if grid[r][c] == 0:
                        grid[r][c] = grid[r][c-1]
                        grid[r][c-1] = 0
                    elif grid[r][c] == grid[r][c-1]:
                        grid[r][c] += grid[r][c-1]
                        grid[r][c-1] = 0
                        pass
                pass
        gen_ceils += 1
        gen_grid()
        show_grid()
        right = False
    pass
show_grid()
gen_grid()
show_grid()
# print("gen ceils before",gen_ceils)
while activiti:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            activiti = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_UP:
                up = True
            elif ev.key == pygame.K_DOWN:
                down = True
            elif ev.key == pygame.K_RIGHT:
                right = True
            elif ev.key == pygame.K_LEFT:
                left = True

    updating()
    drawing()
    pygame.display.flip()
    pygame.time.delay(frame)
    pass
pygame.quit()
