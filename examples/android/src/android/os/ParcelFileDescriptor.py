from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ParcelFileDescriptor"]

class ParcelFileDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/ParcelFileDescriptor"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MODE_APPEND = JavaStaticField("I")
    MODE_CREATE = JavaStaticField("I")
    MODE_READ_ONLY = JavaStaticField("I")
    MODE_READ_WRITE = JavaStaticField("I")
    MODE_TRUNCATE = JavaStaticField("I")
    MODE_WORLD_READABLE = JavaStaticField("I")
    MODE_WORLD_WRITEABLE = JavaStaticField("I")
    MODE_WRITE_ONLY = JavaStaticField("I")
    open = JavaMultipleMethod([("(Ljava/io/File;I)Landroid/os/ParcelFileDescriptor;", True, False), ("(Ljava/io/File;ILandroid/os/Handler;Landroid/os/ParcelFileDescriptor$OnCloseListener;)Landroid/os/ParcelFileDescriptor;", True, False)])
    wrap = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;Landroid/os/Handler;Landroid/os/ParcelFileDescriptor$OnCloseListener;)Landroid/os/ParcelFileDescriptor;")
    dup = JavaMultipleMethod([("(Ljava/io/FileDescriptor;)Landroid/os/ParcelFileDescriptor;", True, False), ("()Landroid/os/ParcelFileDescriptor;", False, False)])
    fromFd = JavaStaticMethod("(I)Landroid/os/ParcelFileDescriptor;")
    adoptFd = JavaStaticMethod("(I)Landroid/os/ParcelFileDescriptor;")
    fromSocket = JavaStaticMethod("(Ljava/net/Socket;)Landroid/os/ParcelFileDescriptor;")
    fromDatagramSocket = JavaStaticMethod("(Ljava/net/DatagramSocket;)Landroid/os/ParcelFileDescriptor;")
    createPipe = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    createReliablePipe = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    createSocketPair = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    createReliableSocketPair = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    parseMode = JavaStaticMethod("(Ljava/lang/String;)I")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getStatSize = JavaMethod("()J")
    getFd = JavaMethod("()I")
    detachFd = JavaMethod("()I")
    close = JavaMethod("()V")
    closeWithError = JavaMethod("(Ljava/lang/String;)V")
    canDetectErrors = JavaMethod("()Z")
    checkError = JavaMethod("()V")
    toString = JavaMethod("()Ljava/lang/String;")
    finalize = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class AutoCloseInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor/AutoCloseInputStream"
        __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False)]
        close = JavaMethod("()V")
        read = JavaMultipleMethod([("()I", False, False), ("([B)I", False, False), ("([BII)I", False, False)])

    class AutoCloseOutputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor/AutoCloseOutputStream"
        __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False)]
        close = JavaMethod("()V")

    class FileDescriptorDetachedException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor/FileDescriptorDetachedException"
        __javaconstructor__ = [("()V", False)]

    class OnCloseListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor/OnCloseListener"
        onClose = JavaMethod("(Ljava/io/IOException;)V")