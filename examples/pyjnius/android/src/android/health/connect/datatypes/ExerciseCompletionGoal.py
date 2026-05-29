from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExerciseCompletionGoal"]

class ExerciseCompletionGoal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal"

    class ActiveCaloriesBurnedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/ActiveCaloriesBurnedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Energy;)V", False)]
        getActiveCalories = JavaMethod("()Landroid/health/connect/datatypes/units/Energy;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class DistanceGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/DistanceGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Length;)V", False)]
        getDistance = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class DistanceWithVariableRestGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/DistanceWithVariableRestGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Length;Ljava/time/Duration;)V", False)]
        getDistance = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")
        getDuration = JavaMethod("()Ljava/time/Duration;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class DurationGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/DurationGoal"
        __javaconstructor__ = [("(Ljava/time/Duration;)V", False)]
        getDuration = JavaMethod("()Ljava/time/Duration;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class RepetitionsGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/RepetitionsGoal"
        __javaconstructor__ = [("(I)V", False)]
        getRepetitions = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class StepsGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/StepsGoal"
        __javaconstructor__ = [("(I)V", False)]
        getSteps = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class TotalCaloriesBurnedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/TotalCaloriesBurnedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Energy;)V", False)]
        getTotalCalories = JavaMethod("()Landroid/health/connect/datatypes/units/Energy;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class UnknownGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/UnknownGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExerciseCompletionGoal$UnknownGoal;")

    class UnspecifiedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExerciseCompletionGoal/UnspecifiedGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExerciseCompletionGoal$UnspecifiedGoal;")