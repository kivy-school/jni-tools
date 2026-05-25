from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Volume"]

class Volume(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Volume"
    fromLiters = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Volume;")
    getInLiters = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Volume;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")