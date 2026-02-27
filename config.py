import os

class Config:
    # Folder to store uploaded files
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    
    # Allowed extensions for file uploads
    ALLOWED_EXTENSIONS = {
        'fingerprint': {'png'},
        'ecg': {'dat'}
    }

    # Secret key for Flask session (can be randomized for security)
    SECRET_KEY = 'your-secret-key'  # Change this in production

    # Path to model weights and encoders
    FINGERPRINT_MODEL_PATH = os.path.join('weights', 'best_fingerprint_vit.pth')
    FINGERPRINT_ENCODER_PATH = os.path.join('weights', 'fingerprint_label_encoder.pkl')
    
    ECG_MODEL_PATH = os.path.join('weights', 'transformer_model.pth')
    ECG_ENCODER_PATH = os.path.join('weights', 'ecg_label_encoder.pkl')

    # Upload size limit (optional)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

