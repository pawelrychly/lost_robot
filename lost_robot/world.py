__author__ = 'Paweł Rychły, Maciej Trojan'


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.landmarks = []

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_landmarks(self):
        return self.landmarks