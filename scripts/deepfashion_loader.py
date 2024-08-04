import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import torch
from PIL import Image

class DeepFashionDataset(Dataset):
    def __init__(self, root_dir, annotations_file, transform=None):
        self.root_dir = root_dir
        self.annotations_file = annotations_file
        self.transform = transform
        self.img_labels = self._load_annotations()

    def _load_annotations(self):
        img_labels = []
        with open(self.annotations_file, 'r') as f:
            lines = f.readlines()[2:]  # Skip the first two header lines
            for line in lines:
                parts = line.strip().split()
                img_path = parts[0]
                attributes = [int(attr) for attr in parts[1:]]
                img_labels.append((img_path, attributes))
        return img_labels

    def __len__(self):
        return len(self.img_labels)
    
    def __getitem__(self, idx):
        img_path, labels = self.img_labels[idx]
        full_img_path = os.path.join(self.root_dir, img_path)
        if not os.path.exists(full_img_path):
            print(f"FileNotFoundError: Image not found at {full_img_path}")
        image = Image.open(full_img_path).convert("RGB")
        if self.transform:
            image = self.transform(image)
        labels = torch.tensor(labels)  # Convert labels to tensor
        return image, labels
    
if __name__ == '__main__':
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    dataset = DeepFashionDataset(
        root_dir='deepfashion/img',
        annotations_file='deepfashion/list_attr_img_fixed.txt',
        transform=transform
    )

    data_loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

    # Iterate through the DataLoader
    for images, labels in data_loader:
        print(images.shape, labels.shape)