from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TelephonyScanManager"]

class TelephonyScanManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/TelephonyScanManager"
    __javaconstructor__ = [("()V", False)]

    class NetworkScanCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/TelephonyScanManager$NetworkScanCallback"
        __javaconstructor__ = [("()V", False)]
        onError = JavaMethod("(I)V")
        onComplete = JavaMethod("()V")
        onResults = JavaMethod("(Ljava/util/List;)V")