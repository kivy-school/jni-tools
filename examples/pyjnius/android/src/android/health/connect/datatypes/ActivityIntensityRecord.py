from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ActivityIntensityRecord"]

class ActivityIntensityRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/ActivityIntensityRecord"
    ACTIVITY_INTENSITY_TYPE_MODERATE = JavaStaticField("I")
    ACTIVITY_INTENSITY_TYPE_VIGOROUS = JavaStaticField("I")
    DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    INTENSITY_MINUTES_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    MODERATE_DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    VIGOROUS_DURATION_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getActivityIntensityType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/ActivityIntensityRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;I)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/ActivityIntensityRecord;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/ActivityIntensityRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/ActivityIntensityRecord$Builder;")