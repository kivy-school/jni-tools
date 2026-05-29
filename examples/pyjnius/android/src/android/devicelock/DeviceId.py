from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeviceId"]

class DeviceId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/devicelock/DeviceId"
    DEVICE_ID_TYPE_IMEI = JavaStaticField("I")
    DEVICE_ID_TYPE_MEID = JavaStaticField("I")
    getId = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")