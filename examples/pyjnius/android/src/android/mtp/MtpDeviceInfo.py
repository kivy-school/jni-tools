from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpDeviceInfo"]

class MtpDeviceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpDeviceInfo"
    getEventsSupported = JavaMethod("()[I")
    getOperationsSupported = JavaMethod("()[I")
    isEventSupported = JavaMethod("(I)Z")
    isOperationSupported = JavaMethod("(I)Z")
    getManufacturer = JavaMethod("()Ljava/lang/String;")
    getModel = JavaMethod("()Ljava/lang/String;")
    getSerialNumber = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()Ljava/lang/String;")