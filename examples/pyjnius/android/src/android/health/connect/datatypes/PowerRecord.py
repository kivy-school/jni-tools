from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PowerRecord"]

class PowerRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/PowerRecord"
    POWER_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    POWER_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    POWER_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getSamples = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PowerRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PowerRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/PowerRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PowerRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/PowerRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/PowerRecord;")

    class PowerRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/PowerRecord/PowerRecordSample"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Power;Ljava/time/Instant;)V", False)]
        getPower = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")