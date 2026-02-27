import torch
import joblib
from models.ecg_model import ECGTransformer

# === Load shared label encoder ===
label_encoder = joblib.load("weights/shared_label_encoder.pkl")
num_users = len(label_encoder.classes_)
print("✅ Shared encoder loaded:", num_users, "classes")

# === Load model ===
model = ECGTransformer(num_classes=num_users)
state_dict = torch.load("weights/transformer_model.pth", map_location="cpu")

# Check classifier head shape
classifier_weights = {k: v.shape for k, v in state_dict.items() if "classifier" in k}
print("🔍 Output layer shapes:")
for name, shape in classifier_weights.items():
    print(f"{name}: {shape}")

# Optional: verify class name at index 0 and 43
print("🧠 Class at index 0:", label_encoder.inverse_transform([0])[0])
print("🧠 Class at index 43:", label_encoder.inverse_transform([43])[0])
