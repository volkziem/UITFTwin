# quad_scan_test.py, V. Ziemann, 260821
import epics, time, sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 4:
  PS='DT:MFHK101:BDL'
  START='GUNVOLT'
  SCREEN='ITVK201A'
  print(f' Execute: ' + sys.argv[0] + ' ' + START + ' ' + PS + ' ' + SCREEN)
else:
  START=sys.argv[1]
  PS=sys.argv[2]
  SCREEN=sys.argv[3]

print(f' XXX ' + sys.argv[0] + ' ' + START + ' ' + PS + ' ' + SCREEN)

epics.caput('DT:TM:FROM',START)

v0=epics.caget(PS)
#scanrange=np.arange(v0-1500,v0+500,250)
scanrange=np.arange(-1800,-1400,50)
sigx=[]
sigy=[]
data=[]
Ax=[]
Ay=[]
xx=[]
yy=[]

for v in scanrange:
  epics.caput(PS,v)
  time.sleep(3)
  epics.caput('DT:SCREEN',SCREEN)
  epics.caput('DT:TM:TO',SCREEN)
  time.sleep(2)
  sigmas=epics.caget('DT:SIGMAS')
  tm=epics.caget('DT:TM')
  print(v,*sigmas,*tm)
  data.append([v,*sigmas,*tm])
  xx.append(sigmas[0]**2)
  yy.append(sigmas[1]**2)
  Ax.append([tm[0]*tm[0],2*tm[0]*tm[1],tm[1]*tm[1]])
  Ay.append([tm[10]**2,2*tm[10]*tm[11],tm[11]**2])
  sigx.append(sigmas[0])
  sigy.append(sigmas[1])
  
epics.caput(PS,v0)
print(data)
np.savetxt("data.txt",np.array(data),delimiter="\n")

xx=np.array(xx)
Ax=np.array(Ax)
sx=np.linalg.pinv(Ax) @ xx
epsx=np.sqrt(sx[0]*sx[2]-sx[1]**2)
betax=sx[0]/epsx
alfax=-sx[1]/epsx

yy=np.array(yy)
Ay=np.array(Ay)
sy=np.linalg.pinv(Ay) @ yy
epsy=np.sqrt(sy[0]*sy[2]-sy[1]**2)
betay=sy[0]/epsx
alfay=-sy[1]/epsx

plt.subplot(1,2,1)
plt.plot(scanrange,sigx,'-*',label='sigmax')
plt.ylabel('sigmax [mm]')
plt.xlabel(PS)
plt.title(f"epsx={epsx:.2f}mm-mrad  betax={betax:.2f}m  alfax={alfax:.2f}")
plt.legend()

plt.subplot(1,2,2)
plt.plot(scanrange,sigy,'-*',label='sigmay')
plt.ylabel('sigmay [mm]')
plt.xlabel(PS)
plt.title(f"epsy={epsy:.2f}mm-mrad  betay={betay:.2f}m  alfay={alfay:.2f}")
plt.legend()

#plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')
plt.show()

