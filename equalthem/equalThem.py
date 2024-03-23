import pygame
import random
pygame.init()
gameIcon=pygame.image.load('icon.bmp')
scr=pygame.display.set_mode((500,600))
pygame.display.set_caption("abhishek's Equal Them")
pygame.display.set_icon(gameIcon)
game=True
restart=False
start=pygame.image.load("bg.png")
previous_button=pygame.image.load("previous.bmp")
restart_button=pygame.image.load("restart.bmp")
next_button=pygame.image.load("next.bmp")
pygame.mixer.music.load("button2.mp3")
levels=["start",
        (7,1,2,2,2,3,2,3,2,2),
        (1,3,4,3,1,3,2,1,1,2),
        (8,1,-1,0,0,-1,0,0,1,0),
        (8,2,0,1,2,-3,-2,2,1,2),
        (7,4,3,3,3,1,2,5,3,5),
        (8,-4,-7,-7,-4,-9,-9,-3,-3,-4),
        (9,-6,-6,-5,-6,-9,-10,-5,-6,-8),        
        (2,0,0,0,0,0,0,0,0,0)]
sol=["start",
     'rruu lldu',
     'ddrr uudd lluu drdl',
     'ruul dudr d',
     'uurl drlr lrld lrru llur rd',
     'rurl lrdu rull durr duld ldrr u',
     'rulr llur rdlu rdlu rdlu rdl',
     'ulrd ulrd ullu rddr']

cur_pos=[(100,100),(200,100),(300,100),(100,200),(200,200),(300,200),(100,300),(200,300),(300,300)]
done=False
bg=pygame.image.load("bg.png")
def keys():
    global cursor,i,done,restart,j
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
        if eve.type==pygame.KEYDOWN:
            pygame.mixer.music.play()
            pygame.mixer.music.play()
            if eve.key==pygame.K_LEFT and cursor>0:
                cursor-=1
                level[cursor+1]+=1
            elif eve.key==pygame.K_RIGHT and cursor<8:
                cursor+=1
                level[cursor+1]+=1
            elif eve.key==pygame.K_UP and cursor>2:
                cursor-=3
                level[cursor+1]+=1
            elif eve.key==pygame.K_DOWN and cursor<6:
                cursor+=3
                level[cursor+1]+=1
            elif eve.key==pygame.K_n:
                j=1
                done=True
            elif eve.key==pygame.K_r:
                j=0
                restart=True
                done=True
            elif eve.key==pygame.K_p:
                j=-1
                restart=True
                done=True
            elif eve.key==pygame.K_e:
                get_level=int(input("Enter level:-"))
                j=get_level-i
                done=True
        if eve.type==pygame.MOUSEBUTTONDOWN:
            pos=eve.pos
            if pos[1]>500 and pos[1]<600:
                if pos[0]>0 and pos[0]<200:
                    j=-1
                    restart=True
                    done=True
                if pos[0]>200 and pos[0]<300:
                    j=0
                    restart=True
                    done=True
                if pos[0]>300 and pos[0]<500:
                    j=1
                    done=True
            print(eve.pos)
                

def graphics(x,y):
    scr.blit(bg,(0,0))
    for ele in range(9):
        font1=pygame.font.Font('freesansbold.ttf',100)
        font2=pygame.font.Font('freesansbold.ttf',50)
        text=font1.render(str(level[ele+1]),True,(a,b,c))
        scr.blit(text,cur_pos[ele])
        l=font1.render("LEVEL:- %a"%i,True,(125,0,125))
        name=font2.render("ABHISHEK's GAMES",True,(0,0,125))
        scr.blit(l,(0,0))
        scr.blit(name,(0,450))
    pygame.draw.rect(scr,(0,0,100),(x,y,100,100),5)
    scr.blit(previous_button,(0,500))
    scr.blit(restart_button,(200,500))
    scr.blit(next_button,(300,500))
    pygame.display.update()


def check_level_complete():
    global done,i,level
    flag=1
    for k in range(1,9):
        
        if level[k]!=level[k+1]:
            flag=0
    if flag==1:
        done=True
    return done,i



i=0
j=1
while i<len(levels):
    a=random.randrange(200)
    b=random.randrange(200)
    c=random.randrange(200)
    if done:
        done=False
    if restart:
        j=0
        done=True
        restart=False
    else:
        j=1    
    level=levels[i]
    if level!="start" and level!=['s', 't', 'a', 'r', 't']:
        level=list(level)
        cursor=level[0]-1
        while not done:
            keys()
            check_level_complete()
            graphics(cur_pos[cursor][0],cur_pos[cursor][1])
            
    i+=j
