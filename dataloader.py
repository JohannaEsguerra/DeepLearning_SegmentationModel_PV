import torch #Import the main PyTorch library, which is used for building and training neural networks.
import torch.nn as nn #Import the neural network module from PyTorch, which contains building blocks for neural networks.
import torch.optim as optim  # Import the optimization module from PyTorch, which contains algorithms for optimizing neural networks.
import torchvision.transforms as transforms  #  Import the transforms module from torchvision, which is used for image transformations.
from torch.utils.data import Dataset, DataLoader # Import classes for creating custom datasets and loading data in batches.
from PIL import Image # Import the Python Imaging Library for image processing.
import os # Import the operating system module for interacting with the file system.
import numpy as np

# Custom dataset class
class SolarPanelSegmentationDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        
        self.image_filenames = sorted(os.listdir(image_dir)) #[:2]
        self.mask_filenames = sorted(os.listdir(mask_dir))#[:2]

        # Ensure the number of images and masks are the same
        assert len(self.image_filenames) == len(self.mask_filenames), "Mismatch in number of images and masks"

        # Check filenames for direct correspondence
        for img_file, mask_file in zip(self.image_filenames, self.mask_filenames):
            assert img_file == mask_file, f"Image and mask filenames do not match: {img_file} != {mask_file}"

    def __len__(self):
        return len(self.image_filenames)

    def __getitem__(self, idx):
        image_path = os.path.join(self.image_dir, self.image_filenames[idx])
        mask_path = os.path.join(self.mask_dir, self.mask_filenames[idx])
        
        image = Image.open(image_path).convert("RGB")
        mask = Image.open(mask_path).convert("L")
        mask = mask.point(lambda p: 255 if p > 0 else 0)
        mask = mask.convert("1")
        
        if self.transform:
            image = self.transform(image)
            mask = self.transform(mask)
        
        return image, mask, self.image_filenames[idx]


