#2 files-allows us to select and deselect the parking spaces and 
#put in a list ,we will take into maain file.
#one s for selecting and other is for running

#pickle--used for save all the places/positions of parking spaces and bring it to main code


import pickle
import cv2

#pickle --->  

#readinimage
img=cv2.imread('/home/malavika/Documents/Deeplearning/Parking Space detection and counter/carParkImg.png')

width,height = 107,48
#list to put all the parking spaces
try:
    with open('CarParkingPos1', 'rb') as f:
        poslist = pickle.load(f)
except:
    poslist = []


# represents 1 parking space - rectangle,157-50=width,240-192 is the height
#we need to create a rectangle around the parking space 
# cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)


def mouseclick(events,x,y,flags,params):
  #rectangle is creted on left mouse click
  if events == cv2.EVENT_LBUTTONDOWN:
    poslist.append((x,y))
    #if click on wrong place,delete as well
  if events == cv2.EVENT_RBUTTONDOWN:
    #checck if our click point is between the positions already have
     for i,pos in enumerate(poslist):
       x1,y1 = pos
       if x1 < x < x1+width and y1 < y < y1+height:
         poslist.pop(i)

  #add to a pickle object,everytime we append and delete

  with open('CarParkingPos1','wb') as f:
    pickle.dump(poslist,f)
         



while True:

  for pos in poslist:
   cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)


  cv2.imshow("image",img)
  cv2.setMouseCallback("image",mouseclick)
  cv2.waitKey()
  cv2.destroyAllWindows()
  
  
 
    



