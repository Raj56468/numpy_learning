import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load and convert to grayscale
img = Image.open("projects/image_as_numbers/sample.png").convert("L")

# Turn into NumPy array
img_array = np.array(img)

print("Shape:", img_array.shape)
print("Min pixel:", img_array.min())
print("Max pixel:", img_array.max())

plt.imshow(img_array, cmap="gray")
plt.title("Original Image")
plt.show()

brighter = np.clip(img_array + 50, 0, 255)

plt.imshow(brighter, cmap="gray")
plt.title("Brighter Image")
plt.show()

h, w = img_array.shape
crop = img_array[h//4:h*3//4, w//4:w*3//4]

plt.imshow(crop, cmap="gray")
plt.title("Cropped Image")
plt.show()

edges = np.abs(img_array[:, 1:] - img_array[:, :-1])

plt.imshow(edges, cmap="gray")
plt.title("Edge Detection")
plt.show()

