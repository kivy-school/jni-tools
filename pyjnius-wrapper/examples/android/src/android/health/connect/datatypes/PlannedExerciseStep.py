from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlannedExerciseStep"]

class PlannedExerciseStep(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PlannedExerciseStep"
    EXERCISE_CATEGORY_ACTIVE = JavaStaticField("I")
    EXERCISE_CATEGORY_COOLDOWN = JavaStaticField("I")
    EXERCISE_CATEGORY_RECOVERY = JavaStaticField("I")
    EXERCISE_CATEGORY_REST = JavaStaticField("I")
    EXERCISE_CATEGORY_UNKNOWN = JavaStaticField("I")
    EXERCISE_CATEGORY_WARMUP = JavaStaticField("I")
    getExerciseType = JavaMethod("()I")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getExerciseCategory = JavaMethod("()I")
    getCompletionGoal = JavaMethod("()Landroid/health/connect/datatypes/ExerciseCompletionGoal;")
    getPerformanceGoals = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PlannedExerciseStep/Builder"
        __javaconstructor__ = [("(IILandroid/health/connect/datatypes/ExerciseCompletionGoal;)V", False)]
        setExerciseType = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        setExerciseCategory = JavaMethod("(I)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        setCompletionGoal = JavaMethod("(Landroid/health/connect/datatypes/ExerciseCompletionGoal;)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        addPerformanceGoal = JavaMethod("(Landroid/health/connect/datatypes/ExercisePerformanceGoal;)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        setPerformanceGoals = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        clearPerformanceGoals = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseStep$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PlannedExerciseStep;")