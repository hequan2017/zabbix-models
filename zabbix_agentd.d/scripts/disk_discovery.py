#/usr/bin/python
#This script is used to discovery disk on the server
import subprocess
import json
args="cat /proc/diskstats |grep -E '\ssd[a-z]\s|\sxvd[a-z]\s|\svd[a-z]\s'|awk '{print $3}'|sort|uniq 2>/dev/null"
t=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]
 
disks=[]
 
for disk in t.split('\n'):
    if len(disk) != 0:
       disks.append({'{#DISK_NAME}':disk})
print json.dumps({'data':disks},indent=4,separators=(',',':'))
