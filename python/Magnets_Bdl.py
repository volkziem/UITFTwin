import tkinter as tk
import epics

root = tk.Tk()
root.title("Magnets")
root.geometry("700x250")

def check_inhibit():
  if inhibit.get() == 1:
     epics.caput('DT:INHIBIT',1)
  else:
     epics.caput('DT:INHIBIT',0)
inhibit=tk.IntVar()
tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,command=check_inhibit).pack()

def show_value_MFHK101(val):
  # print(f"Current Value: {val} and name=MFHK101")
  epics.caput('DT:MFHK101:BDL',val)

f_MFHK101=tk.Frame(root)
f_MFHK101.pack(side="left")
c=tk.Canvas(f_MFHK101, width=50, height=130)
c.create_text(40, 60, text="MFHK101", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFHK101, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFHK101)
slider.pack(side="top")

vv=epics.caget('DT:MFHK101:BDL')
slider.set(vv)

def show_value_MFBK202(val):
  # print(f"Current Value: {val} and name=MFBK202")
  epics.caput('DT:MFBK202:BDL',val)

f_MFBK202=tk.Frame(root)
f_MFBK202.pack(side="left")
c=tk.Canvas(f_MFBK202, width=50, height=130)
c.create_text(40, 60, text="MFBK202", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFBK202, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFBK202)
slider.pack(side="top")

vv=epics.caget('DT:MFBK202:BDL')
slider.set(vv)

def show_value_MQWK202(val):
  # print(f"Current Value: {val} and name=MQWK202")
  epics.caput('DT:MQWK202:BDL',val)

f_MQWK202=tk.Frame(root)
f_MQWK202.pack(side="left")
c=tk.Canvas(f_MQWK202, width=50, height=130)
c.create_text(40, 60, text="MQWK202", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQWK202, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQWK202)
slider.pack(side="top")

vv=epics.caget('DT:MQWK202:BDL')
slider.set(vv)

def show_value_MQWK203(val):
  # print(f"Current Value: {val} and name=MQWK203")
  epics.caput('DT:MQWK203:BDL',val)

f_MQWK203=tk.Frame(root)
f_MQWK203.pack(side="left")
c=tk.Canvas(f_MQWK203, width=50, height=130)
c.create_text(40, 60, text="MQWK203", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQWK203, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQWK203)
slider.pack(side="top")

vv=epics.caget('DT:MQWK203:BDL')
slider.set(vv)

def show_value_MFQK203_US(val):
  # print(f"Current Value: {val} and name=MFQK203_US")
  epics.caput('DT:MFQK203_US:BDL',val)

