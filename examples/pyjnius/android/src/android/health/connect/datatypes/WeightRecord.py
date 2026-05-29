from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WeightRecord"]

class WeightRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/WeightRecord"
    WEIGHT_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    WEIGHT_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    WEIGHT_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getWeight = JavaMethod("()Landroid/health/connect/datatypes/units/Mass;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/WeightRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Mass;)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/WeightRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/WeightRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/WeightRecord;")