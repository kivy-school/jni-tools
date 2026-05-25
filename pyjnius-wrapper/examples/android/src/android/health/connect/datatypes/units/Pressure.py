from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Pressure"]

class Pressure(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Pressure"
    fromMillimetersOfMercury = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Pressure;")
    getInMillimetersOfMercury = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Pressure;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")