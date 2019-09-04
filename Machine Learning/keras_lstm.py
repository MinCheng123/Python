# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:10:49 2019

@author: MIN
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

import keras.backend as K
from keras.callbacks import ReduceLROnPlateau, ModelCheckpoint
from keras.models import load_model

from keras import backend as K
K.tensorflow_backend._get_available_gpus()

list_max_size=0
list_1dim=[]
list_2dim=[]
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
# collect all the csv file data to a list
csv_failed=[]
csv_pass=[]
for (root,dirs,files) in os.walk('D:\SeqGan\Logs\Log files', topdown=True): 

    if root.endswith(("Passed")):
        for loop in range(len(files)):
            if files[loop].endswith((".csv")):
                with open(root+'/'+files[loop], 'r') as csvfile:
                    contents=csvfile.read()   # contents type:str use contents.split() convert to list
                    csv_pass.append(contents.split())
    if root.endswith(("Failed")):
        for loop in range(len(files)):
            if files[loop].endswith((".csv")):
                with open(root+'/'+files[loop], 'r') as csvfile:
                    contents=csvfile.read()   # contents type:str use contents.split() convert to list
                    csv_failed.append(contents.split())  
# collect all the csv file data to a list
csv_fake=[]

for (root,dirs,files) in os.walk('D:/SeqGan/generate', topdown=True): 
    for loop in range(len(files)):
        if files[loop].endswith((".csv")):
            with open(root+'/'+files[loop], 'r') as csvfile:
                contents=csvfile.read()   # contents type:str use contents.split() convert to list
                if len(contents.split())> 99:
                    csv_fake.append(contents.split())
print(len(csv_pass))
print(len(csv_failed))
print(len(csv_fake))
csv_failed_np=np.array(csv_failed)
csv_pass_np=np.array(csv_pass)
csv_fake_np=np.array(csv_fake)
print(csv_failed_np.shape)
print(csv_pass_np.shape)
print(csv_fake_np.shape)
# quantify data as dictionary indices
csv_pass_quantified=csv_pass_np
for case, cases in enumerate(csv_pass):
    for step,steps in enumerate(csv_pass[case]):
        #print('function:',csv_pass[case][step])
        #print('my_dict',my_dict[csv_pass[case][step]])
        csv_pass_quantified[case][step]=my_dict[csv_pass[case][step]]+1 # frist function is zero, zeros means not updateing kind of
        #if csv_pass_quantified[case][step] == 39:
            #print('yes!!!')
            #print(csv_pass_quantified[case][step])
        
       # print('csv_pass_quantified', csv_pass_quantified[case][step])
       # print('csv_pass_quantified type',type(csv_pass_quantified))
csv_failed_quantified=csv_failed_np
for case, cases in enumerate(csv_failed):
    for step,steps in enumerate(csv_failed[case]):
        #print(case ,step)
        #print('function:',csv_failed[case][step])
        #print('my_dict',my_dict[csv_failed[case][step]])
        
        csv_failed_quantified[case][step]=my_dict[csv_failed[case][step]]+1
        #print(my_dict[csv_failed[case][step]]+1)
        #print('csv_failed_quantified', csv_failed_quantified[case][step])
        #print('csv_failed_quantified type',type(csv_failed_quantified))
csv_fake_quantified=csv_fake_np
for case, cases in enumerate(csv_fake):
    for step,steps in enumerate(csv_fake[case]):
        #print(case ,step)
        #print('function:',csv_failed[case][step])
        #print('my_dict',my_dict[csv_failed[case][step]])
        
        csv_fake_quantified[case][step]=my_dict[csv_fake[case][step]]+1
        #print(my_dict[csv_failed[case][step]]+1)
        #print('csv_failed_quantified', csv_failed_quantified[case][step])
        #print('csv_failed_quantified type',type(csv_failed_quantified))
#print('Pad sequences (samples x time)')
y_fail=np.zeros((len(csv_failed)-1,1),dtype=int) # x_fail first element is empty
y_pass=np.ones((len(csv_pass),1),dtype=int)
y_fake=np.zeros((len(csv_fake),1),dtype=int)

x_train_fail = sequence.pad_sequences(csv_failed_quantified, maxlen=300)
x_train_pass = sequence.pad_sequences(csv_pass_quantified, maxlen=300)
x_train_fake = sequence.pad_sequences(csv_fake_quantified, maxlen=300)

# file = 'D:/SeqGan/SeqGAN-PyTorch/generator_sample.txt'
file = 'D:/LeakGAN-python3/Synthetic Data/save/generator_sample.txt'

with open(file, 'r') as f:
    lines = f.readlines()
LeakGan = []
for line in lines:
    l = line.strip().split(' ')
    l = [int(s) for s in l]
    LeakGan.append(l)

LeakGan=np.array(LeakGan)
LeakGan=np.array(LeakGan)
LeakGan_padded = sequence.pad_sequences(LeakGan[0:5000], maxlen=300)
x_train_fake=LeakGan_padded


print('x_train_fake',x_train_fake.shape)

x_train_pass_random, useless1, y_train,useless =train_test_split(x_train_pass, y_pass,test_size=0.001, shuffle=True)
print(len(x_train_pass_random))
print(len(y_train))

