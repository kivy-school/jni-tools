from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CyclingPedalingCadenceRecord"]

class CyclingPedalingCadenceRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord"
    RPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    RPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    RPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSamples = JavaMethod("()Ljava/util/List;")

    class CyclingPedalingCadenceRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord$CyclingPedalingCadenceRecordSample"
        __javaconstructor__ = [("(DLjava/time/Instant;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getRevolutionsPerMinute = JavaMethod("()D")
        getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")