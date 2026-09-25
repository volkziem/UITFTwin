% add_bpm_to_epics.m, V. Ziemann, 260812
function add_bpm_to_epics(fpd,fpp,nam)

% write to database file, horizontal
fprintf(fpd,'record(ai, "$(USER):%s:XPOS") {\n',nam);
fprintf(fpd,'  field(DESC, "%s horizontal")\n',nam);
fprintf(fpd,'  field(SCAN, "2 second")\n  field(DTYP, "stream")\n');
fprintf(fpd,'  field(INP, "@bpm.proto get_%sX $(PORT)")\n}\n\n',nam);
% and vertical
fprintf(fpd,'record(ai, "$(USER):%s:YPOS") {\n',nam);
fprintf(fpd,'  field(DESC, "%s horizontal")\n',nam);
fprintf(fpd,'  field(SCAN, "2 second")\n  field(DTYP, "stream")\n');
fprintf(fpd,'  field(INP, "@bpm.proto get_%sY $(PORT)")\n}\n\n',nam);

% write to protocol file
fprintf(fpp,'get_%sX { out "%s.XPOS?"; in "%s.XPOS %%f"; ',nam,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n');
fprintf(fpp,'get_%sY { out "%s.YPOS?"; in "%s.YPOS %%f"; ',nam,nam,nam);
fprintf(fpp,'ExtraInput = Ignore; }\n\n');

