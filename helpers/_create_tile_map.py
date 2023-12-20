# File: /helpers/_create_tile_map.py
import os
import pickle
from PIL import Image
import numpy as np

def calculate_average_color(image):
    """Calculate the average color of the given image."""
    np_image = np.array(image)
    mean_color = np_image.mean(axis=(0, 1))
    return tuple(mean_color)

def create_color_mapping_dict(tiles_folder, output_file):
    """Create a dictionary mapping the average color of each tile to the tile image and save it."""
    color_mapping = {}
    for tile_name in os.listdir(tiles_folder):
        tile_path = os.path.join(tiles_folder, tile_name)
        try:
            tile_image = Image.open(tile_path)
            avg_color = calculate_average_color(tile_image)
            color_mapping[avg_color] = tile_image
        except IOError:
            print(f"Error in loading tile image: {tile_name}")

    with open(output_file, 'wb') as f:
        pickle.dump(color_mapping, f)

    return color_mapping
