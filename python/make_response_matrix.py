# make_response_matrix.py, V. Ziemann, 260824
import epics, time, sys
import numpy as np
np.set_printoptions(precision=3, suppress=True)

bpmfile="bpmlist.txt"
corfile="corlist.txt"
delta=1
if len(sys.argv)>3:
    bpmfile=sys.argv[1]
    corfile=sys.argv[2]
    delta=sys.argv[3]

c=[]
with open(corfile, "r") as file:
    for line in file:
        c.append(line.strip())
corlist=[]
for cor in c:
    corlist.append('DT:'+cor+'H:BDL')
for cor in c:
    corlist.append('DT:'+cor+'V:BDL')
print(corlist)

b=[]
with open(bpmfile, "r") as file:
    for line in file:
        b.append(line.strip())
bpms=[]
for bpm in b:
    bpms.append('DT:'+bpm+':XPOS')
for bpm in b:
    bpms.append('DT:'+bpm+':YPOS')
print(bpms)
delta=float(delta)
print(delta)

# sys.exit()

ncor=len(corlist)
nbpm=len(bpms)
print(ncor,nbpm)
ORM=np.zeros((ncor,nbpm))

ic=-1
for cornam in corlist:
    print(cornam)
    ic=ic+1
    val0=epics.caget(cornam)
    time.sleep(2)
    x0=np.array(epics.caget_many(bpms))
    val1=val0+delta
    print(cornam,val0,'->',val1)
    epics.caput(cornam,val1)
    time.sleep(5)
    x1=np.array(epics.caget_many(bpms))
    ORM[ic,:]=[*(x1-x0)/delta]
    epics.caput(cornam,val0)
    time.sleep(5)

ORM=ORM.T
print(ORM)
np.save('response_matrix.npy',ORM)
np.savetxt('response_matrix.csv',ORM)

