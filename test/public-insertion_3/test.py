import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import InsertionSort

array = [5, 2, 4, 6, 1, 3] 
InsertionSort(array)

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

# Print without newline/carriage return
ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
