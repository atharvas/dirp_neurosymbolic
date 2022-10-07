import numpy as np
import torch
import requests
import os
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as tf
from PIL import Image

def download_dataset(url, save_dir="data/raw/"):
    """download url to destination"""
    r = requests.get(url)
    assert r.ok, "Request failed w/error {TODO}"
    with open(os.path.join(save_dir, "dataset.zip"), 'wb') as fp:
        fp.write(r.content)


def pil_loader(path):
    # open path as file to avoid ResourceWarning (https://github.com/python-pillow/Pillow/issues/835)
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

class VideoLoader(Dataset):
    @staticmethod
    def setup_dataset(video_dir) -> None:
        "Ideally the above steps should happen here."
        pass
    @staticmethod
    def collate_samples(samples_dir, max_seq_len):
        samples = []
        for video in os.listdir(samples_dir):
            sequence = []
            video_dir = os.path.join(samples_dir, video)
            for sample in sorted(os.listdir(video_dir)):
                sequence.append(os.path.join(video_dir, sample))
                if len(sequence) == max_seq_len:
                    samples.append(sequence)
                    sequence = []

            samples.append(sequence)
        return samples

    def __init__(self, frames_dir, max_seq_len=21, image_size=()):
        # TODO
        self.frames_dir = frames_dir
        self.max_seq_len = max_seq_len
        assert os.path.exists(self.frames_dir)

        self.src_transform = tf.Compose([
                  tf.Resize((256, 256)),
                  tf.ToTensor(),
                ])
        
        self.samples = self.collate_samples(self.frames_dir, max_seq_len=self.max_seq_len)

        pass

    def __len__(self):
        return len(self.samples)


    def __getitem__(self, idx):
        """
        returns [seq_len, 3, 256, 256]
        """
        # Load images with PIL

        sequence = self.samples[idx]
        out = torch.zeros(self.max_seq_len, 3, 256, 256)
        for i, img_path in enumerate(sequence):
          img = pil_loader(img_path)
          out[i] = self.src_transform(img)
        
        return out
          


