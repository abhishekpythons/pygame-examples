levels=open("levels.txt")
class level:
    i=eval(levels.readline())
    def __init__(self,levelNo,cursor=i[0],level=list(i[1]),images={}):
        self.levelNo=levelNo
        self.cursor=cursor
        self.level=level
        self.images=images
        self.nextLevel=False
        
    def load(self,imageList):
        self.images={}
        for i in imageList:
            self.images[i.split(".")[0]]=pygame.image.load(i)
        return self.images
    
    def graphics(self):
        curPos=[(100,100),(200,100),(300,100),(100,200),(200,200),(300,200),(100,300),(200,300),(300,300)]
        scr.blit(self.images['bg'],(0,0))
        for i in range(9):
            font1=pygame.font.Font('freesansbold.ttf',100)
            font2=pygame.font.Font('freesansbold.ttf',50)
            text=font1.render(str(self.level[i]),1,(125,0,125))
            scr.blit(text,curPos[i])
            l=font1.render("LEVEL:- %a"%self.levelNo,1,(125,0,125))
            name=font2.render("ABHISHEK's GAMES",1,(0,0,125))
            scr.blit(l,(0,0))
            scr.blit(name,(0,450))
            pygame.draw.rect(scr,(0,0,255),curPos[self.cursor.cur]+(100,100),5)
            
    def isLevelCompleted(self):
        flag=1
        for i in range(8):
            if self.level[i]!=self.level[i+1]:
                flag=0
                break
        if flag==1:
            self.levelNo+=1
            globals()['i']='2'
        
class cursor:
    def __init__(self,cur,parent):
        self.cur=cur
        self.parent=parent

    def move(self):
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
            if eve.type==pygame.KEYDOWN:
                if eve.key==pygame.K_LEFT and self.cur>0:
                    self.cur-=1
                    self.parent.level[self.cur]+=1
                elif eve.key==pygame.K_RIGHT and self.cur<8:
                    self.cur+=1
                    self.parent.level[self.cur]+=1
                elif eve.key==pygame.K_UP and self.cur>2:
                    self.cur-=3
                    self.parent.level[self.cur]+=1
                elif eve.key==pygame.K_DOWN and self.cur<6:
                    self.cur+=3
                    self.parent.level[self.cur]+=1
                levelHolder.graphics()
                pygame.display.update()
        return self.cur

               

if __name__=="__main__":
    import pygame,random
    pygame.init()
    game=True
    scr=pygame.display.set_mode((500,600))
    levels=open("levels.txt")
    i=1
    cursorHolder=cursor(6,None)
    levelHolder=level(i,cursorHolder)
    levelHolder.load(["bg.png",])
    cursorHolder.parent=levelHolder
    while game:
        levelHolder.cursor.move()
        if levelHolder.isLevelCompleted():
            cursorHolder=cursor(6,None)
            levelHolder=level(i,cursorHolder)
            levelHolder.load(["bg.png",])
            cursorHolder.parent=levelHolder
            i+=1
            levelHolder.nextLevel=False
