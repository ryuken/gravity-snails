import pygame
from pygame.locals import *
from utils import load_image
from utils import load_sound

from enums import Direction
from enums import TurnStatus
from turnmanager import TurnManager
from scenes.scenemanager import SceneManager
from settings import Settings

class Snail(pygame.sprite.Sprite):
    """
    This is the snail class, which is used for handling walking, collision detection,
    and everything else the snail does in the game.
    """
    def __init__(self, team):
        pygame.sprite.Sprite.__init__(self)

        self.id = None

        self.initEvents()
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
        self.hitpoints = Settings.GAME_SNAILS_HP

        # The snail isn't placed yet
        self.isPlaced = False

        # Bullet
        self.bullet = None
        # The snail hasn't shooted yet
        self.hasShot = False

        # The snail doesn't have the turn
        #self.hasTurn = False

        self._hasTurn = False
        pygame.font.init()
        self.font_hp = pygame.font.Font(None, 20)

    def set_hasTurn(self, value):
        """
        set the hasTurn value
        @param value: the value to assign to hasTurn, True or False
        """
        self._hasTurn = value
        self.hasShot = False

    def get_hasTurn(self):
        """
        get the hasTurn value"""
        return self._hasTurn
    """
    Property used to set and get the hasTurn value
    """
    hasTurn = property(get_hasTurn, set_hasTurn)
    

    def initEvents(self):
        """
        Register an event in the SceneManager so we can handle key input from Pygame later.
        """
        SceneManager().registerEventReader(self.do_action)
    
    
    def do_action(self, event):
        """
        Handle events for handling some keys with custom logic in Snail.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.hasTurn:
                self.shoot()

    def collideWithTerrain(self, terrain):
        """
        Check if the snail collides with terrain.
        @param terrain: The terrain object which was created at startup.
        @return: True when a snail collides with terrain else False 
        """
        return len(pygame.sprite.spritecollide(self, terrain, False)) > 0

    def checkHealth(self):
        """
        Check the health of the current snail.
        If the snail hits less or equal than 0 HP, play a sound and set attribut isAlive to false
        This method is called in Snail.update
        """
        if self.hitpoints <= 0:
            kill_sound = load_sound("kill.ogg")
            kill_sound.play()
            self.isAlive = False

    def shoot(self):
        """
        Shoot with the current active weapon of team.
        This method is called in do_action when the space button is pressed
        """
        if self.team.hasTurn and self.hasTurn and False == self.hasShot:
            self.team.active_weapon.shoot()
            self.hasShot = True

    def update(self, input, terrain):
        """
        This is where all the continious logic happens of snail, such as checking health, placing snails,
        updating positions, checking for collision.
        @param input: The input class also used for unit testing
        @param terrain: The terrain object which was created at startup.
        """
        # the checkHealth needs to be run first
        self.checkHealth()

        #E Event
        if(not self.isPlaced and not None == self.team.active_weapon):
            if self.team.hasTurn and self.hasTurn:
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
                        TurnManager().changeTurnSnail(self.team)
        else:
            #check if right mouse is pressed
            if(input.mouse_right_clicked and self.hasTurn and self.team.hasTurn):
                input.mouse_right_clicked = False
                self.team.inventory.visible = True
                #self.update(input, terrain)
                return
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
        """
        Update the image of the snail depending on the direction of the movement and gravity direction
        """
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
            self.team.active_weapon.snail = self

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


    def updateGravity(self):
        """
        Update the gravity so the snail will make a falling movement when jumping
        """
        # Make the snail fall
        self.direction['jump'] += self.speed['fall']
        if self.direction['jump'] > 5:
            self.direction['jump'] = 5

    def updateCollisionVertical(self, terrain):
        """
        Check for vertical collision depending of the gravity direction of snail.
        @param terrain: The terrain object which was created at startup.
        """
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
            if(not TurnManager().status == TurnStatus.CURRENTTURN):
                can_jump = False
            if (pygame.key.get_pressed()[K_RETURN] and can_jump and self.hasTurn and self.team.hasTurn):
                self.direction['jump'] = -self.speed['jump']

    def updateCollisionHorizontal(self, terrain):
        """
        Check for horizontal collision depending of the gravity direction of snail.
        @param terrain: The terrain object which was created at startup.
        """
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
        """
        Load the different images so we can use them later when moving
        """
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
        @param surface: This is the surface created in the game class 
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
            if TurnManager().status == TurnStatus.CURRENTTURN:
                surface.blit(arrow, pos)