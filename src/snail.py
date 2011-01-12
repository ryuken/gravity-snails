import pygame
import random
from pygame.locals import *
from utils import load_image

from enums import Direction
from enums import TurnStatus
from turnmanager import TurnManager

class Snail(pygame.sprite.Sprite):

    def __init__(self, team):
        pygame.sprite.Sprite.__init__(self)

        # Set the speed constants
        self.speed = {'movement' : 2, 'jump' : 10, 'fall' : 0.2}
        # The snail doesn't move
        self.direction = {'movement' : 0.0, 'jump' : 0.0}

        # Remember his own team
        self.team = team

        self.isAlive = True

        # Set the gravity direction
        self.gravity_direction = self.team.gravity_direction

        #load images, using default settings
        self.setImages()

        # Update the rect
        self.rect = self.image.get_rect()

        # The hitpoints of the snail
        self.hitpoints = 100

        # The snail isn't placed yet
        self.isPlaced = False

        # Bullet
        self.bullet = None
        # The snail hasn't shooted yet
        self.hasShot = False
        # The snail doesn't have the turn
        self.hasTurn = False
        
        pygame.font.init()
        self.font_hp = pygame.font.Font(None, 20)

    def collideWithTerrain(self, terrain):
        return len(pygame.sprite.spritecollide(self, terrain, False)) > 0

    def checkHealth(self):
        if self.hitpoints <= 0:
            self.isAlive = False

    def shoot(self):
        if self.team.hasTurn and self.hasTurn:
            self.team.active_weapon.shoot()
            self.hasShot = True

    def update(self, input, terrain):
        # the checkHealth needs to be run first
        self.checkHealth()

        #E Event
        if(not self.isPlaced):
            if self.hasTurn and self.team.hasTurn:
                # The snail is not placed yet
                # Store the current position
                prev_x = self.rect.centerx
                prev_y = self.rect.centery
                # Get the mouse position
                self.rect.centerx = input.mouse_x
                self.rect.centery = input.mouse_y
                # Is the position valid to place the snail?
                if(self.collideWithTerrain(terrain)):
                    # Use the last known valid position
                    self.rect.centerx = prev_x
                    self.rect.centery = prev_y
                else:
                    # Place the snail if the mousebutton is pressed
                    if input.get_mouse_left_click():
                        self.isPlaced = True
                        TurnManager().changeTurn()
        else:
            # If the snail is placed
            # Check if the snail if moving, and check if the snail is falling
            self.updateMove(input)
            self.updateGravity()

            # Update the "horizontal" movement (Walking)
            self.updateCollisionHorizontal(terrain)
            # Update the "vertical" movement (Falling / Jumping)
            self.updateCollisionVertical(terrain)
            list = pygame.sprite.spritecollide(self, terrain.salt, False)
            if(len(list) > 0):
                self.hitpoints = 0

        # Use the correct sprite
        self.updateImage()

    def updateImage(self):
        # Check if the snail is moving left or right
        left_pressed = self.direction['movement'] == -self.speed['movement']
        right_pressed = self.direction['movement'] == self.speed['movement']
        if (left_pressed):
            if(self.gravity_direction == Direction.DOWN):
                # Use the correct sprite
                self.image = self.image_down_left
            elif(self.gravity_direction == Direction.UP):
                # Use the correct sprite
                self.image = self.image_up_left
            elif(self.gravity_direction == Direction.LEFT):
                # Use the correct sprite
                self.image = self.image_left_up
            elif(self.gravity_direction == Direction.RIGHT):
                # Use the correct sprite
                self.image = self.image_right_up
        if (right_pressed):
            if(self.gravity_direction == Direction.DOWN):
                # Use the correct sprite
                self.image = self.image_down_right
            elif(self.gravity_direction == Direction.UP):
                # Use the correct sprite
                self.image = self.image_up_right
            elif(self.gravity_direction == Direction.LEFT):
                # Use the correct sprite
                self.image = self.image_left_down
            elif(self.gravity_direction == Direction.RIGHT):
                # Use the correct sprite
                self.image = self.image_right_down

    def updateMove(self, input):
        # Stop moving left right
        self.direction['movement'] = 0
        # Store the arrowkeys + spacebar in variables
        if self.team.hasTurn and self.hasTurn:
            self.team.active_weapon.snail_rect = self.rect

            left_pressed = input.keyboard_left
            right_pressed = input.keyboard_right
            up_pressed = input.keyboard_up
            down_pressed = input.keyboard_down

            # Check if the gravity is left or right
            if(self.gravity_direction == Direction.LEFT or self.gravity_direction == Direction.RIGHT):
                # switch the left/right arrowkey with up/down
                temp_left, temp_right = left_pressed, right_pressed
                left_pressed, right_pressed = up_pressed, down_pressed
                up_pressed, down_pressed = temp_left, temp_right
            if (left_pressed):
                # Move the snail to the left
                self.direction['movement'] = -self.speed['movement']
            if (right_pressed):
                # Move the snail to the right
                self.direction['movement'] = self.speed['movement']
            if (up_pressed):
                self.team.active_weapon.adjustAngle(0)
            if (down_pressed):
                self.team.active_weapon.adjustAngle(1)

    def updateGravity(self):
        # Make the snail fall
        self.direction['jump'] += self.speed['fall']
        if self.direction['jump'] > 5:
            self.direction['jump'] = 5

    def updateCollisionVertical(self, terrain):
        if(self.gravity_direction == Direction.DOWN):
            self.rect = self.rect.move(0, self.direction['jump'])
        if(self.gravity_direction == Direction.UP):
            self.rect = self.rect.move(0, -self.direction['jump'])
        if(self.gravity_direction == Direction.LEFT):
            self.rect = self.rect.move(-self.direction['jump'], 0)
        if(self.gravity_direction == Direction.RIGHT):
            self.rect = self.rect.move(self.direction['jump'], 0)
        if(self.collideWithTerrain(terrain)):
            list = pygame.sprite.spritecollide(self, terrain, False)
            can_jump = False
            collision_x = list[0].rect.centerx
            collision_y = list[0].rect.centery
            if(self.gravity_direction == Direction.DOWN):
                self.rect = self.rect.move(0, -self.direction['jump'])
                can_jump = collision_y > self.rect.centery
            if(self.gravity_direction == Direction.UP):
                self.rect = self.rect.move(0, self.direction['jump'])
                can_jump = collision_y < self.rect.centery
            if(self.gravity_direction == Direction.LEFT):
                self.rect = self.rect.move(self.direction['jump'], 0)
                can_jump = collision_x < self.rect.centerx
            if(self.gravity_direction == Direction.RIGHT):
                self.rect = self.rect.move(-self.direction['jump'], 0)
                can_jump = collision_x > self.rect.centerx
            self.direction['jump'] = 0
            if (pygame.key.get_pressed()[K_RETURN] and can_jump and self.hasTurn and self.team.hasTurn):
                self.direction['jump'] = -self.speed['jump']

    def updateCollisionHorizontal(self, terrain):
        if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
            self.rect = self.rect.move(self.direction['movement'], 0)
        else:
            self.rect = self.rect.move(0, self.direction['movement'])
        if(self.collideWithTerrain(terrain)):
            if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
                self.rect = self.rect.move(-self.direction['movement'], 0)
            else:
                self.rect = self.rect.move(0, -self.direction['movement'])

    def setImages(self, rightAndLeftImages=['snail1Right.png', 'snail1Left.png']):
        self.rightAndLeftImages = rightAndLeftImages
        # Load every snail sprite
        self.image = load_image(rightAndLeftImages[0])
        self.image_down_right = load_image(rightAndLeftImages[0])
        self.image_down_left = load_image(rightAndLeftImages[1])
        self.image_up_left = pygame.transform.rotate(self.image_down_right, 180)
        self.image_up_right = pygame.transform.rotate(self.image_down_left, 180)
        self.image_left_up = pygame.transform.rotate(self.image_down_left, 270)
        self.image_left_down = pygame.transform.rotate(self.image_down_right, 270)
        self.image_right_up = pygame.transform.rotate(self.image_down_right, 90)
        self.image_right_down = pygame.transform.rotate(self.image_down_left, 90)

        if self.gravity_direction == Direction.DOWN:
            # Use the correct sprite
            self.image = self.image_down_right
        if self.gravity_direction == Direction.UP:
            # Use the correct sprite
            self.image = self.image_up_right
        if self.gravity_direction == Direction.LEFT:
            # Use the correct sprite
            self.image = self.image_left_up
        if self.gravity_direction == Direction.RIGHT:
            # Use the correct sprite
            self.image = self.image_right_up
    
    def draw(self, surface):
        """
        Draw the snail, when the snail has the turn it will
        get an arrow on his head so you know that he got the turn
        """
        
        # draw the snail
        surface.blit(self.image, self.rect)
        
        # draw the snail's HP
        text = self.font_hp.render(str(self.hitpoints), 1, (255, 0, 0)) #returns surface
        if self.team.gravity_direction == Direction.DOWN:
                # set the arrow at the correct position
                pos = [self.rect.topleft[0], self.rect.top - 20]
        elif self.team.gravity_direction == Direction.UP:
            # set the arrow at the correct position
            pos = [self.rect.topleft[0], self.rect.top + 30]
            
        elif self.team.gravity_direction == Direction.LEFT:
            # set the arrow at the correct position
            pos = [self.rect.topleft[0] + 27, self.rect.top - 20]
            
        elif self.team.gravity_direction == Direction.RIGHT:
            # set the arrow at the correct position
            pos = [self.rect.topleft[0] - 20, self.rect.top - 27]
        
        surface.blit(text, pos)
        
        # draw an arrow with the snail who got the turn
        arrow = load_image("arrow.png")
        if self.team.hasTurn and self.hasTurn:
            # !!! DO NOT CHANGE POS VALUES OR BACK THEM UP BEFORE CHANGING THEM !!!
            # !!! WHEN U CHANGE THEM FOR LEFT OR RIGHT THE X AND Y ARE REVERTED !!!
            if self.team.gravity_direction == Direction.DOWN:
                # set the arrow at the correct position
                pos = [self.rect.topleft[0] - 20, self.rect.top - 100]
            elif self.team.gravity_direction == Direction.UP:
                # flip the default image so the arrow will be at the correct direction
                arrow = pygame.transform.flip(arrow, 1, 1)
                # set the arrow at the correct position
                pos = [self.rect.topleft[0] - 20, self.rect.top + 50]
                
            elif self.team.gravity_direction == Direction.LEFT:
                # flip the default image so the arrow will be easier to rotate
                # then rotate it to the correct direction
                arrow = pygame.transform.flip(arrow, 1, 1)
                arrow = pygame.transform.rotate(arrow, 90)
                # set the arrow at the correct position
                pos = [self.rect.topleft[0] + 27, self.rect.top - 20]
                
            elif self.team.gravity_direction == Direction.RIGHT:
                # rotate the default image to the correct direction
                arrow = pygame.transform.rotate(arrow, 90)
                # set the arrow at the correct position
                pos = [self.rect.topleft[0] - 85, self.rect.top - 27]
            
            surface.blit(arrow, pos)