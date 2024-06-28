import pygame
import os

background = pygame.image.load("images/background/background.jpg")

class Field:
    def __init__(self, x, y, width, height, idx, idy):
        self.x = x
        self.y = y
        self.idx = idx
        self.idy = idy
        self.image = None
        self.win_image = None
        self.rect = pygame.rect.Rect(x, y, width, height)
    def is_clicked(self, corx, cory):
        if self.rect.collidepoint(corx,cory):
            return True
        return False
    def set_image(self, image_name):
        self.image = pygame.image.load(f"images/{image_name}/{image_name}.png")
        self.win_image = pygame.image.load(f"images/{image_name}/win_{image_name}.png")

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.image = pygame.image.load(f"images/button/reset_button.png")
        self.rect = pygame.rect.Rect(x, y, width, height)
    def is_clicked(self, corx, cory):
        if self.rect.collidepoint(corx,cory):
            return True
        return False