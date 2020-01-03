from sprites.particle import Particle


class TrailHandler:
    limit = 6
    delay = 1
    particle_size = 4

    def __init__(self):
        self.particles = []
        self.counter = 0

    def update(self, ball):
        self.counter += 1
        if self.counter > self.delay:
            self.particles.append(Particle(self.particle_size, ball.rect.centerx,
                                           ball.rect.centery))
            if len(self.particles) > self.limit:
                del self.particles[0]
            self.counter = 0
