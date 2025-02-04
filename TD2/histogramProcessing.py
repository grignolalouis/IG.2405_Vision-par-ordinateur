# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:08:35 2025

@author: fross
"""

import numpy as np
import matplotlib.pyplot as plt


def myHistogram(im,normalize=True):
    
    N=256
    Hist = np.zeros(N)
    Bins = np.arange(N)
    try:
        assert im.dtype == np.float64 or im.dtype == np.uint8
        
        if im.dtype == np.float64:
            im = -- to be completed
            Bins -- to be completed
        H,W = im.shape
        for i in range(H):
            for j in range(W):
                Hist[-- to be completed] = -- to be completed
        if normalize:
            Hist = -- to be completed
    except AssertionError:
        print('ERROR myHistogram : invalid dtype for im (uint8 or float)')
    
    return Hist,Bins


def myCumulatedHistogram(im):
    
    N=256
    HistC = np.zeros(N)   
    Bins = np.arange(N)
    try:
        assert im.dtype == np.float64 or im.dtype == np.uint8
        
        Hist,Bins=myHistogram(im)
        for k in range(len(Hist)):
            HistC[-- to be completed]= -- to be completed
            
    except AssertionError:
        print('ERROR myHistogram : invalid dtype for im (uint8 or float)')
    
    return HistC,Bins


def myCalibration(im0,p=0.0):
    
    imc = np.empty_like(im0)
    
    try:
        p = float(p)
        assert p>=0 and p<=1 and (im0.dtype == np.float64 or im0.dtype == np.uint8)
        if im0.dtype == np.uint8:
            im = -- to be completed
        else:
            im = -- to be completed
                
            
        if p==0.0:
            minVal = -- to be completed
            maxVal = -- to be completed
        else:
            HistC,BinsC = myCumulatedHistogram(im)
            
            minVal = -- to be completed
            maxVal = -- to be completed
        
        imc = -- to be completed

        
        if im0.dtype == np.uint8:
            imc = np.round(imc*255)
            imc = np.ndarray.astype(imc,np.uint8)
        
    except AssertionError:
        if p<0 or p>1:
            print('ERROR myCalibration : invalid value for p (in [0,1])')
        if im0.dtype != np.float64 and im0.dtype != np.uint8:
            print('ERROR myCalibration : invalid type for im (float64 or uint8)')   
            
    return imc



def myEqualization(im0):
    
    imc = np.empty_like(im0)
    N = 256   

    try:
        assert im0.dtype == np.float64 or im0.dtype == np.uint8
        
        if im0.dtype == np.float64:
            im = -- to be completed
            im = -- to be completed
        else:
            im = im0
        
        H,BinsC = myCumulatedHistogram(im)
        T = -- to be completed          
        H,W  = im.shape
        for i in range(H):
            for j in range(W):
                imc[i,j] = -- to be completed
        
        if im0.dtype == np.float64:
            imc = -- to be completed
            T = -- to be completed
            
    except AssertionError:

        if im0.dtype != np.float64 and im0.dtype != np.uint8:
            print('ERROR myEqualization : invalid type for im (float64 or uint8)')      
            
    return imc,T



