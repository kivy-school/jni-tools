from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseLap"]

class ExerciseLap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseLap"
    getLength = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseLap/Builder"
        __javaconstructor__ = [("(Ljava/time/Instant;Ljava/time/Instant;)V", False)]
        setLength = JavaMethod("(Landroid/health/connect/datatypes/units/Length;)Landroid/health/connect/datatypes/ExerciseLap$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseLap;")