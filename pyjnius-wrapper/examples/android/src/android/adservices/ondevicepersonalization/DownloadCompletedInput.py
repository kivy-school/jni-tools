from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadCompletedInput"]

class DownloadCompletedInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedInput"
    getDownloadedContents = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")