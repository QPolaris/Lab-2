import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import InsertionSort

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
InsertionSort(array)

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
