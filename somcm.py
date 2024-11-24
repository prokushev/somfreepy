from somobj import *

class SOMClassMgr:
	pass

class SOMClassMgr(SOMObject):

	SOMClassMgrClassData=None
	obj=None

	def __init__(self: SOMClassMgr, obj: SOMClassMgr=None):
		if obj==None:
			self.SOMClassMgrClassData=SOMClassMgrClassDataStructure.in_dll(somdll,"SOMClassMgrClassData")
			if self.SOMClassMgrClassData.classObject==None:
				self.SOMClassMgrClassData.classObject=SOMClassMgrNewClass(1, 4)
			mt=somResolveByName(self.SOMClassMgrClassData.classObject, b"somNew")
			functype = WINFUNCTYPE(c_void_p, c_void_p) 
			somNew = functype(mt)
			self.obj=somNew(self.SOMClassMgrClassData.classObject)
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
#	void somBeginPersistentClasses();
#	void somEndPersistentClasses();
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
