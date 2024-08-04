''' Training and evaluating the model using the DataLoader (deepfashion_loader.py) '''

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
from fashion_model import FashionModel
from deepfashion_loader import DeepFashionDataset

# Load Dataset
annotations_file = 'deepfashion/list_attr_img_fixed.txt'
img_dir = 'deepfashion/img'
transform = transforms.Compose([transforms.Resize((128, 128)), transforms.ToTensor()])
dataset = DeepFashionDataset(img_dir, annotations_file, transform=transform)
data_loader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)

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

# Define Model
model = FashionModel()
criterion_category = nn.CrossEntropyLoss()
criterion_attribute = nn.BCEWithLogitsLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training Loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, (category_labels, attribute_labels) in data_loader:
        optimizer.zero_grad()
        category_output, attribute_output = model(images)
        
        # Compute category loss
        category_loss = criterion_category(category_output, category_labels)
        
        # Compute attribute loss
        attribute_loss = criterion_attribute(attribute_output, attribute_labels)
        
        # Combine losses
        loss = category_loss + attribute_loss
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(data_loader)}")

print("Training Finished")

# Evaluation
model.eval()
correct_categories = 0
total_samples = 0
total_attribute_loss = 0.0

with torch.no_grad():
    for images, (category_labels, attribute_labels) in data_loader:
        category_output, attribute_output = model(images)
        
        # Evaluate category predictions
        _, predicted_categories = torch.max(category_output.data, 1)
        total_samples += category_labels.size(0)
        correct_categories += (predicted_categories == category_labels).sum().item()
        
        # Compute attribute loss for evaluation
        attribute_loss = criterion_attribute(attribute_output, attribute_labels)
        total_attribute_loss += attribute_loss.item()

category_accuracy = 100 * correct_categories / total_samples
average_attribute_loss = total_attribute_loss / len(data_loader)

print(f"Category Accuracy: {category_accuracy}%")
print(f"Average Attribute Loss: {average_attribute_loss}")


