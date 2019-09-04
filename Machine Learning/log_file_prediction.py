# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 13:07:17 2019

@author: min.cheng
"""
from __future__ import print_function
import re
import os
import numpy as np
import pandas as pd
from collections import Counter
import csv
from keras.models import model_from_json
from keras.preprocessing import sequence
from keras.models import Sequential,Model
from keras.layers import Dense, Embedding,BatchNormalization,Input
from keras.layers import LSTM
from keras.datasets import imdb
#import import_ipynb
#import logfile_extraction 
from sklearn.model_selection import train_test_split
from keras import optimizers
import matplotlib.pyplot as plt
import keras 
import keras_metrics
import keras.backend as K
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from keras.models import load_model
from keras.callbacks import LambdaCallback
path_spec_fail= 'C:\MasterThesis\document\Logs/Mars 6 (extli) balder/Failed'


my_dict={'extli.light_switch_off()': 0,
 'extli.verify_brake_lights_off()': 1,
 'extli.verify_rear_fog_light_off()': 2,
 'extli.light_switch_auto()': 3,
 'extli.verify_indicate_right_on()': 4,
 'extli.push_hazard_button()': 5,
 'extli.verify_indicate_off()': 6,
 'extli.verify_rear_fog_light_on()': 7,
 'extli.light_switch_lowbeam()': 8,
 'driver.usage_mode_convenience()': 9,
 'extli.light_switch_position()': 10,
 'driver.press_brake()': 11,
 'driver.release_brake()': 12,
 'extli.verify_light_switch_position()': 13,
 'driver.usage_mode_active()': 14,
 'extli.release_turn_stalk()': 15,
 'extli.verify_light_switch_auto()': 16,
 'extli.verify_brake_lights_on()': 17,
 'extli.verify_front_fog_light_on()': 18,
 'extli.verify_low_beam_on()': 19,
 'extli.rear_fog_light()': 20,
 'extli.indicate_neutral()': 21,
 'extli.pull_turn_stalk()': 22,
 'extli.front_fog_light()': 23,
 'extli.verify_indicate_left_on()': 24,
 'driver.verify_usage_mode_driving()': 25,
 'extli.indicate_right()': 26,
 'driver.verify_usage_mode_convenience()': 27,
 'extli.verify_light_switch_off()': 28,
 'extli.indicate_left()': 29,
 'driver.verify_usage_mode_inactive()': 30,
 'driver.verify_usage_mode_active()': 31,
 'driver.usage_mode_inactive()': 32,
 'extli.verify_front_fog_light_off()': 33,
 'extli.verify_beam_shape_off()': 34,
 'driver.usage_mode_driving()': 35,
 'extli.verify_light_switch_lowbeam()': 36,
 'extli.verify_main_beam_on()': 37,
 'extli.verify_hazard_lights_on()': 38}



def csvfile_collect(path):
    csv_file=[]
    for (root,dirs,files) in os.walk(path, topdown=True): 

        for loop in range(len(files)):
            if files[loop].endswith((".csv")):
                with open(root+'/'+files[loop], 'r') as csvfile:
                    contents=csvfile.read()   # contents type:str use contents.split() convert to list
                    csv_file.append(contents.split()) 
    return csv_file 

def csvfile_collect_for_test(path):
    csv_file=[]
    for (root,dirs,files) in os.walk(path, topdown=True): 
        file_list=files
        for loop in range(len(files)):
            if files[loop].endswith((".csv")):
                with open(root+'/'+files[loop], 'r') as csvfile:
                    contents=csvfile.read()   # contents type:str use contents.split() convert to list
                    csv_file.append(contents.split()) 
    return csv_file,file_list 


def quantify_data(csv_file):
    csv_quantified=np.array(csv_file)
    for case, cases in enumerate(csv_file):
        for step,steps in enumerate(csv_file[case]):
            csv_quantified[case][step]=my_dict[csv_file[case][step]]+1 # frist function is zero 

    return csv_quantified
###################################################################################
passed=0
failed=0
threshold=0.4  # threshold for prediction
fail_index=[]

model = load_model('C:\MasterThesis\python\model_saved/lstm90_embedd40_40_lrDynamic_2019_03_01_batch60_maskzero_True_changed_Dictionaryvalue_Mars3included.h5') # specify which trained model needs to be loaded

path_spec_fail= 'C:\MasterThesis\document\Logs/Dec 5 exist\Failed' # specify the log-file which need to be predicted
path_spec_pass= 'C:\MasterThesis\document\Logs/Dec 5 exist\Passed' 

csv_file_fail =csvfile_collect(path_spec_fail)
csv_file_pass =csvfile_collect(path_spec_pass)

csv_file_quantify_pass=quantify_data(csv_file_pass)
csv_file_quantify_fail=quantify_data(csv_file_fail)
maxlength=300
csv_file_quantified_pass=sequence.pad_sequences(csv_file_quantify_pass, maxlen=maxlength)
csv_file_quantified_fail=sequence.pad_sequences(csv_file_quantify_fail, maxlen=maxlength)

csv_test,csv_test_name= csvfile_collect_for_test(path_spec_fail)

prediction_test=model.predict(csv_file_quantified_pass, batch_size=None, verbose=0, steps=None) # prediction output



for j,i in enumerate(prediction_test):
        if i>threshold:
            passed+=1
        else:
            failed+=1
            fail_index.append(j)

print(fail_index)
fail_name=[]            
for i in fail_index:
    fail_name.append(csv_test_name[i*2])
print(fail_name)  
csv_file_fail,csv_file_fail_name =csvfile_collect_for_test(path_spec_fail)

for i,j in enumerate(csv_file_fail_name): 
    if j.endswith((".txt")): 
        csv_file_fail_name.pop(i)

#print(fail_name)
print(' predict fail_name:', len(fail_name),fail_name)
print('actual fail function size :', len(csv_file_fail_name) )
print('actual fail function name :', csv_file_fail_name)
#if len(common_name)<len(fail_name):
common_name=list(fail_name and csv_file_fail_name)