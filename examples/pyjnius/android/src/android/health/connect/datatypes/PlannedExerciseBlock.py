from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlannedExerciseBlock"]

class PlannedExerciseBlock(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PlannedExerciseBlock"
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getSteps = JavaMethod("()Ljava/util/List;")
    getRepetitions = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PlannedExerciseBlock/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setRepetitions = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        addStep = JavaMethod("(Landroid/health/connect/datatypes/PlannedExerciseStep;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        setSteps = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        clearSteps = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseBlock$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseBlock;")