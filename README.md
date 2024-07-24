# Computer Vision Project

## Introduction
This project utilizes various computer vision techniques to analyze and process images and videos, specifically focusing on object detection, segmentation, optical flow, and perspective transformation. The following components are implemented:

1. **Object Detection with YOLOv8 (Ultralytics)**
2. **Custom YOLO Training and Fine-Tuning**
3. **KMeans Clustering for Player Segmentation**
4. **Optical Flow for Camera Movement Measurement**
5. **Perspective Transformation with OpenCV**
6. **Player Speed and Distance Measurement**

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Parts](#usage)
    - [Object Detection](#object-detection)
    - [Custom YOLO Training](#custom-yolo-training)
    - [Player Segmentation](#player-segmentation)
    - [Camera Movement Measurement](#camera-movement-measurement)
    - [Perspective Transformation](#perspective-transformation)
    - [Player Speed and Distance Measurement](#player-speed-and-distance-measurement)
5. [Contributing](#contributing)


## Prerequisites
- Python 3.7+
- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- OpenCV
- NumPy
- Scikit-learn
- sys
- os
- pickle
- supervision
- pandas
- matplotlib

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/computer-vision-project.git
    cd computer-vision-project
    ```

## Project Structure
computer-vision-project/
├── Camera_movement/
│ ├── __init__.py/
│ └── Camera_movement.py/
├── Development_and_analysis/
│ └── color_assignment.ipynb/
├── player_ball_assigner/
│ ├── __init__.py/
│ └── player_ball_assigner.py/
├── Speed_and_distance_estimator/
│ ├── __init__.py/
│ └── Speed_and_distance_estimator.py/
├── stubs/
│ ├── stubs.pkl/
│ └── tracks_stubs.pkl/
├── team_assigner/
│ ├── __init__.py/
│ └── team_assigner.py/
├── trackers/
│ ├── __init__.py/
│ └── trackers.py/
├── utils/
│ ├── __init__.py/
│ └── bbox_utils.py/
│ └── video_utils.py/
├── view_transformer/
│ ├── __init__.py/
│ └── view_transformer.py/
├── main.py
└── Yolo_infrance.py

## Custom YOLO Training
Fine-tune and train your own YOLO model on your custom dataset.

## Player Segmentation
Use KMeans clustering to segment players from the background and accurately identify t-shirt colors.

## Camera Movement Measurement
Measure the camera movement using optical flow techniques

## Perspective Transformation
Apply perspective transformation to represent the scene's depth and perspective.

## Player Speed and Distance Measurement
Measure the player's speed and distance covered in the image.

## Contributing
We welcome contributions to this project. Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.


## Final OutPut
![final_output](https://github.com/user-attachments/assets/1db44106-1d65-4ee6-8acd-41f0931023c2)
