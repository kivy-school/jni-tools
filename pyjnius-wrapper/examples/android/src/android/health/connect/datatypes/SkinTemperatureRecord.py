from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SkinTemperatureRecord"]

class SkinTemperatureRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/SkinTemperatureRecord"
    MEASUREMENT_LOCATION_FINGER = JavaStaticField("I")
    MEASUREMENT_LOCATION_TOE = JavaStaticField("I")
    MEASUREMENT_LOCATION_UNKNOWN = JavaStaticField("I")
    MEASUREMENT_LOCATION_WRIST = JavaStaticField("I")
    SKIN_TEMPERATURE_DELTA_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SKIN_TEMPERATURE_DELTA_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SKIN_TEMPERATURE_DELTA_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    getBaseline = JavaMethod("()Landroid/health/connect/datatypes/units/Temperature;")
    getDeltas = JavaMethod("()Ljava/util/List;")
    getMeasurementLocation = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SkinTemperatureRecord/Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;)V", False)]
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setBaseline = JavaMethod("(Landroid/health/connect/datatypes/units/Temperature;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setDeltas = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setMeasurementLocation = JavaMethod("(I)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord;")

    class Delta(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SkinTemperatureRecord/Delta"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/TemperatureDelta;Ljava/time/Instant;)V", False)]
        getDelta = JavaMethod("()Landroid/health/connect/datatypes/units/TemperatureDelta;")
        getTime = JavaMethod("()Ljava/time/Instant;")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")