from som import *
from somobj import *
from somcm import *
from somcls import *
import CORBA

print("Hello")

# Turn on SOM run-time trace
#SOM_TraceLevel.value=2

# Initialize SOM
cm=somEnvironmentNew()
cm.somDumpSelf(0)
# Create SOMObject
obj=SOMObject()
# Call some methods and dump returned  (must be Python object) object info
obj.somDumpSelf(0)
print(obj)
print(obj.somPrintSelf())
#print("1")
#cls=obj.somGetClass()
#cls.somDumpSelf(0)
# Destroy SOMObect object
del obj
