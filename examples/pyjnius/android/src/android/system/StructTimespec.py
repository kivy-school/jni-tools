from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructTimespec"]

class StructTimespec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructTimespec"
    __javaconstructor__ = [("(JJ)V", False)]
    tv_nsec = JavaField("J")
    tv_sec = JavaField("J")
    compareTo = JavaMethod("(Landroid/system/StructTimespec;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")