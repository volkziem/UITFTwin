% misalign_magnets.m, V. Ziemann, 260814
function out=misalign_magnets(beamline,sigma)
out=beamline;
nlines=size(out,1);

for line=1:nlines
  switch out(line,1)
    case {2,4,5,19,30,31,44}   
      out(line,5:6)=sigma*randn(1,2);
  end
end