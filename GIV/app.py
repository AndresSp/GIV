import os
import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse
import imutils
import random
import datetime

generatedPath = 'generated/'

def generateImages():
    filenames = []
    names = []
    filenames = glob.glob("uploads/*.jpg")
    

    for filename in filenames:
        n = os.path.basename(filename)
        h,t = os.path.splitext(n)
        names.append(h)

    images = [cv2.imread(img) for img in filenames] #Loaded to images
    

    #Rotation
    i = 0 #index
    for img in images:
        createFolder('./' + generatedPath + names[i] +'/')
        createFolder('./' + generatedPath + names[i] +'/' + 'Rotation/')
        for angle in np.arange(0, 25, 1): #Rotate 0-25
            rotated = rotate_img(img, angle)
            cv2.imwrite(str(generatedPath) + names[i] + '/' + 'Rotation' + '/' + names[i] + " - Rotated" + str(angle) + ".jpg", rotated)

        for angle in np.arange(335, 360, 1): #Rotate 0-25
            rotated = rotate_img(img, angle)
            cv2.imwrite(str(generatedPath) + names[i] + '/' + 'Rotation' + '/' + names[i] + " - Rotated" + str(angle) + ".jpg", rotated)
        i=i+1

    #Color
    i = 0 #index
    for img in images:
        createFolder('./' + generatedPath + names[i] +'/')
        createFolder('./' + generatedPath + names[i] +'/' + 'Color/')
        for  k in range(0, 4):
            for f in range(6, 9, 1):
                f = f / 10.0
                img = color_img(img, k, f)
                cv2.imwrite(str(generatedPath) + names[i] + '/' + 'Color' + '/' + names[i] + " - Colored" + str(k) + str(f) +".jpg", img)
        i=i+1

    #Perspective
    i = 0 #index
    for img in images:
        createFolder('./' + generatedPath + names[i] +'/')
        createFolder('./' + generatedPath + names[i] +'/' + 'Perspective/')
        for p in range(6, 9, 1):
            p = p/10.0
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[i] + '/' + 'Perspective' + '/' + names[i] + " - Perspective" + str(p) +".jpg", img)
            p = p + 0.5
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[i] + '/' + 'Perspective' + '/' + names[i] + " - Perspective" + str(p) +".jpg", img)
        i=i+1
    
    #Rotation-Color
    imagesRC = []
    for img in images:
        for angle in np.arange(0, 25, 1):
            imagesRC.append(rotate_img(img, angle))
        
        for angle in np.arange(335, 360, 1):
            imagesRC.append(rotate_img(img, angle))
    
    for img in imagesRC:
        createFolder('./' + generatedPath + names[0] +'/')
        createFolder('./' + generatedPath + names[0] +'/' + 'Rotation-Color/')
        for  k in range(0, 4):
            for f in range(6, 9, 1):
                f = f / 10.0
                img = color_img(img, k, f)
                cv2.imwrite(str(generatedPath) + names[0] + '/' + 'Rotation-Color' + '/' + str(datetime.datetime.now().timestamp()) + str(np.random.randint(low=1, high=10000)) +".jpg", img)
    
    #Rotation-Perspective
    imagesRC = []
    for img in images:
        for angle in np.arange(0, 25, 1):
            imagesRC.append(rotate_img(img, angle))
        
        for angle in np.arange(335, 360, 1):
            imagesRC.append(rotate_img(img, angle))

    for img in imagesRC:
        createFolder('./' + generatedPath + names[0] +'/')
        createFolder('./' + generatedPath + names[0] +'/' + 'Rotation-Perspective/')
        for p in range(6, 9, 1):
            p = p/10.0
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[0] + '/' + 'Rotation-Perspective' + '/' + str(datetime.datetime.now().timestamp()) + str(np.random.randint(low=1, high=10000)) +".jpg", img)
            p = p + 0.5
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[0] + '/' + 'Rotation-Perspective' + '/' + str(datetime.datetime.now().timestamp()) + str(np.random.randint(low=1, high=10000)) +".jpg", img)
    
    #Color-Perspective
    imagesCP = []
    createFolder('./' + generatedPath + names[0] +'/')
    createFolder('./' + generatedPath + names[0] +'/' + 'Color-Perspective/')
    
    for img in images:
        for  k in range(0, 4):
            for f in range(6, 9, 1):
                f = f / 10.0
                imagesCP.append(color_img(img, k, f))
    
    for img in imagesCP:
        for p in range(6, 9, 1):
            p = p/10.0
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[0] + '/' + 'Color-Perspective' + '/' + str(datetime.datetime.now().timestamp()) + str(np.random.randint(low=1, high=10000)) +".jpg", img)
            p = p + 0.5
            img = perspective_img(img, p)
            cv2.imwrite(str(generatedPath) + names[0] + '/' + 'Color-Perspective' + '/' + str(datetime.datetime.now().timestamp()) + str(np.random.randint(low=1, high=10000)) +".jpg", img)




def perspective_img(image, percentage):
    width = round(image.shape[1] *percentage)
    height = image.shape[0] # keep original height
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return image

def color_img(image, const, range):
    mask = cv2.applyColorMap(image, const)
    image = cv2.addWeighted(image,range,mask,1-range,0)
    return image



def rotate_img(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    return cv2.warpAffine(image, M, (nW, nH))

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

generateImages()

