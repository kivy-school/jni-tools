from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloorsClimbedRecord"]

class FloorsClimbedRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/FloorsClimbedRecord"
    FLOORS_CLIMBED_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getFloors = JavaMethod("()D")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/FloorsClimbedRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;D)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/FloorsClimbedRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/FloorsClimbedRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/FloorsClimbedRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/FloorsClimbedRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/FloorsClimbedRecord$Builder;")