clc 
clear all
% [xTrain2, tTrain2, xValid2, tValid2, xTest2, tTest2] = LoadMNIST(1);
% save('xTrain2.mat')
% save('tTrain2.mat')
% save('xValid2.mat')
% save('tValid2.mat')
% save('xTest2.mat')
% save('tTest2.mat')
load('xTrain2.mat')
load('tTrain2.mat')
load('xValid2.mat')
load('tValid2.mat')
load('xTest2.mat')
load('tTest2.mat')
lr=3*10^-3;
mb=10;
mu=size(xTrain2,2);
xtrain=zeros(size(xTrain2,1),1);
x_shuffle=zeros(size(xTrain2));
t_shuffle=zeros(size(tTrain2));
epoch=50;
error_train=zeros(epoch,1);
U=cell(5,epoch);
for i=1:size(xTrain2,2)
    xtrain=xtrain+xTrain2(:,i);
end
mean=xtrain/size(xTrain2,2);
for i=1:size(xTrain2,2)
    xTrain2(:,i)=xTrain2(:,i)-mean;
end
layer_size=6; % input+4hidden+output
w =cell(layer_size-1,1);
b =cell(layer_size-1,1);
v =cell(layer_size,1);
neuron_per_layer=[784 30 30 30 30 10];
energy=zeros(epoch,size(xTrain2,2));
Energy=zeros(epoch,1);
for i=1:size(neuron_per_layer,2)-1
    w{i}=normrnd(0,1/sqrt(neuron_per_layer(i)),neuron_per_layer(i+1),neuron_per_layer(i));
    theta{i}=zeros(neuron_per_layer(i+1),1);
end
delta=cell(layer_size-1,1);
delta_theta=cell(layer_size-1,1);
delta_w=cell(layer_size-1,1);
for k=1:epoch
    start=1;
    shuffle = randperm(mu); 
    for L = 1:mu
        x_shuffle(:,L) = xTrain2(:,shuffle(L));  
        t_shuffle(:,L) = tTrain2(:,shuffle(L));
    end
    for j=1:size(xTrain2,2)/mb
            for i2=1:size(delta,1)
                delta{i2}=[];
                delta_theta{i2}=[];
                delta_w{i2}=[];
            end     
            for i=start:start+mb-1
                v{1}=x_shuffle(:,i);
                for n=1:size(w,1)
                    b{n}= w{n}*v{n}-theta{n};
                    v{n+1}=1./(1+exp(-b{n}));
                end        
               % pred=find(v{end}==max(v{end}));
               % target=find(t_shuffle(:,i)==max(t_shuffle(:,i)));
               % if pred~=target
               %    error_train(k,1)=error_train(k,1)+1;
               % end   
                for h=layer_size-1:-1:1
                    if h==layer_size-1
                       g_prim=(exp(-b{h}))./((1+exp(-b{h})).^2); % ds
                       delta{h}=(t_shuffle(:,i)-v{end}).*g_prim;
                    else
                       g_prim=(exp(-b{h}))./((1+exp(-b{h})).^2);
                       delta{h}=((delta{h+1}'*w{h+1}))'.*g_prim;              
                    end   
                end  
                for H=1:size(delta,1)
                    if i==start
                       delta_theta{H}=zeros(size(delta(H)));
                       delta_w{H}=zeros(size(delta{H}*v{H}'));
                    end
                    delta_theta{H}=delta_theta{H}+delta{H};
                    delta_w{H}=delta_w{H}+delta{H}*v{H}';
                end 
            end  
            for g=1:size(delta_w,1)
                w{g}=w{g}+lr*delta_w{g};         
                theta{g}=theta{g}-lr*delta_theta{g};
            end
            start=start+mb;    
    end 
   for T=1:size(xTrain2,2)
       v{1}=xTrain2(:,T);
       for n=1:size(w,1)
           b{n}= w{n}*v{n}-theta{n};
           v{n+1}=1./(1+exp(-b{n}));
       end       
       energy(k,T)=(t_shuffle(:,T)-v{end})'*(t_shuffle(:,T)-v{end});    
   end
 %  a=0.5*sum(energy,2);
   for abc=1:size(delta,1)
       U{abc,k}=norm(delta{abc});
   end
end
%%
Energy=0.5*sum(energy,2);
subplot(2,1,1)
semilogy([1:1:50]',Energy),title('case4')
xlabel('epochs');
x=linspace(1,50,50);
u1=zeros(size(U));
for i=1:size(U,1)
    for j=1:size(U,2)
        u1(i,j)=U{i,j};
    end
end
subplot(2,1,2)
semilogy([1:1:50],u1(2,:),[1:1:50],u1(2,:),[1:1:50],u1(3,:),[1:1:50],u1(4,:),[1:1:50],u1(5,:)),title('U')
xlabel('epochs');