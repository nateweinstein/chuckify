# Chuck Close Image Transformer

## Project Overview
This project transforms regular images into a style reminiscent of Chuck Close's paintings. It utilizes a grid-based approach to process each segment of the image, applying a unique transformation inspired by Chuck Close's art style.  Big h/t to Scott Blake for providing the tiles: http://www.barcodeart.com/artwork/portraits/chuck_close/index.html

## Features
- Image transformation into Chuck Close style.
- Customizable grid size and orientation (horizontal or diagonal).
- Use of a collection of Chuck Close-style tiles for transformation.
- Interactive user inputs for custom configurations.

## Installation
Ensure that Miniconda is installed on your system. Clone the repository and set up a virtual environment.

```bash
# Clone the repository
git clone [Your Repository URL]

# Navigate to the project directory
cd [Your Project Directory]

# Create a Conda environment
conda create --name chuckclose-env python=3.9

# Activate the environment
conda activate chuckclose-env

# Install dependencies
conda install --file requirements.txt


## Usage
Run the script from the terminal. The script will prompt you for various inputs, such as the file name, grid orientation, number of rows, and output directory. You can either enter your custom values or press Enter to use the default values.

# Run the script
python chuckify.py


## Interactive Inputs
File Name: Name of the image file to be transformed. Default is 'reddit_bay_bridge.jpeg'.
Orientation: Grid orientation ('horizontal' or 'diagonal'). Default is 'horizontal'.
Number of Rows: Number of rows in the grid. Default is 80.
Output Directory: Directory where the transformed image will be saved. Default is 'closifieds'.


# Example
Enter the file name (default: reddit_bay_bridge.jpeg): 
Enter orientation ('horizontal' or 'diagonal') (default: horizontal): diagonal
Enter the number of rows (default: 80): 100
Enter the output directory (default: closifieds): my_output_folder


## Contributing
Contributions to this project are welcome. Please ensure to update tests as appropriate.

## License
MIT License