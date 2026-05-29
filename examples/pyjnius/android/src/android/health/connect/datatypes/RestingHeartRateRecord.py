from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RestingHeartRateRecord"]

class RestingHeartRateRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/RestingHeartRateRecord"
    BPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getBeatsPerMinute = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/RestingHeartRateRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;J)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/RestingHeartRateRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/RestingHeartRateRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/RestingHeartRateRecord$Builder;")