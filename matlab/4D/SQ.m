% Q.m thin quadrupole, V. Ziemann, 240828
function out=SQ(F)
out=eye(4);
if abs(F)<1e-8, return; end
out(2,3)=1/F;
out(4,1)=1/F;

