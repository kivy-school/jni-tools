from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BloodPressureRecord"]

class BloodPressureRecord(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BloodPressureRecord"
    DIASTOLIC_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    DIASTOLIC_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    DIASTOLIC_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SYSTOLIC_AVG = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SYSTOLIC_MAX = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    SYSTOLIC_MIN = JavaStaticField("Landroid/health/connect/datatypes/AggregationType;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getMeasurementLocation = JavaMethod("()I")
    getDiastolic = JavaMethod("()Landroid/health/connect/datatypes/units/Pressure;")
    getBodyPosition = JavaMethod("()I")
    getSystolic = JavaMethod("()Landroid/health/connect/datatypes/units/Pressure;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodPressureRecord$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/datatypes/Metadata;Ljava/time/Instant;ILandroid/health/connect/datatypes/units/Pressure;Landroid/health/connect/datatypes/units/Pressure;I)V", False)]
        build = JavaMethod("()Landroid/health/connect/datatypes/BloodPressureRecord;")
        clearZoneOffset = JavaMethod("()Landroid/health/connect/datatypes/BloodPressureRecord$Builder;")
        setZoneOffset = JavaMethod("(Ljava/time/ZoneOffset;)Landroid/health/connect/datatypes/BloodPressureRecord$Builder;")

    class BodyPosition(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodPressureRecord$BodyPosition"
        BODY_POSITION_LYING_DOWN = JavaStaticField("I")
        BODY_POSITION_RECLINING = JavaStaticField("I")
        BODY_POSITION_SITTING_DOWN = JavaStaticField("I")
        BODY_POSITION_STANDING_UP = JavaStaticField("I")
        BODY_POSITION_UNKNOWN = JavaStaticField("I")

    class BloodPressureMeasurementLocation(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/BloodPressureRecord$BloodPressureMeasurementLocation"
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_LEFT_UPPER_ARM = JavaStaticField("I")
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_LEFT_WRIST = JavaStaticField("I")
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_RIGHT_UPPER_ARM = JavaStaticField("I")
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_RIGHT_WRIST = JavaStaticField("I")
        BLOOD_PRESSURE_MEASUREMENT_LOCATION_UNKNOWN = JavaStaticField("I")