f_MFQK203_US=tk.Frame(root)
f_MFQK203_US.pack(side="left")
c=tk.Canvas(f_MFQK203_US, width=50, height=130)
c.create_text(40, 60, text="MFQK203_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFQK203_US, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFQK203_US)
slider.pack(side="top")

vv=epics.caget('DT:MFQK203_US:BDL')
slider.set(vv)

def show_value_MFQK203_DS(val):
  # print(f"Current Value: {val} and name=MFQK203_DS")
  epics.caput('DT:MFQK203_DS:BDL',val)

f_MFQK203_DS=tk.Frame(root)
f_MFQK203_DS.pack(side="left")
c=tk.Canvas(f_MFQK203_DS, width=50, height=130)
c.create_text(40, 60, text="MFQK203_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFQK203_DS, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFQK203_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFQK203_DS:BDL')
slider.set(vv)

def show_value_MFAK301(val):
  # print(f"Current Value: {val} and name=MFAK301")
  epics.caput('DT:MFAK301:BDL',val)

f_MFAK301=tk.Frame(root)
f_MFAK301.pack(side="left")
c=tk.Canvas(f_MFAK301, width=50, height=130)
c.create_text(40, 60, text="MFAK301", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFAK301, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFAK301)
slider.pack(side="top")

vv=epics.caget('DT:MFAK301:BDL')
slider.set(vv)

def show_value_MFDK302A_US(val):
  # print(f"Current Value: {val} and name=MFDK302A_US")
  epics.caput('DT:MFDK302A_US:BDL',val)

f_MFDK302A_US=tk.Frame(root)
f_MFDK302A_US.pack(side="left")
c=tk.Canvas(f_MFDK302A_US, width=50, height=130)
c.create_text(40, 60, text="MFDK302A_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFDK302A_US, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFDK302A_US)
slider.pack(side="top")

vv=epics.caget('DT:MFDK302A_US:BDL')
slider.set(vv)

def show_value_MFDK302A_DS(val):
  # print(f"Current Value: {val} and name=MFDK302A_DS")
  epics.caput('DT:MFDK302A_DS:BDL',val)

f_MFDK302A_DS=tk.Frame(root)
f_MFDK302A_DS.pack(side="left")
c=tk.Canvas(f_MFDK302A_DS, width=50, height=130)
c.create_text(40, 60, text="MFDK302A_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFDK302A_DS, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFDK302A_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFDK302A_DS:BDL')
slider.set(vv)

def show_value_MFDK302B(val):
  # print(f"Current Value: {val} and name=MFDK302B")
  epics.caput('DT:MFDK302B:BDL',val)

f_MFDK302B=tk.Frame(root)
f_MFDK302B.pack(side="left")
c=tk.Canvas(f_MFDK302B, width=50, height=130)
c.create_text(40, 60, text="MFDK302B", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFDK302B, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFDK302B)
slider.pack(side="top")

vv=epics.caget('DT:MFDK302B:BDL')
slider.set(vv)

def show_value_MFAK303(val):
  # print(f"Current Value: {val} and name=MFAK303")
  epics.caput('DT:MFAK303:BDL',val)

f_MFAK303=tk.Frame(root)
f_MFAK303.pack(side="left")
c=tk.Canvas(f_MFAK303, width=50, height=130)
c.create_text(40, 60, text="MFAK303", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFAK303, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFAK303)
slider.pack(side="top")

vv=epics.caget('DT:MFAK303:BDL')
slider.set(vv)

def show_value_MFQK403_US(val):
  # print(f"Current Value: {val} and name=MFQK403_US")
  epics.caput('DT:MFQK403_US:BDL',val)

f_MFQK403_US=tk.Frame(root)
f_MFQK403_US.pack(side="left")
c=tk.Canvas(f_MFQK403_US, width=50, height=130)
c.create_text(40, 60, text="MFQK403_US", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFQK403_US, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFQK403_US)
slider.pack(side="top")

vv=epics.caget('DT:MFQK403_US:BDL')
slider.set(vv)

def show_value_MFQK403_DS(val):
  # print(f"Current Value: {val} and name=MFQK403_DS")
  epics.caput('DT:MFQK403_DS:BDL',val)

f_MFQK403_DS=tk.Frame(root)
f_MFQK403_DS.pack(side="left")
c=tk.Canvas(f_MFQK403_DS, width=50, height=130)
c.create_text(40, 60, text="MFQK403_DS", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MFQK403_DS, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MFQK403_DS)
slider.pack(side="top")

vv=epics.caget('DT:MFQK403_DS:BDL')
slider.set(vv)

def show_value_MQJM501(val):
  # print(f"Current Value: {val} and name=MQJM501")
  epics.caput('DT:MQJM501:BDL',val)

f_MQJM501=tk.Frame(root)
f_MQJM501.pack(side="left")
c=tk.Canvas(f_MQJM501, width=50, height=130)
c.create_text(40, 60, text="MQJM501", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM501, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM501)
slider.pack(side="top")

vv=epics.caget('DT:MQJM501:BDL')
slider.set(vv)

def show_value_MQJM502(val):
  # print(f"Current Value: {val} and name=MQJM502")
  epics.caput('DT:MQJM502:BDL',val)

f_MQJM502=tk.Frame(root)
f_MQJM502.pack(side="left")
c=tk.Canvas(f_MQJM502, width=50, height=130)
c.create_text(40, 60, text="MQJM502", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM502, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM502)
slider.pack(side="top")

vv=epics.caget('DT:MQJM502:BDL')
slider.set(vv)

def show_value_MQJM503(val):
  # print(f"Current Value: {val} and name=MQJM503")
  epics.caput('DT:MQJM503:BDL',val)

f_MQJM503=tk.Frame(root)
f_MQJM503.pack(side="left")
c=tk.Canvas(f_MQJM503, width=50, height=130)
c.create_text(40, 60, text="MQJM503", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM503, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM503)
slider.pack(side="top")

vv=epics.caget('DT:MQJM503:BDL')
slider.set(vv)

def show_value_MQJM504(val):
  # print(f"Current Value: {val} and name=MQJM504")
  epics.caput('DT:MQJM504:BDL',val)

f_MQJM504=tk.Frame(root)
f_MQJM504.pack(side="left")
c=tk.Canvas(f_MQJM504, width=50, height=130)
c.create_text(40, 60, text="MQJM504", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM504, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM504)
slider.pack(side="top")

vv=epics.caget('DT:MQJM504:BDL')
slider.set(vv)

def show_value_MQJM701(val):
  # print(f"Current Value: {val} and name=MQJM701")
  epics.caput('DT:MQJM701:BDL',val)

f_MQJM701=tk.Frame(root)
f_MQJM701.pack(side="left")
c=tk.Canvas(f_MQJM701, width=50, height=130)
c.create_text(40, 60, text="MQJM701", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM701, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM701)
slider.pack(side="top")

vv=epics.caget('DT:MQJM701:BDL')
slider.set(vv)

def show_value_MQJM702(val):
  # print(f"Current Value: {val} and name=MQJM702")
  epics.caput('DT:MQJM702:BDL',val)

f_MQJM702=tk.Frame(root)
f_MQJM702.pack(side="left")
c=tk.Canvas(f_MQJM702, width=50, height=130)
c.create_text(40, 60, text="MQJM702", angle=90, font=("Arial", 12))
c.pack(side="top",anchor="e")
slider = tk.Scale(f_MQJM702, from_=5000, to=-5000, resolution=10,
   orient="vertical", command=show_value_MQJM702)
slider.pack(side="top")

vv=epics.caget('DT:MQJM702:BDL')
slider.set(vv)

root.mainloop()