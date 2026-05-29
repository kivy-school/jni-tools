from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MtpStorageInfo"]

class MtpStorageInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/mtp/MtpStorageInfo"
    getStorageId = JavaMethod("()I")
    getMaxCapacity = JavaMethod("()J")
    getVolumeIdentifier = JavaMethod("()Ljava/lang/String;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getFreeSpace = JavaMethod("()J")