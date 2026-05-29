from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpStorageInfo"]

class MtpStorageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpStorageInfo"
    getStorageId = JavaMethod("()I")
    getMaxCapacity = JavaMethod("()J")
    getFreeSpace = JavaMethod("()J")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getVolumeIdentifier = JavaMethod("()Ljava/lang/String;")