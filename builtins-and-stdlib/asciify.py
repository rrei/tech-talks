"""Modified from https://www.geeksforgeeks.org/converting-image-ascii-image-python/"""
import numpy as np
from PIL import Image

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/
grayscale10 = "@%#*+=-:. "
grayscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def convert(filepath, cols=150, font_aspect=2 / 3, grayscale=grayscale70):
    image = Image.open(filepath).convert("L")
    tile_width = image.width // cols
    tile_height = int(tile_width / font_aspect)
    tile_cols = image.width // tile_width
    tile_rows = image.height // tile_height
    lines = []
    for row in range(tile_rows):
        tile_top = row * tile_height
        tile_bottom = tile_top + tile_height
        line = []
        for col in range(tile_cols):
            tile_left = col * tile_width
            tile_right = tile_left + tile_width
            tile = image.crop((tile_left, tile_top, tile_right, tile_bottom))
            tile_luminance = int(get_average_luminance(tile))
            tile_char = grayscale[int(tile_luminance / 255 * (len(grayscale) - 1))]
            line.append(tile_char)
        lines.append(line)
    return "\n".join("".join(line) for line in lines)


def get_average_luminance(image):
    array = np.array(image)
    w, h = array.shape
    return np.average(array.reshape(w * h))
