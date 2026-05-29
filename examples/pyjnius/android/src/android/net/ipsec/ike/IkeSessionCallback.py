from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionCallback"]

class IkeSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionCallback"
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onError = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onClosed = JavaMethod("()V")
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/IkeSessionConfiguration;)V")