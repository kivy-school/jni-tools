from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadCompletedOutput"]

class DownloadCompletedOutput(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedOutput"
    getRetainedKeys = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/ondevicepersonalization/DownloadCompletedOutput/Builder"
        __javaconstructor__ = [("()V", False)]
        setRetainedKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput$Builder;")
        addRetainedKey = JavaMethod("(Ljava/lang/String;)Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput$Builder;")
        build = JavaMethod("()Landroid/adservices/ondevicepersonalization/DownloadCompletedOutput;")