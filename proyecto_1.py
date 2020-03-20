# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:00:44 2020

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt
from csv import reader as reader_csv
import scipy.signal as signal

class File_bci :
    def __init__(self, name, channels, hsize, time, sample_rate):
        self.name= name
        self.channels= channels
        self.hsize= hsize
        self.row_number=0
        self.header=''
        self.time=time
        self.sample_rate=sample_rate
    
    def data_open(self):
        self.data=open(self.name)
        self.lines=reader_csv(self.data)
    
    def channels(self):
        lines=self.lines
        row_number=self.row_number
        header_size=self.hsize
        header=self.header
        channels=self.channels
        data=[]
        for row in lines:
            if row_number < header_size:
                header=header+row[0]+'\n';
                row_number = row_number+1;
                print(row);
            else:
                temp=[];
                counter=0;
                for column in row:
                    if counter ==0:
                        counter = counter+1;
                        continue;
                    elif counter == channels+1:
                        break;
                    else: 
                        temp.append(float(column));
                        
                    counter = counter+1;
                data.append(temp);

        biosignal= np.asarray(data, order = 'C');
        self.biosignal = np.transpose(biosignal);
        
    def Graph_cg(self):
        time=self.time
        sample_rate=self.sample_rate
        points=time*sample_rate
        vtime=np.linspace(0,time+1,points)
        for i in range (8): #Importante: TENER EN CUENTA QUE HAY CANALES QUE PERTENECEN A LAS LECTURAS DE ACELEROMETROS. ¿Como saber cuantos son?
            plt.plot(vtime, self.biosignal [i,:], linewidth = 0.1); #igual para todas
        plt.title ("EEG")
        plt.show()
        
    def Graph_cgn(self, channel):
        self.channel=channel
        time=self.time
        sample_rate=self.sample_rate
        points=time*sample_rate
        vtime=np.linspace(0,time+1,points)
        plt.plot(vtime, self.biosignal [self.channel,:], linewidth = 0.1); #igual para todas
        plt.title ("EEG")
        plt.show()
        
class Files_mat:
    def __init__(self, name):
        
    
    
