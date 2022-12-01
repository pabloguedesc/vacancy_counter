import cv2  
import numpy as np

# areaX = ["x", "y", "width", "height"]
area1 = [1, 89, 108, 213]
area2 = [115, 87, 152, 211]
area3 = [289, 89, 138, 212]
area4 = [439, 87, 135, 212]
area5 = [591, 92, 132, 213]
area6 = [737, 95, 132, 211]
area7 = [876, 94, 147, 208]
area8 = [1021, 89, 148, 209]

areas = [area1, area2, area3, area4, area5, area6, area7, area8]

video = cv2.VideoCapture("./files/video.mp4")

while True:
  check, frame = video.read()
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame_thresh = cv2.adaptiveThreshold(
    frame_gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV, 25, 16
  )
  frame_blur = cv2.medianBlur(frame_thresh, 5)
  kernel = np.ones((3, 3), np.int8)
  frame_dilate = cv2.dilate(frame_blur, kernel)

  quantity_available_areas = 0

  for x, y, w, h in areas:
    clipping = frame_dilate[y: y + h, x: x + w]
    quantity_px_white = cv2.countNonZero(clipping)
    cv2.putText(frame, str(quantity_px_white), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    if (quantity_px_white > 3000): 
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    else:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      quantity_available_areas +=1
  cv2.rectangle(frame, (90, 0), (415, 60), (0, 0, 0), -1)
  cv2.putText(frame, f"FREE: {quantity_available_areas}/8", (90, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

  cv2.imshow("video", frame)
  cv2.imshow("video2", frame_dilate)
  cv2.waitKey(10)