from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Mass"]

class Mass(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Mass"
    fromGrams = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Mass;")
    getInGrams = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Mass;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")