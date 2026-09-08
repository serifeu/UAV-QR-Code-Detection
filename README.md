# UAV Computer Vision System

A Python-based **computer vision system for UAV applications**, focusing on real-time object detection, object tracking, QR code recognition, and computer vision performance analysis.

The project was developed as part of a UAV project to explore different approaches for processing camera streams, detecting objects, tracking targets, and performing vision-based task verification.

---

## 🚀 Overview

The system combines several computer vision components into a single experimental framework:

* **Object Detection** using YOLO-based models
* **Object Tracking** using multiple tracking algorithms
* **QR Code Detection & Decoding** using OpenCV and PyZBar
* **Performance Analysis** using FPS, latency, precision, and overlap metrics
* **Camera Stream Processing** for real-time computer vision applications

The main goal of the project was to investigate different computer vision approaches and compare their suitability for real-time UAV systems.

---

## 🧩 System Architecture

```text
                    ┌─────────────────┐
                    │  Camera Stream  │
                    └────────┬────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
        ┌───────────────┐        ┌──────────────────┐
        │ YOLO Detection│        │ QR Code Detection│
        │               │        │  OpenCV / PyZBar │
        └───────┬───────┘        └──────────────────┘
                │
                ▼
        ┌─────────────────┐
        │ Object Tracking │
        │ KCF / DSST /    │
        │ Re3 / GOTURN    │
        └────────┬────────┘
                 │
                 ▼
        ┌──────────────────────┐
        │ Vision-Based Target  │
        │ Tracking & Analysis  │
        └──────────────────────┘
```

---

## 📂 Project Structure

| File        | Description                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------- |
| `yolo.py`   | Compares YOLOv5 variants and EfficientDet models using detection performance metrics such as latency and COCO AP. |
| `fps.py`    | Visualizes FPS and Expected Overlap performance for different object tracking algorithms.                         |
| `score.py`  | Generates OPE (One-Pass Evaluation) precision curves for tracking algorithms using benchmark data.                |
| `QRcode.py` | Detects and decodes QR codes from a live camera stream using OpenCV and PyZBar.                                   |
| `qrcr.py`   | Generates QR codes for testing and vision-based task verification scenarios.                                      |
| `test.py`   | Checks whether the required OpenCV and PyZBar dependencies are correctly installed and functioning.               |

---

## 🔍 Computer Vision Components

### 1. Object Detection

The project includes experiments with different object detection architectures, including:

* YOLOv5s
* YOLOv5m
* YOLOv5l
* YOLOv5x
* EfficientDet

The purpose of the comparison is to investigate the trade-off between **detection accuracy and computational latency**, which is particularly important for real-time embedded computer vision applications.

---

### 2. Object Tracking

Several tracking approaches are analyzed:

* Re3
* KCF
* DSST
* GOTURN
* ASMS

The project evaluates tracking performance using metrics such as:

* FPS
* Expected Overlap
* Precision
* OPE evaluation results

These experiments help demonstrate the trade-offs between computational efficiency and tracking performance.

---

### 3. QR Code Recognition

The QR code module provides real-time detection and decoding through a camera.

The process consists of:

```text
Camera Input
     ↓
Frame Processing
     ↓
QR Code Detection
     ↓
Data Decoding
     ↓
Visual Bounding Box
     ↓
Decoded Information
```

The implementation uses **OpenCV** for camera and image processing and **PyZBar** for QR code decoding.

---

## 📊 Performance Analysis

The project includes separate scripts for analyzing different aspects of computer vision performance.

### YOLO Model Comparison

`yolo.py` is used to compare detection models based on factors such as:

* Detection accuracy
* COCO AP
* GPU latency
* Computational requirements

The results can be used to understand the trade-off between lightweight and more computationally demanding models.

### Tracking Performance

`fps.py` and `score.py` provide visual analysis of tracking algorithms using:

* Frames Per Second (FPS)
* Expected Overlap
* Precision
* OPE evaluation

This allows different tracking approaches to be compared from both **speed and accuracy** perspectives.

> Performance values may vary depending on the hardware, model configuration, input resolution, and test environment.

---

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **NumPy**
* **PyZBar**
* **YOLO**
* **EfficientDet**
* **Matplotlib**
* **Seaborn**
* **Pandas**
* **QR Code**

---

## ⚙️ Installation

### Requirements

* Python 3.8+
* OpenCV
* NumPy
* PyZBar
* QRCode
* Matplotlib
* Seaborn
* Pandas

Install the required Python packages:

```bash
pip install opencv-python numpy pyzbar qrcode[pil] matplotlib seaborn pandas
```

### Linux / Ubuntu

PyZBar may require the ZBar system library:

```bash
sudo apt-get update
sudo apt-get install -y libzbar0
```

---

## ▶️ Usage

### Test Dependencies

Run the dependency test:

```bash
python test.py
```

### Generate a QR Code

```bash
python qrcr.py
```

### Run Real-Time QR Detection

```bash
python QRcode.py
```

Press **Q** to close the camera window.

### Run YOLO Analysis

```bash
python yolo.py
```

### Run Tracking FPS Analysis

```bash
python fps.py
```

### Generate Tracking Precision Curves

```bash
python score.py
```

---

## 🎯 Future Improvements

* [ ] YOLOv8 / YOLOv11 integration
* [ ] TensorRT optimization for embedded platforms
* [ ] ByteTrack / BoT-SORT tracking integration
* [ ] Kalman Filter-based target prediction
* [ ] Integration with UAV onboard camera systems
* [ ] Real-time telemetry integration
* [ ] Improved multi-object tracking
* [ ] Performance optimization for NVIDIA Jetson platforms

---

## 📚 Learning Outcomes

This project provided practical experience in:

* Real-time computer vision
* Deep learning-based object detection
* Object tracking algorithms
* QR code detection and decoding
* Camera stream processing
* Computer vision performance evaluation
* Python-based AI development
* UAV-oriented computer vision systems

---

## 👨‍💻 Project Context

This project was developed as part of my **UAV and computer vision studies**, combining deep learning, image processing, object tracking, and vision-based task verification into a practical experimental system.

It represents my experience working with **Python, OpenCV, YOLO, computer vision algorithms, and real-time image processing** for UAV-related applications.
