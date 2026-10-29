# Gesture Volume Control 

A computer vision project that lets you control music volume using hand gestures detected through a webcam.

Built with Python, OpenCV, MediaPipe, and Pygame, this project demonstrates how hand tracking can be used to interact with a computer without touching a keyboard or mouse.

## Features

- Detects hands in real time using a webcam.
- Tracks finger positions using MediaPipe Hands.
- Increases music volume when two fingers are raised.
- Decreases music volume when three fingers are raised.
- Plays music continuously using Pygame.
- Displays the webcam feed while detecting gestures.
- Press `q` to exit the application.

## Technologies Used

- **Python** — main programming language
- **OpenCV (cv2)** — webcam access and image processing
- **MediaPipe** — real-time hand landmark detection
- **Pygame** — music playback and volume control

## How It Works

The application captures video from the webcam and processes each frame to detect hand landmarks.

It checks the positions of four fingertips to count raised fingers. Depending on the number detected, it adjusts the music volume.

| Hand gesture | Action |
|---|---|
| Two raised fingers | Increase volume |
| Three raised fingers | Decrease volume |
| Press `q` | Exit the application |

**Note:** The current implementation counts four fingers and does not include thumb detection. Holding a gesture may change the volume repeatedly because the program processes gestures continuously.

## Project Structure

```text
gesture-volume-control/
├── src
    ├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The music file is stored locally and is not included in the repository.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ph4848/gesture-volume-control.git
cd gesture-volume-control
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Music Setup

The application uses an MP3 file for music playback.

1. Place your music file in a local folder.
2. Update the `music_path` variable in `app.py` to point to that file.

For example:

```python
music_path = "assets/Sweden.mp3"
```

Make sure the path matches the actual location of your music file.

The music file is not included in this repository. Only use music you have the right to use and distribute.

## Run the Application

Connect a webcam, activate your virtual environment, and run:

```bash
python app.py
```

The webcam window will open and the music will start playing. Raise two fingers to increase the volume or three fingers to decrease it.

Press `q` to close the webcam window and stop the application.
