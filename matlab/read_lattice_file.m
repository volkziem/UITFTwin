% read_lattice_file.m, V. Ziemann, 260805
function [a,b]=read_lattice_file(fn)
fid=fopen(fn);
a=zeros(2,6); b=strings(2,1);
ic=0;
while 1
  line=fgetl(fid);
  if isempty(line), break; end
  if line==-1, break; end
  if strfind(line,'%'), continue; end
  if strfind(line,'#STOP'), break; end
  ic=ic+1;
  token=split(line);
  if isempty(cell2mat(token(end))), token(end)=[]; end
  if isempty(cell2mat(token(1))), token(1)=[]; end
  lt=length(token);
  a(ic,1:4)=str2double(token(1:4));
  %a(ic,1:4)=sscanf(line,'%g %g %g %g ');
  if lt>4, b(ic)=token(5); end
  if lt>5, a(ic,5:6)=str2double(token(6:7)); end
  %if ic>3, break; end
end
fclose(fid);
