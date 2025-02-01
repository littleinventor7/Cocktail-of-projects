import pygame
import os
pygame.font.init()
pygame.mixer.init()
width,height = 690, 450
fps = 60
pinkhit = pygame.USEREVENT +1
bluehit = pygame.USEREVENT +2
mxbullet = 3
winfont = pygame.font.SysFont("comicsans", 70)
rec = pygame.Rect(345-15,0,33,450)
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")
bluesspaceship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets','spaceship222.png')),(50,39)),270)
pinksspaceship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets','spaceship111.png')),(50,39)),90)
bluelasser = pygame.image.load(os.path.join('assets','pixel_laser_blue.png'))
yellowlasser = pygame.image.load(os.path.join('assets','pixel_laser_yellow.png'))
greenlasser = pygame.image.load(os.path.join('assets','pixel_laser_green.png'))
redlasser = pygame.image.load(os.path.join('assets','pixel_laser_red.png'))
pinklasser = pygame.image.load(os.path.join('assets','pixel_laser_pink.png'))
bg = pygame.image.load(os.path.join('assets','downloaad.jpg'))
greenalien =pygame.transform.rotate(pygame.image.load(os.path.join('assets','green.png')),90)
yellowalien = pygame.transform.rotate(pygame.image.load(os.path.join('assets','yellow.png')),90)
redalien = pygame.transform.rotate(pygame.image.load(os.path.join('assets','red.png')),90)
bsp = 7
def drawwin(text):
    dtxt = winfont.render(text,1,(255,255,255))
    win.blit(dtxt,(190,160))
    pygame.display.update()
    pygame.time.delay(2000)
def draw(blue,pink,pinkbullets,bluebullets,bluehealthbar,pinkhealthbar):
   # win.fill((0,0,255))
    win.blit(pygame.transform.scale(bg,(width,height)),(0,0))
    pygame.draw.rect(win,(0,0,0),rec)
   # win.blit(redalien,(345-15,0)) 
    #win.blit(greenalien,(345-15,0))
    #win.blit(yellowalien,(345-15,0))
    win.blit(pinksspaceship,(pink.x,pink.y))
    win.blit(bluesspaceship,(blue.x,blue.y))
    for bullet in bluebullets:
        pygame.draw.rect(win, (137,207,240), bullet)
    for bullet in pinkbullets:
        pygame.draw.rect(win, (255,192,203), bullet)
    bluehealthbar.draw(win,blue.x,blue.y)
    pinkhealthbar.draw(win,pink.x,pink.y)   
    pygame.display.update()
def bulletcollison(pinkbullet, bluebullet,pink,blue):
    for bullet in bluebullet:
        bullet.x -= bsp
        if pink.colliderect(bullet):
            pygame.event.post(pygame.event.Event(pinkhit))
            bluebullet.remove(bullet)
        elif bullet.x < 0:
            bluebullet.remove(bullet)
    for bullet in pinkbullet:
        bullet.x += bsp
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(bluehit))
            pinkbullet.remove(bullet)
        elif bullet.x > width:
            pinkbullet.remove(bullet)
class Ship:
       
        def __init__(self, x, y, health=20): 
            self.x = x
            self.y = y
            self.health = health 
            self.shipimg = bluesspaceship
            self.lasers = []
            self.cooldowncounter = 0
            self.rect = self.shipimg.get_rect()  
            self.rect.topleft = (x, y)  
            pass
        def draw(self, window):
           window.blit(self.shipimg,(self.x,self.y))
   
        def get_width(self):
            return self.shipimg.get_width()
        def get_height(self):
            return self.shipimg.get_height() 
class Playerhealthbar(Ship):
    def __init__(self, x, y, health=20):
        super().__init__(x, y, health)
        #self.mask = pygame.mask.from_surface(self.shipimg)
        self.mxhealth = health
    def draw(self, window,x,y):
        self.x = x 
        self.y = y 
        #super().draw(window)
        self.healthbar(window)
    def healthbar(self, window):
        pygame.draw.rect(window,(255,50,0),(self.x,self.y + self.shipimg.get_height()+10, self.shipimg.get_width(),10))
        pygame.draw.rect(window,(50,255,0),(self.x,self.y + self.shipimg.get_height()+10, self.shipimg.get_width()* (self.health/self.mxhealth), 10))
def main():
    bluebullet = []
    pinkbullet = []
    ssp = 5
    pink = pygame.Rect(20,194,50,39)
    blue = pygame.Rect(640,192,50,39)
    bluehealth = 20
    pinkhealth = 20
    bluehealthbar = Playerhealthbar(640,186)
    pinkhealthbar = Playerhealthbar(20,190)
    #win.blit(blue,(100,200))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        bluehealthbar.draw(win,blue.x,blue.y)
        pinkhealthbar.draw(win,pink.x,pink.y)
        pygame.display.update()   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(pinkbullet) < mxbullet:
                   bullet = pygame.Rect(pink.x+pink.width,pink.y+pink.height//2 + 2,10,5)
                   pinkbullet.append(bullet)
                if event.key == pygame.K_RCTRL and len(bluebullet) < mxbullet:
                   bullet = pygame.Rect(blue.x,blue.y+blue.height//2 + 2,10,5)
                   bluebullet.append(bullet)
            if event.type == bluehit:
               bluehealthbar.health -= 1
               bluehealth -= 1
               if bluehealthbar.health <= 0:
                  wintxt = "Pink Wins!"
        
            if event.type == pinkhit:
                pinkhealth -= 1
                pinkhealthbar.health -= 1
                if pinkhealthbar.health <= 0:
                   wintxt = "Blue Wins!"
        

            #bluehealthbar.draw(win)
            #pinkhealthbar.draw(win)
            #pygame.display.update()
        
        
        wintxt =""
        if bluehealth <= 0:
           wintxt ="Pink Wins!"
        if pinkhealth <= 0:
           wintxt ="Blue Wins!"
        if wintxt != "":
            drawwin(wintxt)
            break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and blue.x - ssp > 360:
            blue.x -= ssp
        if keys[pygame.K_RIGHT] and blue.x + ssp + 40 < 690:
            blue.x += ssp
        if keys[pygame.K_UP] and blue.y - ssp > 0:
            blue.y -= ssp
        if keys[pygame.K_DOWN] and blue.y - ssp + 10 < 400:
            blue.y += ssp
        if keys[pygame.K_a] and pink.x - ssp > 0:
            pink.x -= ssp
        if keys[pygame.K_d] and pink.x + ssp + 40 < 333:
            pink.x += ssp
        if keys[pygame.K_w]  and pink.y - ssp > 0:
            pink.y -= ssp
        if keys[pygame.K_s] and pink.y - ssp + 10 < 400:
            pink.y += ssp
        bulletcollison(pinkbullet,bluebullet,pink,blue)
        draw(blue, pink, pinkbullet, bluebullet, bluehealthbar, pinkhealthbar) 
    main()
if __name__ == "__main__":
    main()