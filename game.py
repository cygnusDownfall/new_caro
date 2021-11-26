import MAUSAC
import pygame,sys
from pygame.locals import *

pygame.init()

DAI=1000
RONG =800

locationlist=[]
data=[(255,255,255)*20]*10

player1= True

x=0
y=10
FPS = 60
fpsClock = pygame.time.Clock()


def save(color,x,y): 
    data[y][x]=color
    locationlist.append((x,y))

DISPLAYSURF= pygame.display.set_mode((DAI, RONG))
pygame.display.set_caption('New caro ')

# tô nền và vẽ bàn cờ- xong 
    DISPLAYSURF.fill(MAUSAC.WHITE)
    for i in range(21):
        pygame.draw.line(DISPLAYSURF,MAUSAC.BLACK,(i*50,0),(i*50,500),2)
    for j in range(11):
        pygame.draw.line(DISPLAYSURF,MAUSAC.BLACK,(0,j*50),(1000,j*50),2)


while True:
# vẽ khung tính điểm 

#bắt sự kiện
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_SPACE:
                if player1==True:
                    color=MAUSAC.RED
                    save(color,x,y)

                else :
                    color=MAUSAC.BLUE
                    save(color,x,y)
                player1 = not player1

#vẽ lại khi k thay đổi -xong 
        for bl in locationlist:
            pygame.draw.rect(DISPLAYSURF,data[bl[1]][bl[0]],bl[0]*50,bl[1]*50)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    

#cập nhật mỗi lần lặp
    pygame.display.update()
    fpsClock.tick(FPS)