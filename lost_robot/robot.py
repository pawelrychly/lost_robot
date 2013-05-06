__author__ = 'Pawel Rychly, Maciej Trojan'


#This code base on Udacity example
import random
from math import *
import scipy.special

class Robot:

    __STEP_SIZE = 1

    def __init__(self, world):
        self.world = world
        self.x = random.random() * self.world.get_width()
        self.y = random.random() * self.world.get_height()
        self.direction = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;

    def sense(self):
        sensors_data = []
        for i in range(len(self.world.get_landmarks())):
            dist = sqrt((self.x - self.world.get_landmarks()[i][0]) ** 2 + (self.y - self.world.get_landmarks()[i][1]) ** 2)
            #dist += random.gauss(0.0, self.sense_noise)
            sensors_data.append(dist)
        return sensors_data

    def get_real_position(self):
        position = {"x":self.x, "y":self.y }
        return position

    def change_direction(self, angle):
        self.direction = (self.direction + float(angle)) % (2 * pi) #+ random.gauss(0.0, self.turn_noise)

    def get_direction(self):
        return self.direction

    def move_forward(self):
        # move, and add randomness to the motion command
        dist = float(self.__STEP_SIZE) + random.gauss(0.0, self.forward_noise)

        self.x = (self.x + (cos(self.direction) * dist)) % self.world.get_width()
        self.y = (self.y + (sin(self.direction) * dist)) % self.world.get_height()
        print self


    #Method from Udacity example.
    def Gaussian(self, mu, sigma, x):

        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((x - mu) ** 2) / ((sigma ** 2) * 2.0)) / (sqrt(2.0 * pi) *sigma)

    #Method from Udacity example.
    def measurement_prob(self, measurement):
        return
    # calculates how likely a measurement should be
    #    prob = 1.0;
    #    for i in range(len(landmarks)):
    #        dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
    #        prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
    #    return prob


    def __str__(self):
        return '[x=%.6s y=%.6s direction=%.6s]' % (str(self.x), str(self.y), str(self.direction))