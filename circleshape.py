import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x,y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",
            self.triangle(),
            2
        )

    def update(self, dt):
        pass

    def check_collision(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= self.radius + other.radius:
            return True
        return False
