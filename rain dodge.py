import pygame
import time
import random
import os
import asyncio
pygame.font.init()
width,height = 700 , 560
fps = 60
timefont = pygame.font.SysFont("timesroman", 30)
font = pygame.font.SysFont("timesroman", 60)
gofont = pygame.font.SysFont("timesroman", 100)
pygame.init()  # إضافة هذا السطر لحل المشكلة
win =  pygame.display.set_mode((width,height))
pygame.display.set_caption("Rain Dodge")
def loadhighestscore():
    if os.path.exists("score.txt"):
        with open("score.txt", "r") as file:
            return int(file.read().strip())
    return 0
highestscore = loadhighestscore()
def savehighestscore(score):
    with open("score.txt", "w") as file:
        file.write(str(score))
def draw(player ,passedtime,rains):
    win.fill((0,0,0))
    timetxt = timefont.render(f"Time :{round(passedtime)}s", 1, (255,255,255))
    win.blit(timetxt, (20,20))
    pygame.draw.rect(win, (0,0,255),player)
    for rain in rains:
        pygame.draw.rect(win,(255,255,255),rain)
    pygame.display.update()
def checkhighestscore(passedtime):
    global highestscore
    if passedtime > highestscore:
        highestscore = passedtime
        savehighestscore(highestscore)
  

async def main():
    run = True
    player = pygame.Rect(200,height-50,50,50)
    clock =pygame.time.Clock()
    sttime = time.time()
    passedtime = 0
    raindaddincreaseing = 1000
    raincnt = 0
    rains = []
    hit = False
    while run:
        clock.tick(fps)
        passedtime = time.time() - sttime
        raincnt += clock.tick(fps)
        if raincnt > raindaddincreaseing:
            for i in range(5):
                rainx = random.randint(0,width-10)
                rain = pygame.Rect(rainx, -20,5,10)
                rains.append(rain)
            raindaddincreaseing = max(400,raindaddincreaseing - 50)
            raincnt = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
               break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - 7 >= 0:
            player.x -= 7
        if keys[pygame.K_RIGHT]and player.x + 7 <= 700-50:
            player.x += 7
        for rain in rains[:]:
            rain.y += 5
            if rain.y > 560:
                rains.remove(rain)
            elif rain.y + 10 >= player.y and rain.colliderect(player):
                rains.remove(rain)
                hit = True
                break   
        if hit:
             checkhighestscore(round(passedtime))
             losttext =gofont.render(f"Game Over", 1, (255,255,255))
             win.blit(losttext,(width/2 - losttext.get_width()/2,height/2 - losttext.get_height()/2))
             pygame.display.update()
             pygame.time.delay(3000)
             win.fill((0,0,0))
             pygame.display.update()
             highestscoretxt =font.render(f"Highest Score: {round(highestscore)}s", 1, (255,255,255))
             win.blit(highestscoretxt,(width/2 - highestscoretxt.get_width()/2,height/2 - highestscoretxt.get_height()/2))
             pygame.display.update()
             pygame.time.delay(3000)
             break ###
        draw(player,passedtime,rains)     
    await asyncio.sleep(0)
    pygame.quit()

#if __name__ == "__main__":
asyncio.run(main())