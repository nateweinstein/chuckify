# Example usage script
from chuck_close_transformer import ChuckCloseTransformer

# Load Chuck Close tile images
# TODO: Load tile images into a list

transformer = ChuckCloseTransformer('path/to/input/image.jpg', 10, 'horizontal')
transformer.transform(tile_images, 'path/to/output/image.png', (1920, 1080))
