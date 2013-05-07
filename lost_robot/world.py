__author__ = 'Pawel Rychly, Maciej Trojan'

from robot import Robot
import time
import random

class World:

    __NUM_OF_LANDMARKS = 3

    def __init__(self, width, height):
        self.is_stopped = False
        self.width = width
        self.height = height
        self.landmarks = []
        for i in range(self.__NUM_OF_LANDMARKS):
            x = random.random() * self.width
            y = random.random() * self.height
            landmark = {"x": x, "y":y }
            self.landmarks.append(landmark)

        self.robot = Robot(self, 1, 0.1, 50)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_landmarks(self):
        return self.landmarks

    def add_landmark(self, landmark):
        self.landmarks.append(landmark)

    def stop(self):
        self.is_stopped = True

    def run(self):
        self.robot.move_forward()

    def get_robot(self):
        return self.robot
