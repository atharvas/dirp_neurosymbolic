import torch
import requests
import os
from torch.utils.data import Dataset, DataLoader

def download_dataset(url, save_dir="data/raw/"):
    """download url to destination"""
    r = requests.get(url)
    assert r.ok, "Request failed w/error {TODO}"
    with open(os.path.join(save_dir, "dataset.zip"), 'wb') as fp:
        fp.write(r.content)

class VideoLoader(Dataset):
    @staticmethod
    def setup_dataset(video_dir) -> None:
        "Ideally the above steps should happen here."
        pass
    @staticmethod
    def collate_samples(samples_dir):
        for video in os.listdir(samples_dir):
            print(video)
        return []


    def __init__(self, frames_dir):
        # TODO
        self.frames_dir = frames_dir
        assert os.path.exists(self.frames_dir)

        self.collate_samples(self.frames_dir)
        
        pass

