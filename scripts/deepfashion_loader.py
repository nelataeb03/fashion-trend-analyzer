''' Script to verify that deepfashion dataset is properly loaded,
preprocessed, and ready for training a machine learning model. '''

import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch
from PIL import Image

class DeepFashionDataset(Dataset):
    def __init__(self, root_dir, category_file, attribute_file, transform=None):
        self.root_dir = root_dir
        self.category_file = category_file
        self.attribute_file = attribute_file
        self.transform = transform
        self.img_labels = self._load_annotations()

    def _load_annotations(self):
        category_labels = {}
        with open(self.category_file, 'r') as f:
            lines = f.readlines()[2:]  # Skip the first two header lines
            for line in lines:
                parts = line.strip().split()
                img_path = parts[0]
                category = int(parts[1])
                category_labels[img_path] = category

        img_labels = []
        with open(self.attribute_file, 'r') as f:
            lines = f.readlines()[2:]  # Skip the first two header lines
            for line in lines:
                parts = line.strip().split()
                img_path = parts[0]
                attributes = [int(attr) for attr in parts[1:]]
                category = category_labels.get(img_path, -1)  # Get category or -1 if not found
                img_labels.append((img_path, category, attributes))
        return img_labels

    def __len__(self):
        return len(self.img_labels)
    
    def __getitem__(self, idx):
        img_path, category, attributes = self.img_labels[idx]
        full_img_path = os.path.join(self.root_dir, img_path)
        if not os.path.exists(full_img_path):
            print(f"FileNotFoundError: Image not found at {full_img_path}")
        image = Image.open(full_img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        category = torch.tensor(category)  # Convert category to tensor
        attributes = torch.tensor(attributes)  # Convert attributes to tensor
        return image, category, attributes
    
if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    dataset = DeepFashionDataset(
        root_dir='deepfashion/img',
        category_file='deepfashion/list_category_img_fixed.txt',
        attribute_file='deepfashion/list_attr_img_fixed.txt',
        transform=transform
    )

    data_loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

    # Iterate through the DataLoader
    for images, categories, attributes in data_loader:
        print(images.shape, categories.shape, attributes.shape)
