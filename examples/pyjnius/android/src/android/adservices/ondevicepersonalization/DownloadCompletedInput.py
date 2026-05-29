from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadCompletedInput"]

class DownloadCompletedInput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedInput"
    __javaconstructor__ = [("(Landroid/adservices/ondevicepersonalization/KeyValueStore;)V", False)]
    getDownloadedContents = JavaMethod("()Landroid/adservices/ondevicepersonalization/KeyValueStore;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")