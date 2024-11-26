import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi # type: ignore
import shutil

def deleteDirectoryAndContents(directory):
    """
    Deletes a directory and all its contents (files and subdirectories).

    Parameters:
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