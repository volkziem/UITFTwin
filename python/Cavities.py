import tkinter as tk
import epics

root = tk.Tk()
root.title("Cavities")
root.geometry("300x250")

def check_inhibit():
  if inhibit.get() == 1:
     epics.caput('DT:INHIBIT',1)
  else:
     epics.caput('DT:INHIBIT',0)
inhibit=tk.IntVar()
tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,command=check_inhibit).pack()

def show_ampl_ENID1(val):
  # print(f"Current Value: {val} and name=ENID1")
  epics.caput('DT:ENID1:AMPL',val)

f_ENID1=tk.Frame(root)
f_ENID1.pack(side="left")
c=tk.Canvas(f_ENID1, width=50, height=130)
c.create_text(40, 60, text="ENID1:AMPL", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_ENID1, from_=12, to=0, resolution=0.5,
   orient="vertical", command=show_ampl_ENID1)
slider.pack(side="top")

vv=epics.caget('DT:ENID1:AMPL')
slider.set(vv)

def show_phase_ENID1(val):
  # print(f"Current Value: {val} and name=ENID1")
  epics.caput('DT:ENID1:PHASE',val)

f_ENID1=tk.Frame(root)
f_ENID1.pack(side="left")
c=tk.Canvas(f_ENID1, width=50, height=130)
c.create_text(40, 60, text="ENID1:PHASE", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_ENID1, from_=90, to=-90, resolution=5,
   orient="vertical", command=show_phase_ENID1)
slider.pack(side="top")

vv=epics.caget('DT:ENID1:PHASE')
slider.set(vv)

def show_ampl_ENID2(val):
  # print(f"Current Value: {val} and name=ENID2")
  epics.caput('DT:ENID2:AMPL',val)

f_ENID2=tk.Frame(root)
f_ENID2.pack(side="left")
c=tk.Canvas(f_ENID2, width=50, height=130)
c.create_text(40, 60, text="ENID2:AMPL", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_ENID2, from_=12, to=0, resolution=0.5,
   orient="vertical", command=show_ampl_ENID2)
slider.pack(side="top")

vv=epics.caget('DT:ENID2:AMPL')
slider.set(vv)

def show_phase_ENID2(val):
  # print(f"Current Value: {val} and name=ENID2")
  epics.caput('DT:ENID2:PHASE',val)

f_ENID2=tk.Frame(root)
f_ENID2.pack(side="left")
c=tk.Canvas(f_ENID2, width=50, height=130)
c.create_text(40, 60, text="ENID2:PHASE", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_ENID2, from_=90, to=-90, resolution=5,
   orient="vertical", command=show_phase_ENID2)
slider.pack(side="top")

vv=epics.caget('DT:ENID2:PHASE')
slider.set(vv)

root.mainloop()