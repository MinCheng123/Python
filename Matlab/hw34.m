clc 
clear all
% [xTrain4, tTrain4, xValid4, tValid4, xTest4, tTest4] = LoadMNIST(4);
% save('xTrain4.mat')
% save('tTrain4.mat')
% save('xValid4.mat')
% save('tValid4.mat')
% save('xTest4.mat')
% save('tTest4.mat')
load('xTrain4.mat')
load('tTrain4.mat')
load('xValid4.mat')
load('tValid4.mat')
load('xTest4.mat')
load('tTest4.mat')
%%
layers1 = [ 
    imageInputLayer([28 28 1])
    convolution2dLayer(5,20,'Stride',1,'Padding',1)
    reluLayer
    maxPooling2dLayer(2,'Stride',2,'Padding',0)
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];

opts = trainingOptions('sgdm', ...
    'Momentum',0.9,...
    'InitialLearnRate',0.001,...
    'MaxEpochs',60, ...
    'MiniBatchSize',8192,...
    'ValidationPatience',5,...
    'ValidationFrequency',30,...
    'Shuffle', 'every-epoch',...
    'Plots','training-progress', ...
    'Verbose',false, ...
    'ExecutionEnvironment','gpu',...
    'ValidationData',{xValid4,tValid4});
net = trainNetwork(xTrain4,tTrain4,layers1,opts);
%%
error1_test=0;
result=net.classify(xTest4);
for z1=1:size(result,1)  
      if tTest4(z1,1)~=result(z1,1)
         error1_test=error1_test+1;
      end            
end
error1_test= error1_test/size(result,1)  
%%
error1_train=0;
result=net.classify(xTrain4);
for z1=1:size(result,1)  
      if tTrain4(z1,1)~=result(z1,1)
         error1_train=error1_train+1;
      end            
end
error1_train= error1_train/size(result,1)  
%%
layers2 = [ 
    imageInputLayer([28 28 1])
    
    convolution2dLayer(3,20,'Stride',1,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,30,'Stride',1,'Padding',1)
    batchNormalizationLayer
    reluLayer
    
    maxPooling2dLayer(2,'Stride',2)
    
    convolution2dLayer(3,50,'Stride',1,'Padding',1)
    batchNormalizationLayer
    reluLayer
  
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];

opts = trainingOptions('sgdm', ...
    'Momentum',0.9,...
    'InitialLearnRate',0.01,...
    'MaxEpochs',30, ...
    'MiniBatchSize',8192,...
    'ValidationPatience',5,...
    'ValidationFrequency',30,...
    'Shuffle', 'every-epoch',...
    'Plots','training-progress', ...
    'Verbose',false, ...
    'ExecutionEnvironment','gpu',...
    'ValidationData',{xValid4,tValid4});
net = trainNetwork(xTrain4,tTrain4,layers2,opts);

error2_test=0;
result=net.classify(xTest4);
for z1=1:size(result,1)  
      if tTest4(z1,1)~=result(z1,1)
         error2_test=error2_test+1;
      end            
end
error2_test= error2_test/size(result,1)  


error2_train=0;
result=net.classify(xTrain4);
for z1=1:size(result,1)  
      if tTrain4(z1,1)~=result(z1,1)
         error2_train=error2_train+1;
      end            
end
error2_train= error2_train/size(result,1)  

