import numpy as np
import cv2
import PIL
from PIL import Image
import glob
import os
path = "./"
path1 = "./org1"
os.chdir("./org1/")
imglist=glob.glob("*.jpg")
print(imglist)

for i in range(len(imglist)):
    #SIGN CROP
    image = Image.open(imglist[i])
    width, height = image.size
    box = (1750, 2950, width-150, height-200)
    cropped_image = image.crop(box)
    basewidth = 330
    
    wpercent = (basewidth / float(cropped_image.size[0]))
    hsize = int((float(cropped_image.size[1]) * float(wpercent)))
    cropped_image = cropped_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    #img.save(‘resized_image.jpg')
    
    try:
        os.mkdir("./crop-sign")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    cropped_image.save(path+"/crop-sign/"+imglist[i])
     
    face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_alt2.xml')

    eye_cascade = cv2.CascadeClassifier('../haarcascade_eye.xml')

    img = cv2.imread(imglist[i])
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        image = Image.open(imglist[i])
        width, height = image.size
        box = (x-90, y-90, x+90, y+90)
        cropped_image = image.crop(box)
        basewidth = 370
    
        wpercent = (basewidth / float(cropped_image.size[0]))
        hsize = int((float(cropped_image.size[1]) * float(wpercent)))
        cropped_image = cropped_image.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        
        try:
            os.mkdir("./crop-photo")
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        cropped_image.save(path+"/crop-photo/"+imglist[i])
cv2.imshow('img',img)
cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()
os.chdir("..")
