from som import *
from somobj import *
import CORBA

print("Hello\n")

# Initialize SOM
cm=somEnvironmentNew()

# Find methos of SOMClassMgrbject
mt=somResolveByName(cm, b"somPrintSelf")
functype = WINFUNCTYPE(None, c_void_p) 
somPrintSelf = functype(mt)
# Call it
somPrintSelf(cm)

# Create SOMObject
obj=SOMObject()
# Call some methods
obj.somPrintSelf()
obj.somDumpSelf(0)
print(obj.somGetClassName())
# Destroy SOMObect object
del obj
