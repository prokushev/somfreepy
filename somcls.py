from somobj import *

somdll.SOMClassNewClass.argtypes = [c_int, c_int]
somdll.SOMClassNewClass.restype = c_void_p
SOMClassNewClass=somdll.SOMClassNewClass

class SOMClassClassDataStructure(Structure):
    _fields_ = (("classObject", c_void_p),
		("somNew", somMToken),
		("somRenew", somMToken),
		("somInitClass", somMToken),
		("somClassReady", somMToken),
		("somGetName", somMToken),
		("somGetParent", somMToken),
		("somDescendedFrom", somMToken),
		("somCheckVersion", somMToken),
		("somFindMethod", somMToken),
		("somFindMethodOk", somMToken),
		("somSupportsMethod", somMToken),
		("somGetNumMethods", somMToken),
		("somGetInstanceSize", somMToken),
		("somGetInstanceOffset", somMToken),
		("somGetInstancePartSize", somMToken),
		("somGetMethodIndex", somMToken),
		("somGetNumStaticMethods", somMToken),
		("somGetPClsMtab", somMToken),
		("somGetClassMtab", somMToken),
		("somAddStaticMethod", somMToken),
		("somOverrideSMethod", somMToken),
		("somAddDynamicMethod", somMToken),
		("somGetMethodOffset", somMToken),
		("somGetApplyStub", somMToken),
		("somFindSMethod", somMToken),
		("somFindSMethodOk", somMToken),
		("somGetMethodDescriptor", somMToken),
		("somGetNthMethodInfo", somMToken),
		("somSetClassData", somMToken),
		("somGetClassData", somMToken),
		("somNewNoInit", somMToken),
		("somRenewNoInit", somMToken),
		("somGetInstanceToken", somMToken),
		("somGetMemberToken", somMToken),
		("somSetMethodDescriptor", somMToken),
		("somGetMethodData", somMToken),
		("somOverrideMtab", somMToken),
		("somGetMethodToken", somMToken),
		("somGetParents", somMToken),
		("somGetPClsMtabs", somMToken),
		("somInitMIClass", somMToken),
		("somGetVersionNumbers", somMToken),
		("somLookupMethod", somMToken),
		("_get_somInstanceDataOffsets", somMToken),
		("somRenewNoZero", somMToken),
		("somRenewNoInitNoZero", somMToken),
		("somAllocate", somMToken),
		("somDeallocate", somMToken),
		("somGetRdStub", somMToken),
		("somGetNthMethodData", somMToken),
		("somCloneClass", somMToken),
		("_get_somMethodOffsets", somMToken),
		("_get_somDirectInitClasses", somMToken),
		("_set_somDirectInitClasses", somMToken),
		("somGetInstanceInitMask", somMToken),
		("somGetInstanceDestructionMask", somMToken),
		("somCastObjCls", somMToken),
		("somResetObjCls", somMToken),
		("_get_somTrueClass", somMToken),
		("_get_somCastedClass", somMToken),
		("somRegLPMToken", somMToken),
		("somDefinedMethod", somMToken),
		("somAddMethod", somMToken),
		("_get_somCClassData", somMToken),
		("_set_somCClassData", somMToken),
		("somClassOfNewClassWithParents", somMToken),
		("_set_somClassDataOrder", somMToken),
		("_get_somClassDataOrder", somMToken),
		("somGetClassDataEntry", somMToken),
		("somSetClassDataEntry", somMToken),
		("_get_somDataAlignment", somMToken),
		("somGetInstanceAssignmentMask", somMToken),
		("_get_somDirectAssignClasses", somMToken),
		("setUserPCallDispatch", somMToken),
		("_get_somClassAllocate", somMToken),
		("_get_somClassDeallocate", somMToken)
		)

SOMClassClassData=SOMClassClassDataStructure.in_dll(somdll,"SOMClassClassData")

class SOMClass:
	pass

class SOMClass(SOMObject):

#	SOMClassClassData=None
#	obj=None

	def __init__(self: SOMClass, obj: SOMClass=None):
		if isinstance(obj, SOMClass):
			obj=obj.obj
		if obj==None:
			if SOMClassClassData.classObject==None:
				SOMClassClassData.classObject=SOMClassNewClass(1, 6)
			mt=somResolveByName(SOMClassClassData.classObject, b"somNew")
			somTD_SOMClass_somNew = WINFUNCTYPE(c_void_p, c_void_p) 
			somNew = somTD_SOMClass_somNew(mt)
			self.obj=somNew(SOMClassClassData.classObject)
		else:
			self.obj=obj

