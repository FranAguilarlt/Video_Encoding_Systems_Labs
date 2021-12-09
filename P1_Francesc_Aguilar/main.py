from typing import Set

from PIL import Image
import numpy as np
import rgb2yuv, yuv2rgb, rl_encoding, dct
import rl_decoding
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

myImage = Image.open("/home/fran/Documents/rango.jpg");

r, g, b = myImage.getpixel((100, 100))

yuv = rgb2yuv.RGB2YUV(r, g, b)

print("\nThe original value of the pixel : ", (r, g, b))
print("\nThe YUV value of the pixel", yuv)

rgb = yuv2rgb.YUV2RGB(yuv)

print("\nThe inverse operation", rgb)

original_message = "AAEEIOOOOUU"
encoded_message = rl_encoding.encode_message(original_message)
decoded_message = rl_decoding.decode(encoded_message)

print("\n\nThe Original text is: [" + original_message + "]")

print("\n The Encoded message is: [" + encoded_message + "]")

print("\n The Decoded message is: [" + decoded_message + "]")

M = np.array([[255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ],
              [255, 255, 255, 255, 255, 255, 255, 255, ], ])

aaa = dct.dct(M)

plt.imshow(aaa, norm=LogNorm())
plt.colorbar()
plt.show()
