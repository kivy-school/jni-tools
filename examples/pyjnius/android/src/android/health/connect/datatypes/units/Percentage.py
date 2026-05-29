from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Percentage"]

class Percentage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Percentage"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Percentage;)I", False, False)])
    getValue = JavaMethod("()D")
    fromValue = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Percentage;")