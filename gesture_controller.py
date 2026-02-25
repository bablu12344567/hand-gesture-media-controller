import cv2
import mediapipe as mp
import pyautogui
import time
import os
import platform

def count_fingers(lst):
    cnt = 0
    fingers = []

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    fingers.append((lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh)   # Index
    fingers.append((lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh)  # Middle
    fingers.append((lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh) # Ring
    fingers.append((lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh) # Pinky
    thumb = (lst.landmark[4].x * 100 - lst.landmark[5].x * 100) > 6                # Thumb

    cnt = sum(fingers) + thumb
    return cnt, fingers, thumb

def adjust_brightness(change):
    if platform.system() == "Windows":
        try:
            import screen_brightness_control as sbc
            current = sbc.get_brightness(display=0)[0]
            sbc.set_brightness(min(max(current + change, 0), 100))
        except Exception:
            pass
    else:
        pass

cap = cv2.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand_obj = mp_hands.Hands(max_num_hands=1)

prev = -1
last_action_time = 0
action_interval = 0.3  # seconds

while True:
    current_time = time.time()
    ret, frm = cap.read()
    if not ret:
        break

    frm = cv2.flip(frm, 1)
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:
        hand_keypoints = res.multi_hand_landmarks[0]
        cnt, fingers, thumb = count_fingers(hand_keypoints)

        is_thumb_only = thumb and not any(fingers)
        is_pinky_only = fingers[-1] and not any(fingers[:-1]) and not thumb

        if cnt != prev or (current_time - last_action_time >= action_interval):
            if is_thumb_only:
                adjust_brightness(5)

            elif is_pinky_only:
                adjust_brightness(-5)

            elif cnt == 1:
                pyautogui.press("right")

            elif cnt == 2:
                pyautogui.press("left")

            elif cnt == 3:
                pyautogui.press("volumeup")

            elif cnt == 4:
                pyautogui.press("volumedown")

            elif cnt == 5 and prev != 5:
                pyautogui.press("playpause")

            last_action_time = current_time
            prev = cnt

        mp_drawing.draw_landmarks(frm, hand_keypoints, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", frm)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
