from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalServerSocket"]

class LocalServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LocalServerSocket"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Ljava/io/FileDescriptor;)V", False)]
    getLocalSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")
    accept = JavaMethod("()Landroid/net/LocalSocket;")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    close = JavaMethod("()V")