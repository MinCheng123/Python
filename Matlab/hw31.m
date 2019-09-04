clc 
clear all
% [xTrain, tTrain, xValid, tValid, xTest, tTest] = LoadMNIST(1);
% save('xTrain.mat')
% save('tTrain.mat')
% save('xValid.mat')
% save('tValid.mat')
% save('xTest.mat')
% save('tTest.mat')
load('xTrain.mat')
load('tTrain.mat')
load('xValid.mat')
load('tValid.mat')
load('xTest.mat')
load('tTest.mat')
lr=0.3;
mb=10;
mu=size(xTrain,2);
xtrain=zeros(size(xTrain,1),1);
x_shuffle=zeros(size(xTrain));
t_shuffle=zeros(size(tTrain));
epoch=30;
w1=normrnd(0,1/sqrt(784*10),10,784);
theta1=zeros(10,1);
error_train=zeros(epoch,1);
error_test=zeros(epoch,1);
for i=1:size(xTrain,2)
    xtrain=xtrain+xTrain(:,i);
end
xtrain_mean=xtrain/size(xTrain,2);
X=zeros(size(xTrain));
for i=1:size(xTrain,2)
    X(:,i)=xTrain(:,i)-xtrain_mean;
end
%%
for k=1:epoch
    start=1;
    shuffle = randperm(mu); 
    for L = 1:mu
        x_shuffle(:,L) = X(:,shuffle(L));  
        t_shuffle(:,L) = tTrain(:,shuffle(L));
    end
    for j=1:size(xTrain,2)/mb
        delta_theta=0;
        delta_batch=zeros(10,1);
        for i=start:start+mb-1
            b1 = w1*x_shuffle(:,i)-theta1;
            v1=1./(1+exp(-b1));    
            pred=find(v1==max(v1));
            target=find(t_shuffle(:,i)==max(t_shuffle(:,i)));
            if pred~=target
                error_train(k)=error_train(k)+1;
            end            
            ds=(exp(-b1))./((1+exp(-b1)).^2); % ds
            delta1=(t_shuffle(:,i)-v1).*ds;
            delta_theta=delta_theta+delta1;     % update theta
            delta_batch=delta_batch+delta1*x_shuffle(:,i)';
        end
        start=start+mb;
        dtheta=lr*delta_theta;
        delta_batch=lr*delta_batch;
        w1=w1+delta_batch;
        theta1=theta1-dtheta;  
    end 
    for m=1:size(xTest,2)
        b1 = w1*xTest(:,m)-theta1;
        v1=1./(1+exp(-b1));    
        pred=find(v1==max(v1));
        target=find(tTest(:,m)==max(tTest(:,m)));
        if pred~=target
           error_test(k)=error_test(k)+1;
        end            
    end
    error_train(k)=error_train(k)/50000
    error_test(k)=error_test(k)/10000
end

%% test

