import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

min = st.number_input('min', value=100)
max = st.number_input('max', value=200)

if img_file_buffer is not None:
      # To read image file buffer with OpenCV:
      bytes_data = img_file_buffer.getvalue()
      cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
      gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
      #ar, thresh = cv2.threshold(gray,40,255,cv2.THRESH_BINARY)
      blur = cv2.GaussianBlur(gray, (11,11), 1)
      canny = cv2.Canny(blur, min, max, 1)
      dilated = cv2.dilate(canny, (1,1), iterations = 4)
      (cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
      rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)
      plt.figure(figsize = (5,5))
      rgb = cv2.putText(rgb, 'Ovos na palheta: '+ str(len(cnt)), (30, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 255, 255) , 2, cv2.LINE_AA)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
      st.write(type(rgb))

