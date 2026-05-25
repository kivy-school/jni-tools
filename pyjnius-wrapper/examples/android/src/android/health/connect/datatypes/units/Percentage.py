from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Percentage"]

class Percentage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Percentage"
    fromValue = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Percentage;")
    getValue = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Percentage;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")