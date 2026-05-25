from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSessionCallback"]

class ChildSessionCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionCallback"
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionConfiguration;)V")
    onClosed = JavaMethod("()V")
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onIpSecTransformCreated = JavaMethod("(Landroid/net/IpSecTransform;I)V")
    onIpSecTransformDeleted = JavaMethod("(Landroid/net/IpSecTransform;I)V")