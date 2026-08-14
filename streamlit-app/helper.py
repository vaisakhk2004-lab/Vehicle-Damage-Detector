import torch
import torch.nn as nn
from torchvision import transforms,models
from pathlib import Path
from PIL import Image
from io import BytesIO
model=None
MODEL_PATH = Path(__file__).resolve().parent / "model" / "model.pth"
print(MODEL_PATH)
class CarClassifierUsingResNet(nn.Module):

    def __init__(self, num_of_class, dropout=0.4):
        super().__init__()
        self.network = models.resnet50(weights='DEFAULT')
        for params in self.network.parameters():
            params.requires_grad = False
        for param in self.network.layer4.parameters():
            param.requires_grad = True
        in_features = self.network.fc.in_features
        self.network.fc = nn.Sequential(nn.Dropout(dropout), nn.Linear(in_features, num_of_class))

    def forward(self, x):
        x = self.network(x)
        return x
classes=['F_Breakage', 'F_Crushed', 'F_Normal', 'R_Breakage', 'R_Crushed', 'R_Normal']

def predict_damage(image_bytes):
    global model
    image=Image.open(BytesIO(image_bytes)).convert('RGB')
    transform = transforms.Compose([transforms.Resize((224,224)),transforms.ToTensor(),transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])])
    tensor_image=transform(image).unsqueeze(0)
    if model is None:
       model = CarClassifierUsingResNet(6)
       model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
       model.eval()
    with torch.no_grad():
        output=model(tensor_image)
        _,predicted=torch.max(output,1)
        return classes[predicted.item()]