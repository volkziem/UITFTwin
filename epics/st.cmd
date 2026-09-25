#!../../bin/linux-x86_64/uitftwin

#- SPDX-FileCopyrightText: 2003 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change dtwin to something else
#- everywhere it appears in this file

< envPaths

epicsEnvSet(STREAM_PROTOCOL_PATH,"../../uitftwinApp/Db")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/uitftwin.dbd"
uitftwin_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("SOCKET1","127.0.0.1:8000",0,0,0)

dbLoadRecords("uitftwinApp/Db/wienfilter.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("uitftwinApp/Db/magnets.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("uitftwinApp/Db/bpm.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("uitftwinApp/Db/misc.db","PORT='SOCKET1',USER='DT'")
dbLoadRecords("uitftwinApp/Db/cavities.db","PORT='SOCKET1',USER='DT'")

cd "${TOP}/iocBoot/${IOC}"
iocInit
