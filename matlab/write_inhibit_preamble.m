% write_inhibit_preamble.m, V. Ziemann, 260908
function write_inhibit_preamble(fp)
fprintf(fp,"def check_inhibit():\n");
fprintf(fp,"  if inhibit.get() == 1:\n     epics.caput('DT:INHIBIT',1)\n");
fprintf(fp,"  else:\n     epics.caput('DT:INHIBIT',0)\n");
fprintf(fp,"inhibit=tk.IntVar()\n");
fprintf(fp,'tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,command=check_inhibit).pack()\n\n');
