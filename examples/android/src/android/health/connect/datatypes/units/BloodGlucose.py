from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BloodGlucose"]

class BloodGlucose(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/BloodGlucose"
    fromMillimolesPerLiter = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/BloodGlucose;")
    getInMillimolesPerLiter = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/BloodGlucose;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")