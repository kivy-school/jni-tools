from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsDownloadReceiver"]

class MbmsDownloadReceiver(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/MbmsDownloadReceiver"
    __javaconstructor__ = [("()V", False)]
    onReceive = JavaMethod("(Landroid/content/Context;Landroid/content/Intent;)V")