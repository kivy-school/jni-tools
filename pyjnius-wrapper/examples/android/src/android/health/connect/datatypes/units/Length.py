from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Length"]

class Length(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Length"
    fromMeters = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Length;")
    getInMeters = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")