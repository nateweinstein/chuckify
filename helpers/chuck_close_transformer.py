# File: chuck_close_transformer.py
from PIL import Image
import numpy as np
import random
from tqdm import tqdm


class TileProcessor:
    def __init__(self, tile_images):
        self.tile_images = tile_images

    def process_tile(self, cell_image):
        # TODO: Implement the logic to process each cell using the Chuck Close tiles
        pass

class ChuckCloseTransformer:
    def __init__(self, input_image_path, rows, orientation, number_of_neighbors):
        self.image = self._load_image(input_image_path)
        self.rows = rows
        self.orientation = orientation
        self.number_of_neighbors = number_of_neighbors
        self.tile_processor = None
        self.grid = []

    def _load_image(self, file_path):
        try:
            image = Image.open(file_path)
            return image
        except IOError:
            print("Error in loading the image")
            return None

    def _create_grid(self):
        if self.image is None:
            return

        img_width, img_height = self.image.size
        cell_size = img_height // self.rows

        if self.orientation == 'horizontal':
            columns = img_width // cell_size
        elif self.orientation == 'diagonal':
            columns = (img_width // cell_size) + self.rows

        for row in range(self.rows):
            row_offset = (cell_size // 2) * (row % 2)
            for col in range(columns):
                top_left = (max(col * cell_size - row_offset, 0), row * cell_size)
                bottom_right = (min((col + 1) * cell_size - row_offset, img_width), (row + 1) * cell_size)
                self.grid.append((top_left, bottom_right))

    def _calculate_average_color(self, cell_coordinates):
        """Calculate the average color of a given cell."""
        cell_image = self.image.crop((cell_coordinates[0][0], cell_coordinates[0][1], 
                                      cell_coordinates[1][0], cell_coordinates[1][1]))
        np_image = np.array(cell_image)
        mean_color = np_image.mean(axis=(0, 1))
        return tuple(mean_color)

    def _find_closest_tile(self, avg_color):
        """Find a random tile from the self.number_of_neighbors closest average color tiles."""
        # Calculate color differences and sort
        color_differences = {tile_avg_color: np.linalg.norm(np.array(avg_color) - np.array(tile_avg_color))
                             for tile_avg_color in self.tile_processor.keys()}
        sorted_color_keys = sorted(color_differences, key=color_differences.get)

        # Select from the top NUMBER_OF_NEIGHBORS closest color keys
        if len(sorted_color_keys) > self.number_of_neighbors:
            selected_color_key = random.choice(sorted_color_keys[:self.number_of_neighbors])
        else:
            selected_color_key = random.choice(sorted_color_keys)

        return self.tile_processor[selected_color_key]

    def _process_cells(self):
        processed_image = Image.new('RGB', self.image.size)
        total_cells = len(self.grid)

        # Use tqdm to create a progress bar
        for cell in tqdm(self.grid, desc="Processing cells", total=total_cells):
            avg_color = self._calculate_average_color(cell)
            selected_tile = self._find_closest_tile(avg_color)
            processed_image.paste(selected_tile, (cell[0][0], cell[0][1]))

        return processed_image


    def transform_image(self, tile_images, output_image_path, output_width=1920):
        if self.image is None:
            return

        self._create_grid()
        self.tile_processor = tile_images

        processed_image = self._process_cells()

        # Calculate the new height to maintain the aspect ratio
        original_width, original_height = self.image.size
        aspect_ratio = original_height / original_width
        new_height = int(output_width * aspect_ratio)

        # Resize the image
        processed_image = processed_image.resize((output_width, new_height), Image.Resampling.LANCZOS)
        processed_image.save(output_image_path)