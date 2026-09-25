% write_epics_cavity_files.m, V. Ziemann, 260911
fpd=fopen('cavities.db','w');     % database file
fprintf(fpd,'# ./uitftwinApp/Db/cavities.db\n\n');
fpp=fopen('cavities.proto','w');  % protocol file
fprintf(fpp,'# ./uitftwinApp/Db/cavities.proto\n\n');
fprintf(fpp,'Terminator = CR LF;\n\n');
for line=1:nlines
  switch beamline(line,1)
    case {50, 52}   % cavities
      add_cavity_to_protocol_file(fpd,fpp,names(line));
  end
end
fclose(fpd);
fclose(fpp);