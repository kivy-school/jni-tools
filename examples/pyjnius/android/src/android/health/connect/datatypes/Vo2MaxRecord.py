from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Vo2MaxRecord"]

class Vo2MaxRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/Vo2MaxRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMeasurementMethod = JavaMethod("()I")
    getVo2MillilitersPerMinuteKilogram = JavaMethod("()D")

    class Vo2MaxMeasurementMethod(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/Vo2MaxRecord$Vo2MaxMeasurementMethod"
        MEASUREMENT_METHOD_COOPER_TEST = JavaStaticField("I")
        MEASUREMENT_METHOD_HEART_RATE_RATIO = JavaStaticField("I")
        MEASUREMENT_METHOD_METABOLIC_CART = JavaStaticField("I")
        MEASUREMENT_METHOD_MULTISTAGE_FITNESS_TEST = JavaStaticField("I")
        MEASUREMENT_METHOD_OTHER = JavaStaticField("I")
        MEASUREMENT_METHOD_ROCKPORT_FITNESS_TEST = JavaStaticField("I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/Vo2MaxRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;ID)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/Vo2MaxRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/Vo2MaxRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/Vo2MaxRecord$Builder;")