from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ExercisePerformanceGoal"]

class ExercisePerformanceGoal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal"

    class AmrapGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/AmrapGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExercisePerformanceGoal$AmrapGoal;")

    class CadenceGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/CadenceGoal"
        __javaconstructor__ = [("(DD)V", False)]
        getMinRpm = JavaMethod("()D")
        getMaxRpm = JavaMethod("()D")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class HeartRateGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/HeartRateGoal"
        __javaconstructor__ = [("(II)V", False)]
        getMinBpm = JavaMethod("()I")
        getMaxBpm = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class PowerGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/PowerGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Power;Landroid/health/connect/datatypes/units/Power;)V", False)]
        getMinPower = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")
        getMaxPower = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class RateOfPerceivedExertionGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/RateOfPerceivedExertionGoal"
        __javaconstructor__ = [("(I)V", False)]
        getRpe = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class SpeedGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/SpeedGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Velocity;Landroid/health/connect/datatypes/units/Velocity;)V", False)]
        getMinSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")
        getMaxSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")

    class UnknownGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/UnknownGoal"
        INSTANCE = JavaStaticField("Landroid/health/connect/datatypes/ExercisePerformanceGoal$UnknownGoal;")

    class WeightGoal(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ExercisePerformanceGoal/WeightGoal"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Mass;)V", False)]
        getMass = JavaMethod("()Landroid/health/connect/datatypes/units/Mass;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")