import torch
import requests
import os

def download_dataset(url, save_dir="data/raw/"):
    """download url to destination"""
    r = requests.get(url)
    assert r.ok, "Request failed w/error {TODO}"
    with open(os.path.join(save_dir, "dataset.zip"), 'wb') as fp:
        fp.write(r.content)



        