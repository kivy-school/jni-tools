from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseSegment"]

class ExerciseSegment(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseSegment"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getStartTime = JavaMethod("()Ljava/time/Instant;")
    getSegmentType = JavaMethod("()I")
    getRepetitionsCount = JavaMethod("()I")
    getEndTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseSegment$Builder"
        __javaconstructor__ = [("(Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/ExerciseSegment;")
        setRepetitionsCount = JavaMethod("(I)Landroid/health/connect/datatypes/ExerciseSegment$Builder;")