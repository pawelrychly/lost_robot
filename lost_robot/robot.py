__author__ = 'Pawel Rychly, Maciej Trojan'


#This code base on Udacity example
import random
from math import *

class Robot:

    __STEP_SIZE = 1

    def __init__(self, world, f_noise = float(0), d_noise = float(0), s_noise = float(0)):
        self.world = world
        self.x = random.random() * self.world.get_width()
        self.y = random.random() * self.world.get_height()
        self.direction = random.random() * 2.0 * pi
        self.forward_noise = f_noise;
        self.direction_noise = d_noise;
        self.sense_noise = s_noise;
        self.probability = 0

    def sense(self):
        sensors_data = []
        landmarks = self.world.get_landmarks()
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i]["x"]) ** 2 + (self.y - landmarks[i]["y"]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            sensors_data.append(dist)
        return sensors_data

    def get_probability(self):
        return self.probability

    def set_probability(self, prob):
        self.probability = prob

    def get_position(self):
        position = {"x":self.x, "y":self.y }
        return position

    def change_direction(self, angle):
        self.direction = (self.direction + float(angle) + random.gauss(0.0, self.direction_noise)) % (2 * pi)

    def get_direction(self):
        return self.direction

    def move_forward(self):
        # move, and add randomness to the motion command
        dist = float(self.__STEP_SIZE) + random.gauss(0.0, self.forward_noise)

        self.x = (self.x + (cos(self.direction) * dist)) % self.world.get_width()
        self.y = (self.y + (sin(self.direction) * dist)) % self.world.get_height()


    def Gaussian(self, mu, sigma, x):
        return exp(- ((x - mu) ** 2) / ((sigma ** 2) * 2.0)) / (sqrt(2.0 * pi) *sigma)

    #Method from Udacity example.
    def measure_probability(self, robot_sense_data):
        probability = float(1)
        landmarks = self.world.get_landmarks()
        for i, landmark in enumerate(landmarks):
            distance = sqrt((self.x - landmark["x"]) ** 2 + (self.y - landmark["y"]) ** 2)
            #print self.sense_noise

            probability *= self.Gaussian(distance, self.sense_noise, robot_sense_data[i])
        return probability


    def __str__(self):
        return '[x=%.6s y=%.6s direction=%.6s]' % (str(self.x), str(self.y), str(self.direction))