import os

pathToDFA = "C:\\Users\\Amalie\\Documents\\GitHub\\TMM4275-KBE-project\\DFAs\\My_Chair_order.dfa"

timeElapsed = os.path.getmtime(pathToDFA)
print(timeElapsed)