__author__ = 'Pawel Rychly, Maciej Trojan'

import random

class ParticleFilter:

    def __init__(self):
        self.particles = []
        return

    def resampling(self, w):
        N = len(self.particles)
        resampled_particles = []
        index = int(random.random() * N)
        beta = 0.0
        mw = max(w)
        for i in range(N):
            beta += random.random() * 2.0 * mw
            while beta > w[index]:
                beta -= w[index]
                index = (index + 1) % N
            resampled_particles.append(self.particles[index])
        self.particles = resampled_particles