import cv2
import mediapipe as mp

hands = mp.solutions.hands.Hands()
video = cv2.VideoCapture(0)

i = 0
filters = ['Sepia','Blur','Negative','Edge']
while True:
    ret,cam = video.read()
    if not ret:
        break
    else:
        cam = cv2.flip(cam,1)
        result = hands.process(cv2.cvtColor(cam, cv2.COLOR_BGR2RGB))

        if(result.multi_hand_landmarks):
            hand = result.multi_hand_landmarks[0]
            mp.solutions.drawing_utils.draw_landmarks(cam, hand, mp.solutions.hands.HAND_CONNECTIONS)

            t,p = hand.landmark[4], hand.landmark[8]
            if (abs(t.x-p.x) < 0.03 and abs(t.y-p.y) < 0.03):
               cv2.imwrite('Image.jpg',cam)

        if(filters[i] == 'Negative'):
            cam = cv2.bitwise_not(cam)

        elif(filters[i] == 'Blur'):
            cam = cv2.GaussianBlur(cam,(15,15),0)

        elif(filters[i] == 'Edge'):
            cam = cv2.Canny(cam,40,60)
        else:
            cam = cv2.applyColorMap(cam,cv2.COLORMAP_BONE)
        cv2.imshow('Image',cam)

        key = cv2.waitKey(1) & 0xFF

        if(key == ord('f')):
            i = (i+1)%4
        elif(key == ord('q')):
            break

cv2.destroyAllWindows()
video.release()
hands.close()
