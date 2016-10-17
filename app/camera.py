from time import time

from render import PressureMap


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.pressuremap = PressureMap()

    def get_frame(self):
        return self.pressuremap.show_pressuremap()
