import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import InsertionSort

array = [20,19,18,17,16,15,14,13,12,11,10,19,8,7,6,5,4,3,2,1,0] 
InsertionSort(array)

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
