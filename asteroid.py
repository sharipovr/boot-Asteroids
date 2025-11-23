import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()   # any asteroid technically is killed
    
    # but if it's small it disappears and we return
    if self.radius < ASTEROID_MIN_RADIUS: 
      return
    
    log_event("asteroid_split")
    rnd_angle = random.uniform(20,50)
  
  
    # calling the .rotate method on the asteroid's velocity vector to create two new vectors representing the new asteroids movement
    vector_one = self.velocity.rotate(rnd_angle)
    vector_two = self.velocity.rotate(-rnd_angle)

    new_radius = self.radius - ASTEROID_MIN_RADIUS

    # creating two new asteroids themselves 
    ast1 = Asteroid(self.position.x, self.position.y, new_radius)
    ast2 = Asteroid(self.position.x, self.position.y, new_radius)

    # Set the asteroids's .velocity to the new vectors, but make them move faster by scaling it up 1.2.
    ast1.velocity = vector_one * 1.2
    ast2.velocity = vector_two * 1.2
