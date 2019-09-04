clc
clear all
% [xTrain3, tTrain3, xValid3, tValid3, xTest3, tTest3] = LoadMNIST(3);
% save('xTrain3.mat')
% save('tTrain3.mat')
% save('xValid3.mat')
% save('tValid3.mat')
% save('xTest3.mat')
% save('tTest3.mat')
load('xTrain3.mat')
load('tTrain3.mat')
load('xValid3.mat')
load('tValid3.mat')
load('xTest3.mat')
load('tTest3.mat')
%%
layers1 = [ 
    imageInputLayer([28 28 1])
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];
%%
opts = trainingOptions('sgdm', ...
    'Momentum',0.9,...
    'InitialLearnRate',0.01,...
    'MaxEpochs',200, ...
    'MiniBatchSize',8192,...
    'ValidationPatience',5,...
    'ValidationFrequency',30,...
    'Shuffle', 'every-epoch',...
    'Plots','training-progress', ...
    'Verbose',false, ...
    'ExecutionEnvironment','gpu',...
    'ValidationData',{xValid3,tValid3});
net = trainNetwork(xTrain3,tTrain3,layers1,opts);
%%
error1_test=0;
result=net.classify(xTest3);
for z1=1:size(result,1)  
      if tTest3(z1,1)~=result(z1,1)
         error1_test=error1_test+1;
      end            
end
error1_test = error1_test/size(result,1)  
%%
error1_train=0;
result=net.classify(xTrain3);
for z1=1:size(result,1)  
      if tTrain3(z1,1)~=result(z1,1)
         error1_train=error1_train+1;
      end            
end
error1_train = error1_train/size(result,1)  
%%
layers2 = [ 
    imageInputLayer([28 28 1])
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(100)
    reluLayer
    fullyConnectedLayer(10)
    softmaxLayer
    classificationLayer];
%%
opts = trainingOptions('sgdm', ...
    'Momentum',0.9,...
    'InitialLearnRate',0.01,...
    'MaxEpochs',200, ...
    'MiniBatchSize',8192,...
    'ValidationPatience',5,...
    'ValidationFrequency',30,...
    'Shuffle', 'every-epoch',...
    'Plots','training-progress', ...
    'Verbose',false, ...
    'ExecutionEnvironment','gpu',...
    'ValidationData',{xValid3,tValid3});
net = trainNetwork(xTrain3,tTrain3,layers2,opts);
%%
error2_test=0;
result=net.classify(xTest3);
for z1=1:size(result,1)  
      if tTest3(z1,1)~=result(z1,1)96
         error2_test=error2_test+1;
      end            
end
error2_test= error2_test/size(result,1)  
%%
error2_train=0;
result=net.classify(xTrain3);
for z1=1:size(result,1)  
      if tTrain3(z1,1)~=result(z1,1)
         error2_train=error2_train+1;
      end            
end
error2_train= error2_train/size(result,1)  
%%
opts = trainingOptions('sgdm', ...
    'Momentum',0.9,...
    'InitialLearnRate',0.01,...
    'MaxEpochs',200, ...
    'MiniBatchSize',8192,...
    'ValidationPatience',5,...
    'ValidationFrequency',30,...
    'Shuffle', 'every-epoch',...
    'Plots','training-progress', ...
    'Verbose',false, ...
    'L2Regularization',0.03,...
    'ExecutionEnvironment','gpu',...
    'ValidationData',{xValid3,tValid3});
net = trainNetwork(xTrain3,tTrain3,layers1,opts);
%%
error3_test=0;
result=net.classify(xTest3);
for z1=1:size(result,1)  
      if tTest3(z1,1)~=result(z1,1)
         error3_test=error3_test+1;
      end            
end
error3_test= error3_test/size(result,1)  

error3_train=0;
result=net.classify(xTrain3);
for z1=1:size(result,1)  
      if tTrain3(z1,1)~=result(z1,1)
         error3_train=error3_train+1;
      end            
end
error3_train= error3_train/size(result,1)  
