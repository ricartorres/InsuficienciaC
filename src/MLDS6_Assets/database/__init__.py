import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi # type: ignore
import shutil
import re

def separateImages(originalPath,targetPath):
  """
  Given a target path, separates the images by class in a target directory

  Parameters:
  ----------
    originalPath (str): Source path of the images
    targetPath (str): Desgtiny path to the images separated by classes
  """
  pattern = re.compile(r'MLDS2_Project_Data[/\\]([^/\\]+)[/\\]([^/\\]+)$')
  m = pattern.search(targetPath)
  s1 , s2 = m.groups()

  mapper_path = {
      'Normal' : 'NORMAL',
      'bacterialPneumonia' : 'PNEUMONIA',
      'virusPneumonia' : 'PNEUMONIA'
  }

  originPath = originalPath+f'/{s1}/{mapper_path[s2]}'

  mapper = {
      'bacterialPneumonia' : 'bacteria',
      'virusPneumonia' : 'virus'
  }

  if mapper_path[s2]=='NORMAL':
    for item in os.listdir(originPath):
        s = os.path.join(originPath, item)
        d = os.path.join(targetPath, item)
        shutil.copy2(s, d)
  else:
    for item in os.listdir(originPath):
      if mapper[s2] in item:
        s = os.path.join(originPath, item)
        d = os.path.join(targetPath, item)
        shutil.copy2(s, d)
  print(f'Copied files to {targetPath}')

def createDirectoryWithSubdirs(base_dir, subdirs):
    """
    Given a base dir, creates a set of subdirs inside of it

    Parameters:
    ----------
    base_dir (str): Path of the base directory that is wanted to be created
    subdirs (str): Name of the subdirectories that are wanted to be created inside the base directory

    Returns:
    ----------
        List of path names of the created directories (List of str)

    """
    os.makedirs(base_dir, exist_ok=True)
    dirs = []
    for subdir in subdirs:
        path = os.path.join(base_dir, subdir)
        os.makedirs(path, exist_ok=True)
        dirs.append(path)
        print(f"Directory created: {path}")
    return dirs

def deleteDirectoryAndContents(directory):
    """
    Deletes a directory and all its contents (files and subdirectories).

    Parameters:
    ----------
    directory (str): The path to the directory to delete.
    """
    try:
        # Delete the directory and its contents
        shutil.rmtree(directory)
        print(f"Deleted directory and all contents: {directory}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied: {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")


def authenticateKaggle(kaggle_json_path="~/.kaggle/kaggle.json"):
    """
    Authenticates the Kaggle API using the kaggle.json file.

    Parameters:
    ----------
    kaggle_json_path : str, optional
        The path to the Kaggle API credentials file (default is "~/.kaggle/kaggle.json").
    
    Returns:
    -------
    KaggleApi
        An authenticated instance of the Kaggle API.
    """
    kaggle_json_path = os.path.expanduser(kaggle_json_path)
    
    if not os.path.exists(kaggle_json_path):
        raise FileNotFoundError(f"Kaggle authentication file not found at {kaggle_json_path}. "
                                f"Please download the 'kaggle.json' file from https://www.kaggle.com/docs/api "
                                f"and place it in this directory.")
    
    with open(kaggle_json_path, "r") as f:
        credentials = json.load(f)
    
    # Set up the Kaggle API environment
    os.environ['KAGGLE_USERNAME'] = credentials['username']
    os.environ['KAGGLE_KEY'] = credentials['key']
    
    # Authenticate and return the API instance
    api = KaggleApi()
    api.authenticate()
    print("Authenticated with Kaggle successfully.")
    return api


def downloadUnzipDataset(api, dataset_url, download_path="./datasets"):
    """
    Downloads and unzips a Kaggle dataset given its URL.

    Parameters:
    ----------
    api : KaggleApi
        An authenticated instance of the Kaggle API.
    dataset_url : str
        The URL of the Kaggle dataset (e.g., "https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia").
    download_path : str, optional
        The directory to download the dataset into (default is "./datasets").
    
    Returns:
    -------
    None
    """
    try:
        dataset_slug = dataset_url.split("datasets/")[1].strip("/")
    except IndexError:
        raise ValueError("Invalid Kaggle dataset URL. Ensure it includes '/datasets/'.")
    
    os.makedirs(download_path, exist_ok=True)

    # Download and unzip dataset
    print(f"Downloading and unzipping dataset: {dataset_slug} to {download_path}...\n")
    api.dataset_download_files(dataset_slug, path=download_path, unzip=True, quiet=False)
    print(f"Dataset '{dataset_slug}' downloaded and unzipped to '{download_path}'.\n")