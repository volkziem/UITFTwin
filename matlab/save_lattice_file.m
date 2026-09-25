% save_lattice_file.m, V. Ziemann, 260914
fp=fopen(filnam,'w');
fprintf(fp,'%% Saved on %s\n',char(datetime));
disp(['Save file ',filnam,' at ',char(datetime)])
for line=1:nlines
  fprintf(fp,' %5d %4d %12.6g %12.6g',beamline(line,1:4));
  if ~ismissing(names(line))
    fprintf(fp,' %s ',names(line));
  end
  if abs(beamline(line,5))+abs(beamline(line,6))>1e-16
    fprintf(fp,'  %12.6g %12.6g',beamline(line,5:6));
  end
  fprintf(fp,'\n');
end
fclose(fp);