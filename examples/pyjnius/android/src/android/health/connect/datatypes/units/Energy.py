from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Energy"]

class Energy(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Energy"
    fromCalories = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Energy;")
    getInCalories = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Energy;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")