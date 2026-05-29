from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AttachCallback"]

class AttachCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/AttachCallback"
    __javaconstructor__ = [("()V", False)]
    onAttached = JavaMethod("(Landroid/net/wifi/aware/WifiAwareSession;)V")
    onAttachFailed = JavaMethod("()V")
    onAwareSessionTerminated = JavaMethod("()V")