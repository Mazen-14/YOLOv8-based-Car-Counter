# CarCounter-YOLOv8

This repository contains a **Car Counter** using **YOLOv8** and SORT tracker. It detects and counts cars in a specified lane from a video feed.

## 📌 Project Structure
```
CarCounter-YOLOv8
│── Photos/            # Contains mask and overlay graphics
│── Videos/            # Video footage for testing
│── Yolo/              # YOLOv8 model file (yolov8n.pt)
│── src/               # Source code
│   ├── car_counter.py # Main script
│   ├── sort.py        # Tracker implementation
│   ├── names.py       # Class names for YOLOv8
│   ├── sizing.py      # Resizes mask to fit video
│── README.md          # Project documentation
│── requirements.txt   # Required dependencies
```

## 🛠 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/CarCounter-YOLOv8.git
   cd CarCounter-YOLOv8
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the car counter script:
```sh
python src/car_counter.py
```

## 📜 Dependencies
- `ultralytics` (YOLOv8)
- `opencv-python`
- `cvzone`
- `numpy`
- `sort`

Install them using:
```sh
pip install -r requirements.txt
```

## 🔍 Features
✅ Detects and tracks cars using YOLOv8 + SORT tracker  
✅ Counts cars crossing a predefined lane  
✅ Overlays graphics and masks to refine detection  
✅ Works with pre-recorded videos

## 📌 Notes
- Ensure `mask.png` matches the resolution of the video (use `sizing.py` if needed)
- Change `Videos/cars.mp4` to use a different input video (upload compatible mask first) 

## 🖼 Example Output
![Example Screenshot](example_output.png)

---
**Contributors:** Mazen Mohamed Hemdan (@Mazen-14)
