from som import *
from ctypes import *

# Forward declatation of SOMClass
class SOMClass:
	pass

class SOMObjectClassDataStructure(Structure):
    _fields_ = (("classObject", c_void_p),
                ("somInit", c_void_p),
                ("somUninit", c_void_p),
                ("somFree", c_void_p),
                ("somDefaultVCopyInit", c_void_p),
                ("somGetClassName", c_void_p),
                ("somGetClass", c_void_p),
                ("somIsA", c_void_p),
                ("somRespondsTo", c_void_p),
                ("somIsInstanceOf", c_void_p),
                ("somGetSize", c_void_p),
                ("somDumpSelf", c_void_p),
                ("somDumpSelfInt", c_void_p),
                ("somPrintSelf", c_void_p),
                ("somDefaultConstVCopyInit", c_void_p),
                ("somDispatchV", c_void_p),
                ("somDispatchL", c_void_p),
                ("somDispatchA", c_void_p),
                ("somDispatchD", c_void_p),
                ("somDispatch", c_void_p),
                ("somClassDispatch", c_void_p),
                ("somCastObj", c_void_p),
                ("somResetObj", c_void_p),
                ("somDefaultInit", c_void_p),
                ("somDestruct", c_void_p),
                ("somComputeForwardVisitMask", c_void_p),
                ("somComputeReverseVisitMask", c_void_p),
                ("somDefaultCopyInit", c_void_p),
                ("somDefaultConstCopyInit", c_void_p),
                ("somDefaultAssign", c_void_p),
                ("somDefaultConstAssign", c_void_p),
                ("somDefaultVAssign", c_void_p),
                ("somDefaultConstVAssign", c_void_p),
                ("release", c_void_p),
                ("duplicate", c_void_p),
                ("get_interface", c_void_p),
                ("get_implementation", c_void_p),
                ("is_proxy", c_void_p),
                ("create_request", c_void_p),
                ("create_request_args", c_void_p),
                ("is_nil", c_void_p)
               )


class SOMObject:
	
#	typedef sequence<SOMObject> SOMObjectSequence;
#	typedef sequence<octet> BooleanSequence;
#	struct somObjectOffset { SOMObject obj;	long offset; };
#	typedef sequence<somObjectOffset> somObjectOffsets;

	SOMObjectClassData=None
	obj=None

	def __init__(self):
		self.SOMObjectClassData=SOMObjectClassDataStructure.in_dll(somdll,"SOMObjectClassData")
		if self.SOMObjectClassData.classObject==None:
			somdll.SOMObjectNewClass.argtypes = [c_int, c_int]
			somdll.SOMObjectNewClass.restype = c_void_p
			self.SOMObjectClassData.classObject=somdll.SOMObjectNewClass(1, 4)
		mt=somResolveByName(self.SOMObjectClassData.classObject, b"somNew")
		functype = WINFUNCTYPE(c_void_p, c_void_p) 
		somNew = functype(mt)
		self.obj=somNew(self.SOMObjectClassData.classObject)

	def __del__(self):
		print(self)
		self.somFree()
		print(self.obj)

	def somInit(self):
		pass

	def somUninit(self):
		pass

	def somFree(self):
		mp=somResolveByName(self.obj, b"somFree")
		somTD_SOMObject_somFree = WINFUNCTYPE(None, c_void_p) 
		somFree = somTD_SOMObject_somFree(mp)
		somFree(self.obj)
		self.obj=None

	def somGetClass(self):
		pass #return #SOMClass

	def somGetClassName(self):
		mp=somResolveByName(self.obj, b"somGetClassName")
		somTD_SOMObject_somGetClassName = WINFUNCTYPE(c_char_p, c_void_p) 
		somGetClassName = somTD_SOMObject_somGetClassName(mp)
		return somGetClassName(self.obj) #return string

	def somGetSize(self):
		pass #return long

	def somIsA(self, aClassObj): #in SOMClass 
		pass #return boolean

	def somIsInstanceOf(self, aClassObj): #in SOMClass 
		pass #return boolean 

	def somRespondsTo(self, mId): #in somId 
		pass #return boolean

	def somDispatch(self, retValue, methodId, ap): #out somToken, in somId, in va_list
		pass #return boolean

	def somClassDispatch(self, clsObj, retValue, methodId, ap): #in SOMClass,out somToken,in somId,in va_list
		pass #return boolean

	def somCastObj(self, castedCls): #in SOMClass
		pass #return boolean

	def somResetObj(self):
		pass #return boolean 

	def somPrintSelf(self):
		mp=somResolveByName(self.obj, b"somPrintSelf")
		somTD_SOMObject_somPrintSelf = WINFUNCTYPE(c_void_p, c_void_p) 
		somPrintSelf = somTD_SOMObject_somPrintSelf(mp)
		return somPrintSelf(self.obj) #return SOMObject

	def somDumpSelf(self, level): #in long
		mp=somResolveByName(self.obj, b"somDumpSelf")
		somTD_SOMObject_somDumpSelf = WINFUNCTYPE(None, c_void_p, c_long) 
		somDumpSelf = somTD_SOMObject_somDumpSelf(mp)
		somDumpSelf(self.obj, level) #return SOMObject

	def somDumpSelfInt(self, level): #in long
		mp=somResolveByName(self.obj, b"somDumpSelfInt")
		somTD_SOMObject_somDumpSelfInt = WINFUNCTYPE(None, c_void_p, c_long) 
		somDumpSelfInt = somTD_SOMObject_somDumpSelfInt(mp)
		somDumpSelfInt(self.obj, level) #return SOMObject

	# SOM 2.1 style constructors/destructors

	def somDefaultInit(self, ctrl): #inout somInitCtrl
		pass

	def somDefaultCopyInit(self, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultConstCopyInit(self, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultVCopyInit(self, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultConstVCopyInit(self, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultAssign(self, ctrl, fromObj): #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultConstAssign(self, ctrl, fromObj): #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultVAssign(self, ctrl, fromObj): #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultConstVAssign(self, ctrl, fromObj): #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDestruct(self, doFree, ctrl): #in octet, inout somDestructCtrl
		pass

