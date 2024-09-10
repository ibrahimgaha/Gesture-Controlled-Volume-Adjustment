# Gesture-Controlled Volume Adjustment


## Overview

This project is a gesture-based control system that allows you to adjust the volume of your computer using hand gestures. By leveraging **MediaPipe's** hand tracking module, the system captures hand movements through a webcam and recognizes specific gestures to adjust the volume seamlessly. The project offers a hands-free, contactless solution for volume control, making it both intuitive and efficient.

## Features

- **Real-time Hand Tracking**: Detects and tracks hands using **MediaPipe's** hand landmarks detection.
- **Gesture-Based Volume Control**: Recognizes hand gestures such as finger pinching to adjust the volume.
- **Responsive and Smooth**: Optimized for 30 FPS performance on CPU to ensure smooth tracking and gesture recognition.
- **Intuitive UI**: Simple and natural hand movements for controlling the system's volume.

## Technologies Used

- **OpenCV**: For image processing and capturing video from the webcam.
- **MediaPipe**: Hand tracking and landmark detection.
- **Numpy**: For efficient array operations.
- **Python**: The core language for the application.

## How It Works

1. **Hand Detection**: The system uses **MediaPipe** to detect hands in real-time.
2. **Landmark Identification**: It identifies 21 key hand landmarks for each detected hand.
3. **Gesture Recognition**: The program checks specific landmarks to detect gestures (e.g., pinch gesture).
4. **Volume Adjustment**: Based on the gesture, the system increases or decreases the computer's volume.

## Setup & Installation

### Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- OpenCV
- MediaPipe
- Numpy

Install the required libraries by running:

```bash
pip install opencv-python mediapipe numpy
