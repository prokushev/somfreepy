from som import *
from somobj import *
import CORBA

print("Hello\n")
cm=somEnvironmentNew()
mt=somResolveByName(cm, b"somPrintSelf")
functype = WINFUNCTYPE(None, c_void_p) 
somPrintSelf = functype(mt)
somPrintSelf(cm)

obj=SOMObject()
obj.somPrintSelf()
obj.somDumpSelf(0)
print(obj.somGetClassName())
del obj
