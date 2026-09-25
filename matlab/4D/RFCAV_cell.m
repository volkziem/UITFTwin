% RFCAV_cell.m, V. Ziemann, 260908
function [R4,gammaf]=RFCAV_cell(L,dEdz,phi,gammai)
if abs(dEdz)<1e-6, dEdz=1e-6; end
phirad=phi*pi/180;
mc2=0.511;  % Restmass of electron in MeV
gammap=dEdz*cos(phirad)/mc2;  % dEdz in MeV/m
gammaf=gammai+gammap*L;
alpha=log(gammaf/gammai);
omega=sqrt(1/(8*cos(phirad)^2));
c=cos(omega*alpha);
s=sin(omega*alpha);

R2=[c,gammai*s/(omega*gammap); -omega*s*gammap/gammai, gammai*c/gammaf];

R4=zeros(4,4);
R4(1:2,1:2)=R2;
R4(3:4,3:4)=R2;

