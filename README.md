# 🔐 Multimodal Biometric Authentication System (Fingerprint + ECG)

This project is a secure and intelligent multimodal biometric authentication system that verifies identity using *fingerprint images* and *ECG time-series signals*. By combining anatomical and physiological biometric traits, the system delivers stronger spoof-resistance and robust authentication compared to traditional single-modality systems.

It includes deep-learning-based feature extraction with *Vision Transformers (ViT)* for fingerprints and *Transformer encoders* for ECG signals, along with a *Flask-based real-time web interface* for user interaction.

---

## 🚀 Key Features
- 🖐 *Fingerprint Recognition* using Vision Transformer (ViT)
- ❤ *ECG-based biometric authentication* using Time-Series Transformer
- 🔀 *Multimodal fusion* for final identity verification
- 🌐 *Flask web application* for real-time inference
- 🧠 *Deep learning with PyTorch*
- 🔐 *Highly secure & spoof-resistant*
- ⚡ *Real-time processing support*

---

## 🧬 Technology Stack

| Component | Details |
|----------|---------|
| Language | Python 3.8+ |
| Web Framework | Flask |
| Deep Learning | PyTorch, Transformers |
| Preprocessing | NumPy, SciPy, WFDB, PIL, Torchvision |
| Models | Vision Transformer + Transformer Encoder |
| Hardware (optional) | ESP32, NodeMCU, R307 Fingerprint Sensor, AD8232 ECG Sensor |

---

## 📂 Project Folder Structure
```
project/
│── app.py
│── config.py
│── requirements.txt
│── .gitattributes
│
├── models
│   ├── ecg_model.py
│   └── fingerprint_model.py
│
├── utils
│   ├── preprocess_ecg.py
│   └── preprocess_fingerprint.py
│
├── templates
│   ├── index.html
│   ├── result.html
│   └── error.html
│
├── static
│   ├── uploads/
│   └── assets/
│
└── weights
    └── README.md
```


---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/Multimodal-Biometric-System.git
cd Multimodal-Biometric-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application
```bash
python app.py
```

### 4️⃣ Open in Browser
```
http://localhost:5000
```


## 🌐 How It Works
- Upload a **fingerprint image** and **ECG (.dat + .hea)** file
- System preprocesses & extracts feature embeddings using deep learning
- Predictions from both modalities are fused using **score-level averaging**
- Final identity result & confidence value displayed in the browser

---

## 🔮 Future Scope
- Mobile-based biometric authentication application
- Support for additional modalities (**face / voice**)
- Edge-device deployment (**Jetson Nano / Raspberry Pi**)
- Federated or on-device learning for enhanced privacy
- Incremental user enrollment capability
- Blockchain-based identity management for secure storage

---

## 📄 License
This project is open-source and available for **academic and research** purposes only.

