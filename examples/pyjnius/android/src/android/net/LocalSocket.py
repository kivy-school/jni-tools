from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalSocket"]

class LocalSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LocalSocket"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    SOCKET_DGRAM = JavaStaticField("I")
    SOCKET_SEQPACKET = JavaStaticField("I")
    SOCKET_STREAM = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    connect = JavaMultipleMethod([("(Landroid/net/LocalSocketAddress;)V", False, False), ("(Landroid/net/LocalSocketAddress;I)V", False, False)])
    bind = JavaMethod("(Landroid/net/LocalSocketAddress;)V")
    getLocalSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    close = JavaMethod("()V")
    shutdownInput = JavaMethod("()V")
    shutdownOutput = JavaMethod("()V")
    setReceiveBufferSize = JavaMethod("(I)V")
    getReceiveBufferSize = JavaMethod("()I")
    setSoTimeout = JavaMethod("(I)V")
    getSoTimeout = JavaMethod("()I")
    setSendBufferSize = JavaMethod("(I)V")
    getSendBufferSize = JavaMethod("()I")
    getRemoteSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")
    isConnected = JavaMethod("()Z")
    isClosed = JavaMethod("()Z")
    isBound = JavaMethod("()Z")
    isOutputShutdown = JavaMethod("()Z")
    isInputShutdown = JavaMethod("()Z")
    setFileDescriptorsForSend = JavaMethod("([Ljava/io/FileDescriptor;)V")
    getAncillaryFileDescriptors = JavaMethod("()[Ljava/io/FileDescriptor;")
    getPeerCredentials = JavaMethod("()Landroid/net/Credentials;")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")