# 🏀 Basketball Object Detection Pipeline

An end-to-end vision pipeline to detect basketball entities (players, referees, ball) from video footage using automatic annotation, YOLOv8 training, and real-time inference.

---

## 📂 Project Structure

```bash
├── small-Model3/                      # Folder containing trained YOLOv8 weights
├── 1_Extract_Images_from_Video.py     # Extracts frames from video
├── 2_Automatic_Dataset_Annotation.py  # Zero-shot annotation using GroundingDINO + CaptionOntology
├── 3_Display_Annotations.py           # Visualizes predicted/annotated bounding boxes
├── 4_Training_on_Frames.py            # Trains YOLOv8 model
├── 5_Testing_On_Video.py              # Tests model on unseen videos
├── Combine_Images.py                  # Merges output for visual comparison
├── app.py                             # Optional Streamlit/Flask web demo
├── create_subset.py                   # Create smaller dataset for debugging
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation

## 🚀 Features

- 🎥 **Extracts high-quality video frames**  
  Converts basketball match footage into clean, structured image frames for annotation and model training.

- 🔍 **Zero-shot auto-annotation (GroundingDINO + CaptionOntology)**  
  Automatically labels entities (players, ball, referee) in images without manual effort using vision-language models.

- 📦 **Efficient YOLOv8 model training (via Ultralytics)**  
  Trains state-of-the-art object detection models on custom basketball datasets with minimal code.

- 📈 **Evaluation with PR Curves and mAP@0.5**  
  Tracks performance with standard metrics like precision, recall, and mean Average Precision.

- ⚙️ **Real-time inference using CamGear**  
  Processes live or recorded videos with minimal latency using optimized frame grabbing.

- 🌐 **Web demo**  
  Provides a lightweight interface (Streamlit/Flask) to test the model in real time.

## 🛠️ Tools & Technologies

| Tool                | Role                                                             |
|---------------------|------------------------------------------------------------------|
| **YOLOv8 (Ultralytics)** | Object detection model training and prediction                |
| **GroundingDINO**        | Vision-language annotation without manual labels             |
| **CaptionOntology**      | Generates accurate and contextual class prompts              |
| **CamGear**              | Efficient video frame grabbing from large videos             |
| **Python + OpenCV**      | Core logic, data processing, and visualization               |
| **Streamlit / Flask**    | Lightweight deployment as a web app                          |
