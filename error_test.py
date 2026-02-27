import joblib
label_encoder = joblib.load("weights/shared_label_encoder.pkl")
print("Index of user010:", label_encoder.transform(["user010"])[0])
