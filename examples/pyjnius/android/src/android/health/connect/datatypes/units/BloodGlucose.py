from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BloodGlucose"]

class BloodGlucose(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/BloodGlucose"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/BloodGlucose;)I", False, False)])
    fromMillimolesPerLiter = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/BloodGlucose;")
    getInMillimolesPerLiter = JavaMethod("()D")