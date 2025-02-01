import pygame
import time
import math 
import os
pygame.init()
fps = 60
grass =  pygame.image.load(os.path.join('assets','grass03.png'))
track1 =  pygame.image.load(os.path.join('assets','tark1.png'))
track1broder =  pygame.image.load(os.path.join('assets','tark1-border.png'))
trakck1bordermask = pygame.mask.from_surface(pygame.transform.scale(track1broder,(500,500)))
track2 =  pygame.image.load(os.path.join('assets','track2.png'))
track2border =  pygame.image.load(os.path.join('assets','trak2_border.png'))
finish =  pygame.image.load(os.path.join('assets','finish.png'))
finishmask = pygame.mask.from_surface(pygame.transform.scale(finish,(52,12)))
redcar =  pygame.image.load(os.path.join('assets','redcar.png'))
bluecar =  pygame.image.load(os.path.join('assets','bluecar.png'))
def blitrotcen(win,img,topl,angle):
    rottedimg = pygame.transform.rotate(img,angle)
    nrect = rottedimg.get_rect(
        center=img.get_rect(topleft=topl).center)
    win.blit(rottedimg,nrect.topleft)
class Abcar:
    def __init__(self,mxsp,rotsp):
        self.img =self.image
        self.mxsp = mxsp
        self.sp = 0
        self.rotsp =rotsp
        self.angle = 0
        self.x = self.stx
        self.y = self.sty
        self.acc = 0.05
    def rot(self,l=False,r=False):
        if l:
            self.angle += self.rotsp
        elif r:
            self.angle -= self.rotsp
    def movef(self):
        self.sp = min(self.sp+self.acc,self.mxsp)
        self.move()
    def moveb(self):
        self.sp = max(self.sp-self.acc,-self.mxsp/2)
        self.move()
    def move(self,b=True):
        rad = math.radians(self.angle)
        vert = math.cos(rad)*self.sp
        horz = math.sin(rad)*self.sp
        if b:
            self.y -= vert
            self.x -= horz
        else:
            self.y += vert
            self.x += horz
    def collide(self,mask,x=0,y=0):
        carmask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x),int(self.y - y))
        po = mask.overlap(carmask,offset)
        return po
    def draw(self,win):
        blitrotcen(win, self.img,(self.x,self.y),self.angle)
    def reset(self):
        self.x, self.y = self.stx, self.sty
        self.angle = 0
        self.sp =0

class Player(Abcar):
    image = pygame.transform.rotate(pygame.transform.scale(bluecar,(30,14.8875)),90)
    stx = 90
    sty = 85
    def redsp(self): 
        self.sp = max(self.sp-self.acc/2,0)
        self.move()
    def stop(self):
        #self.sp = -1*self.sp
        self.move(b=False)
class Player2(Abcar):
    image = pygame.transform.rotate(pygame.transform.scale(redcar,(30,14.8875)),90)
    stx = 67
    sty = 85
    def redsp(self): 
        self.sp = max(self.sp-self.acc/2,0)
        self.move()
    def stop(self):
        #self.sp = -1*self.sp
        self.move(b=False)    
txt = 0
pygame.display.set_caption("Car Race Game")
width , height = 500,500
win = pygame.display.set_mode((width,height))
def main(): 
    p2 = Player2(3,3) 
    run = True
    clock = pygame.time.Clock()
    sttime = time.time()
    p = Player(3,3)
    while run:
        clock.tick(fps)
        passedtime = time.time() - sttime
        win.blit(grass,(0,0))
        win.blit(pygame.transform.scale(track1,(500,500)),(0,0))
        win.blit(pygame.transform.scale(finish,(52,12)),(63,120))
        win.blit(pygame.transform.scale(track1broder,(500,500)),(0,0))
        p.draw(win)
        p2.draw(win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()
            
            
        key = pygame.key.get_pressed()
        moved = False
        if key[pygame.K_LEFT]:
            p.rot(l=True)
        if key[pygame.K_RIGHT]:
            p.rot(r=True)
        if key[pygame.K_UP]:
            moved =True
            p.movef()
        if key[pygame.K_DOWN]:
            moved =True
            p.moveb()
        if not moved:
            p.redsp()
        if p.collide(trakck1bordermask) != None :
            p.stop()
        
        fpc = p.collide(finishmask, 63, 120)
        if fpc != None :
            if fpc[1] == 0:
                p.stop()
            else :
                p.reset()
                #break
        moved = False
        if key[pygame.K_a]:
            p2.rot(l=True)
        if key[pygame.K_d]:
            p2.rot(r=True)
        if key[pygame.K_w]:
            moved =True
            p2.movef()
        if key[pygame.K_s]:
            moved =True
            p2.moveb()
        if not moved:
            p2.redsp()
        if p2.collide(trakck1bordermask) != None :
            p2.stop()
        
        fp2c = p2.collide(finishmask, 63, 120)
        if fp2c != None :
            if fp2c[1] == 0:
                p2.stop()
            else :
                p2.reset()
                #break
        
    
    
    main()

main()
