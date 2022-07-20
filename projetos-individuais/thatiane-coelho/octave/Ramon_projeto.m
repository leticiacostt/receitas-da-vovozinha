function Ramon_projeto()
  clear all
  global obj
  figure('Units','Normalized','Position',[0 0 1 1],'MenuBar','none','Color','w');
  axes('Units','Normalized','Position',[0.25 0.25 0.5 0.5])
  obj.pb1 = uicontrol('Style','Pushbutton','Units','Normalized','Position',[0.01 0.9 0.1 0.08],...
  'String','Acc X','FontName','Times New Roman','FontSize',16,'Callback',@importAccX,'Visible','on');
  obj.pb2 = uicontrol('Style','Pushbutton','Units','Normalized','Position',[0.15 0.9 0.1 0.08],...
  'String','Acc Y','FontName','Times New Roman','FontSize',16,'Callback',@importAccY,'Visible','off');
  obj.pb3 = uicontrol('Style','Pushbutton','Units','Normalized','Position',[0.26 0.9 0.1 0.08],...
  'String','Acc Z','FontName','Times New Roman','FontSize',16,'Callback',@importAccZ,'Visible','off');
  
function importAccX()
  global rec
  global obj
  [file,dir] = uigetfile('.txt','Importar Acc X');
  Arquivo = [dir,file];
  rec.X = dlmread(Arquivo);
  set(obj.pb2,'Visible','on')

function importAccY()
  global rec
  global obj
  [file,dir] = uigetfile('.txt','Importar Acc Y');
  Arquivo = [dir,file];
  rec.Y = dlmread(Arquivo);  
  set(obj.pb3,'Visible','on')
  
