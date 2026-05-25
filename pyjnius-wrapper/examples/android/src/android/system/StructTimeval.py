from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructTimeval"]

class StructTimeval(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructTimeval"
    tv_sec = JavaField("J")
    tv_usec = JavaField("J")
    fromMillis = JavaStaticMethod("(J)Landroid/system/StructTimeval;")
    toMillis = JavaMethod("()J")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")