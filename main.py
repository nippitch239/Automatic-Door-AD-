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




class OCR:
       
    def __init__(self, modelFile, labelFile): 
           
        self.model_file = modelFile 
        self.label_file = labelFile 
        self.label = self.load_label(self.label_file) 
        self.graph = self.load_graph(self.model_file) 
        self.sess = tf.compat.v1.Session(graph=self.graph,  
                                         config=tf.compat.v1.ConfigProto()) 
   
    def load_graph(self, modelFile): 
           
        graph = tf.Graph() 
        graph_def = tf.compat.v1.GraphDef() 
           
        with open(modelFile, "rb") as f: 
            graph_def.ParseFromString(f.read()) 
           
        with graph.as_default(): 
            tf.import_graph_def(graph_def) 
           
        return graph 
   
    def load_label(self, labelFile): 
        label = [] 
        proto_as_ascii_lines = tf.io.gfile.GFile(labelFile).readlines()