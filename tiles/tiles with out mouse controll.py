import pygame
import random
pygame.init()
scr=pygame.display.set_mode((400,500))
bg=pygame.image.load("tile_bg.png")
tile=pygame.image.load("tile.png")
tile_rect=tile.get_rect()
tile_rect.center=(50,50)
scr.blit(bg,(0,0))
pos=list(range(1,20))+[" "]
val=list(range(1,20))+[" "]
random.shuffle(val)
while True:
  if val==pos:
    break
  for eve in pygame.event.get():
    scr.blit(bg,(0,0))
    i=val.index(" ")
    if eve.type==pygame.QUIT:
      pygame.quit()
    if eve.type==pygame.KEYDOWN:
      if eve.key==pygame.K_LEFT:
        if i in (3,7,11,15,19) or i+1>=20:
          pass
        else:
          val[i+1],val[i]=" ",val[i+1]
      if eve.key==pygame.K_RIGHT:
        if i in (0,4,8,12,16):
          pass
        else:
          val[i]=val[i-1]
          val[i-1]=" "
      if eve.key==pygame.K_DOWN:
        if i in(0,1,2,3):
          pass
        else:
          val[i]=val[i-4]
          val[i-4]=" "
      if eve.key==pygame.K_UP:
        if i+4>=20:
          pass
        else:
          val[i+4],val[i]=" ",val[i+4]      
  for x in range(4):
    for y in range(5):
      font=pygame.font.Font('freesansbold.ttf',65)
      text=font.render(str(val[y*4+x]),True,(100,0,0))
      if val[y*4+x]!=" ":
        scr.blit(tile,(x*100,y*100))
      scr.blit(text,(x*100+25,y*100+25))
  pygame.display.update()
print("you won")
