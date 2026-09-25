% VWIEN.m, V. Ziemann, 260716
function out=VWIEN(L,psi)
out=eye(4); out(1,2)=L; out(3,4)=L; % default driftspace
if abs(psi)>1e-8                    % is non-zero
  psirad=psi*pi/180;                % convert to radians
  R=L/psirad;
  c=cos(psirad); s=sin(psirad);
  out(1:2,1:2)=[c,R*s;-s/R,c];
end
  