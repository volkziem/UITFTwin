% add_cavity_to_protocol_file.m, V. Ziemann, 260911
function add_cavity_to_protocol_file(fpd,fpp,name)

% write to database file
nam=strcat(name,':AMPL');
fprintf(fpd,'record(ao, "$(USER):%s") {\n',nam);
fprintf(fpd,'  field(DESC, "magnet %s value")\n',nam);
fprintf(fpd,'  field(DTYP, "stream")\n');
fprintf(fpd,'  field(OUT, "@cavities.proto set_ampl_%s $(PORT)")\n}\n\n',name);

nam=strcat(name,':PHASE');
fprintf(fpd,'record(ao, "$(USER):%s") {\n',nam);
fprintf(fpd,'  field(DESC, "magnet %s value")\n',nam);
fprintf(fpd,'  field(DTYP, "stream")\n');
fprintf(fpd,'  field(OUT, "@cavities.proto set_phase_%s $(PORT)")\n}\n\n',name);

nam=strcat(name,':WL');
fprintf(fpd,'record(ao, "$(USER):%s") {\n',nam);
fprintf(fpd,'  field(DESC, "magnet %s value")\n',nam);
fprintf(fpd,'  field(DTYP, "stream")\n');
fprintf(fpd,'  field(OUT, "@cavities.proto set_wavelength_%s $(PORT)")\n}\n\n',name);

% write to protocol file
nam=strcat(name,'.4');
fprintf(fpp,'get_ampl_%s { out "%s?"; in "%s %%f"; ',name,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n');

fprintf(fpp,'set_ampl_%s { out "%s %%f"; ',name,nam);
fprintf(fpp,'ExtraInput = Ignore; @init { get_ampl_%s; } }\n\n',name);

nam=strcat(name,'.5');
fprintf(fpp,'get_phase_%s { out "%s?"; in "%s %%f"; ',name,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n');

fprintf(fpp,'set_phase_%s { out "%s %%f"; ',name,nam);
fprintf(fpp,'ExtraInput = Ignore; @init { get_phase_%s; } }\n\n',name);

nam=strcat(name,'.6');
fprintf(fpp,'get_wavelength_%s { out "%s?"; in "%s %%f"; ',name,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n');

fprintf(fpp,'set_wavelength_%s { out "%s %%f"; ',name,nam);
fprintf(fpp,'ExtraInput = Ignore; @init { get_wavelength_%s; } }\n\n',name);