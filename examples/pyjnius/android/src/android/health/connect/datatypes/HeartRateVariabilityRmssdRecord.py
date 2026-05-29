from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeartRateVariabilityRmssdRecord"]

class HeartRateVariabilityRmssdRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/HeartRateVariabilityRmssdRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getHeartRateVariabilityMillis = JavaMethod("()D")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeartRateVariabilityRmssdRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;D)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/HeartRateVariabilityRmssdRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeartRateVariabilityRmssdRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeartRateVariabilityRmssdRecord$Builder;")