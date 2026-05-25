from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RestingHeartRateRecord"]

class RestingHeartRateRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/RestingHeartRateRecord"
    BPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    BPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getBeatsPerMinute = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/RestingHeartRateRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;J)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/RestingHeartRateRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/RestingHeartRateRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/RestingHeartRateRecord;")