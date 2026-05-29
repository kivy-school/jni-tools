from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Temperature"]

class Temperature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Temperature"
    fromCelsius = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Temperature;")
    getInCelsius = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Temperature;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")