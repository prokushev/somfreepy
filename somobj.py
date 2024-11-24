from som import *
from ctypes import *

# Forward declaration of SOMClass
class SOMClass:
	pass

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

class SOMObject:
	
#	typedef sequence<SOMObject> SOMObjectSequence;
#	typedef sequence<octet> BooleanSequence;
#	struct somObjectOffset { SOMObject obj;	long offset; };
#	typedef sequence<somObjectOffset> somObjectOffsets;

	SOMObjectClassData=None
	obj=None

	def __init__(self: SOMObject, obj: SOMObject=None):
		if obj==None:
			self.SOMObjectClassData=SOMObjectClassDataStructure.in_dll(somdll,"SOMObjectClassData")
			if self.SOMObjectClassData.classObject==None:
				self.SOMObjectClassData.classObject=SOMObjectNewClass(1, 4)
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
		#@todo Destroy Python object too?
		mp=somResolveByName(self.obj, b"somFree")
		somTD_SOMObject_somFree = WINFUNCTYPE(None, c_void_p) 
		somFree = somTD_SOMObject_somFree(mp)
		somFree(self.obj)
		self.obj=None

	def somGetClass(self: SOMObject) -> SOMClass:
		#@todo  Return Python class???
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
		#@todo check type of aClassObj. If it is Python object then get SOM Object
		mp=somResolveByName(self.obj, b"somIsA")
		somTD_SOMObject_somIsA = WINFUNCTYPE(c_boolean, c_void_p, c_void_p) 
		somIsA = somTD_SOMObject_somIsA(mp)
		return somGetSize(self.obj, aClassObj) #return boolean

	def somIsInstanceOf(self: SOMObject, aClassObj: SOMClass) -> bool: #in SOMClass 
		#@todo check type of aClassObj. If it is Python object then get SOM Object
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
		#@todo check type of aClassObj. If it is Python object then get SOM Object
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
		obj=somPrintSelf(self.obj)
		if obj==self.obj:
			return self
		# This must not be happen
		else:
			return SOMObject(obj)

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
		somDefaultInit(self.obj, level)

	def somDefaultCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultConstCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultVCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultConstVCopyInit(self: SOMObject, ctrl, fromObj): #inout somInitCtrl, in SOMObject
		pass

	def somDefaultAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultConstAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultVAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDefaultConstVAssign(self: SOMObject, ctrl, fromObj) -> SOMObject: #inout somAssignCtrl, in SOMObject
		pass #return SOMObject

	def somDestruct(self: SOMObject, doFree, ctrl): #in octet, inout somDestructCtrl
		pass

