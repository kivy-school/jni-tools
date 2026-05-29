from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpeedRecord"]

class SpeedRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/SpeedRecord"
    SPEED_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SPEED_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SPEED_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSamples = JavaMethod("()Ljava/util/List;")

    class SpeedRecordSample(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SpeedRecord$SpeedRecordSample"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/Velocity;Ljava/time/Instant;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getSpeed = JavaMethod("()Landroid/health/connect/datatypes/units/Velocity;")
        getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SpeedRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;Ljava/util/List;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SpeedRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SpeedRecord$Builder;")