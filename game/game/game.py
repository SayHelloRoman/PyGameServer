import pygame

from .user import User

import sys

import json

from websocket import create_connection

class Main:
    def __init__(self):
        pygame.init()
        self.sc = pygame.display.set_mode((500, 500))
        self.user = User()
        self.con = create_connection("ws://127.0.0.1:8000/game")
    
    def update(self):
        clock = pygame.time.Clock()
        FPS = 30
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
            
            self.map = json.loads(self.con.recv())["map"]
            self.draw()

            self.user.move(pygame.key.get_pressed())
            self.con.send(json.dumps({
                "x": self.user.x,
                "y": self.user.y
            }))
            self.x = [[0 for b in range(11)] for i in range(11)]
            self.x[self.user.x][self.user.y] = 1

            pygame.display.update()

            clock.tick(FPS)
        

    def draw(self):
        for i in range(len(self.map)):
            for g in range(len(self.map[i])):
                if self.map[i][g] == 0:
                    pygame.draw.rect(self.sc, (124, 252, 0), (i*50, g*50, 50, 50))
                    
                elif self.map[i][g] == 1:
                    pygame.draw.rect(self.sc, (0, 0, 0), (i*50, g*50, 50, 50))
    
