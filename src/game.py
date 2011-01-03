import pygame
from terrain import Terrain
from snail import Snail
from team import Team
#from weapon import Item

#D Display
surface = pygame.display.set_mode([640,640]) #retourneert Surface
pygame.display.set_caption("Gravity Snails")

pygame.mouse.set_visible(False)

#A Assign
terrain = Terrain()
team = Team('groep6')
snail = Snail(terrain)
snail.rect.move_ip(400, surface.get_height() - snail.rect.height - 100)
team.add(snail)
#weapon = Weapon()

blue     = 0, 0, 128
clock     = pygame.time.Clock()
keepGoing = True

#L Loop
while keepGoing:
    #T Timer (framerate)
    clock.tick(90)

    #E Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.locals.KEYDOWN:
        #    if event.key == pygame.locals.K_SPACE:
        #        weapon.shoot(snail)
        #        print 0
            if event.key == pygame.locals.K_t:
                terrain.createTerrain()
    terrain.update()
    team.update()

    #R refresh
    surface.fill(blue)
    terrain.draw(surface)
    team.draw(surface)
    pygame.display.flip()