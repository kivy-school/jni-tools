from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChildSessionCallback"]

class ChildSessionCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ipsec/ike/ChildSessionCallback"
    onIpSecTransformCreated = JavaMethod("(Landroid/net/IpSecTransform;I)V")
    onClosedWithException = JavaMethod("(Landroid/net/ipsec/ike/exceptions/IkeException;)V")
    onIpSecTransformDeleted = JavaMethod("(Landroid/net/IpSecTransform;I)V")
    onClosed = JavaMethod("()V")
    onOpened = JavaMethod("(Landroid/net/ipsec/ike/ChildSessionConfiguration;)V")