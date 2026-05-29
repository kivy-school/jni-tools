from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StructMsghdr"]

class StructMsghdr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/system/StructMsghdr"
    __javaconstructor__ = [("(Ljava/net/SocketAddress;[Ljava/nio/ByteBuffer;[Landroid/system/StructCmsghdr;I)V", False)]
    msg_control = JavaField("[Landroid/system/StructCmsghdr;")
    msg_flags = JavaField("I")
    msg_iov = JavaField("[Ljava/nio/ByteBuffer;")
    msg_name = JavaField("Ljava/net/SocketAddress;")