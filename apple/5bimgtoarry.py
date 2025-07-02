from PIL import Image
import numpy as np

img = Image.open("white.png")
array = np.array(img)
print(array)
