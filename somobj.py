from som import *
from ctypes import *

somdll.SOMObjectNewClass.argtypes = [c_int, c_int]
somdll.SOMObjectNewClass.restype = c_void_p
SOMObjectNewClass=somdll.SOMObjectNewClass

class SOMObjectClassDataStructure(Structure):
    _fields_ = (("classObject", c_void_p),
                ("somInit", somMToken),
                ("somUninit", somMToken),
                ("somFree", somMToken),
                ("somDefaultVCopyInit", somMToken),
                ("somGetClassName", somMToken),
                ("somGetClass", somMToken),
                ("somIsA", somMToken),
                ("somRespondsTo", somMToken),
                ("somIsInstanceOf", somMToken),
                ("somGetSize", somMToken),
                ("somDumpSelf", somMToken),
                ("somDumpSelfInt", somMToken),
                ("somPrintSelf", somMToken),
                ("somDefaultConstVCopyInit", somMToken),
                ("somDispatchV", somMToken),
                ("somDispatchL", somMToken),
                ("somDispatchA", somMToken),
                ("somDispatchD", somMToken),
                ("somDispatch", somMToken),
                ("somClassDispatch", somMToken),
                ("somCastObj", somMToken),
                ("somResetObj", somMToken),
                ("somDefaultInit", somMToken),
                ("somDestruct", somMToken),
                ("somComputeForwardVisitMask", somMToken),
                ("somComputeReverseVisitMask", somMToken),
                ("somDefaultCopyInit", somMToken),
                ("somDefaultConstCopyInit", somMToken),
                ("somDefaultAssign", somMToken),
                ("somDefaultConstAssign", somMToken),
                ("somDefaultVAssign", somMToken),
                ("somDefaultConstVAssign", somMToken),
                ("release", somMToken),
                ("duplicate", somMToken),
                ("get_interface", somMToken),
                ("get_implementation", somMToken),
                ("is_proxy", somMToken),
                ("create_request", somMToken),
                ("create_request_args", somMToken),
                ("is_nil", somMToken)
               )


class SOMObject:
	pass

class SOMClass:
	pass

class SOMObject:
	
