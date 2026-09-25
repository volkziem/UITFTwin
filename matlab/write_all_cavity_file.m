% write_all_cavity_file.m, V. Ziemann, 260911
clear all;

[beamline,names]=read_lattice_file('uitf.lattice'); % load input file
nlines=size(beamline,1);

fn='Cavities.py';
fp=fopen(fn,'w');

fprintf(fp,'import tkinter as tk\n');
fprintf(fp,'import epics\n\n');
fprintf(fp,'root = tk.Tk()\n');
fprintf(fp,'root.title("Cavities")\n');
fprintf(fp,'root.geometry("300x250")\n\n');
write_inhibit_preamble(fp);

for line=1:nlines
  switch beamline(line,1)
    case {50, 52}
%     nam=strcat(names(line),prefix);
      write_python_cavity_file(fp,names(line));
  end
end

fprintf(fp,'root.mainloop()');
fclose(fp);
