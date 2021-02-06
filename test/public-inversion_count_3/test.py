import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import countNumberOfInversions

array = [3,1,2,5,10,0,11,9] 
addresult = str(countNumberOfInversions(array))

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
