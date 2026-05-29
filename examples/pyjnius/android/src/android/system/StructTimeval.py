from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructTimeval"]

class StructTimeval(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructTimeval"
    tv_sec = JavaField("J")
    tv_usec = JavaField("J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    toMillis = JavaMethod("()J")
    fromMillis = JavaStaticMethod("(J)Landroid/system/StructTimeval;")