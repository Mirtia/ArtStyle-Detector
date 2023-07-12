import os

import matplotlib.pyplot
from colorthief import ColorThief

def rgb_to_hex(rgb: tuple) -> str:
    """
    The function `rgb_to_hex` takes a tuple representing an RGB color and returns the corresponding
    hexadecimal color code.
    
    :param rgb: The `rgb` parameter is a tuple containing three integers representing the red, green,
    and blue values of a color
    :type rgb: tuple
    :return: The function `rgb_to_hex` returns a string representation of the RGB color in hexadecimal
    format.
    """
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def hex_to_rgb(hex: str) -> tuple:
    """
    The function `hex_to_rgb` takes a hexadecimal color code as input and returns the corresponding RGB
    values as a tuple.
    
    :param hex: A string representing a hexadecimal color code
    :type hex: str
    :return: The function `hex_to_rgb` returns a tuple containing the RGB values corresponding to the
    given hexadecimal color code.
    """
    hex = hex.lstrip("#")
    return tuple([int(hex[i : i + 2], 16) for i in range(0, len(hex), 2)])

def get_color_console(rgb: tuple) -> str:
    """
    The function `get_color_console` returns a string that represents a console color based on the given
    RGB values.
    
    :param rgb: The `rgb` parameter is a tuple that represents the RGB values of a color. It should
    contain three integers, where the first integer represents the red value, the second integer
    represents the green value, and the third integer represents the blue value
    :type rgb: tuple
    :return: a string that represents a console color using the RGB values provided.
    """
    return f"\033[48:2::{rgb[0]}:{rgb[1]}:{rgb[2]}m \033[49m"

def print_colors_to_console(hex_list: list) -> str:
    """
    The function takes a list of hexadecimal color codes and returns a string with each color code
    printed on a new line.
    
    :param hex_list: A list of hexadecimal color codes
    :type hex_list: list
    :return: a string that contains all the elements of the input list, separated by newlines.
    """
    return "\n".join(hex_list)

def plot_colors(hex_list: list, dominant_color: tuple, side: int, output:str):
    """
    The function `plot_colors` takes a list of hexadecimal color codes, a dominant color as a tuple, a
    side length for the color patches, and an output directory path, and plots the colors as rectangles
    in a palette, saves the plot as an image file with the dominant color as the filename, and displays
    the plot.
    
    :param hex_list: The `hex_list` parameter is a list of hexadecimal color codes. These codes
    represent the colors that will be plotted in the palette
    :type hex_list: list
    :param dominant_color: The `dominant_color` parameter is a tuple representing the RGB values of the
    dominant color in the `hex_list`
    :type dominant_color: tuple
    :param side: The parameter "side" represents the length of each side of the rectangle that
    represents a color in the plot. It is used to determine the size of each color patch in the plot
    :type side: int
    :param output: The `output` parameter is a string that specifies the directory where the output
    image file will be saved
    :type output: str
    """
    figure = matplotlib.pyplot.figure()
    palette = figure.add_subplot()
    for i in range(len(hex_list)):
        palette.add_patch(matplotlib.patches.Rectangle((side * i, 0), side, side, color=hex_list[i]))
    matplotlib.pyplot.xlim([0, len(hex_list) * side])
    matplotlib.pyplot.ylim([0, side])
    matplotlib.pyplot.axis("off")
    matplotlib.pyplot.tight_layout()

    os.makedirs(output, exist_ok=True)
    matplotlib.pyplot.savefig(os.path.join(output, rgb_to_hex(dominant_color) + ".jpg" ))
    matplotlib.pyplot.show()

# Still not sure how to use this code, may `sort` images by their color scheme
# Example usage:
# color_thief = ColorThief("tests/monet_impressionism.jpg")
# dominant_color = color_thief.get_color(quality=1)
# palette = color_thief.get_palette(color_count=6)
# hex_palette = [rgb_to_hex(color) for color in palette]
# plot_colors(hex_palette, dominant_color, side=50, output="output/palette")