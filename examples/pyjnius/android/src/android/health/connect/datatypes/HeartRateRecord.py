from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeartRateRecord"]

class HeartRateRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/HeartRateRecord"
    BPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    HEART_MEASUREMENTS_COUNT = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSamples = JavaMethod("()Ljava/util/List;")

    class HeartRateSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeartRateRecord$HeartRateSample"
        __javaconstructor__ = [("(JLjava/time/Instant;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getBeatsPerMinute = JavaMethod("()J")
        getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeartRateRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeartRateRecord$Builder;")