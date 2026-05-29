from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlannedExerciseBlock"]

class PlannedExerciseBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PlannedExerciseBlock"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getRepetitions = JavaMethod("()I")
    getSteps = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PlannedExerciseBlock$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        setSteps = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        addStep = JavaMethod("(Landroid/health/connect/datatypes/PlannedExerciseStep;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        clearSteps = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        setRepetitions = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseBlock;")