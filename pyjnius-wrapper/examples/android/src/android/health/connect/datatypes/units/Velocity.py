from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Velocity"]

class Velocity(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/units/Velocity"
    fromMetersPerSecond = JavaStaticMethod("(D)Landroid/health/connect/datatypes/units/Velocity;")
    getInMetersPerSecond = JavaMethod("()D")
    compareTo = JavaMethod("(Landroid/health/connect/datatypes/units/Velocity;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")