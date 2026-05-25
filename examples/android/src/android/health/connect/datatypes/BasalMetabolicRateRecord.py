from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BasalMetabolicRateRecord"]

class BasalMetabolicRateRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BasalMetabolicRateRecord"
    BASAL_CALORIES_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getBasalMetabolicRate = JavaMethod("()Landroid/health/connect/datatypes/units/Power;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BasalMetabolicRateRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Power;)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/BasalMetabolicRateRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/BasalMetabolicRateRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/BasalMetabolicRateRecord;")