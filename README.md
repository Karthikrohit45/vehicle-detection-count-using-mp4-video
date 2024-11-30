Vehicle Detection System:

This is a Vehicle Detection System built using Python and OpenCV for detecting vehicles in video streams. The system processes a video file, detects moving vehicles, and counts the number of vehicles crossing a specified line in the video.

Features:

Vehicle Detection: Uses OpenCV's background subtraction and contour detection to identify vehicles.
Real-time Vehicle Count: Displays the number of vehicles crossing a virtual line drawn on the screen.
Customizable: You can change the video source or adjust detection parameters based on your needs.
Requirements

Before running the system, make sure you have the following installed:

Python 3.x (preferably Python 3.7 or later)
Virtual Environment for managing dependencies (optional but recommended)
Python Libraries


This project uses the following Python libraries:

OpenCV: For video processing and vehicle detection.
NumPy: For handling array-based data.
To install these dependencies, you can use pip:

pip install -r requirements.txt
Where requirements.txt should contain the following:

opencv-python==4.10.0.84
numpy==2.1.3
Setup and Installation

Clone the repository:

git clone https://github.com/yourusername/VehicleDetectionSystem.git
cd VehicleDetectionSystem

Create a Virtual Environment (optional but recommended):

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

On Windows:
python -m venv venv
.\venv\Scripts\activate

Install dependencies:
If you have a requirements.txt file in your repository, you can install the necessary dependencies by running:

pip install -r requirements.txt
Add your video file:
Make sure the video file (traffic.mp4) is located in the same directory as main.py for easy access. You can use any video file of your choice for testing.

/path/to/project/VehicleDetectionSystem/
    ├── main.py
    ├── traffic.mp4  # Your video file
    └── venv/        # Virtual environment folder
Run the script:

To start vehicle detection, simply run the main.py script:
python main.py

Quit the program:
To quit the program, press the q key while the OpenCV window is active.

How It Works

The program opens a video file (traffic.mp4) using OpenCV’s cv2.VideoCapture.
It processes each frame to detect vehicles using background subtraction (cv2.createBackgroundSubtractorMOG2) and contour detection (cv2.findContours).
It counts vehicles that cross a virtual line drawn in the frame.
The vehicle count is displayed in real-time on the screen, and the system continues processing until the user presses the q key to quit.
