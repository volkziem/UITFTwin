% test_write_corrector_file.m, V. Ziemann, 260814
clear all;

prefix='V';    % H for horizontal, V for vertical

[beamline,names]=read_lattice_file('uitf.lattice'); % load input file
nlines=size(beamline,1);

fn=strcat(prefix,'correctors.py');
fp=fopen(fn,'w');

fprintf(fp,'import tkinter as tk\n');
fprintf(fp,'import epics\n\n');
fprintf(fp,'root = tk.Tk()\n');
fprintf(fp,'root.title("Injector correctors %s")\n',prefix);
fprintf(fp,'root.geometry("700x250")\n\n');

write_inhibit_preamble(fp);

for line=1:nlines
  switch beamline(line,1)
    case 7   % correctors
      nam=strcat(names(line),prefix);
      write_python_corrector_file(fp,nam);
  end
end

fprintf(fp,'root.mainloop()');
fclose(fp);
