# ✋ Gesture Control
A Python-based Computer Vision Project for Gesture-Based System Controls

## 🧠 Overview
Gesture Control is an open-source Python project that leverages computer vision to enable gesture-based control of system functionalities such as volume, brightness, and mouse operations. Utilizing the power of MediaPipe and OpenCV, this project interprets hand gestures captured via webcam to perform real-time system adjustments, offering a touchless interaction experience.

🚀 Features
- Hand Tracking Module: Detects and tracks hand landmarks using MediaPipe.
- Volume Control: Adjusts system volume by varying the distance between the thumb and index finger.
- Brightness Control: Modifies screen brightness using similar hand gestures.
- Gesture-Based Mouse Control: Controls mouse movements and clicks through specific hand gestures.

## 🛠️ Technologies Used
<table> <thead> <tr> <th>Category</th> <th>Tech Stack</th> </tr> </thead> <tbody> <tr> <td>Programming Language</td> <td>Python 3.x</td> </tr> <tr> <td>Computer Vision</td> <td>OpenCV</td> </tr> <tr> <td>Hand Tracking</td> <td>MediaPipe</td> </tr> <tr> <td>System Control</td> <td>pycaw (Volume), screen-brightness-control (Brightness)</td> </tr> <tr> <td>Mouse Control</td> <td>pyautogui, wxPython</td> </tr> </tbody> </table>

## 📁 Project Structure
```env
Gesture_Control/
├── handTrackingModule.py     # Module for hand landmark detection
├── VolumeControl.py          # Script to control system volume via gestures
├── BrightnessControl.py      # Script to control screen brightness via gestures
├── Gesture_Mouse.py          # Script to control mouse using hand gestures
└── README.md                 # Project documentation
```

## ⚙️ Setup & Installation
1. Clone the Repository:
   ```bash
   git clone https://github.com/tuhindutta/Gesture-Control.git
   cd Gesture-Control
   ```
2. Create a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install Dependencies

## 🧪 Usage
- Volume Control:
  ```bash
  python VolumeControl.py
  ```
  Gesture: Bringing the thumb and index finger closer decreases the volume; moving them apart increases it.

- Brightness Control:
  ```bash
  python BrightnessControl.py
  ```
  Gesture: Similar to volume control; adjusts screen brightness based on the distance between thumb and index finger.

- Mouse Control:
  ```bash
  python Gesture_Mouse.py
  ```
  Gestures:
    - Move Cursor: Move your index finger to control the cursor.
    - Left Click: Bring the index and middle fingers close together.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. For more details and updates, visit the [GitHub Repository](https://github.com/tuhindutta/Gesture-Control).

## 🙏 Acknowledgements
This project was inspired by the outstanding tutorials and educational content from Murtaza Hassan, whose work in practical computer vision and real-time AI applications has been instrumental in shaping this implementation.

Special thanks to the broader open-source community for libraries like MediaPipe, OpenCV, and other tools that make gesture-based interaction accessible and exciting to build.
