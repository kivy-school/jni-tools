from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseLap"]

class ExerciseLap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseLap"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLength = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseLap$Builder"
        __javaconstructor__ = [("(Ljava/time/Instant;Ljava/time/Instant;)V", False)]
        setLength = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseLap$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseLap;")