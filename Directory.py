import os

work= os.getcws()
print (" My directory of my project are :" work)

CHANGE="/root" # new root

print ( " i want to change my working directory",work ," to /root")
os.chdir( CHANGE)

os.listdir(CHANGE)

path_check = "/2025/25/10/15/"
os.path.exist ( path_check )
