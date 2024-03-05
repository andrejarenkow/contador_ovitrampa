import cv2
import numpy as np
import matplotlib.pyplot as plt

st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    min = st.number_input('mínimo Canny')
    max = st.number_input('maximo Canny')
    image = cv2.imread(frame)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #ar, thresh = cv2.threshold(gray,40,255,cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(gray, (11,11), 1)
    canny = cv2.Canny(blur, min, max, 1)
    dilated = cv2.dilate(canny, (1,1), iterations = 4)
    (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)
    plt.figure(figsize = (5,5))
    FRAME_WINDOW.image(rgb)
    st.text(str(len(cnt)))
else:
    st.write('Stopped')