#	typedef sequence<SOMObject> SOMObjectSequence;
#	typedef sequence<octet> BooleanSequence;
#	struct somObjectOffset { SOMObject obj;	long offset; };
#	typedef sequence<somObjectOffset> somObjectOffsets;

	SOMObjectClassData=None
	obj=None

	def __init__(self: SOMObject, obj: SOMObject=None):
		if isinstance(obj, SOMObject):
			obj=obj.obj
		if obj==None:
			self.SOMObjectClassData=SOMObjectClassDataStructure.in_dll(somdll,"SOMObjectClassData")
			if self.SOMObjectClassData.classObject==None:
				self.SOMObjectClassData.classObject=SOMObjectNewClass(1, 7)
			mt=somResolveByName(self.SOMObjectClassData.classObject, b"somNew")
			functype = WINFUNCTYPE(c_void_p, c_void_p) 
			somNew = functype(mt)
			self.obj=somNew(self.SOMObjectClassData.classObject)
		else:
			self.obj=obj

	def __del__(self: SOMObject):
		self.somFree()

	def somInit(self: SOMObject):
		mp=somResolveByName(self.obj, b"somInit")
		somTD_SOMObject_somInit = WINFUNCTYPE(None, c_void_p) 
		somInit = somTD_SOMObject_somInit(mp)
		somInit(self.obj)

	def somUninit(self: SOMObject):
		mp=somResolveByName(self.obj, b"somUninit")
		somTD_SOMObject_somUninit = WINFUNCTYPE(None, c_void_p) 
		somUninit = somTD_SOMObject_somUninit(mp)
		somUninit(self.obj)

	def somFree(self: SOMObject):
		mp=somResolveByName(self.obj, b"somFree")
		somTD_SOMObject_somFree = WINFUNCTYPE(None, c_void_p) 
		somFree = somTD_SOMObject_somFree(mp)
		somFree(self.obj)

	# Returns a pointer to an object’s class object. Not generally overridden.
	def somGetClass(self: SOMObject) -> 'SOMClass':
		mp=somResolveByName(self.obj, b"somGetClass")
		somTD_SOMObject_somGetClass = WINFUNCTYPE(c_void_p, c_void_p) 
		somGetClass = somTD_SOMObject_somGetClass(mp)
		return somGetClass(self.obj) #return SOMClass

	def somGetClassName(self: SOMObject) -> str:
		mp=somResolveByName(self.obj, b"somGetClassName")
		somTD_SOMObject_somGetClassName = WINFUNCTYPE(c_char_p, c_void_p) 
		somGetClassName = somTD_SOMObject_somGetClassName(mp)
		return somGetClassName(self.obj) #return string

	def somGetSize(self: SOMObject) -> int:
		mp=somResolveByName(self.obj, b"somGetSize")
		somTD_SOMObject_somGetSize = WINFUNCTYPE(c_long, c_void_p) 
		somGetSize = somTD_SOMObject_somGetSize(mp)
		return somGetSize(self.obj) #return long

	def somIsA(self: SOMObject, aClassObj: SOMClass) -> bool: #in SOMClass
		mp=somResolveByName(self.obj, b"somIsA")
		somTD_SOMObject_somIsA = WINFUNCTYPE(c_boolean, c_void_p, c_void_p) 
		somIsA = somTD_SOMObject_somIsA(mp)
		return somGetSize(self.obj, aClassObj) #return boolean

	def somIsInstanceOf(self: SOMObject, aClassObj: SOMClass) -> bool: #in SOMClass 
		mp=somResolveByName(self.obj, b"somIsInstanceOf")
		somTD_SOMObject_somIsInstanceOf = WINFUNCTYPE(c_boolean, c_void_p, c_void_p) 
		somIsInstanceOf = somTD_SOMObject_somIsInstanceOf(mp)
		return somGetSize(self.obj, aClassObj) #return boolean

	def somRespondsTo(self: SOMObject, mId) -> bool: #in somId 
		mp=somResolveByName(self.obj, b"somRespondsTo")
		somTD_SOMObject_somRespondsTo = WINFUNCTYPE(c_boolean, c_void_p, c_void_p) 
		somRespondsTo = somTD_SOMObject_somRespondsTo(mp)
		return somRespondsTo(self.obj, aClassObj) #return boolean

	def somDispatch(self: SOMObject, retValue, methodId, ap) -> bool: #out somToken, in somId, in va_list
		pass #return boolean

	def somClassDispatch(self: SOMObject, clsObj, retValue, methodId, ap) -> bool: #in SOMClass,out somToken,in somId,in va_list
		pass #return boolean

	def somCastObj(self: SOMObject, castedCls: SOMClass) -> bool: #in SOMClass
		mp=somResolveByName(self.obj, b"somCastObj")
		somTD_SOMObject_somCastObj = WINFUNCTYPE(c_boolean, c_void_p, c_void_p) 
		somCastObj = somTD_SOMObject_somCastObj(mp)
		return somCastObj(self.obj, aClassObj) #return boolean

	def somResetObj(self: SOMObject) -> bool:
		mp=somResolveByName(self.obj, b"somResetObj")
		somTD_SOMObject_somResetObj = WINFUNCTYPE(c_boolean, c_void_p) 
		somResetObj = somTD_SOMObject_somResetObj(mp)
		return somResetObj(self.obj) #return boolean

	# Outputs a brief description that identifies the receiving object. Designed to be overridden
	def somPrintSelf(self: SOMObject) -> SOMObject:
		mp=somResolveByName(self.obj, b"somPrintSelf")
		somTD_SOMObject_somPrintSelf = WINFUNCTYPE(c_void_p, c_void_p) 
		somPrintSelf = somTD_SOMObject_somPrintSelf(mp)
		return somPrintSelf(self.obj)

	# Writes out a detailed description of the receiving object. Intended for use by object clients.
	# Not generally overridden.
	def somDumpSelf(self: SOMObject, level: int): #in long
		mp=somResolveByName(self.obj, b"somDumpSelf")
		somTD_SOMObject_somDumpSelf = WINFUNCTYPE(None, c_void_p, c_long) 
		somDumpSelf = somTD_SOMObject_somDumpSelf(mp)
		somDumpSelf(self.obj, level)

	#Outputs the internal state of an object. Intended to be overridden by class implementors.
	#Not intended to be directly invoked by object clients
	def somDumpSelfInt(self: SOMObject, level: int): #in long
		mp=somResolveByName(self.obj, b"somDumpSelfInt")
		somTD_SOMObject_somDumpSelfInt = WINFUNCTYPE(None, c_void_p, c_long) 
		somDumpSelfInt = somTD_SOMObject_somDumpSelfInt(mp)
		somDumpSelfInt(self.obj, level)

	# SOM 2.1 style constructors/destructors

	def somDefaultInit(self: SOMObject, ctrl): #inout somInitCtrl
		mp=somResolveByName(self.obj, b"somDefaultInit")
		somTD_SOMObject_somDefaultInit = WINFUNCTYPE(None, c_void_p, c_void_p) 
		somDefaultInit = somTD_SOMObject_somDefaultInit(mp)
		somDefaultInit(self.obj, ctrl)

	def somDefaultCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultCopyInit")
		somTD_SOMObject_somDefaultCopyInit = WINFUNCTYPE(None, c_void_p, c_void_p, c_void_p) 
		somDefaultCopyInit = somTD_SOMObject_somDefaultCopyInit(mp)
		somDefaultCopyInit(self.obj, ctrl, fromObj)

	def somDefaultConstCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultConstCopyInit")
		somTD_SOMObject_somDefaultConstCopyInit = WINFUNCTYPE(None, c_void_p, c_void_p, c_void_p) 
		somDefaultConstCopyInit = somTD_SOMObject_somDefaultConstCopyInit(mp)
		somDefaultConstCopyInit(self.obj, ctrl, fromObj)

	def somDefaultVCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultVCopyInit")
		somTD_SOMObject_somDefaultVCopyInit = WINFUNCTYPE(None, c_void_p, c_void_p, c_void_p) 
		somDefaultVCopyInit = somTD_SOMObject_somDefaultVCopyInit(mp)
		somDefaultVCopyInit(self.obj, ctrl, fromObj)

	def somDefaultConstVCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultConstVCopyInit")
		somTD_SOMObject_somDefaultConstVCopyInit = WINFUNCTYPE(None, c_void_p, c_void_p, c_void_p) 
		somDefaultConstVCopyInit = somTD_SOMObject_somDefaultConstVCopyInit(mp)
		somDefaultConstVCopyInit(self.obj, ctrl, fromObj)

	def somDefaultAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultAssign")
		somTD_SOMObject_somDefaultAssign = WINFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p) 
		somDefaultAssign = somTD_SOMObject_somDefaultAssign(mp)
		return somDefaultAssign(self.obj, ctrl, fromObj) #return SOMObject

	def somDefaultConstAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultConstAssign")
		somTD_SOMObject_somDefaultConstAssign = WINFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p) 
		somDefaultConstAssign = somTD_SOMObject_somDefaultConstAssign(mp)
		return somDefaultConstAssign(self.obj, ctrl, fromObj) #return SOMObject

	def somDefaultVAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultVAssign")
		somTD_SOMObject_somDefaultVAssign = WINFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p) 
		somDefaultVAssign = somTD_SOMObject_somDefaultVAssign(mp)
		return somDefaultVAssign(self.obj, ctrl, fromObj) #return SOMObject

	def somDefaultConstVAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		mp=somResolveByName(self.obj, b"somDefaultConstVAssign")
		somTD_SOMObject_somDefaultConstVAssign = WINFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p) 
		somDefaultConstVAssign = somTD_SOMObject_somDefaultConstVAssign(mp)
		return somDefaultConstVAssign(self.obj, ctrl, fromObj) #return SOMObject

	def somDestruct(self: SOMObject, doFree, ctrl): #in octet, inout somDestructCtrl
		mp=somResolveByName(self.obj, b"somDestruct")
		somTD_SOMObject_somDestruct = WINFUNCTYPE(c_void_p, c_void_p, c_byte, c_void_p) 
		somDestruct = somTD_SOMObject_somDestruct(mp)
		somDestruct(self.obj, doFree, ctrl)

