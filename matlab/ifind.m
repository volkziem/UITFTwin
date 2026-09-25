% ifind.m, V. Ziemann, 260714
function ipos=ifind(name,names)
ipos=[]; ic=0;
for k=1:size(names,1)
  %if strfind(name,names(k)), ipos=k; break; end
  if contains(names(k),name), ic=ic+1; ipos(ic)=k; end
end