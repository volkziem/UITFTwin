% test_write_quad_file.m, V. Ziemann, 260814
clear all;

%prefix='V';    % H for horizontal, V for vertical

[beamline,names]=read_lattice_file('uitf.lattice'); % load input file
nlines=size(beamline,1);

fn='Magnets_Bdl.py';
fp=fopen(fn,'w');

fprintf(fp,'import tkinter as tk\n');
fprintf(fp,'import epics\n\n');
fprintf(fp,'root = tk.Tk()\n');
fprintf(fp,'root.title("Magnets")\n');
fprintf(fp,'root.geometry("700x250")\n\n');
write_inhibit_preamble(fp);

for line=1:nlines
  switch beamline(line,1)
    case {5, 19}
%     nam=strcat(names(line),prefix);
      write_python_magnet_file(fp,names(line));
  end
end

fprintf(fp,'root.mainloop()');
fclose(fp);
