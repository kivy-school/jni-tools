from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemperatureDelta"]

class TemperatureDelta(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/TemperatureDelta"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/TemperatureDelta;)I", False, False)])
    getInCelsius = JavaMethod("()D")
    fromCelsius = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/TemperatureDelta;")