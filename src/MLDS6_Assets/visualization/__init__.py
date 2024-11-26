import matplotlib.pyplot as plt
import os
from PIL import Image # type: ignore

def showImage(path, size=(8, 8), title='Radiografia del conjunto de datos'):
    """
    Displays an image from a specified file path with customizable size and title.

    Parameters:
    path : str
        The file path to the image to be displayed.
    size : tuple, optional
        A tuple specifying the size of the figure in inches (width, height). Default is (8, 8).
    title : str, optional
        The title to be displayed above the image. Default is 'Radiografia del conjunto de datos'.
    """
    img = Image.open(path)
    plt.figure(figsize=size)
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def printTree(directory, indent_level=0):
    """
    Recursively prints the folder tree for the given directory.

    Parameters:
    directory (str): The path of the directory to start the tree.
    indent_level (int): The level of indentation for the current folder.
    """
    try:
        # Print the current directory
        print(' ' * (4 * indent_level) + f'📁 {os.path.basename(directory)}')
        # Iterate over items in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                # Recursively print subdirectory
                printTree(item_path, indent_level + 1)
    except PermissionError:
        print(' ' * (4 * indent_level) + f'🚫 Permission denied: {directory}')
    except FileNotFoundError:
        print(' ' * (4 * indent_level) + f'❓ Directory not found: {directory}')

