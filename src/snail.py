import pygame
import sys
import math
from pygame.locals import *
from utils import load_image
from weapon import Weapon
from enums import *
from bullet import Bullet
from turnmanager import TurnManager
from settings import Settings
class Snail(pygame.sprite.Sprite):

    def __init__(self, team):
        pygame.sprite.Sprite.__init__(self)
        # Load every snail sprite
        self.image = load_image('snailRight.png')
        self.image_down_right = load_image('snailRight.png')
        self.image_down_left = load_image('snailLeft.png')
        self.image_up_left = pygame.transform.rotate(self.image_down_right, 180)
        self.image_up_right = pygame.transform.rotate(self.image_down_left, 180)
        self.image_left_up = pygame.transform.rotate(self.image_down_left, 270)
        self.image_left_down = pygame.transform.rotate(self.image_down_right, 270)
        self.image_right_up = pygame.transform.rotate(self.image_down_right, 90)
        self.image_right_down = pygame.transform.rotate(self.image_down_left, 90)
        # Set the speed constants
        self.speed = {'movement' : 2, 'jump' : 10, 'fall' : 0.2}
        # The snail doesn't move
        self.direction = {'movement' : 0.0, 'jump' : 0.0}
        
        # Remember his own team
        self.team = team
        
        # Set the gravity direction
        self.gravity_direction = self.team.gravity_direction
        
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
        # Update the rect
        self.rect = self.image.get_rect()
        
        # The hitpoints of the snail
        self.hitpoints = 100
        # The id of the snail
        self.id = None
        # The snail isn't placed yet
        self.isPlaced = False
        # Give the snail a weapon
        self.weapon = Weapon("laser", 100)
        # Set the aiming direction
        self.weaponAngle = 45
        # Bullet
        self.bullet = None
        # The snail hasn't shooted yet
        self.has_shooted = False
        # The snail doesn't have the turn
        self.hasTurn = False
    
    def collideWithTerrain(self, terrain):
        return len(pygame.sprite.spritecollide(self, terrain, False)) > 0
    
    def update(self, input, terrain):
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
                self.kill()
            self.updateBullet(terrain)
    def updateBullet(self, terrain):
        if self.bullet <> None:
            self.bullet.update(terrain)
            if self.bullet.alive == False:
                self.bullet.kill()
                self.bullet = None

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
        if self.team.hasTurn and self.hasTurn and TurnManager().status == TurnStatus.CURRENTTURN:
            left_pressed = input.keyboard_left
            right_pressed = input.keyboard_right
            up_pressed = input.keyboard_up
            down_pressed = input.keyboard_down
            space_pressed = input.keyboard_space
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
                # Adjust the aiming
                self.weaponAngle += 1
                if self.weaponAngle > 360:
                    self.weaponAngle = self.weaponAngle - 360
            if (down_pressed):
                # Adjust the aiming
                self.weaponAngle -= 1
                if self.weaponAngle < 0:
                    self.weaponAngle = 360 + self.weaponAngle
            # Check if the spacebar is pressed and the snail is allowed to shoot
            if (space_pressed and self.bullet == None):
                # Calculate the x and y speed of the bullet
                bullet_speed_x = math.cos(math.radians(self.weaponAngle)) * 10.0 #(self.rect.width)
                bullet_speed_y = math.sin(math.radians(self.weaponAngle)) * 10.0 #(self.rect.height)
                # Calculate the start position of the bullet
                bullet_margin_x = math.cos(math.radians(self.weaponAngle)) * (self.rect.width)
                bullet_margin_y = math.sin(math.radians(self.weaponAngle)) * (self.rect.height)
                bullet_position = [0,0]
                bullet_position[0] = self.rect.centerx
                bullet_position[1] = self.rect.centery
                bullet_position[0] += bullet_margin_x
                bullet_position[1] += bullet_margin_y
                # Add the bullet to the game
                self.bullet = Bullet(bullet_position, [bullet_speed_x, bullet_speed_y])
                print "created bullet"
                TurnManager().changeTurn()
                #self.game.addBullet(Bullet(self.game, bullet_position, [bullet_speed_x, bullet_speed_y]))

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
            if (pygame.key.get_pressed()[K_RETURN] and can_jump and self.hasTurn):
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

    def draw(self, surface):
        if self.hasTurn and self.team.hasTurn:
            x_margin = 0
            y_margin = 0
            #if(self.gravity_direction == Direction.DOWN or self.gravity_direction == Direction.UP):
            x_margin = math.cos(math.radians(self.weaponAngle)) * (self.rect.width * 2)
            #if(self.gravity_direction == Direction.LEFT or self.gravity_direction == Direction.RIGHT):
            y_margin = math.sin(math.radians(self.weaponAngle)) * (self.rect.height * 2)
            #if(self.image == self.im)
            self.weapon.rect.centerx = self.rect.centerx + x_margin
            self.weapon.rect.centery = self.rect.centery + y_margin
            #self.weapon.rect.move_ip(self.rect.centerx, self.rect.centery)
            surface.blit(self.weapon.image, self.weapon.rect)
        
        if self.bullet <> None:
            surface.blit(self.bullet.image, self.bullet.rect)
