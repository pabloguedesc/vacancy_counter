import cv2

def determine_spaces():
  video = cv2.VideoCapture("./files/video.mp4")
  video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
  video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

  check, frame = video.read()

  frame = cv2.resize(frame, (int(video_width), int(video_height)))

  roi = cv2.selectROI("Select the area", frame)

  return print(roi)

determine_spaces()