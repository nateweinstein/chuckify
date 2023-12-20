import os
import pickle
import datetime
import webbrowser
from helpers.chuck_close_transformer import ChuckCloseTransformer
from helpers._create_tile_map import create_color_mapping_dict

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (default: {default}): ").strip()
    return user_input if user_input else default

# Default configurations
DEFAULT_FILE_NAME = 'reddit_bay_bridge.jpeg'
DEFAULT_ORIENTATION = 'horizontal'  # or 'diagonal'
DEFAULT_ROWS = 80
DEFAULT_OUTPUT_DIR = 'closifieds'
DEFAULT_NUMBER_OF_NEIGHBORS = 20

# User inputs with defaults
FILE_NAME = get_user_input("Enter the file name", DEFAULT_FILE_NAME)
ORIENTATION = get_user_input("Enter orientation ('horizontal' or 'diagonal')", DEFAULT_ORIENTATION)
ROWS = get_user_input("Enter the number of rows", DEFAULT_ROWS)
NUMBER_OF_NEIGHBORS = get_user_input("Enter the number of color neighbors", DEFAULT_ROWS)
OUTPUT_DIR = get_user_input("Enter the output directory", DEFAULT_OUTPUT_DIR)

print("Let's chuckify this...")
# Check if the tile color mapping file exists
color_mapping_file = 'tile_color_map.pkl'
if not os.path.exists(color_mapping_file):
    print("...creating tile color mapping")
    tiles_folder = 'chuck_tiles'
    create_color_mapping_dict(tiles_folder, color_mapping_file)

# Load the color mapping dictionary
with open(color_mapping_file, 'rb') as f:
    color_mapping_dict = pickle.load(f)

# Create a unique output filename
input_name = os.path.splitext(FILE_NAME)[0]
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"{input_name}_{ROWS}_{timestamp}.png"
output_path = os.path.join(OUTPUT_DIR, output_filename)

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Perform the transformation
print("... starting transformation")
transformer = ChuckCloseTransformer(FILE_NAME, ROWS, ORIENTATION, NUMBER_OF_NEIGHBORS)
transformer.transform_image(color_mapping_dict, output_path)

print(f"Image complete:::: {output_filename}!!!")
# Open the output file
# webbrowser.open(output_path)
