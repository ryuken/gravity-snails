import pygame
from terrain import Terrain
from snail import Snail
from team import Team
from timer import Timer

#I Import
pygame.font.init()

#D Display
surface = pygame.display.set_mode([640,640]) #retourneert Surface
pygame.display.set_caption("Gravity Snails")
#pygame.mouse.set_visible(False)

#A Assign
terrain = Terrain()
team1 = Team('groep5')
team2 = Team('groep6')
snail = Snail(terrain)
#snail.rect.move_ip(400, surface.get_height() - snail.rect.height - 100)
team1.add(snail)
timer = Timer(position=(0,0), size=(20,20), startTime="30")

blue     = 0, 0, 128
clock     = pygame.time.Clock()
keepGoing = True

#L Loop
while keepGoing:
    #T Timer (framerate)
    clock.tick(90)

    #E Event
    for event in pygame.event.get():
        timer.update(event)
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.MOUSEBUTTONUP:
            if (snail.isPlaced):
                snail = Snail(terrain)
                team1.add(snail)
        
    terrain.update()
    team1.update()

    #R refresh
    surface.fill(blue)
    terrain.draw(surface)
    team1.draw(surface)
    timer.draw(surface)
    pygame.display.flip()