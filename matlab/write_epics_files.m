% write_epics_files.m, V. Ziemann, 260811
clear all

[beamline,names]=read_lattice_file('uitf.lattice'); % load input file
nlines=size(beamline,1);

% first the magnets
fpd=fopen('magnets.db','w');     % database file
fprintf(fpd,'# ./uitftwinApp/Db/magnets.db\n\n');
fpp=fopen('magnets.proto','w');  % protocol file
fprintf(fpp,'# ./uitftwinApp/Db/magnets.proto\n');
fprintf(fpp,'Terminator = CR LF;\n\n');
for line=1:nlines
  switch beamline(line,1)
    case {5, 19} % quadrupole and solenoid 
      add_magnet_to_protocol_file(fpd,fpp,names(line));
    case 7   % correctors
      nam=strcat(names(line),'H');
      add_magnet_to_protocol_file(fpd,fpp,nam);
      nam=strcat(names(line),'V');
      add_magnet_to_protocol_file(fpd,fpp,nam);
    % case 19   % individual solenoids
    %   add_magnet_to_protocol_file(fpd,fpp,names(line));
  end
end
fclose(fpd);
fclose(fpp);

% second the bpm
fpd=fopen('bpm.db','w');     % database file
fprintf(fpd,'# ./uitftwinApp/Db/bpm.db\n\n');
fpp=fopen('bpm.proto','w');  % protocol file
fprintf(fpp,'# ./uitftwinApp/Db/bpm.proto\n\n');
fprintf(fpp,'Terminator = CR LF;\n\n');
for line=1:nlines
  switch beamline(line,1)
    case 103   % bpm
      add_bpm_to_epics(fpd,fpp,names(line));
  end
end
fclose(fpd);
fclose(fpp);
