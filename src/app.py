import cv2
import mediapipe as mp
import pygame

mp_hands = mp.solutions.hands.Hands()
draw_utils = mp.solutions.drawing_utils
finger_counter = 0
finger_tips = [8, 12, 16, 20]
volume = 0.5
music_path = r"C:\Users\pooya\OneDrive\Desktop\python 103\mediapipe_music_project\src\Sweden.mp3"

cap = cv2.VideoCapture(0)

pygame.mixer.init()
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

while True:
    finger_counter = 0
    success, frame = cap.read()

    if not success:
        break

    framRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(framRGB)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            landmark = hand.landmark
            #draw_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            for tip in finger_tips:
                if landmark[tip].y < landmark[tip-2].y:
                    finger_counter += 1

    cv2.putText(frame, "raise 2 or 3 fingers 2 increase or decrease the volume", (25, 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0), 3)

    if finger_counter == 3:
        if volume > 0.0:
            volume -= 0.1
    elif finger_counter == 2:
        if volume < 1.0:
            volume += 0.1

    pygame.mixer.music.set_volume(volume)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()