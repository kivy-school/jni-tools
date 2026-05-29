from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalServerSocket"]

class LocalServerSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LocalServerSocket"
    __javaconstructor__ = [("(Ljava/io/FileDescriptor;)V", False), ("(Ljava/lang/String;)V", False)]
    close = JavaMethod("()V")
    accept = JavaMethod("()Landroid/net/LocalSocket;")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getLocalSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")