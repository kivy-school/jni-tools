from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IkeSessionCallback"]

class IkeSessionCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/IkeSessionCallback"
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/IkeSessionConfiguration;)V")
    onClosed = JavaMethod("()V")
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onError = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")