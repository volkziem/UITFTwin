import tkinter as tk
import epics

root = tk.Tk()
root.title("Injector correctors H")
root.geometry("700x250")

def check_inhibit():
  if inhibit.get() == 1:
     epics.caput('DT:INHIBIT',1)
  else:
     epics.caput('DT:INHIBIT',0)
inhibit=tk.IntVar()
tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,command=check_inhibit).pack()

def show_value_MBHK101H(val):
  # print(f"Current Value: {val} and name=MBHK101H:BDL")
  epics.caput('DT:MBHK101H:BDL',val)

f_MBHK101H=tk.Frame(root)
f_MBHK101H.pack(side="left")
c=tk.Canvas(f_MBHK101H, width=50, height=130)
c.create_text(40, 60, text="MBHK101H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK101H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK101H)
slider.pack(side="top")

vv=epics.caget('DT:MBHK101H:BDL')
slider.set(vv)

def show_value_MBHK102H(val):
  # print(f"Current Value: {val} and name=MBHK102H:BDL")
  epics.caput('DT:MBHK102H:BDL',val)

f_MBHK102H=tk.Frame(root)
f_MBHK102H.pack(side="left")
c=tk.Canvas(f_MBHK102H, width=50, height=130)
c.create_text(40, 60, text="MBHK102H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK102H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK102H)
slider.pack(side="top")

vv=epics.caget('DT:MBHK102H:BDL')
slider.set(vv)

def show_value_MLHK201H(val):
  # print(f"Current Value: {val} and name=MLHK201H:BDL")
  epics.caput('DT:MLHK201H:BDL',val)

f_MLHK201H=tk.Frame(root)
f_MLHK201H.pack(side="left")
c=tk.Canvas(f_MLHK201H, width=50, height=130)
c.create_text(40, 60, text="MLHK201H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK201H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK201H)
slider.pack(side="top")

vv=epics.caget('DT:MLHK201H:BDL')
slider.set(vv)

def show_value_MBHK202H(val):
  # print(f"Current Value: {val} and name=MBHK202H:BDL")
  epics.caput('DT:MBHK202H:BDL',val)

f_MBHK202H=tk.Frame(root)
f_MBHK202H.pack(side="left")
c=tk.Canvas(f_MBHK202H, width=50, height=130)
c.create_text(40, 60, text="MBHK202H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK202H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK202H)
slider.pack(side="top")

vv=epics.caget('DT:MBHK202H:BDL')
slider.set(vv)

def show_value_MBHK203H(val):
  # print(f"Current Value: {val} and name=MBHK203H:BDL")
  epics.caput('DT:MBHK203H:BDL',val)

f_MBHK203H=tk.Frame(root)
f_MBHK203H.pack(side="left")
c=tk.Canvas(f_MBHK203H, width=50, height=130)
c.create_text(40, 60, text="MBHK203H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK203H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK203H)
slider.pack(side="top")

vv=epics.caget('DT:MBHK203H:BDL')
slider.set(vv)

def show_value_MBHK301H(val):
  # print(f"Current Value: {val} and name=MBHK301H:BDL")
  epics.caput('DT:MBHK301H:BDL',val)

f_MBHK301H=tk.Frame(root)
f_MBHK301H.pack(side="left")
c=tk.Canvas(f_MBHK301H, width=50, height=130)
c.create_text(40, 60, text="MBHK301H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MBHK301H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MBHK301H)
slider.pack(side="top")

vv=epics.caget('DT:MBHK301H:BDL')
slider.set(vv)

def show_value_MLHK302H(val):
  # print(f"Current Value: {val} and name=MLHK302H:BDL")
  epics.caput('DT:MLHK302H:BDL',val)

f_MLHK302H=tk.Frame(root)
f_MLHK302H.pack(side="left")
c=tk.Canvas(f_MLHK302H, width=50, height=130)
c.create_text(40, 60, text="MLHK302H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK302H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK302H)
slider.pack(side="top")

vv=epics.caget('DT:MLHK302H:BDL')
slider.set(vv)

def show_value_MLHK401H(val):
  # print(f"Current Value: {val} and name=MLHK401H:BDL")
  epics.caput('DT:MLHK401H:BDL',val)

f_MLHK401H=tk.Frame(root)
f_MLHK401H.pack(side="left")
c=tk.Canvas(f_MLHK401H, width=50, height=130)
c.create_text(40, 60, text="MLHK401H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK401H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK401H)
slider.pack(side="top")

vv=epics.caget('DT:MLHK401H:BDL')
slider.set(vv)

def show_value_MLHK401AH(val):
  # print(f"Current Value: {val} and name=MLHK401AH:BDL")
  epics.caput('DT:MLHK401AH:BDL',val)

f_MLHK401AH=tk.Frame(root)
f_MLHK401AH.pack(side="left")
c=tk.Canvas(f_MLHK401AH, width=50, height=130)
c.create_text(40, 60, text="MLHK401AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK401AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK401AH)
slider.pack(side="top")

vv=epics.caget('DT:MLHK401AH:BDL')
slider.set(vv)

def show_value_MLHK402H(val):
  # print(f"Current Value: {val} and name=MLHK402H:BDL")
  epics.caput('DT:MLHK402H:BDL',val)

f_MLHK402H=tk.Frame(root)
f_MLHK402H.pack(side="left")
c=tk.Canvas(f_MLHK402H, width=50, height=130)
c.create_text(40, 60, text="MLHK402H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK402H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK402H)
slider.pack(side="top")

vv=epics.caget('DT:MLHK402H:BDL')
slider.set(vv)

def show_value_MLHK403H(val):
  # print(f"Current Value: {val} and name=MLHK403H:BDL")
  epics.caput('DT:MLHK403H:BDL',val)

f_MLHK403H=tk.Frame(root)
f_MLHK403H.pack(side="left")
c=tk.Canvas(f_MLHK403H, width=50, height=130)
c.create_text(40, 60, text="MLHK403H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHK403H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHK403H)
slider.pack(side="top")

vv=epics.caget('DT:MLHK403H:BDL')
slider.set(vv)

def show_value_MLHM201H(val):
  # print(f"Current Value: {val} and name=MLHM201H:BDL")
  epics.caput('DT:MLHM201H:BDL',val)

f_MLHM201H=tk.Frame(root)
f_MLHM201H.pack(side="left")
c=tk.Canvas(f_MLHM201H, width=50, height=130)
c.create_text(40, 60, text="MLHM201H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM201H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM201H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM201H:BDL')
slider.set(vv)

def show_value_MLHM401H(val):
  # print(f"Current Value: {val} and name=MLHM401H:BDL")
  epics.caput('DT:MLHM401H:BDL',val)

f_MLHM401H=tk.Frame(root)
f_MLHM401H.pack(side="left")
c=tk.Canvas(f_MLHM401H, width=50, height=130)
c.create_text(40, 60, text="MLHM401H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM401H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM401H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM401H:BDL')
slider.set(vv)

def show_value_MLHM501H(val):
  # print(f"Current Value: {val} and name=MLHM501H:BDL")
  epics.caput('DT:MLHM501H:BDL',val)

f_MLHM501H=tk.Frame(root)
f_MLHM501H.pack(side="left")
c=tk.Canvas(f_MLHM501H, width=50, height=130)
c.create_text(40, 60, text="MLHM501H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM501H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM501H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM501H:BDL')
slider.set(vv)

def show_value_MLHM502H(val):
  # print(f"Current Value: {val} and name=MLHM502H:BDL")
  epics.caput('DT:MLHM502H:BDL',val)

f_MLHM502H=tk.Frame(root)
f_MLHM502H.pack(side="left")
c=tk.Canvas(f_MLHM502H, width=50, height=130)
c.create_text(40, 60, text="MLHM502H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM502H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM502H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM502H:BDL')
slider.set(vv)

def show_value_MLHM503H(val):
  # print(f"Current Value: {val} and name=MLHM503H:BDL")
  epics.caput('DT:MLHM503H:BDL',val)

f_MLHM503H=tk.Frame(root)
f_MLHM503H.pack(side="left")
c=tk.Canvas(f_MLHM503H, width=50, height=130)
c.create_text(40, 60, text="MLHM503H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM503H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM503H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM503H:BDL')
slider.set(vv)

def show_value_MLHM504H(val):
  # print(f"Current Value: {val} and name=MLHM504H:BDL")
  epics.caput('DT:MLHM504H:BDL',val)

f_MLHM504H=tk.Frame(root)
f_MLHM504H.pack(side="left")
c=tk.Canvas(f_MLHM504H, width=50, height=130)
c.create_text(40, 60, text="MLHM504H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM504H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM504H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM504H:BDL')
slider.set(vv)

def show_value_MLHM504AH(val):
  # print(f"Current Value: {val} and name=MLHM504AH:BDL")
  epics.caput('DT:MLHM504AH:BDL',val)

f_MLHM504AH=tk.Frame(root)
f_MLHM504AH.pack(side="left")
c=tk.Canvas(f_MLHM504AH, width=50, height=130)
c.create_text(40, 60, text="MLHM504AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM504AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM504AH)
slider.pack(side="top")

vv=epics.caget('DT:MLHM504AH:BDL')
slider.set(vv)

def show_value_MLHM601AH(val):
  # print(f"Current Value: {val} and name=MLHM601AH:BDL")
  epics.caput('DT:MLHM601AH:BDL',val)

f_MLHM601AH=tk.Frame(root)
f_MLHM601AH.pack(side="left")
c=tk.Canvas(f_MLHM601AH, width=50, height=130)
c.create_text(40, 60, text="MLHM601AH", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM601AH, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM601AH)
slider.pack(side="top")

vv=epics.caget('DT:MLHM601AH:BDL')
slider.set(vv)

def show_value_MLHM701H(val):
  # print(f"Current Value: {val} and name=MLHM701H:BDL")
  epics.caput('DT:MLHM701H:BDL',val)

f_MLHM701H=tk.Frame(root)
f_MLHM701H.pack(side="left")
c=tk.Canvas(f_MLHM701H, width=50, height=130)
c.create_text(40, 60, text="MLHM701H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM701H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM701H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM701H:BDL')
slider.set(vv)

def show_value_MLHM702H(val):
  # print(f"Current Value: {val} and name=MLHM702H:BDL")
  epics.caput('DT:MLHM702H:BDL',val)

f_MLHM702H=tk.Frame(root)
f_MLHM702H.pack(side="left")
c=tk.Canvas(f_MLHM702H, width=50, height=130)
c.create_text(40, 60, text="MLHM702H", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MLHM702H, from_=10, to=-10, resolution=0.1,
   orient="vertical", command=show_value_MLHM702H)
slider.pack(side="top")

vv=epics.caget('DT:MLHM702H:BDL')
slider.set(vv)

root.mainloop()