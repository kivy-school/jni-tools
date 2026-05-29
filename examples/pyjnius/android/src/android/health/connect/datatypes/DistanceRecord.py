from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DistanceRecord"]

class DistanceRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/DistanceRecord"
    DISTANCE_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getDistance = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/DistanceRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Length;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/DistanceRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/DistanceRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/DistanceRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/DistanceRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/DistanceRecord$Builder;")