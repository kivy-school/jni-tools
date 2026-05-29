from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CyclingPedalingCadenceRecord"]

class CyclingPedalingCadenceRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord"
    RPM_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    RPM_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    RPM_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getSamples = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/CyclingPedalingCadenceRecord;")

    class CyclingPedalingCadenceRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/CyclingPedalingCadenceRecord/CyclingPedalingCadenceRecordSample"
        __javaconstructor__ = [("(DLjava/time/Instant;)V", False)]
        getRevolutionsPerMinute = JavaMethod("()D")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")