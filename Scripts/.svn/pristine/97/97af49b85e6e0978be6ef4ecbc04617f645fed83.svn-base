#a script to create RGB and RGBA bitmap
from PIL import Image
from itertools import product
colors_per_dim = 100
gradient = ""
for i, j in product(range(colors_per_dim), range(colors_per_dim)):
    red = int(255*i/colors_per_dim)
    blue = int(255*j/colors_per_dim)
    alpha = int(255*j/colors_per_dim)
    # gradient += f"{red:02X}00{blue:02X}" #for RGB
    gradient += f"{red:02X}00{blue:02X}{alpha:02X}" #for RGBA
# im = Image.frombytes("RGB", (colors_per_dim, colors_per_dim), bytes.fromhex(gradient)) #for RGB
im = Image.frombytes("RGBA", (colors_per_dim, colors_per_dim), bytes.fromhex(gradient))
im.save("red-blue1.bmp")