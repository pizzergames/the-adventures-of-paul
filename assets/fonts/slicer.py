import image_slicer
import os

os.chdir(os.path.split(__file__)[0])

image_slicer.slice('med\\white\\main.png', 38, 16)
