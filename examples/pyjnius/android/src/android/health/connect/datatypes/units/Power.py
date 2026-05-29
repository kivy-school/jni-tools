from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Power"]

class Power(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Power"
    fromWatts = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Power;")
    getInWatts = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Power;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")