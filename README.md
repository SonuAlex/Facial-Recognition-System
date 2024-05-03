# Facial Recognition System
This project implements a live facial recognition system. It uses computer vision techniques to detect and recognize faces in real-time. The system can be used for various applications such as access control, surveillance, and personal identification. It utilizes machine learning algorithms to train a model on a dataset of known faces and then uses that model to identify faces in a video stream or image. The system provides accurate and efficient face recognition capabilities, making it suitable for both small-scale and large-scale deployments.

## Requirements
There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.
- `OpenCV`
- `dlib`
- `numpy`
- `Pillow`

## Usage
### **Preprocessing**
1. Add your image in `/Images` and name it (preferably an Id number).
2. Add the initial data to the firebase realtime database through the `addDatatoDatabase.py` file.
3. Run `encodeGenerator.py` to create an updated `encodeFile.p` and also upload the images to the firebase storage.

### **Working**
1. **Execution**: Execute the `main.py` script within an Integrated Development Environment (IDE) or a terminal environment with appropriate permissions and dependencies installed.
2. **Webcam Activation**: Upon execution, the script activates the webcam to capture live video feed.
3. **Facial Detection**: Utilizing computer vision techniques, the script detects faces within the video frames.
4. **Recognition**: Each detected face is compared against a predefined database of authorized individuals to determine a match.
5. **Attendance Tracking**: Upon successful recognition, the attendance count for the respective individual is incremented by one.
6. **Logging**: The system logs attendance updates for further analysis and record-keeping purposes.
     
## Disclaimer
The system is intended for lawful and ethical use cases only. It is the responsibility of the user to ensure compliance with applicable privacy regulations and obtain necessary permissions before deploying the system in any environment.