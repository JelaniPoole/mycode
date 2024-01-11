#!/usr/bin/env python3

#imports
import shutil
import os

#lets user run program from any location on the system
os.chdir('/home/student/mycode/')

#calling shutil.move(source destination)
shutil.move('raynor.obj', 'ceph_storage/')

#Prompt the user for a new name for the kerrigan.obj file.
xname = input('What is the new name for kerrigan.obj? ')

#Rename the current kerrigan.obj file.
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
