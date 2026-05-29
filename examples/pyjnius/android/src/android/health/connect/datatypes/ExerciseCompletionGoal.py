from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseCompletionGoal"]

class ExerciseCompletionGoal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal"

    class UnspecifiedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$UnspecifiedGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExerciseCompletionGoal$UnspecifiedGoal;")

    class UnknownGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$UnknownGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExerciseCompletionGoal$UnknownGoal;")

    class TotalCaloriesBurnedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$TotalCaloriesBurnedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Energy;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getTotalCalories = JavaMethod("()Landroid/health/connect/datatypes/units/Energy;")

    class StepsGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$StepsGoal"
        __javaconstructor__ = [("(I)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getSteps = JavaMethod("()I")

    class RepetitionsGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$RepetitionsGoal"
        __javaconstructor__ = [("(I)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getRepetitions = JavaMethod("()I")

    class DurationGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$DurationGoal"
        __javaconstructor__ = [("(Ljava/time/Duration;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getDuration = JavaMethod("()Ljava/time/Duration;")

    class DistanceWithVariableRestGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$DistanceWithVariableRestGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Length;Ljava/time/Duration;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getDuration = JavaMethod("()Ljava/time/Duration;")
        getDistance = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")

    class DistanceGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$DistanceGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Length;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getDistance = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")

    class ActiveCaloriesBurnedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal$ActiveCaloriesBurnedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Energy;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getActiveCalories = JavaMethod("()Landroid/health/connect/datatypes/units/Energy;")