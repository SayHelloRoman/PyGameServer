import pygame


class User:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, key):
        if key[pygame.K_d] and self.x + 1 <= 9:
            self.x += 1
        
        elif key[pygame.K_a] and self.x - 1 >= 0:
            self.x -= 1
        
        elif key[pygame.K_s] and self.y + 1 <= 9:
            self.y += 1
        
        elif key[pygame.K_w] and self.y - 1 >= 0:
            self.y -= 1