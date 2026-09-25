#!/usr/bin/python3
# SideBySide.py
import tkinter as tk
import sys, epics

reso=10   # resolution of slider
scal=5000  # scale of slider

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class LinkedWidgets(tk.Frame):
  def __init__(self, parent,name): 
    super().__init__(parent)
    self.DEVNAM=name
    self.DEV="DT:" + self.DEVNAM + ":BDL"
    self.DEV2=self.DEVNAM.replace("_US","") + ".BDL"
    print(f"in class:  " + self.DEV + "\t" + self.DEV2)
    
    self.la1=tk.Label(self, text=self.DEVNAM.replace("_US",""),
                      font=("Arial", 14), width=12, justify="left")
    self.la1.pack(side="left")
    
    self.sl1=tk.Scale(self, length=200, from_=-scal, to=scal, resolution=reso,
             orient="horizontal", command=self.on_sl1_move,showvalue=False)
    self.sl1.pack(side="left", padx=10)

    self.ev1=tk.StringVar()
    self.en1= tk.Entry(self, textvariable=self.ev1, font=("Arial", 12),
              justify="right", width=10)
    self.en1.pack(padx=10,side="left")
    self.en1.bind("<Return>",self.on_en1_change)

    self.but1=tk.Button(self,text="-->", command=self.on_but1_click)
    self.but1.pack(side="left")

    self.but2=tk.Button(self,text="<--", command=self.on_but2_click)
    self.but2.pack(side="left")

    self.ev2=tk.StringVar()
    self.en2= tk.Entry(self, textvariable=self.ev2, font=("Arial", 12),
              justify="right", width=10)
    self.en2.pack(padx=10,side="left")
    self.en2.bind("<Return>",self.on_en2_change)
    
    self.sl2=tk.Scale(self, length=200, from_=-scal, to=scal, resolution=reso, 
             orient="horizontal", command=self.on_sl2_move,showvalue=False)
    self.sl2.pack(side="left", padx=10)
    
    self.sl1.set(epics.caget(self.DEV))
    try:
#      self.sl2.set(epics.caget(self.DEV2))
      pass
    except:
      pass
      
  def on_sl1_move(self,val):
    self.en1.delete(0, tk.END)
    self.en1.insert(0, val)
    epics.caput(self.DEV.replace("_US",""),val)
    
  def on_en1_change(self,*args):
    val_str=self.ev1.get()
    if is_number(val_str):
      val = float(val_str)
      self.sl1.set(val)

  def on_but1_click(self):
    v=self.en1.get()
    self.en2.delete(0,tk.END)
    self.en2.insert(0,v)
    self.sl2.set(v)

  def on_but2_click(self):
    v=self.en2.get()
    self.en1.delete(0,tk.END)
    self.en1.insert(0,v)
    self.sl1.set(v)

  def on_en2_change(*args):
    val_str = self.ev2.get()
    if is_number(val_str):
      val = float(val_str)
      self.sl2.set(val)

  def on_sl2_move(self,val):
    self.en2.delete(0, tk.END)
    self.en2.insert(0, val)
    
#define __main__

if __name__ == "__main__":
  if len(sys.argv) < 2:
      print('*** Need setup file as command-line argument')
      sys.exit()
      
  fn=sys.argv[1]
  params=[]
  with open(fn, "r") as file:
    for line in file:
        params.append(line.strip())
  #print(params)

  root = tk.Tk()
  root.title(f"SideBySide: " + fn)
  root.geometry("900x250")
  
  def check_inhibit():
    if inhibit.get() == 1:
      epics.caput('DT:INHIBIT',1)
    else:
      epics.caput('DT:INHIBIT',0)
  inhibit=tk.IntVar()
  cb=tk.Checkbutton(root,text="Inhibit updates",variable=inhibit,
                 command=check_inhibit)
  cb.pack()
#  cb.select()
 
  for p in params:
    LinkedWidgets(root,p).pack(side="top")
    
  root.mainloop()
