from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MethodHandleInfo"]

class MethodHandleInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/invoke/MethodHandleInfo"
    REF_getField = JavaStaticField("I")
    REF_getStatic = JavaStaticField("I")
    REF_putField = JavaStaticField("I")
    REF_putStatic = JavaStaticField("I")
    REF_invokeVirtual = JavaStaticField("I")
    REF_invokeStatic = JavaStaticField("I")
    REF_invokeSpecial = JavaStaticField("I")
    REF_newInvokeSpecial = JavaStaticField("I")
    REF_invokeInterface = JavaStaticField("I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaStaticMethod("(ILjava/lang/Class;Ljava/lang/String;Ljava/lang/invoke/MethodType;)Ljava/lang/String;")
    getModifiers = JavaMethod("()I")
    getDeclaringClass = JavaMethod("()Ljava/lang/Class;")
    isVarArgs = JavaMethod("()Z")
    getReferenceKind = JavaMethod("()I")
    getMethodType = JavaMethod("()Ljava/lang/invoke/MethodType;")
    reflectAs = JavaMethod("(Ljava/lang/Class;Ljava/lang/invoke/MethodHandles$Lookup;)Ljava/lang/reflect/Member;")
    referenceKindToString = JavaStaticMethod("(I)Ljava/lang/String;")