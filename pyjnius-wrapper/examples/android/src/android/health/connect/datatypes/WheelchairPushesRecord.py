from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WheelchairPushesRecord"]

class WheelchairPushesRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/WheelchairPushesRecord"
    WHEEL_CHAIR_PUSHES_COUNT_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getCount = JavaMethod("()J")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/WheelchairPushesRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;J)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord;")