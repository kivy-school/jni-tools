from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocalSocket"]

class LocalSocket(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/LocalSocket"
    __javaconstructor__ = [("()V", False), ("(I)V", False)]
    SOCKET_DGRAM = JavaStaticField("I")
    SOCKET_SEQPACKET = JavaStaticField("I")
    SOCKET_STREAM = JavaStaticField("I")
    connect = JavaMultipleMethod([("(Landroid/net/LocalSocketAddress;I)V", False, False), ("(Landroid/net/LocalSocketAddress;)V", False, False)])
    isConnected = JavaMethod("()Z")
    getAncillaryFileDescriptors = JavaMethod("()[Ljava/io/FileDescriptor;")
    getPeerCredentials = JavaMethod("()Landroid/net/Credentials;")
    setFileDescriptorsForSend = JavaMethod("([Ljava/io/FileDescriptor;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    close = JavaMethod("()V")
    getInputStream = JavaMethod("()Ljava/io/InputStream;")
    isBound = JavaMethod("()Z")
    isClosed = JavaMethod("()Z")
    getOutputStream = JavaMethod("()Ljava/io/OutputStream;")
    bind = JavaMethod("(Landroid/net/LocalSocketAddress;)V")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getRemoteSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")
    getLocalSocketAddress = JavaMethod("()Landroid/net/LocalSocketAddress;")
    setSoTimeout = JavaMethod("(I)V")
    getSoTimeout = JavaMethod("()I")
    setSendBufferSize = JavaMethod("(I)V")
    getSendBufferSize = JavaMethod("()I")
    setReceiveBufferSize = JavaMethod("(I)V")
    getReceiveBufferSize = JavaMethod("()I")
    isInputShutdown = JavaMethod("()Z")
    isOutputShutdown = JavaMethod("()Z")
    shutdownInput = JavaMethod("()V")
    shutdownOutput = JavaMethod("()V")