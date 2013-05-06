__author__ = 'Pawel Rychly, Maciej Trojan'

from robot import Robot
import time

class World:

    def __init__(self, width, height):
        self.is_stopped = False
        self.width = width
        self.height = height
        self.landmarks = []
        self.particles = []
        self.robot = Robot(self)

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
