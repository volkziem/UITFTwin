% RFCAV.m, V. Ziemann, 260904
% based on Rosenzweig+Serafini PRE 49 (1994) 1599
function [R4,gammaf]=RFCAV(L,dEdz,phi,gammai)
phirad=phi*pi/180;
mc2=0.511;  % Restmass of electron in MeV
gammap=dEdz*cos(phirad)/mc2;  % dEdz in MeV/m
gammaf=gammai+gammap*L;
alpha=log(gammaf/gammai);
omega=sqrt(1/(8*cos(phirad)^2));
c=cos(omega*alpha);
s=sin(omega*alpha);

R2=[c-0.5*s/omega, gammai*s/(omega*gammap); ...
  -(gammap/gammaf)*(0.25/omega+omega)*s, ...
  (gammai/gammaf)*(c+0.5*s/omega)];
R4=zeros(4,4);
R4(1:2,1:2)=R2;
R4(3:4,3:4)=R2;

return
%test
% R1=RFCAV_entrance(gammai,gammap);
% R2=RFCAV_cell(L,dEdz,phi,gammai);
% R3=RFCAV_exit(gammaf,gammap);
% RR4test=R3*R2*R1
