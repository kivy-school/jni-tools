from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HardwarePropertiesManager"]

class HardwarePropertiesManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/HardwarePropertiesManager"
    DEVICE_TEMPERATURE_BATTERY = JavaStaticField("I")
    DEVICE_TEMPERATURE_CPU = JavaStaticField("I")
    DEVICE_TEMPERATURE_GPU = JavaStaticField("I")
    DEVICE_TEMPERATURE_SKIN = JavaStaticField("I")
    TEMPERATURE_CURRENT = JavaStaticField("I")
    TEMPERATURE_SHUTDOWN = JavaStaticField("I")
    TEMPERATURE_THROTTLING = JavaStaticField("I")
    TEMPERATURE_THROTTLING_BELOW_VR_MIN = JavaStaticField("I")
    UNDEFINED_TEMPERATURE = JavaStaticField("F")
    getDeviceTemperatures = JavaMethod("(II)[F")
    getCpuUsages = JavaMethod("()[Landroid/os/CpuUsageInfo;")
    getFanSpeeds = JavaMethod("()[F")