import numpy as np
from PIL import Image

img = Image.open(r"D:\numPy\numpy_learning\projects\image_as_numbers\sample.png").convert("L")

img_arr = np.array(img)

print(img_arr.shape)
print(img_arr.min())
print(img_arr.max())

flip = np.flip(img_arr, axis=0)

flip_img = Image.fromarray(flip)
flip_img.save("flip.png")

rotated = np.rot90(img_arr, k=1)
rotated_img = Image.fromarray(rotated)
rotated_img.save("rotated.png")

crop = img_arr[50:300, 100:400]
crop_img = Image.fromarray(crop)
crop_img.save("crop_img.png")

img_np = np.array(img).astype(np.float32)
bright = img_np + 40
bright = np.clip(bright, 0, 255).astype(np.uint8)
bright_img = Image.fromarray(bright).save("bright.png")