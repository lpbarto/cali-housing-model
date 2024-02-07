import torch.nn as nn
import torch.nn.functional as F

class CaliforniaRegressrModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(in_features=8, out_features=18, bias=True)
        self.fc2 = nn.Linear(in_features=18, out_features=18, bias=True)
        self.fc3 = nn.Linear(in_features=18, out_features=12, bias=True)
        self.fc4 = nn.Linear(in_features=12, out_features=1, bias=True)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return self.fc4(x)