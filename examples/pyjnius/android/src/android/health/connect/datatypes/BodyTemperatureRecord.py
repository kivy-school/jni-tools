from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BodyTemperatureRecord"]

class BodyTemperatureRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BodyTemperatureRecord"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMeasurementLocation = JavaMethod("()I")
    getTemperature = JavaMethod("()Landroid/health/connect/datatypes/units/Temperature;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BodyTemperatureRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;ILandroid/health/connect/datatypes/units/Temperature;)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/BodyTemperatureRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/BodyTemperatureRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/BodyTemperatureRecord$Builder;")