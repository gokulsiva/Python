#Demo
import os
import time

source = ['/home/gokul/Workspace']

target_dir = '/home/gokul/Backup'

target = target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {} {}".format(target,' '.join(source))

print 'Zip Command :',zip_command

print "Zipping started :"


if os.system(zip_command) == 0:
    print "Successfully backed up to",target
else:
    print "Backup failed."

