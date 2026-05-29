from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StepsCadenceRecord"]

class StepsCadenceRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord"
    STEPS_CADENCE_RATE_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    STEPS_CADENCE_RATE_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    STEPS_CADENCE_RATE_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSamples = JavaMethod("()Ljava/util/List;")

    class StepsCadenceRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord$StepsCadenceRecordSample"
        __javaconstructor__ = [("(DLjava/time/Instant;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getRate = JavaMethod("()D")
        getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")