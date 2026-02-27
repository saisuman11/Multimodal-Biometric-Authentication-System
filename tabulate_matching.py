import joblib
from tabulate import tabulate

# Load the encoders
shared_le = joblib.load("weights/shared_label_encoder.pkl")
ecg_le = joblib.load("weights/ecg_label_encoder.pkl")
fp_le = joblib.load("weights/fingerprint_label_encoder (1).pkl")

# Extract class labels
shared_classes = list(shared_le.classes_)
ecg_classes = list(ecg_le.classes_)
fp_classes = list(fp_le.classes_)

# Quick checks
print("✅ shared_label_encoder contains", len(shared_classes), "users.")
print("✅ ecg_label_encoder contains   ", len(ecg_classes), "users.")
print("✅ fingerprint_label_encoder has", len(fp_classes), "users.")

label_encoder = joblib.load("weights/shared_label_encoder.pkl")

print("Index 9 →", label_encoder.inverse_transform([9])[0])
print("Index 33 →", label_encoder.inverse_transform([33])[0])
print("Expected for user010:", label_encoder.transform(["user010"])[0])
# Check if all encoders have same classes
all_match = (shared_classes == fp_classes)

if all_match:
    print("\n🎉 All three label encoders match perfectly in order and content.\n")
else:
    print("\n❗ Label encoders DO NOT match. Showing mismatches:\n")
    max_len = max(len(shared_classes), len(ecg_classes), len(fp_classes))
    
    rows = []
    for i in range(max_len):
        shared = shared_classes[i] if i < len(shared_classes) else "---"
        ecg = ecg_classes[i] if i < len(ecg_classes) else "---"
        fp = fp_classes[i] if i < len(fp_classes) else "---"
        mismatch = shared != ecg or shared != fp or ecg != fp
        rows.append([i, shared, ecg, fp, "❌" if mismatch else "✅"])

    print(tabulate(rows, headers=["Index", "Shared", "ECG", "Fingerprint", "Match"]))
