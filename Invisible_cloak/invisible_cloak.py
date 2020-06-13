import cv2
import numpy as np 

#Frame dimension and video capture

widthStream = 1920
heightStream = 1080

Stream = cv2.VideoCapture(0, cv2.CAP_DSHOW)

streamID = 0

#grean hue value range

LowerG = 40
UpperG = 80

while True:
    ret, stream = Stream.red()

    if not ret:

        break 
    stream = cv2.flip(stream,1 )
    stream = cv2.resize(stream,(widthStream, heightStream))

    #Create green hue mask

    HSV = cv2.cvtColor(stream, cs2.COLOR_BGR2HSV)

    binary = cv2.inRange(HSV, np.array([LowerG, 0,0],np.array([UpperG, 255, 255])))

    binary = cv2.bitwise_not(binary)

#apply mask to video feed frame

video_frame_masked = cv2.bitwise_and(stream, stream, mask = binary)

#apply mask to background sample frame

if streamID == 60: #capture 60th frame only with background
    Sample = stream.copy()
elif streamID > 60: # for the rest frames, use this sample image 
    Sample_mask = cv2.bitwise_not(binary)

    Sample_masked = cv2.bitwise_and(Sample, Sample, mask =Sample_mask)

    #create display frame

    Cloak = cv2.bitwise_or(video_frame_masked, Sample_masked)

    cv2.imshow("invisiblility cloak", Cloak)

StreamID += 1

if cv2.waitKey(1) & 0xFF == ord("S"):
    break 
Stream.release()
cv2.destoryAllWindows()