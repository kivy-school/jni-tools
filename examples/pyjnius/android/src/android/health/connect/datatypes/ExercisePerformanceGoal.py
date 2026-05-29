from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExercisePerformanceGoal"]

class ExercisePerformanceGoal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal"

    class WeightGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$WeightGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Mass;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMass = JavaMethod("()Landroid/health/connect/datatypes/units/Mass;")

    class UnknownGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$UnknownGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExercisePerformanceGoal$UnknownGoal;")

    class SpeedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$SpeedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Velocity;Landroid/health/connect/datatypes/units/Velocity;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMinSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")
        getMaxSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")

    class RateOfPerceivedExertionGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$RateOfPerceivedExertionGoal"
        __javaconstructor__ = [("(I)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getRpe = JavaMethod("()I")

    class PowerGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$PowerGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Power;Landroid/health/connect/datatypes/units/Power;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMinPower = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")
        getMaxPower = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")

    class HeartRateGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$HeartRateGoal"
        __javaconstructor__ = [("(II)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMaxBpm = JavaMethod("()I")
        getMinBpm = JavaMethod("()I")

    class CadenceGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$CadenceGoal"
        __javaconstructor__ = [("(DD)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getMaxRpm = JavaMethod("()D")
        getMinRpm = JavaMethod("()D")

    class AmrapGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal$AmrapGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExercisePerformanceGoal$AmrapGoal;")