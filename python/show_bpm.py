# show_bpm.py, V. Ziemann, 260908
import epics
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) >1:
  bpmfile=sys.argv[1]
else:
  bpmfile="bpmlist.txt"

def on_close(event):
  plt.ioff()
  sys.exit()
    
plt.ion()

fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)

b=[]
with open(bpmfile, "r") as file:
    for line in file:
        b.append(line.strip())
print(b)

bpmx=[]
for bpm in b:
    bpmx.append('DT:'+bpm+':XPOS')

bpmy=[]
for bpm in b:
    bpmy.append('DT:'+bpm+':YPOS')

    
while True:
  bpmxpos=epics.caget_many(bpmx)
  bpmypos=epics.caget_many(bpmy)
  xrms=np.std(bpmxpos)
  yrms=np.std(bpmypos)
  plt.clf()
  plt.subplot(2,1,1)
  plt.bar(range(len(bpmxpos)),bpmxpos,color='blue')
  plt.ylabel('x [mm]')
  plt.ylim([-5,5])
  plt.text(0,3,"rms = {:.2f}".format(xrms))
  plt.title(' Horizontal and Vertical BPM')
  plt.subplot(2,1,2)
  plt.bar(range(len(bpmypos)),bpmypos,color='red')
  plt.ylabel('y [mm]')
  plt.ylim([-5,5])
  plt.text(0,3,"rms = {:.2f}".format(yrms))
  plt.draw()
  plt.pause(1) 
  
plt.ioff()
plt.show()
  
