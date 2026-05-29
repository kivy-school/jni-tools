from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SensorAdditionalInfo"]

class SensorAdditionalInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/SensorAdditionalInfo"
    TYPE_FRAME_BEGIN = JavaStaticField("I")
    TYPE_FRAME_END = JavaStaticField("I")
    TYPE_INTERNAL_TEMPERATURE = JavaStaticField("I")
    TYPE_SAMPLING = JavaStaticField("I")
    TYPE_SENSOR_PLACEMENT = JavaStaticField("I")
    TYPE_UNTRACKED_DELAY = JavaStaticField("I")
    TYPE_VEC3_CALIBRATION = JavaStaticField("I")
    floatValues = JavaField("[F")
    intValues = JavaField("[I")
    sensor = JavaField("Landroid/hardware/Sensor;")
    serial = JavaField("I")
    type = JavaField("I")