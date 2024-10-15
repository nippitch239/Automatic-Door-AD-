import cv2
import numpy as np
from skimage.filters import threshold_local
import tensorflow as tf
from skimage import measure
import imutils
import os 
   
def sort_cont(character_contours): 
    """ 
    To sort contours 
    """
    i = 0
    boundingBoxes = [cv2.boundingRect(c) for c in character_contours] 
       
    (character_contours, boundingBoxes) = zip(*sorted(zip(character_contours,boundingBoxes),key = lambda b: b[1][i],reverse = False))
       
    return character_contours