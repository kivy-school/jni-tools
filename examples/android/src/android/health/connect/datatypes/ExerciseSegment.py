from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseSegment"]

class ExerciseSegment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseSegment"
    getSegmentType = JavaMethod("()I")
    getRepetitionsCount = JavaMethod("()I")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getEndTime = JavaMethod("()Ljava/time/Instant;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseSegment/Builder"
        __javaconstructor__ = [("(Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        setRepetitionsCount = JavaMethod("(I)Landroid/health/connect/datatypes/ExerciseSegment$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseSegment;")