# Solar Panel Damage Detection Using YOLO Models

## 📌 Project Overview  
This project focuses on **automated solar panel damage detection** using **deep learning and object detection models**. The solution aims to reduce maintenance costs, optimize resources, and improve monitoring efficiency for **large-scale photovoltaic (PV) systems**. 

We leverage **YOLOv5, YOLOv8, and YOLOv9** to detect various types of panel damages, with **images annotated using Roboflow**.

---
## 🚀 Business Problem  
### Challenges Faced:
1. **High Maintenance Costs** – Manual inspections are costly and inefficient.  
2. **Delayed Fault Detection** – Early identification is crucial to avoid energy loss.  
3. **Resource Optimization** – Need for automated monitoring to minimize manpower and operational overhead.

### Business Impact:
- **Minimized Downtime** – Ensures quick fault detection and rectification.
- **Cost Savings** – Reduces manual inspection and repair expenses.
- **Scalability** – Enables efficient monitoring across **large PV systems**.

---
## 🎯 Business Objective  
✔ **Maximize solar PV system uptime** with automated fault detection.  
✔ **Reduce operational costs** by minimizing manual interventions.  
✔ **Improve detection accuracy** using deep learning techniques.  
✔ **Ensure scalability** for handling large-scale solar installations.  

---
## 🔥 Future Scope  
🚀 **Advanced Model Integration** – Explore transformer-based models for improved accuracy.  
🔍 **Predictive Maintenance** – Forecast faults before they occur using AI.  
☁ **Cloud Deployment & IoT Integration** – Real-time monitoring using cloud solutions.  
📱 **Mobile App Development** – Enable on-the-go fault detection through an app.  
🖼 **Dataset Expansion** – Incorporate diverse images covering additional fault types.

---
## 📌 Project Pipeline (CRISP-ML(Q) Methodology)  
This project follows the **CRISP-ML(Q)** framework:
1. **Business & Data Understanding** – Identify key objectives and data sources.
2. **Data Preparation** – Preprocess, clean, and augment the dataset.
3. **Model Building** – Train and evaluate YOLO models for fault detection.
4. **Model Evaluation** – Measure performance using **mAP (Mean Average Precision)**.
5. **Model Deployment** – Deploy a real-time **Streamlit-based fault detection app**.
6. **Monitoring & Maintenance** – Ensure ongoing model updates and performance optimization.

---
## 🔧 Installation  
Clone the repository and install dependencies:
```bash
# Clone the repository
git clone https://github.com/ImAbhijeetPanda/Solar-Panel-Fault-Detection
cd Solar-Panel-Fault-Detection

# Install required libraries
pip install -r requirements.txt
```
Ensure required packages are installed:
```bash
pip install torch torchvision torchaudio ultralytics opencv-python roboflow streamlit
```

---
## 📊 Dataset and Preprocessing  
### **Data Sources**  
- **Kaggle & Google Images** – Images of solar panels with different fault types.  
- **Manual Annotation** – Images labeled using **Roboflow**.  

### **Data Preprocessing Steps**  
✅ **Image Augmentation** – Applied rotation, scaling, and flipping.  
✅ **Resizing & Normalization** – Standardized images to **640x640 pixels**.  
✅ **Dataset Splitting** – **70% Training | 15% Validation | 15% Test**.  

---
## 🧠 Model Training and Evaluation  
### **Models Used**  
✔ **YOLOv5** – Baseline object detection model.  
✔ **YOLOv8** – Enhanced detection and efficiency.  
✔ **YOLOv9** – Best-performing model with **highest accuracy**.  

### **Evaluation Metrics**  
- **mAP (Mean Average Precision)** – Measures object detection accuracy.
- **IoU (Intersection over Union)** – Ensures precise bounding box predictions.

| Model  | mAP@50 | mAP@50-95 |
|--------|--------|----------|
| YOLOv5 | 69%    | 42%      |
| YOLOv8 | 79%    | 59%      |
| YOLOv9 | 79%    | 63%      |

🏆 **Best Model: YOLOv9** (Highest accuracy with **79% mAP50-95**)

---
## 🚀 Deployment  
We deployed the **YOLOv9 model** using **Streamlit** for an interactive web application.

### **Deployment Steps:**  
1. **Model Integration** – Incorporate YOLOv9 into a **Streamlit** app.
2. **User Interface** – Allows image uploads for real-time damage detection.
3. **Inference & Visualization** – Detects and highlights faults with bounding boxes.

Run the app locally:
```bash
streamlit run app.py
```

---
## 📈 Results  
- Successfully detected **multiple types of solar panel damage**.  
- Achieved **79% mAP50** and **63% mAP50-95** with **YOLOv9**.  
- **Streamlit Deployment** enables real-time fault detection and visualization.

---
## 🏆 Contributors   
👤 **Abhijeet Panda** (LinkedIn: [Abhijeet's Profile](https://www.linkedin.com/in/imabhijeetpanda))  

---
## 🎉 Acknowledgments  
Special thanks to:  
- **Roboflow** for image annotation.  
- **YOLO community** for advanced object detection.  
- **Google Colab** for providing training resources.

---
## 🔗 Repository Link  
🔗 [GitHub Repository](https://github.com/ImAbhijeetPanda/Solar-Panel-Fault-Detection)

For any questions or feedback, feel free to reach out:

- **Email**: [iamabhijeetpanda@gmail.com](mailto:iamabhijeetpanda@gmail.com)
- **LinkedIn**: [Abhijeet Panda](https://www.linkedin.com/in/imabhijeetpanda)
- **GitHub**: [ImAbhijeetPanda](https://github.com/ImAbhijeetPanda)



🚀 **Feel free to fork, contribute, or raise an issue!** 😃
