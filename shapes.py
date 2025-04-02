import pygame

class Shape():
    def __init__(self,screen,color,thick):
        self.screen = screen
        self.color = color
        self.thick = thick

    def change_color(self, new_color):
        self.color = new_color

class Circ(Shape):

    def __init__(self, screen, color, center, radius, thick):
        super().__init__(screen, color, thick)
        self.center = center
        self.radius = radius
        
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius, self.thick)

class Rect(Shape):
    def __init__(self, screen, color,x,y, height, width, thick):
        super().__init__(screen,color,thick)
        self.rect = pygame.Rect(x,y,width,height)
        
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
    def change_x_pos(self, new_x):
        self.x = new_x

        self.rect = pygame.Rect(new_x, self.y, self.width, self.height)

    def change_y_pos(self, new_y):
        self.y = new_y

        self.rect = pygame.Rect(self.x, new_y, self.width, self.height)
        
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.thick)

