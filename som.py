from ctypes import *

# Load SOM.DLL
somdll = WinDLL("som.dll", winmode=0)

##
# SOM Run-time types
##

#	typedef struct somMethodTabStruct 
#	{
#		SOMClass        SOMSTAR  classObject;
#		somClassInfo			 *classInfo;
#		char					 *className;
#		long					 instanceSize;
#		long					 dataAlignment;
#		long					 mtabSize;
#		long                     protectedDataOffset;
#		somDToken                protectedDataToken;
#		somEmbeddedObjStruct     *embeddedObjs;
#
#		somMethodPtr entries[1];
#	} somMethodTab, *somMethodTabPtr;

somToken=c_void_p;

somDToken=somToken;
somMToken=somToken;

somClassInfo=somToken;

somMethodProc = WINFUNCTYPE(None) 

somMethodPtr=POINTER(somMethodProc)

class somMethodTab(Structure):
	_fields_ = [
		("classObject", c_void_p),
		("classInfo", POINTER(somClassInfo)),
		("className", c_char_p),
		("instanceSize", c_long),
		("dataAlignment", c_long),
		("mtabSize", c_long),
		("protectedDataOffset", c_long),
		("protectedDataToken", somDToken),
		("embeddedObjs", c_void_p),
		("entries", ARRAY(somMethodProc,1))
		]
	

class SOMAny(Structure):
	_fields_ = [("mtab", POINTER(somMethodTab))]

##
# Variables
##

SOM_TraceLevel=c_int.in_dll(somdll,"SOM_TraceLevel")

##
# SOM Run-time functions
##

#SOMEXTERN SOM_IMPORTEXPORT_som somMethodProc * SOMLINK somResolveByName(SOMObject SOMSTAR obj,char *methodName);
somdll.somResolveByName.argtypes = [c_void_p, c_char_p]
somdll.somResolveByName.restype = c_void_p
somResolveByName=somdll.somResolveByName

from somcm import *

#SOMEXTERN SOM_IMPORTEXPORT_som SOMClassMgr SOMSTAR SOMLINK somEnvironmentNew(void);
somdll.somEnvironmentNew.argtypes = None
somdll.somEnvironmentNew.restype = c_void_p
def somEnvironmentNew():
	return SOMClassMgr(somdll.somEnvironmentNew())