function importAccZ()
  global rec
  global obj
  [file,dir] = uigetfile('.txt','Importar Acc Z');
  Arquivo = [dir,file];
  tempo = 0:0.01:30;
  rec.Z = dlmread(Arquivo); 
  rec.X = detrend(rec.X);
  rec.Y = detrend(rec.Y);
  rec.Z = detrend(rec.Z); 
  rec.R = sqrt((rec.X).^2+(rec.Y).^2+(rec.Z).^2);
  
  [m,n] = size(rec.X);
  pkg load signal
  for i = 1:n
    zerocross.X = length(zerocrossing(tempo,rec.X(:,i)))
    zerocross.Y = length(zerocrossing(tempo,rec.Y(:,i)));
    zerocross.Z = length(zerocrossing(tempo,rec.Z(:,i)));
    zerocross.R(1,i) = zerocross.X + zerocross.Y + zerocross.Z;
  endfor
    zerocross_female_20D = mean(zerocross.R(1,1:15));    
    zerocross_male_20D = mean(zerocross.R(1,16:24));    
    zerocross_female_30D = mean(zerocross.R(1,25:40));    
    zerocross_male_30D = mean(zerocross.R(1,41:57));
    zerocross_female_40D = mean(zerocross.R(1,58:64));    
    zerocross_male_40D = mean(zerocross.R(1,65:74));
    zerocross_female_50D = mean(zerocross.R(1,75:81));    
    zerocross_male_50D = mean(zerocross.R(1,82:88));
    zerocross_female_60D = mean(zerocross.R(1,89:96));    
    zerocross_male_60D = mean(zerocross.R(1,97:102));
    zerocross_female_70D = mean(zerocross.R(1,103:109));    
    zerocross_male_70D = mean(zerocross.R(1,110:113));
    zerocross_female_80D = mean(zerocross.R(1,114:123));    
    zerocross_male_80D = mean(zerocross.R(1,124:128));
    
    zerocross_female = [zerocross_female_20D zerocross_female_30D zerocross_female_40D zerocross_female_50D zerocross_female_60D zerocross_female_70D zerocross_female_80D];
    zerocross_male = [zerocross_male_20D zerocross_male_30D zerocross_male_40D zerocross_male_50D zerocross_male_60D zerocross_male_70D zerocross_male_80D];
    zerocross_group = mean([zerocross_female;zerocross_male]);
    
  for i = 1:n
    avgRms.X(1,i) = std(rec.X(:,i));
    avgRms.Y(1,i) = std(rec.Y(:,i));
    avgRms.Z(1,i) = std(rec.Z(:,i));
    avgRms.R(1,i) = std(rec.R(:,i));
  endfor
  
  avgRms_female_20D = mean(avgRms.R(1,1:15));
  avgRms_male_20D = mean(avgRms.R(1,16:24));
  avgRms_female_30D = mean(avgRms.R(1,25:40));
  avgRms_male_30D = mean(avgRms.R(1,41:57));
  avgRms_female_40D = mean(avgRms.R(1,58:64));
  avgRms_male_40D = mean(avgRms.R(1,65:74));
  avgRms_female_50D = mean(avgRms.R(1,75:81));
  avgRms_male_50D = mean(avgRms.R(1,82:88));
  avgRms_female_60D = mean(avgRms.R(1,89:96));
  avgRms_male_60D = mean(avgRms.R(1,97:102));
  avgRms_female_70D = mean(avgRms.R(1,103:109));
  avgRms_male_70D = mean(avgRms.R(1,110:113));
  avgRms_female_80D = mean(avgRms.R(1,114:123));
  avgRms_male_80D = mean(avgRms.R(1,124:128));
  avgRms_female = [avgRms_female_20D avgRms_female_30D avgRms_female_40D avgRms_female_50D avgRms_female_60D avgRms_female_70D avgRms_female_80D];
  avgRms_male = [avgRms_male_20D avgRms_male_30D avgRms_male_40D avgRms_male_50D avgRms_male_60D avgRms_male_70D avgRms_male_80D];
  avgRms_group = mean([avgRms_female;avgRms_male]);
  
  [m,n] = size(rec.X)
  for i = 1:n
    a = 0;
    b = 1;
    for j = 1:100:m-100
      Yx = fft(rec.X(j:j+100,i));
      Yy = fft(rec.Y(j:j+100,i));
      Yz = fft(rec.Z(j:j+100,i));
      Yr = fft(rec.R(j:j+100,i));
      Ax(:,i) = abs(Yx)/length(Yx);
      Ay(:,i) = abs(Yy)/length(Yy);
      Az(:,i) = abs(Yz)/length(Yz);
      Ar(:,i) = abs(Yr)/length(Yr);
      b = b + 1;
    endfor  
  endfor
  freq = 0:100/length(Ar):100-100/length(Ar);
    
  for j = 1:n
    for i = 1:length(Ax(:,j))
      Px = sum(Ax(2:30,j));
      if sum(Ax(2:i,j))>Px/2;
        fmed.X(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
  for j = 1:n
    for i = 1:length(Ay(:,j))
      Py = sum(Ay(2:30,j));
      if sum(Ay(2:i,j))>Py/2;
        fmed.Y(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
 for j = 1:n
    for i = 1:length(Az(:,j))
      Pz = sum(Az(2:30,j));
      if sum(Az(2:i,j))>Pz/2;
        fmed.Z(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
 for j = 1:n
    for i = 1:length(Ar(:,j))
      Pr = sum(Ar(2:30,j));
      if sum(Ar(2:i,j))>Pr/2;
        fmed.R(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  fmed_female_20D = mean(fmed.R(1,1:15));
  fmed_male_20D = mean(fmed.R(1,16:24));
  fmed_female_30D = mean(fmed.R(1,25:40));
  fmed_male_30D = mean(fmed.R(1,41:57));
  fmed_female_40D = mean(fmed.R(1,58:64));
  fmed_male_40D = mean(fmed.R(1,65:74));
  fmed_female_50D = mean(fmed.R(1,75:81));
  fmed_male_50D = mean(fmed.R(1,82:88));
  fmed_female_60D = mean(fmed.R(1,89:96));
  fmed_male_60D = mean(fmed.R(1,97:102));
  fmed_female_70D = mean(fmed.R(1,103:109));
  fmed_male_70D = mean(fmed.R(1,110:113));
  fmed_female_80D = mean(fmed.R(1,114:123));
  fmed_male_80D = mean(fmed.R(1,124:128));
  age = [20:10:80];
  
  fmed_female = [fmed_female_20D fmed_female_30D fmed_female_40D fmed_female_50D fmed_female_60D fmed_female_70D fmed_female_80D];
  fmed_male = [fmed_male_20D fmed_male_30D fmed_male_40D fmed_male_50D fmed_male_60D fmed_male_70D fmed_male_80D];
  fmed_group = mean([fmed_female;fmed_male]);
  
  for j = 1:n
    for i = 1:length(Ax(:,j))
      Mx = max(Ax(2:30,j));
      if Ax(i,j)== Mx
        fpeak.X(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
  for j = 1:n
    for i = 1:length(Ay(:,j))
      My = max(Ay(2:30,j));
      if Ay(i,j)== My
        fpeak.Y(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
  for j = 1:n
    for i = 1:length(Az(:,j))
      Mz = max(Az(2:30,j));
      if Az(i,j)== Mz
        fpeak.Z(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  
  for j = 1:n
    for i = 1:length(Ar(:,j))
      Mr = max(Ar(2:30,j));
      if Ar(i,j)== Mr
        fpeak.R(1,j) = freq(1,i);
        break
      endif
    endfor
  endfor
  size(fpeak.R)
  fpeak_female_20D = mean(fpeak.R(1,1:15));
  fpeak_male_20D = mean(fpeak.R(1,16:24));
  fpeak_female_30D = mean(fpeak.R(1,25:40));
  fpeak_male_30D = mean(fpeak.R(1,41:57));
  fpeak_female_40D = mean(fpeak.R(1,58:64));
  fpeak_male_40D = mean(fpeak.R(1,65:74));
  fpeak_female_50D = mean(fpeak.R(1,75:81));
  fpeak_male_50D = mean(fpeak.R(1,82:88));
  fpeak_female_60D = mean(fpeak.R(1,89:96));
  fpeak_male_60D = mean(fpeak.R(1,97:102));
  fpeak_female_70D = mean(fpeak.R(1,103:109));
  fpeak_male_70D = mean(fpeak.R(1,110:113));
  fpeak_female_80D = mean(fpeak.R(1,114:123));
  fpeak_male_80D = mean(fpeak.R(1,124:128));
  age = [20:10:80];
  
  fpeak_female = [fpeak_female_20D fpeak_female_30D fpeak_female_40D fpeak_female_50D fpeak_female_60D fpeak_female_70D fpeak_female_80D];
  fpeak_male = [fpeak_male_20D fpeak_male_30D fpeak_male_40D fpeak_male_50D fpeak_male_60D fpeak_male_70D fpeak_male_80D];
  fpeak_group = mean([fpeak_female;fpeak_male]);
  
  subplot(2,3,1)
  bar(age,avgRms_female)
  
  subplot(2,3,2)
  bar(age,avgRms_male)
  
  subplot(2,3,3)
  bar(age,avgRms_group)
 
  
##  subplot(2,3,4)   
##  bar(age,zerocross_female)
##  
##  subplot(2,3,5)
##  bar(age,zerocross_male)
##  
##  subplot(2,3,6)
##  bar(age,zerocross_group)
##  
##  