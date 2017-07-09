#this module import files
#and import variables from files
#then calculate the average wage in 2013 dollar
#then delete all "*.pyc" files in this directory
#!/local/bin/python
import os
import getaverage
from getaverage import average

import getwbdata
from getwbdata import totalcpi

adjaverage=average*totalcpi

print "The average wage in 2013 dollar is:",adjaverage
os.system("find . -name '*.pyc' -type f -delete")
#find . -name "*.pyc" -type f -delete
#or in bash, just input this command line above to delete all pyc files
