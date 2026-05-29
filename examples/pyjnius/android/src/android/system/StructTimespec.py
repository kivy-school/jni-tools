from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructTimespec"]

class StructTimespec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructTimespec"
    __javaconstructor__ = [("(JJ)V", False)]
    tv_nsec = JavaField("J")
    tv_sec = JavaField("J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Landroid/system/StructTimespec;)I", False, False), ("(Ljava/lang/Object;)I", False, False)])