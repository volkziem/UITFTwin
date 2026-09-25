% write_python_cavity_file.m, V. Ziemann, 260814
function write_python_cavity_file(fp,name)

nam=strcat(name,':AMPL');
lines={'def show_ampl_%s(val):\n',
  '  # print(f"Current Value: {val} and name=%s")\n',
  '  epics.caput(''DT:%s'',val)\n\n'};
fprintf(fp,cell2mat(lines(1)),name);
fprintf(fp,cell2mat(lines(2)),name);
fprintf(fp,cell2mat(lines(3)),nam);

lines={'f_%s=tk.Frame(root)\n',
  'f_%s.pack(side="left")\n',
  'c=tk.Canvas(f_%s, width=50, height=130)\n',
  'c.create_text(40, 60, text="%s:AMPL", angle=90, font=("Arial", 12))\n',
  'c.pack(side="top",anchor="e")\n',
  'slider = tk.Scale(f_%s, from_=12, to=0, resolution=0.5,\n',
  '   orient="vertical", command=show_ampl_%s)\n',
  'slider.pack(side="top")\n\n'};
fprintf(fp,cell2mat(lines(1)),name);
fprintf(fp,cell2mat(lines(2)),name);
fprintf(fp,cell2mat(lines(3)),name);
fprintf(fp,cell2mat(lines(4)),name);
fprintf(fp,cell2mat(lines(5)));
fprintf(fp,cell2mat(lines(6)),name);
fprintf(fp,cell2mat(lines(7)),name);
fprintf(fp,cell2mat(lines(8)));

nam=strcat('DT:',name);
nam=strcat(nam,':AMPL');
fprintf(fp,'vv=epics.caget(''%s'')\n',nam);
fprintf(fp,'slider.set(vv)\n\n');

nam=strcat(name,':PHASE');
lines={'def show_phase_%s(val):\n',
  '  # print(f"Current Value: {val} and name=%s")\n',
  '  epics.caput(''DT:%s'',val)\n\n'};
fprintf(fp,cell2mat(lines(1)),name);
fprintf(fp,cell2mat(lines(2)),name);
fprintf(fp,cell2mat(lines(3)),nam);

lines={'f_%s=tk.Frame(root)\n',
  'f_%s.pack(side="left")\n',
  'c=tk.Canvas(f_%s, width=50, height=130)\n',
  'c.create_text(40, 60, text="%s:PHASE", angle=90, font=("Arial", 12))\n',
  'c.pack(side="top",anchor="e")\n',
  'slider = tk.Scale(f_%s, from_=90, to=-90, resolution=5,\n',
  '   orient="vertical", command=show_phase_%s)\n',
  'slider.pack(side="top")\n\n'};
fprintf(fp,cell2mat(lines(1)),name);
fprintf(fp,cell2mat(lines(2)),name);
fprintf(fp,cell2mat(lines(3)),name);
fprintf(fp,cell2mat(lines(4)),name);
fprintf(fp,cell2mat(lines(5)));
fprintf(fp,cell2mat(lines(6)),name);
fprintf(fp,cell2mat(lines(7)),name);
fprintf(fp,cell2mat(lines(8)));

nam=strcat('DT:',name);
nam=strcat(nam,':PHASE');
fprintf(fp,'vv=epics.caget(''%s'')\n',nam);
fprintf(fp,'slider.set(vv)\n\n');



