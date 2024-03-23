import pygame
import random
pygame.init()
scr=pygame.display.set_mode((400,565))
bg=pygame.image.load("tile_bg.png")
tile=pygame.image.load("tile.png")
tile_won=pygame.image.load("tile_won.png")
#pygame.mixer.music.load('drag.mp3')
tile_rect=tile.get_rect()
tile_rect.center=(50,50)
scr.blit(bg,(0,0))
ideal=list(range(1,20))+[" "]
val=list(range(1,20))+[" "]
random.shuffle(val)
#val[-1],val[-2]=val[-2],val[-1]    #for checking purpose remove first '#'

def move_left():
    if i in (3,7,11,15,19) or i+1>=20:
        pass
    else:
        val[i+1],val[i]=" ",val[i+1]
def move_right():
    if i in (0,4,8,12,16):
        pass
    else:
        val[i]=val[i-1]
        val[i-1]=" "
def move_down():
    if i in(0,1,2,3):
        pass
    else:
        val[i]=val[i-4]
        val[i-4]=" "
def move_up():
    if i+4>=20:
        pass
    else:
        val[i+4],val[i]=" ",val[i+4]

def graphics():
    for x in range(4):
        for y in range(5):
          font=pygame.font.Font('freesansbold.ttf',65)
          text=font.render(str(val[y*4+x]),True,(100,0,0))
          time=int(pygame.time.get_ticks()/1000)
          time="time:-"+str(time//60)+":"+str(time%60)
          time=font.render(time,True,(0,100,0))
          if val[y*4+x]!=" ":
            scr.blit(tile,(x*100,y*100))
          scr.blit(text,(x*100+25,y*100+25))
          scr.blit(time,(0,500))
    pygame.display.update()
while True:
  scr.blit(bg,(0,0))
  if val==ideal:
    break
  for eve in pygame.event.get():
    i=val.index(" ")
    if eve.type==pygame.QUIT:
      pygame.quit()
    if eve.type==pygame.KEYDOWN:
        if eve.key==pygame.K_LEFT:
            move_left()
        if eve.key==pygame.K_RIGHT:
            move_right()
        if eve.key==pygame.K_DOWN:
            move_down()
        if eve.key==pygame.K_UP:
            move_up()
        
  if eve.type==pygame.MOUSEBUTTONDOWN:
      if eve.button==1:
        blank=[i%4,i//4]
        pos=(eve.pos[0]//100,eve.pos[1]//100)
        if pos[0]==blank[0]:
          #pygame.mixer.music.play(2)
          step=pos[1]-blank[1]
          if step>0:
              for y in range(step):
                  j=val.index(" ")
                  if j+4<20:
                      val[j],val[j+4]=val[j+4]," "
                      pygame.time.delay(100)
          if step<0:
              for y in range(-step):
                  j=val.index(" ")
                  if j not in (0,1,2,3):
                      val[j],val[j-4]=val[j-4]," "
                      pygame.time.delay(100)                
  #          move_y(step)
        if pos[1]==blank[1]:
          #pygame.mixer.music.play(2)
          step=pos[0]-blank[0]
          if step>0:
              for x in range(step):
                  j=val.index(" ")
                  if j not in (3,7,11,15,19) or i+1<20:
                      val[j],val[j+1]=val[j+1]," "
                      pygame.time.delay(100)
                  
          if step<0:
              for x in range(-step):
                  j=val.index(" ")
                  if j not in (0,4,8,12,16):
                      val[j],val[j-1]=val[j-1]," "
                      pygame.time.delay(100)
                  
  #          move_x()
  graphics()
  
font=pygame.font.Font('freesansbold.ttf',50)
time_taken=int(pygame.time.get_ticks()/1000)
time_taken=str(time_taken//60)+":"+str(time_taken%60)
time_taken=font.render(time_taken,True,(0,0,100))
scr.blit(tile_won,(0,0))
scr.blit(time_taken,(200,300))
pygame.display.update()
pygame.time.delay(10000)
