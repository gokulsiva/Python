import os
import time
import zipfile

target_dir = "/home/gokul/Backup/"
source = "Workspace/python_workspace/"
fileName = time.strftime('%Y%m%d%H%M%S')+'.zip'
zf = zipfile.ZipFile(fileName, "w")
for dirname, subdirs, files in os.walk(source):
    zf.write(dirname)
    print "=================="
    print dirname
    print "=================="
    for filename in files:
        print "~~~~~~~~~~~~~~"
        print filename
        print "~~~~~~~~~~~~~~"
        zf.write(os.path.join(dirname, filename))
zf.close()

os.system('mv {} {}'.format(fileName,target_dir))
