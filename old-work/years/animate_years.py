import os, sys

os.system("convert -delay 20 -loop 0 *.png " + "years.gif")
os.system("animate years.gif")