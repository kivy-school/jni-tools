from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WheelchairPushesRecord"]

class WheelchairPushesRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/WheelchairPushesRecord"
    WHEEL_CHAIR_PUSHES_COUNT_TOTAL = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getCount = JavaMethod("()J")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/WheelchairPushesRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;J)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/WheelchairPushesRecord$Builder;")