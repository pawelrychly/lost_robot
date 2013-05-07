__author__ = 'Pawel Rychly, Maciej Trojan'

import random
from robot import Robot
from copy import deepcopy

class ParticleFilter:

    __NUM_OF_PARTICLES = 50

    def __init__(self, world):
        self.world = world
        self.particles = []
        for i in range(self.__NUM_OF_PARTICLES):
            particle = Robot(world,  10, 0.5, 100)
            self.particles.append(particle)
        return

    def resampling(self, w):
        resampled_particles = []
        index = int(random.random() * self.__NUM_OF_PARTICLES)
        beta = 0.0
        mw = max(w)

        for i in range(self.__NUM_OF_PARTICLES):
            beta += random.random() * 2.0 * mw
            while beta > w[index]:
                beta -= w[index]
                index = (index + 1) % self.__NUM_OF_PARTICLES
            new_particle = deepcopy(self.particles[index])
            resampled_particles.append(new_particle)

        self.particles = []
        self.particles = resampled_particles

    def get_particles(self):
        return self.particles

    def next_step(self, turn):
        robot_sense_data = self.world.get_robot().sense()
        probabilities = []
        for particle in self.particles:
            if turn is 0:
                particle.move_forward()
            else:
                particle.change_direction(turn)

            probabilities.append(particle.measure_probability(robot_sense_data))
        self.resampling(probabilities)
