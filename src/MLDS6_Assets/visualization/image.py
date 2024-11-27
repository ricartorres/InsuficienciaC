import matplotlib.pyplot as plt # type: ignore
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