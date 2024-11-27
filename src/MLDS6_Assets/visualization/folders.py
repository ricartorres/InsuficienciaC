import os

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