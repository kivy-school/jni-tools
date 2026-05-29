from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpDeviceInfo"]

class MtpDeviceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpDeviceInfo"
    getManufacturer = JavaMethod("()Ljava/lang/String;")
    getModel = JavaMethod("()Ljava/lang/String;")
    getVersion = JavaMethod("()Ljava/lang/String;")
    getSerialNumber = JavaMethod("()Ljava/lang/String;")
    getOperationsSupported = JavaMethod("()[I")
    getEventsSupported = JavaMethod("()[I")
    isOperationSupported = JavaMethod("(I)Z")
    isEventSupported = JavaMethod("(I)Z")