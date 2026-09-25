% RFCAV_entrance.m, V. Ziemann, 260908
function R4=RFCAV_entrance(gammai,gammap)
R2=[1,0;-0.5*gammap/gammai,1];  % focusing
R4=zeros(4,4);
R4(1:2,1:2)=R2;
R4(3:4,3:4)=R2;
