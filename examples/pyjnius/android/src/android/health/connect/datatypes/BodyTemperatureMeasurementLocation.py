from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BodyTemperatureMeasurementLocation"]

class BodyTemperatureMeasurementLocation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/BodyTemperatureMeasurementLocation"
    MEASUREMENT_LOCATION_ARMPIT = JavaStaticField("I")
    MEASUREMENT_LOCATION_EAR = JavaStaticField("I")
    MEASUREMENT_LOCATION_FINGER = JavaStaticField("I")
    MEASUREMENT_LOCATION_FOREHEAD = JavaStaticField("I")
    MEASUREMENT_LOCATION_MOUTH = JavaStaticField("I")
    MEASUREMENT_LOCATION_RECTUM = JavaStaticField("I")
    MEASUREMENT_LOCATION_TEMPORAL_ARTERY = JavaStaticField("I")
    MEASUREMENT_LOCATION_TOE = JavaStaticField("I")
    MEASUREMENT_LOCATION_UNKNOWN = JavaStaticField("I")
    MEASUREMENT_LOCATION_VAGINA = JavaStaticField("I")
    MEASUREMENT_LOCATION_WRIST = JavaStaticField("I")