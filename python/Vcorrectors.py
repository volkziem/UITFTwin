import tkinter as tk
import epics

root = tk.Tk()
root.title("Injector correctors V")
root.geometry("700x250")

def check_inhibit():
  if inhibit.get() == 1:
     epics.caput('DT:INHIBIT',1)
  else:
     epics.caput('DT:INHIBIT',0)
inhibit=tk.IntVar()
tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,command=check_inhibit).pack()

def show_value_MBHK101V(val):
  # print(f"Current Value: {val} and name=MBHK101V:BDL")
  epics.caput('DT:MBHK101V:BDL',val)

f_MBHK101V=tk.Frame(root)
f_MBHK101V.pack(side="left")
c=tk.Canvas(f_MBHK101V, width=50, height=130)
c.create_text(40, 60, text="MBHK101V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK101V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK101V)
slider.pack(side="top")

vv=epics.caget('DT:MBHK101V:BDL')
slider.set(vv)

def show_value_MBHK102V(val):
  # print(f"Current Value: {val} and name=MBHK102V:BDL")
  epics.caput('DT:MBHK102V:BDL',val)

f_MBHK102V=tk.Frame(root)
f_MBHK102V.pack(side="left")
c=tk.Canvas(f_MBHK102V, width=50, height=130)
c.create_text(40, 60, text="MBHK102V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK102V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK102V)
slider.pack(side="top")

vv=epics.caget('DT:MBHK102V:BDL')
slider.set(vv)

def show_value_MLHK201V(val):
  # print(f"Current Value: {val} and name=MLHK201V:BDL")
  epics.caput('DT:MLHK201V:BDL',val)

f_MLHK201V=tk.Frame(root)
f_MLHK201V.pack(side="left")
c=tk.Canvas(f_MLHK201V, width=50, height=130)
c.create_text(40, 60, text="MLHK201V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK201V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK201V)
slider.pack(side="top")

vv=epics.caget('DT:MLHK201V:BDL')
slider.set(vv)

def show_value_MBHK202V(val):
  # print(f"Current Value: {val} and name=MBHK202V:BDL")
  epics.caput('DT:MBHK202V:BDL',val)

f_MBHK202V=tk.Frame(root)
f_MBHK202V.pack(side="left")
c=tk.Canvas(f_MBHK202V, width=50, height=130)
c.create_text(40, 60, text="MBHK202V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK202V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK202V)
slider.pack(side="top")

vv=epics.caget('DT:MBHK202V:BDL')
slider.set(vv)

def show_value_MBHK203V(val):
  # print(f"Current Value: {val} and name=MBHK203V:BDL")
  epics.caput('DT:MBHK203V:BDL',val)

f_MBHK203V=tk.Frame(root)
f_MBHK203V.pack(side="left")
c=tk.Canvas(f_MBHK203V, width=50, height=130)
c.create_text(40, 60, text="MBHK203V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK203V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK203V)
slider.pack(side="top")

vv=epics.caget('DT:MBHK203V:BDL')
slider.set(vv)

def show_value_MBHK301V(val):
  # print(f"Current Value: {val} and name=MBHK301V:BDL")
  epics.caput('DT:MBHK301V:BDL',val)

f_MBHK301V=tk.Frame(root)
f_MBHK301V.pack(side="left")
c=tk.Canvas(f_MBHK301V, width=50, height=130)
c.create_text(40, 60, text="MBHK301V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK301V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK301V)
slider.pack(side="top")

vv=epics.caget('DT:MBHK301V:BDL')
slider.set(vv)

def show_value_MLHK302V(val):
  # print(f"Current Value: {val} and name=MLHK302V:BDL")
  epics.caput('DT:MLHK302V:BDL',val)

f_MLHK302V=tk.Frame(root)
f_MLHK302V.pack(side="left")
c=tk.Canvas(f_MLHK302V, width=50, height=130)
c.create_text(40, 60, text="MLHK302V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK302V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK302V)
slider.pack(side="top")

vv=epics.caget('DT:MLHK302V:BDL')
slider.set(vv)

def show_value_MLHK401V(val):
  # print(f"Current Value: {val} and name=MLHK401V:BDL")
  epics.caput('DT:MLHK401V:BDL',val)

f_MLHK401V=tk.Frame(root)
f_MLHK401V.pack(side="left")
c=tk.Canvas(f_MLHK401V, width=50, height=130)
c.create_text(40, 60, text="MLHK401V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK401V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK401V)
slider.pack(side="top")

vv=epics.caget('DT:MLHK401V:BDL')
slider.set(vv)

def show_value_MLHK401AV(val):
  # print(f"Current Value: {val} and name=MLHK401AV:BDL")
  epics.caput('DT:MLHK401AV:BDL',val)

f_MLHK401AV=tk.Frame(root)
f_MLHK401AV.pack(side="left")
c=tk.Canvas(f_MLHK401AV, width=50, height=130)
c.create_text(40, 60, text="MLHK401AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK401AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK401AV)
slider.pack(side="top")

vv=epics.caget('DT:MLHK401AV:BDL')
slider.set(vv)

def show_value_MLHK402V(val):
  # print(f"Current Value: {val} and name=MLHK402V:BDL")
  epics.caput('DT:MLHK402V:BDL',val)

f_MLHK402V=tk.Frame(root)
f_MLHK402V.pack(side="left")
c=tk.Canvas(f_MLHK402V, width=50, height=130)
c.create_text(40, 60, text="MLHK402V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK402V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK402V)
slider.pack(side="top")

vv=epics.caget('DT:MLHK402V:BDL')
slider.set(vv)

def show_value_MLHK403V(val):
  # print(f"Current Value: {val} and name=MLHK403V:BDL")
  epics.caput('DT:MLHK403V:BDL',val)

f_MLHK403V=tk.Frame(root)
f_MLHK403V.pack(side="left")
c=tk.Canvas(f_MLHK403V, width=50, height=130)
c.create_text(40, 60, text="MLHK403V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK403V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK403V)
slider.pack(side="top")

vv=epics.caget('DT:MLHK403V:BDL')
slider.set(vv)

def show_value_MLHM201V(val):
  # print(f"Current Value: {val} and name=MLHM201V:BDL")
  epics.caput('DT:MLHM201V:BDL',val)

f_MLHM201V=tk.Frame(root)
f_MLHM201V.pack(side="left")
c=tk.Canvas(f_MLHM201V, width=50, height=130)
c.create_text(40, 60, text="MLHM201V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM201V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM201V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM201V:BDL')
slider.set(vv)

def show_value_MLHM401V(val):
  # print(f"Current Value: {val} and name=MLHM401V:BDL")
  epics.caput('DT:MLHM401V:BDL',val)

f_MLHM401V=tk.Frame(root)
f_MLHM401V.pack(side="left")
c=tk.Canvas(f_MLHM401V, width=50, height=130)
c.create_text(40, 60, text="MLHM401V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM401V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM401V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM401V:BDL')
slider.set(vv)

def show_value_MLHM501V(val):
  # print(f"Current Value: {val} and name=MLHM501V:BDL")
  epics.caput('DT:MLHM501V:BDL',val)

f_MLHM501V=tk.Frame(root)
f_MLHM501V.pack(side="left")
c=tk.Canvas(f_MLHM501V, width=50, height=130)
c.create_text(40, 60, text="MLHM501V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM501V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM501V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM501V:BDL')
slider.set(vv)

def show_value_MLHM502V(val):
  # print(f"Current Value: {val} and name=MLHM502V:BDL")
  epics.caput('DT:MLHM502V:BDL',val)

f_MLHM502V=tk.Frame(root)
f_MLHM502V.pack(side="left")
c=tk.Canvas(f_MLHM502V, width=50, height=130)
c.create_text(40, 60, text="MLHM502V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM502V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM502V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM502V:BDL')
slider.set(vv)

def show_value_MLHM503V(val):
  # print(f"Current Value: {val} and name=MLHM503V:BDL")
  epics.caput('DT:MLHM503V:BDL',val)

f_MLHM503V=tk.Frame(root)
f_MLHM503V.pack(side="left")
c=tk.Canvas(f_MLHM503V, width=50, height=130)
c.create_text(40, 60, text="MLHM503V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM503V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM503V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM503V:BDL')
slider.set(vv)

def show_value_MLHM504V(val):
  # print(f"Current Value: {val} and name=MLHM504V:BDL")
  epics.caput('DT:MLHM504V:BDL',val)

f_MLHM504V=tk.Frame(root)
f_MLHM504V.pack(side="left")
c=tk.Canvas(f_MLHM504V, width=50, height=130)
c.create_text(40, 60, text="MLHM504V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM504V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM504V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM504V:BDL')
slider.set(vv)

def show_value_MLHM504AV(val):
  # print(f"Current Value: {val} and name=MLHM504AV:BDL")
  epics.caput('DT:MLHM504AV:BDL',val)

f_MLHM504AV=tk.Frame(root)
f_MLHM504AV.pack(side="left")
c=tk.Canvas(f_MLHM504AV, width=50, height=130)
c.create_text(40, 60, text="MLHM504AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM504AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM504AV)
slider.pack(side="top")

vv=epics.caget('DT:MLHM504AV:BDL')
slider.set(vv)

def show_value_MLHM601AV(val):
  # print(f"Current Value: {val} and name=MLHM601AV:BDL")
  epics.caput('DT:MLHM601AV:BDL',val)

f_MLHM601AV=tk.Frame(root)
f_MLHM601AV.pack(side="left")
c=tk.Canvas(f_MLHM601AV, width=50, height=130)
c.create_text(40, 60, text="MLHM601AV", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM601AV, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM601AV)
slider.pack(side="top")

vv=epics.caget('DT:MLHM601AV:BDL')
slider.set(vv)

def show_value_MLHM701V(val):
  # print(f"Current Value: {val} and name=MLHM701V:BDL")
  epics.caput('DT:MLHM701V:BDL',val)

f_MLHM701V=tk.Frame(root)
f_MLHM701V.pack(side="left")
c=tk.Canvas(f_MLHM701V, width=50, height=130)
c.create_text(40, 60, text="MLHM701V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM701V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM701V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM701V:BDL')
slider.set(vv)

def show_value_MLHM702V(val):
  # print(f"Current Value: {val} and name=MLHM702V:BDL")
  epics.caput('DT:MLHM702V:BDL',val)

f_MLHM702V=tk.Frame(root)
f_MLHM702V.pack(side="left")
c=tk.Canvas(f_MLHM702V, width=50, height=130)
c.create_text(40, 60, text="MLHM702V", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM702V, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM702V)
slider.pack(side="top")

vv=epics.caget('DT:MLHM702V:BDL')
slider.set(vv)

root.mainloop()