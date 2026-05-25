from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeartRateRecord"]

class HeartRateRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/HeartRateRecord"
    BPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    HEART_MEASUREMENTS_COUNT = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getSamples = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeartRateRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/HeartRateRecord;")

    class HeartRateSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeartRateRecord/HeartRateSample"
        __javaconstructor__ = [("(JLjava/time/Instant;)V", False)]
        getBeatsPerMinute = JavaMethod("()J")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")