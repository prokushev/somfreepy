from som import *
from somobj import *
from somcm import *
import CORBA

print("Hello")

# Turn on SOM run-time trace
#SOM_TraceLevel.value=2

# Initialize SOM
cm=somEnvironmentNew()

# Call some methods of SOMClassMAnager object
cm.somDumpSelf(0)
print(cm.somGetInitFunction())

# Create SOMObject
obj=SOMObject()
# Dump object info
print(obj)
# Call some methods and dump returned  (must be Python object) object info
print(obj.somPrintSelf())
obj.somDumpSelf(0)
print(obj.somGetClassName())
# Destroy SOMObect object
del obj