x_train_fail= np.delete(x_train_fail, (0), axis=0)
x_dataset=np.concatenate((x_train_pass_random[0:(len(x_train_fake))],x_train_fake), axis=0)
x_dataset_len=len(x_dataset)
y_dataset=np.concatenate((y_pass[0:len(x_train_fake)],y_fake[0:len(x_train_fake)]),axis=0)



x_pre_train, x_val, y_pre_train, y_val =train_test_split(x_dataset,y_dataset,test_size=0.10, shuffle=True)

print('x_pre_train',x_pre_train.shape, y_pre_train.shape)
print('x_val',x_val.shape)
# file = 'D:/SeqGan/SeqGAN-PyTorch/generator_sample.txt'



#x_dataset=np.concatenate((x_train_pass_random[x_dataset_len:(x_dataset_len+len(x_train_fake))],x_train), axis=0)
#print('x_train no fake data', x_dataset.shape)

#y_dataset=np.concatenate((y_pass[x_dataset_len:(x_dataset_len+len(x_train_fake))],y_train),axis=0)



x_dataset=np.concatenate((x_train_pass_random[len(x_train_fake):(len(x_train_fake)+len(x_train_fail))],x_train_fail), axis=0)
y_dataset=np.concatenate((y_pass[0:len(x_train_fail)],y_fake[0:len(x_train_fail)]),axis=0)
print('x_train_pass shape:', x_train_pass.shape)
print('x_train_fail shape:', x_train_fail.shape)
print('x_train_fail',x_train_fail)
print('x_train_fail type:', type(x_train_fail))
print('x_train shape', x_dataset.shape)
print('y_dataset shape',y_dataset.shape)
print('x_dataset', x_dataset[5])
#print(y_dataset[4000:4500])
#print(y_dataset[6000:6100])




x_train, x_test, y_train, y_test =train_test_split(x_dataset,y_dataset,test_size=0.20, shuffle=True)
print('x_train shape',x_train.shape)
print('x_test shape',x_test.shape)
print('y_train:\n', y_train)
print('y_train shape', y_train.shape)

max_features = 40 # max dictionary value +1
batch_size = 32   # recommend small batch size
####################################################
SEED= 88
Gaussian=keras.initializers.RandomNormal(mean=0.0, stddev=0.05, seed=SEED)
##############################################
a=Input(shape=(300,))
x=Embedding(max_features, 40,embeddings_initializer=Gaussian)(a)
x=LSTM(90,dropout=0.2, recurrent_dropout=0.2,kernel_initializer=Gaussian,recurrent_initializer=Gaussian,)(x)
#x=BatchNormalization()(x)
x=Dense(1, activation='sigmoid',kernel_initializer=Gaussian, bias_initializer=Gaussian,)(x)
model = Model(inputs=a, outputs=x)
opt=optimizers.Nadam(lr=0.015,beta_1=0.9, beta_2=0.999, epsilon=None, schedule_decay=0.001)  # this optimizers works best learning rate 0.0004
model.compile(loss='binary_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])


model.summary()
#
# the result is quite strange need to be disccused, it increase and vastly decrease repeatly
def create_model_checkpoint(dir, model_name):
    filepath = dir + '/' + model_name + ".h5" 
    directory = os.path.dirname(filepath)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    checkpointer = ModelCheckpoint(filepath=filepath, verbose=1, save_best_only=True)
    return checkpointer

checkpointer = create_model_checkpoint('D:/SeqGan/generate', 'data_augmentaion_4_12_pretrain')


print('Pre-Train...')

change_lr=ReduceLROnPlateau(monitor='val_loss', factor=0.7, patience=4, verbose=1, mode='auto', min_delta=0.0001, cooldown=0, min_lr=0)
earlyStopping = keras.callbacks.EarlyStopping(monitor='loss', patience=7, verbose=1, mode='auto',restore_best_weights=False)
history = model.fit(x_pre_train, y_pre_train,
          batch_size=batch_size,
          epochs=50,
          shuffle=True,
          verbose=1,
          #validation_data=(x_test, y_test),
          validation_split=0.2,
          callbacks=[change_lr,checkpointer],
            )
#model=load_model('D:/SeqGan/generate/data_augmentaion_4_02_lstm_emb_40_.h5') 
score, acc = model.evaluate(x_val, y_val,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
model.save('D:/SeqGan/generate/lstm90_embedd40_40_lrDynamic_04_12.h5')
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
#plt.plot(history.history['val_recall'])
#plt.plot(history.history['val_precision'])
plt.title('Model pretrain accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validate'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model pretain loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

print('Train...')
checkpointer2 = create_model_checkpoint('D:/SeqGan/generate', 'data_augmentaion_4_12_train2')
history = model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=150,
          shuffle=True,
          verbose=1,
          #validation_data=(x_test, y_test),
          validation_split=0.2,
          callbacks=[change_lr,checkpointer2],
            )
#model=load_model('D:/SeqGan/generate/data_augmentaion_4_08_lstm_emb_40_.h5') 
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
model.save('D:/SeqGan/generate/train_original_epoch_100_4_12.h5')
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
#plt.plot(history.history['val_recall'])
#plt.plot(history.history['val_precision'])
plt.title('Model refine accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validate'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model refine loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validate'], loc='upper left')
plt.show()
