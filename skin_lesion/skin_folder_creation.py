# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:49:10 2021

@author: mob
"""

from PIL import Image
from tqdm import tqdm

import tifffile as tiff
import os
import numpy as np
import shutil
import torch

def rm_mk_folders(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)

def split_folders(folder,seed=23,ratio=(0.80,0.1,0.1)):
    '''
    folder contains both images folder and masks folder
    
    '''
    
    l = os.listdir(folder+"\\images\\")
    
    train_img_folder = folder+"\\images\\train\\"
    train_mask_folder = folder+"\\masks\\train\\"
    val_img_folder = folder+"\\images\\val\\"
    val_mask_folder = folder+"\\masks\\val\\"
    test_img_folder = folder+"\\images\\test\\"
    test_mask_folder = folder+"\\masks\\test\\"
       
    rm_mk_folders(train_img_folder)
    rm_mk_folders(train_mask_folder)
    rm_mk_folders(val_img_folder)
    rm_mk_folders(val_mask_folder)
    rm_mk_folders(test_img_folder)
    rm_mk_folders(test_mask_folder)
    
    train_list = l[:int(len(l)*ratio[0])]
    val_list = l[int(len(l)*ratio[0]):int(len(l)*ratio[0]+len(l)*ratio[1])]
    test_list = l[int(len(l)*ratio[0]+len(l)*ratio[1]):]    
    
    
    try:
        for train_idx in tqdm(train_list):
            os.replace(folder+"\\images\\"+train_idx,
                       folder+"\\images\\train\\"+train_idx)
            os.replace(folder+"\\masks\\"+train_idx.split(".")[0]+"_Segmentation.png",
                       folder+"\\masks\\train\\"+train_idx.split(".")[0]+"_Segmentation.png")
    except:
        return train_idx,train_list
    
    try:
        for val_idx in tqdm(val_list):
            os.replace(folder+"\\images\\"+val_idx,
                       folder+"\\images\\val\\"+val_idx)
            os.replace(folder+"\\masks\\"+val_idx.split(".")[0]+"_Segmentation.png",
                       folder+"\\masks\\val\\"+val_idx.split(".")[0]+"_Segmentation.png")
    except:
        return val_idx,val_list
    
    try:        
        for test_idx in tqdm(test_list):
            os.replace(folder+"\\images\\"+test_idx,
                       folder+"\\images\\test\\"+test_idx)
            os.replace(folder+"\\masks\\"+test_idx.split(".")[0]+"_Segmentation.png",
                       folder+"\\masks\\test\\"+test_idx.split(".")[0]+"_Segmentation.png")   
    except:
        return test_idx,test_list

