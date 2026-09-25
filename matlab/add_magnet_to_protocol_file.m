% add_magnet_to_protocol_file.m, V. Ziemann, 260811
function add_magnet_to_protocol_file(fpd,fpp,name)

% write to database file
nam=strcat(name,':BDL');
fprintf(fpd,'record(ao, "$(USER):%s") {\n',nam);
fprintf(fpd,'  field(DESC, "magnet %s value")\n',nam);
fprintf(fpd,'  field(DTYP, "stream")\n');
fprintf(fpd,'  field(OUT, "@magnets.proto set_%s $(PORT)")\n}\n\n',name);

% write to protocol file
nam=strcat(name,'.BDL');
fprintf(fpp,'get_%s { out "%s?"; in "%s %%f"; ',name,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n');

fprintf(fpp,'set_%s { out "%s %%f"; ',name,nam);
fprintf(fpp,'ExtraInput = Ignore; @init { get_%s; } }\n\n',name);
