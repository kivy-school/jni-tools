from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Mass"]

class Mass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Mass"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Mass;)I", False, False)])
    getInGrams = JavaMethod("()D")
    fromGrams = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Mass;")