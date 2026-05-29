from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OxygenSaturationRecord"]

class OxygenSaturationRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/OxygenSaturationRecord"
    getPercentage = JavaMethod("()Landroid/health/connect/datatypes/units/Percentage;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/OxygenSaturationRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Landroid/health/connect/datatypes/units/Percentage;)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/OxygenSaturationRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/OxygenSaturationRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/OxygenSaturationRecord;")