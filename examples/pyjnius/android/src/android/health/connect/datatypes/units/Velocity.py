from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Velocity"]

class Velocity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Velocity"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    compareTo = JavaMultipleMethod([("(Ljava/lang/Object;)I", False, False), ("(Landroid/health/connect/datatypes/units/Velocity;)I", False, False)])
    fromMetersPerSecond = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Velocity;")
    getInMetersPerSecond = JavaMethod("()D")