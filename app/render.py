from skimage.io import imread
import numpy as np
import seaborn as sns
from skimage.filters import gaussian
from pylab import *

from io import BytesIO

import scipy.misc

import time

class PressureMap():
    
    def __init__(self):
        self.img = (imread("body.png"))
        self.img[self.img < 0.25] = 0
        self.img[self.img > 0.75] = 1
        self.img[(self.img > 0.25) & (self.img < 0.75)] = 0.5


        self.render_img = self.img.copy()

    def plot_heatmap(self,pressure_vals, sigma=25., shape=(568,367)):
        heatmap = zeros(shape)
        
        # map sensor to position in the heatmap
        positions = {"head" : (221,79),
                     "shoulder_left":(189,150),
                     "shoulder_right":(255,150),
                     "bottom_left" : (190,290),
                     "bottom_right" : (250,290),
                     "leg_left" : (188,421),
                     "leg_right" : (256,421),
                     "foot_left" : (194,509),
                     "foot_right" : (256, 509)
                    }
        
        sensor2pos = {0 : ("head",),
                      1: ("shoulder_left", "shoulder_right"),
                      2: ("bottom_left","bottom_right"),
                      3: ("leg_left", "leg_right"),
                      4: ("foot_left", "foot_right"),
                      5: (),
                     }
        
        for i in sensor2pos.keys():
            for sensor in sensor2pos[i]:
                p = positions[sensor]
                newpos = zeros((568,367))
                newpos[p[1], p[0]] = 1
                heatmap_addition = gaussian(newpos, sigma)
                heatmap += heatmap_addition / heatmap_addition.max() * pressure_vals[i]
                
        return heatmap

    def show_pressuremap(self):
        self.render_img[:] = self.img[:]

        heat = 0.8 * (self.plot_heatmap(np.random.uniform(0, 1, size = (6,))))
        self.render_img[self.render_img == 0.5] = heat[self.render_img == 0.5]
        
        pil_buffer = scipy.misc.toimage(self.render_img, cmin=0.0, cmax=1.0)
        b = BytesIO()
        pil_buffer.save(b, "png")

        return b.getvalue()

if __name__ == '__main__':
    pm = PressureMap()
    tic = time.time()
    for i in range(10):
        print(i)
        img = pm.show_pressuremap()
    toc = time.time()
    print("Average time per frame: ", (toc-tic)/10)

    with open("testimg.png", "wb") as f:
        f.write(img)
