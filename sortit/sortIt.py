class tube:
    def __init__(self,conf,tubeNo):
        self.conf=[ball(self,conf[i],i) for i in range(len(conf))]
        self.str_no=tubeNo+1
        self.x=tubeSepX*tubeNo+tubeSepX//2 if tubeNo<=max(4,len(conf)//2) else tubeSepX*(tubeNo-4.5)+tubeSepX//2
        self.y=100 if tubeNo<=4 else 300
        self.thickness=2
    def  isMatched(self):
        comp=False
        if len(self.conf)==capacity:
            comp=True
            for i in range(capacity-1):
                if self.conf[i].color!=self.conf[i+1].color:
                    comp=False
        return comp
    def select(self):
        pygame.draw.polygon(scr,(0,0,255),((self.x+10,self.y-2*ballsize),(self.x,self.y),(self.x+20,self.y)))
    def click(self,From):
        if not self.isMatched():
            pygame.draw.polygon(scr,(0,255,0),((self.x+10,self.y),(self.x,self.y-2*ballsize),(self.x+2*ballsize,self.y-2*ballsize)))
            pygame.draw.line(scr,(0,255,0),(From.x+10,From.y-25),(self.x+10,self.y-25))
            pygame.draw.line(scr,(0,255,0),(From.x+10,From.y-25),(From.x+10,From.y-10))
            pygame.draw.polygon(scr,(0,0,255),((From.x+10,From.y-2*ballsize),(From.x+3,From.y-3),(From.x+17,From.y-3)))
            pygame.draw.line(scr,(0,255,0),(self.x+10,self.y),(self.x+10,self.y-25))
    def draw(self):
        pygame.draw.rect(scr,(255,255,255),(self.x-self.thickness,self.y-self.thickness,2*ballsize+2*self.thickness,2*ballsize*capacity+2*self.thickness),self.thickness)
        pygame.draw.rect(scr,(255,255,255),(self.x-3*self.thickness,self.y-5*self.thickness,2*ballsize+6*self.thickness,4*self.thickness),self.thickness)
        pygame.draw.circle(scr,(255,255,255),(int(self.x-2*self.thickness-self.thickness//2),int(self.y-3*self.thickness)),2*self.thickness)
        pygame.draw.circle(scr,(255,255,255),(int(self.x+2*ballsize+3*self.thickness),int(self.y-3*self.thickness)),2*self.thickness)
        pygame.draw.rect(scr,bgColor,(self.x,self.y-4*self.thickness,2*ballsize+self.thickness//2,2*ballsize*capacity+4*self.thickness+self.thickness//2))
        pygame.draw.rect(scr,bgColor,(self.x-2*self.thickness,self.y-4*self.thickness,2*ballsize+4*self.thickness+self.thickness//2,2*self.thickness+self.thickness//2))
        str_no=indFont.render(str(self.str_no),1,(255,255,255))
        scr.blit(str_no,(self.x+ballsize-str_no.get_size()[0]//2,self.y+2*ballsize*capacity+5))
        if self.isMatched():
            pygame.draw.polygon(scr,(200,200,0),((self.x-5,self.y-20),(self.x+2*ballsize+5,self.y-20),(self.x+2*ballsize-5,self.y),(self.x+5,self.y)))
        [self.conf[i].draw() for i in range(len(self.conf))]
    def pour(From,To):
        if  len(From.conf)>0 and len(To.conf)<capacity and (len(To.conf)==0 or From.conf[-1].color==To.conf[-1].color):
            To.conf+=[From.conf.pop(-1),]
            To.conf[-1].parent=To
            To.conf[-1].stackNo=len(To.conf)-1
            return True
        else:
            return False

class ball:
    def __init__(self,parent,color,stackNo):
        self.parent=parent
        self.color=color
        self.size=ballsize
        self.stackNo=stackNo
    def draw(self):
        pygame.draw.circle(scr,self.color,(int(self.parent.x+self.size),int(self.parent.y+(capacity-self.stackNo)*2*self.size-self.size)),self.size)
        

class level:
    def __init__(self,tubeList):
        self.tubeList=tubeList
    def start(self):
        self.tubes=[tube(self.tubeList[i],i) for i in range(len(self.tubeList))]
    def ifCompleted(self):
        completed=True
        for i in self.tubes:
            if len(i.conf)!=0:
                if not i.isMatched():
                    completed=False
        return completed
    def set(index):
        temp=[]
        for i in range(len(levels[index])):
            temp.append([colors[j] for j in levels[index][i]])
        return level(temp)
        
    def next():
        currLevel=level(levels[index+1])

class button:
    def refresh():
        currLevel=level.set(index)
        currLevel.start()
        
        
if __name__=='__main__':
    import pygame,random
    pygame.init()
    capacity=4
    index=0
    ballsize=10
    tubeSepX=100
    game=True
    selected=clicked=None
    levels=open('levels.txt')
    levels=levels.readlines()
    levels=[eval(i) for i in levels]
    levels=levels[:levels.index('')]
    goodWords=['Brilliant','Excellent','Stunning','Well Done','Out Standing','Too Fast','Masterly','Bravo','Wow','Nice','Good Job','Perfcet']
    scr=pygame.display.set_mode((525,500))
    colors={'r':(247,0,0),'b':(0,121,255),'y':(255,242,0),
            'g':(0,195,40),'m':(170,2,137),'o':(255,135,0),
            'c':(0,240,255),'ol':(65,115,0),'te':(2,142,144)}
    currLevel=level.set(index)
    currLevel.start()
    font=pygame.font.Font('freesansbold.ttf',50)
    indFont=pygame.font.Font('freesansbold.ttf',25)
    bgColor=(0,66,76)
    caution='please select'
    while game:
        scr.fill(bgColor)
        for x in range(0,525,50):
                pygame.draw.line(scr,(200,200,255,50),(x-15,0),(x-15,500),2)
                pygame.draw.line(scr,(200,200,255,50),(0,x),(525,x),2)
        for eve in pygame.event.get():
            caution=''
            if eve.type==pygame.QUIT:
                game=False
            if eve.type==pygame.KEYDOWN:
                if eve.unicode.isdigit():
                    if 0<eval(eve.unicode)<=len(currLevel.tubes):
                        if not selected:
                            selected=currLevel.tubes[eval(eve.unicode)-1]
                        else:
                            clicked=currLevel.tubes[eval(eve.unicode)-1]
                if eve.key==pygame.K_r:
                    currLevel=level.set(index)
                    currLevel.start()
                if eve.key==pygame.K_p:
                    if index>=1:
                        index-=1
                        currLevel=level.set(index)
                        currLevel.start()
                if eve.key==pygame.K_n:
                    index+=1
                    currLevel=level.set(index) if levels[index]!='finished' else None
                    if currLevel==None:
                        game=False
                    else:
                        currLevel.start()
                        
            if eve.type==pygame.MOUSEBUTTONDOWN:
                if 100<eve.pos[1]<100+capacity*2*ballsize:
                    if eve.pos[0]//tubeSepX<len(currLevel.tubes):
                        if not selected:
                            selected=currLevel.tubes[eve.pos[0]//tubeSepX]
                        else:
                            clicked=currLevel.tubes[eve.pos[0]//tubeSepX]
                elif eve.pos[0]>50 and 300<eve.pos[1]<300+capacity*2*ballsize and len(currLevel.tubes)>=5:
                    eve.pos=list(eve.pos)
                    eve.pos[0]=eve.pos[0]-50
                    if eve.pos[0]//tubeSepX<len(currLevel.tubes)-5:
                        if not selected:
                            selected=currLevel.tubes[5+eve.pos[0]//tubeSepX]
                        else:
                            clicked=currLevel.tubes[5+eve.pos[0]//tubeSepX]
                elif 450<eve.pos[1]<500 and 158<eve.pos[0]<358:
                    currLevel=level.set(index)
                    currLevel.start()
                elif 450<eve.pos[1]<500 and 0<eve.pos[0]<140:
                    if index>=1:
                        index-=1
                        currLevel=level.set(index)
                        currLevel.start()
                elif 450<eve.pos[1]<500 and 375<eve.pos[0]<525:
                    index+=1
                    currLevel=level.set(index) if levels[index]!='finished' else None
                    if currLevel==None:
                        game=False
                    else:
                        currLevel.start()
                    
            if eve.type==pygame.MOUSEBUTTONUP or eve.type==pygame.KEYUP:
                if selected and clicked:
                    if tube.pour(selected,clicked):
                        caution='please click tube "from"'
                    else:
                        caution='can put only on matching ball, select again!'
                    selected=clicked=None
        if selected:
            selected.select()
            caution='please click tube "to"'
        if clicked:
            clicked.click(selected)
        if currLevel==None:
            game=False
            break
        if currLevel.ifCompleted():
            scr.fill((170,170,255))
            word=font.render(random.choice(goodWords),1,(255,0,0))
            scr.blit(word,(250-word.get_size()[0]//2,100))
            pygame.display.update()
            pygame.time.delay(2000)
            index+=1
            currLevel=level.set(index) if levels[index]!='finished' else None
            if not currLevel:
                game=False
                break
            else:
                currLevel.start()
        [i.draw() for i in currLevel.tubes]
        l=font.render('Level :- '+str(index+1),1,(255,0,0))
        r=font.render(' Restart ',1,(255,0,0))
        n=font.render('   Next ',1,(255,0,0))
        p=font.render(' Prev ',1,(255,0,0))
        c=indFont.render(caution,1,(255,0,0))
        scr.blit(c,(250-c.get_size()[0]//2,400))
        scr.blit(l,(260-l.get_size()[0]//2,0))
        pygame.draw.rect(scr,(255,200,200),(375,450,150,50))
        pygame.draw.rect(scr,(255,100,100),(375,450,150,50),5)
        scr.blit(n,(350,450))
        pygame.draw.rect(scr,(255,200,200),(0,450,140,50))
        pygame.draw.rect(scr,(255,100,100),(0,450,140,50),5)
        scr.blit(p,(0,450))
        pygame.draw.rect(scr,(200,200,255),(158,450,200,50))
        pygame.draw.rect(scr,(100,100,255),(158,450,200,50),5)
        scr.blit(r,(150,450))
        pygame.display.update()
    pygame.quit()
