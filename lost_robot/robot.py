__author__ = 'Paweł Rychły, Maciej Trojan'


#This code base on Udacity example
import random
from math import *

class robot:
    def __init__(self, world):
        self.world = world
        self.x = random.random() * self.world.get_with()
        self.y = random.random() * self.world.get_height()
        self.orientation = random.random() * 2.0 * pi

    def sense(self):
        #This method return an array of data from sensors. The noise is expected
        sensors_data = []
        return sensors_data

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
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))