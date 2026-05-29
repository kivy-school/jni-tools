from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BodyTemperatureRecord"]

class BodyTemperatureRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BodyTemperatureRecord"
    getMeasurementLocation = JavaMethod("()I")
    getTemperature = JavaMethod("()Landroid/health/connect/datatypes/units/Temperature;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BodyTemperatureRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;ILandroid/health/connect/datatypes/units/Temperature;)V", False)]
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/BodyTemperatureRecord$Builder;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/BodyTemperatureRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/BodyTemperatureRecord;")