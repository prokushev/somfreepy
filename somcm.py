from somobj import *

class SOMClassMgr:
	pass

somdll.SOMClassMgrNewClass.argtypes = [c_int, c_int]
somdll.SOMClassMgrNewClass.restype = c_void_p
SOMClassMgrNewClass=somdll.SOMClassMgrNewClass

class SOMClassMgrClassDataStructure(Structure):
    _fields_ = (("classObject", c_void_p),
		("somFindClsInFile", somMToken),
		("somFindClass", somMToken),
		("somClassFromId", somMToken),
		("somRegisterClass", somMToken),
		("somUnregisterClass", somMToken),
		("somLocateClassFile", somMToken),
		("somLoadClassFile", somMToken),
		("somUnloadClassFile", somMToken),
		("somGetInitFunction", somMToken),
		("somMergeInto", somMToken),
		("somGetRelatedClasses", somMToken),
		("somSubstituteClass", somMToken),
		("_get_somInterfaceRepository", somMToken),
		("_set_somInterfaceRepository", somMToken),
		("_get_somRegisteredClasses", somMToken),
		("somBeginPersistentClasses", somMToken),
		("somEndPersistentClasses", somMToken),
		("somReleaseClasses", somMToken),
		("somRegisterThreadUsage", somMToken),
		("somRegisterClassLibrary", somMToken),
		("somJoinAffinityGroup", somMToken),
		("somUnregisterClassLibrary", somMToken),
		("somImportObject", somMToken),
		("private23", somMToken),
		("private24", somMToken)
		)

SOMClassMgrClassData=SOMClassMgrClassDataStructure.in_dll(somdll,"SOMClassMgrClassData")

class SOMClassMgr(SOMObject):

#	SOMClassMgrClassData=None
#	obj=None

	def __init__(self: SOMClassMgr, obj: SOMClassMgr=None):
		if isinstance(obj, SOMClassMgr):
			obj=obj.obj
		if obj==None:
			if SOMClassMgrClassData.classObject==None:
				SOMClassMgrClassData.classObject=SOMClassMgrNewClass(1, 4)
			mt=somResolveByName(SOMClassMgrClassData.classObject, b"somNew")
			somTD_SOMClass_somNew = WINFUNCTYPE(c_void_p, c_void_p) 
			somNew = somTD_SOMClass_somNew(mt)
			self.obj=somNew(SOMClassMgrClassData.classObject)
		else:
			self.obj=obj

#	typedef SOMClass * SOMClassArray;

#	SOMClass somLoadClassFile(in somId classId,in long majorVersion,in long minorVersion,in string file);
#	string somLocateClassFile(in somId classId,in long majorVersion,in long minorVersion);
#	void somRegisterClass(in SOMClass classObj);
#	void somRegisterClassLibrary(in string libraryName,in somMethodPtr libraryInitRtn);
#	void somUnregisterClassLibrary(in string libraryName);
#	long somUnloadClassFile(in SOMClass classObj);
#	long somUnregisterClass(in SOMClass classObj);
	def somBeginPersistentClasses(self):
		mp=somResolveByName(self.obj, b"somBeginPersistentClasses")
		somTD_SOMClassMgr_somBeginPersistentClasses = WINFUNCTYPE(None, c_void_p) 
		somBeginPersistentClasses = somTD_SOMClassMgr_somBeginPersistentClasses(mp)
		somBeginPersistentClasses(self.obj)

	def somEndPersistentClasses(self):
		mp=somResolveByName(self.obj, b"somEndPersistentClasses")
		somTD_SOMClassMgr_somEndPersistentClasses = WINFUNCTYPE(None, c_void_p) 
		somEndPersistentClasses = somTD_SOMClassMgr_somEndPersistentClasses(mp)
		somEndPersistentClasses(self.obj)

#	boolean somJoinAffinityGroup(in SOMClass newClass,in SOMClass affClass);

	def somGetInitFunction(self: SOMClassMgr) -> str:
		mp=somResolveByName(self.obj, b"somGetInitFunction")
		somTD_SOMClassMgr_somGetInitFunction = WINFUNCTYPE(c_char_p, c_void_p) 
		somGetInitFunction = somTD_SOMClassMgr_somGetInitFunction(mp)
		return somGetInitFunction(self.obj)
		
#	attribute Repository somInterfaceRepository;
#	readonly attribute sequence<SOMClass> somRegisteredClasses;
#	SOMClassArray somGetRelatedClasses(in SOMClass classObj);
#	SOMClass somClassFromId(in somId classId);
#	SOMClass somFindClass(in somId classId,in long majorVersion,in long minorVersion);
#	SOMClass somFindClsInFile(in somId classId,in long majorVersion,in long minorVersion,in string file);
#	void somMergeInto(in SOMObject targetObj);
#	long somSubstituteClass(in string origClassName,in string newClassName);
#/*	boolean somImportObject(in SOMObject objToBeShared);*/
