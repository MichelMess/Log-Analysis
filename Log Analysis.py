#!/usr/bin/python
#This program analyses the auth.log files*
#---------------------------------------------------------------------------------------------------------
import sys
import time
import os
 
FailedAndSuccessful_list = []
FaliedIP_list = []
FaliedUser_list = []
SuccessIP_list = []
SuccessUser_list = [] 
    
#Log = "/var/lab/assignment3/var/log/auth.log"
Log= "/var/log/auth.log"
FinalDirectory = "/var/lab/assignment3/var/resumo_log"
   
from os.path import join as pjoin
file = time.asctime()
LogAnalysisResults_Path = pjoin(FinalDirectory, file)
file  = open(LogAnalysisResults_Path, "w")
      
   
# Opening the file
try:
   logfile  = open(Log,"r")
except Exception, e:
    print"I can't  read your Logfile: Issue:" ,e
    sys.exit()

# Reading File
lines = logfile.readline()
while lines:
    a = lines.split(":")
    FailedAndSuccessful_list.append(a[3])
    lines = logfile.readline()
    if not lines:
       break 
      

for i in FailedAndSuccessful_list:
    if i[1] == 'F':
        b = i.split("'")
        FaliedIP_list.append(b[3])
        FaliedUser_list.append(b[5])
            
    elif i[1:3] == 'Su':
        c = i.split()
        SuccessIP_list.append(c[3])
        SuccessUser_list.append(c[5])
        
    else:
        continue   
      
#Writes Failed and Successful analysis into a file     
file.write('Failed Access\n')
for i in range(len(FaliedIP_list)):
    file.writelines(' '.join(('\nFailed Acess:#',str(i),'\nSource:',FaliedIP_list[i],'\nUser:',FaliedUser_list[i],'\n----------------------------')))
    file.write((time.asctime()))
     
    
file.write('\nSuccessful Access\n')
for i in range(len(SuccessIP_list)):
    file.writelines(' '.join(('\nSuccess Acess:#',str(i),'\nSource:',SuccessIP_list[i],'\nUser:',SuccessUser_list[i],'\n----------------------------')))
    file.write((time.asctime()))
        
     
file.close
    

 