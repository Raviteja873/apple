import numpy as np
from PIL import Image

array = np.ones((100, 100, 3), dtype=np.uint8) * 255
img = Image.fromarray(array)
img.show()
