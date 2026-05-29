from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HeightRecord"]

class HeightRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/HeightRecord"
    HEIGHT_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    HEIGHT_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    HEIGHT_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getHeight = JavaMethod("()Landroid/health/connect/datatypes/units/Length;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/HeightRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Length;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/HeightRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/HeightRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/HeightRecord$Builder;")