import pygame
import sys
pygame.font.init()
width,height = 400,300
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Timer")
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
#def main():
font = pygame.font.SysFont("timesroman", 30)
timeleft = 5 *60
sttime = pygame.time.get_ticks()
timerun =True
reb = pygame.Rect(150, 200, 100, 50)

clock = pygame.time.Clock()
run = True
while run:
    win.fill(WHITE)
    if timerun:
        passedtime = pygame.time.get_ticks() -sttime
        remaintime = timeleft - (passedtime// 1000)

        if remaintime <= 0 :
            remaintime =0
            timerun = False
        mint  = remaintime //60
        seconds = remaintime % 60
        #milliseconds = (remaintime % 1000) // 10
        timetext = font.render(f"{mint:02}:{seconds:02}", True, BLACK)
        win.blit(timetext, (width // 2 - 40, 100))
        pygame.draw.rect(win, RED, reb)
        win.blit(font.render("Reset", True, WHITE), (reb.x + 20, reb.y + 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reb.collidepoint(event.pos):
                        timerun = True
                        sttime =pygame.time.get_ticks()
                        timeleft = 5 *60
            pygame.display.update()
        pygame.display.flip()
        clock.tick(30)
        
