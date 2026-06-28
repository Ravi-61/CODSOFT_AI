# Face Detection using OpenCV

## Overview

This project is a Face Detection application developed using Python and OpenCV. It detects human faces in an image using the Haar Cascade Classifier and highlights each detected face by drawing a rectangle around it.

This project demonstrates the fundamentals of Computer Vision and image processing using a pre-trained face detection model.

## Features

- Detects one or more human faces in an image
- Uses OpenCV's pre-trained Haar Cascade Classifier
- Draws rectangles around detected faces
- Simple and beginner-friendly implementation
- Fast and accurate for frontal face detection

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier

## Project Structure

```
Task5_Face_Detection/
│
├── face_detection.py
├── sample.jpg
├── README.md
├── requirements.txt
└── screenshots/
```

## Installation

Install the required library:

```bash
pip install opencv-python
```

## How to Run

1. Place an image named `sample.jpg` in the project folder.
2. Open the terminal in the project directory.
3. Run the program:

```bash
python face_detection.py
```

## Working

1. The program loads the input image.
2. Converts the image to grayscale.
3. Uses the Haar Cascade Classifier to detect faces.
4. Draws blue rectangles around detected faces.
5. Displays the output image with detected faces.

## Example Output

Input:

- Image containing one or more human faces.

Output:

- Faces are detected and highlighted with rectangles.

## AI Concepts Used

- Computer Vision
- Face Detection
- Image Processing
- Haar Cascade Classifier
- OpenCV

## Future Enhancements

- Real-time face detection using a webcam.
- Face recognition using DeepFace, FaceNet, or ArcFace.
- Face mask detection.
- Smile and eye detection.
- Emotion recognition.

## Author

**Akasam Ravi**

CodSoft AI Internship – Task 5
