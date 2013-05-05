__author__ = 'Pawel Rychly, Maciej Trojan'


#This code base on Udacity example
import random
from math import *

class Robot:

    __STEP_SIZE = 5

    def __init__(self, world):
        self.world = world
        self.x = random.random() * self.world.get_width()
        self.y = random.random() * self.world.get_height()
        self.orientation = random.random() * 2.0 * pi
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

    def turn(self, angle):
        self.orientation = (self.orientation + float(angle) + random.gauss(0.0, self.turn_noise)) % 2 * pi

    def move_forward(self):
        # move, and add randomness to the motion command
        dist = float(self.__STEP_SIZE) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(self.orientation) * dist) % self.world.get_width()
        y = self.y + (sin(self.orientation) * dist) % self.world.get_height()
        print self


    #Method from Udacity example.
    def Gaussian(self, mu, sigma, x):

        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

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
        return '[x=%.6s y=%.6s orientation=%.6s]' % (str(self.x), str(self.y), str(self.orientation))