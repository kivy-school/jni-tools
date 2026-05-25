from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpeedRecord"]

class SpeedRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/SpeedRecord"
    SPEED_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SPEED_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SPEED_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getSamples = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SpeedRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord;")

    class SpeedRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SpeedRecord/SpeedRecordSample"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Velocity;Ljava/time/Instant;)V", False)]
        getSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")