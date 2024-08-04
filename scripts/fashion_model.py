''' Creating a neural network model for fashion image classification '''

import torch
import torch.nn as nn
import torch.nn.functional as F

class FashionModel(nn.Module):
    def __init__(self):
        super(FashionModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(64 * 32 * 32, 128)  # Adjust dimensions as necessary
        self.fc2 = nn.Linear(128, 50)  # 50 categories
        self.fc3 = nn.Linear(128, 1000)  # 1000 attributes

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 32 * 32)  # Adjust dimensions as necessary
        x = F.relu(self.fc1(x))
        category_output = self.fc2(x)
        attribute_output = self.fc3(x)
        return category_output, attribute_output


