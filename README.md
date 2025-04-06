# 🛡️ Real-Time Toxic Content Detector

A powerful, modular AI system to detect **toxic text** and **NSFW images** in real time. Built for hackathons and production-ready environments to help moderate content across websites, apps, and social platforms.

## 🌐 Live API Deployment

**Render URL:** [https://toxic-detector-ai.onrender.com](https://toxic-detector-ai.onrender.com)  
(You can integrate this API into any frontend/backend application.)

---

## 🚀 Features

- ✅ Real-time **toxic text detection** using `DistilBERT` or `Toxic-BERT`
- 🖼️ **NSFW image classification** using a MobileNetV2 CNN model
- ⚡ FastAPI backend for high-performance REST APIs
- 🔌 Ready to plug into any frontend (React, Next.js, Vue, etc.)
- 📦 Easily deployable to **Render**, **Railway**, or any cloud provider

---

## 🧠 AI Models

| Module        | Model                            | Library      |
|---------------|----------------------------------|--------------|
| Text Analysis | `unitary/toxic-bert` (HF Model)  | 🤗 Transformers |
| Image Analysis| Custom MobileNetV2               | TensorFlow / Keras |

---

## 📁 Project Structure
toxic-detector-ai/
├── app/
│   ├── main.py             
│   ├── utils.py            
│   ├── model_image.py
│   ├── model_text.py 
│   └── schemas.py 
│           
├── requirements.txt                       
├── README.md   
