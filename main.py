import cv2
import pickle
import cvzone
# Computer vision package that makes its easy to run Image processing and AI function
import numpy as np

# Video feed
cap = cv2.VideoCapture('/home/malavika/Documents/Deeplearning/Parking Space detection and counter/carPark.mp4')


#importing the positions
with open('CarParkingPos1', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48


def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos

        imgCrop = imgPro[y:y + height, x:x + width]
        #cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        
        if count < 900:
            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))


while True:

    #looping the video,current frame=total frames,resetting the frame
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()



    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #kernelsize-height and width,sigmax,std deviation along x axis
   
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)

    #converting into binary images.
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    
   
    
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernel = np.ones((3, 3), np.uint8)
     #to make pixels big
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)
    cv2.imshow("Image", img)
    # cv2.imshow("ImageBlur", imgBlur)
    # cv2.imshow("ImageThres", imgMedian)
    if cv2.waitKey(1) & 0XFF == 27:
        break
cap.release
cv2.destroyAllWindows() 


                       
                           
    





  



#read video-loooping the video,import the parking positions we saved,crop the spaces

#we need to find if there is a car inside it??

#looking at pixel count-convert our image into binary img based on its edges and corners,if it does have a lot of edges ,plane image
#and no car present
#we se a threshold 


#convert to grayscale--blur--binary image
#no car-no or less pixels



