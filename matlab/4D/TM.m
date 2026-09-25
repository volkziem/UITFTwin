% TM.m, V. Ziemann, 250508
function R=TM(ic,ib)
global Racc
if ib<ic, R=zeros(4,4); return; end     % no upstream response
R=Racc(:,:,ib)*inv(Racc(:,:,ic-1));