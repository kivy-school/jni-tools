from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemperatureDelta"]

class TemperatureDelta(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/TemperatureDelta"
    fromCelsius = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/TemperatureDelta;")
    getInCelsius = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/TemperatureDelta;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")