#	typedef sequence<somToken> somTokenSequence;
#	typedef sequence<SOMClass> SOMClassSequence;
#	struct somOffsetInfo { SOMClass cls; long offset; };
#	typedef sequence<somOffsetInfo> somOffsets;
#	typedef sequence<somId> somIdSequence;

	def somNew(self) -> 'SOMObject':
		pass

#	SOMObject somNewNoInit();
#	SOMObject somRenew(in void * obj);
#	SOMObject somRenewNoInit(in void * obj);
#	SOMObject somRenewNoZero(in void * obj);
#	SOMObject somRenewNoInitNoZero(in void * obj);
#	somToken somAllocate(in long size);
#	void somDeallocate(in somToken memptr);
#	SOMClass somGetParent();
#/*	SOMClass somJoin(in SOMClass secondParent,in string nameOfNewClass);
#	SOMClass somEndow(in SOMClass parent,in string nameOfNewClass);*/
#	SOMClass somClassOfNewClassWithParents(in string newClassName,in SOMClassSequence parents,in SOMClass explicitMeta);
#	void somInitClass(in string className,in SOMClass parentClass,in long dataSize,in long maxStaticMethods,in long majorVersion,in long minorVersion);
#	void somInitMIClass(in unsigned long inherit_vars,in string className,in SOMClassSequence parentClasses,
#		in long dataSize,in long dataAlignment,in long maxNDMethods,in long majorVersion,in long minorVersion);
#	somMToken somAddStaticMethod(in somId methodId,in somId methodDescriptor,
#		in somMethodPtr method,in somMethodPtr redispatchStub,in somMethodPtr applyStub);
#	void somOverrideSMethod(in somId methodId,in somMethodPtr method);
#	void somClassReady();
#	void somAddDynamicMethod(in somId methodId,in somId methodDescriptor,in somMethodPtr methodImpl,in somMethodPtr applyStub);
#	string somGetName();
#	void somGetVersionNumbers(out long majorVersion,out long minorVersion);
#	long somGetNumMethods();
#	long somGetNumStaticMethods();
#	SOMClassSequence somGetParents();
#	long somGetInstanceSize();
#	long somGetInstancePartSize();
#	somDToken somGetInstanceToken();
#	somDToken somGetMemberToken(in long memberOffset,in somDToken instanceToken);
#	somMethodTab * somGetClassMtab();
#/*	somMethodTabs somGetPClsMtabs(); disappeared in SOM 3.0 */
#	somClassDataStructure *somGetClassData();
#	void somSetClassData(in somClassDataStructure *cds);
#	boolean somSetMethodDescriptor(in somId methodId,in somId descriptor);
#	readonly attribute long somDataAlignment;
#	readonly attribute somOffsets somInstanceDataOffsets;
#	attribute SOMClassSequence somDirectInitClasses;
#	somId somGetMethodDescriptor(in somId methodId);
#	long somGetMethodIndex(in somId id);
#	somMToken somGetMethodToken(in somId methodId);
#	somId somGetNthMethodInfo(in long n,out somId descriptor);
#/*	somToken somGetMarshalPlan(in somId methodId);*/
#	boolean somGetMethodData(in somId methodId,out somMethodData md);
#	boolean somGetNthMethodData(in long n,out somMethodData md);
#	boolean somFindMethod(in somId methodId,out somMethodPtr m);
#	boolean somFindMethodOk(in somId methodId,out somMethodPtr m);
#	somMethodPtr somFindSMethod(in somId methodId);
#	somMethodPtr somFindSMethodOk(in somId methodId);
#	somMethodPtr somLookupMethod(in somId methodId);
#	somMethodPtr somGetApplyStub(in somId methodId);
#	somMethodTabs somGetPClsMtab();
#	boolean somCheckVersion(in long majorVersion,in long minorVersion);
#	boolean somDescendedFrom(in SOMClass aClassObj);
#	boolean somSupportsMethod(in somId mId);
#	somMethodPtr somDefinedMethod(in somMToken method);
#/*	SOMClass somMethodImplOwner(inout somMethodData md);*/
#	somMethodProc * somGetRdStub(in somId methodId);
#	void somOverrideMtab();
#/*	long somGetInstanceOffset(); disappeared in SOM 3.0 */
#
#	readonly attribute somMethodPtr somClassAllocate;
#	readonly attribute somMethodPtr somClassDeallocate;
