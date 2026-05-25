from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StepsCadenceRecord"]

class StepsCadenceRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord"
    STEPS_CADENCE_RATE_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    STEPS_CADENCE_RATE_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    STEPS_CADENCE_RATE_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getSamples = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/StepsCadenceRecord;")

    class StepsCadenceRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/StepsCadenceRecord/StepsCadenceRecordSample"
        __javaconstructor__ = [("(DLjava/time/Instant;)V", False)]
        getRate = JavaMethod("()D")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")