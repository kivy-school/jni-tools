from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getBaseline = JavaMethod("()Landroid/health/connect/datatypes/units/Temperature;")
    getMeasurementLocation = JavaMethod("()I")
    getDeltas = JavaMethod("()Ljava/util/List;")

    class Delta(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SkinTemperatureRecord$Delta"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/units/TemperatureDelta;Ljava/time/Instant;)V", False)]
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        hashCode = JavaMethod("()I")
        getDelta = JavaMethod("()Landroid/health/connect/datatypes/units/TemperatureDelta;")
        getTime = JavaMethod("()Ljava/time/Instant;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/SkinTemperatureRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;Ljava/time/Instant;)V", False)]
        setDeltas = JavaMethod("(Ljava/util/List;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setMeasurementLocation = JavaMethod("(I)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setBaseline = JavaMethod("(Landroid/health/connect/datatypes/units/Temperature;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord;")
        clearEndZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        clearStartZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setEndZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")
        setStartZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/SkinTemperatureRecord$Builder;")