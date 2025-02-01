import pygame
import sys
pygame.font.init()
width,height = 400,300
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Stopwatch")
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("timesroman", 30)

def main():
    sttb =pygame.Rect(50,200,80,50)
    stpb =pygame.Rect(160,200,80,50)
    reb =pygame.Rect(270,200,80,50)
    runn =False
    sttime =0
    passedtime =0
    run = True
    clock = pygame.time.Clock()
    while run:
        win.fill((WHITE))
        if runn:
            passedtime =pygame.time.get_ticks()- sttime
        

        seconds =passedtime //1000
        millis = (passedtime % 1000) // 10
        timext = font.render(f"{seconds:02}:{millis:02}",1,BLACK)
        win.blit(timext,(width// 2 -40,100))
        pygame.display.update()
        pygame.draw.rect(win,GREEN,sttb)
        pygame.draw.rect(win,RED,stpb)
        pygame.draw.rect(win,GRAY,reb)
        win.blit(font.render("Start", True, WHITE), (sttb.x + 10, sttb.y + 10))
        win.blit(font.render("Stop", True, WHITE), (stpb.x + 15, stpb.y + 10))
        win.blit(font.render("Reset", True, WHITE), (reb.x + 10, reb.y + 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sttb.collidepoint(event.pos):
                    if not runn:
                        sttime = pygame.time.get_ticks() - passedtime
                        runn =True
                elif stpb.collidepoint(event.pos):
                        runn=False
                elif reb.collidepoint(event.pos):
                        run =False
                        passedtime =0
            pygame.display.update()
        pygame.display.flip()
        clock.tick(30)
    main()
main()





