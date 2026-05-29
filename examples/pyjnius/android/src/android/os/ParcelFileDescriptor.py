from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    wrap = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;Landroid/os/Handler;Landroid/os/ParcelFileDescriptor$OnCloseListener;)Landroid/os/ParcelFileDescriptor;")
    close = JavaMethod("()V")
    open = JavaMultipleMethod([("(Ljava/io/File;ILandroid/os/Handler;Landroid/os/ParcelFileDescriptor$OnCloseListener;)Landroid/os/ParcelFileDescriptor;", True, False), ("(Ljava/io/File;I)Landroid/os/ParcelFileDescriptor;", True, False)])
    checkError = JavaMethod("()V")
    dup = JavaMultipleMethod([("()Landroid/os/ParcelFileDescriptor;", False, False), ("(Ljava/io/FileDescriptor;)Landroid/os/ParcelFileDescriptor;", True, False)])
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    closeWithError = JavaMethod("(Ljava/lang/String;)V")
    adoptFd = JavaStaticMethod("(I)Landroid/os/ParcelFileDescriptor;")
    createReliablePipe = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    canDetectErrors = JavaMethod("()Z")
    createPipe = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    detachFd = JavaMethod("()I")
    createSocketPair = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")
    fromDatagramSocket = JavaStaticMethod("(Ljava/net/DatagramSocket;)Landroid/os/ParcelFileDescriptor;")
    parseMode = JavaStaticMethod("(Ljava/lang/String;)I")
    fromFd = JavaStaticMethod("(I)Landroid/os/ParcelFileDescriptor;")
    fromSocket = JavaStaticMethod("(Ljava/net/Socket;)Landroid/os/ParcelFileDescriptor;")
    getStatSize = JavaMethod("()J")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getFd = JavaMethod("()I")
    createReliableSocketPair = JavaStaticMethod("()[Landroid/os/ParcelFileDescriptor;")

    class OnCloseListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor$OnCloseListener"
        onClose = JavaMethod("(Ljava/io/IOException;)V")

    class FileDescriptorDetachedException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor$FileDescriptorDetachedException"
        __javaconstructor__ = [("()V", False)]

    class AutoCloseOutputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor$AutoCloseOutputStream"
        __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False)]
        close = JavaMethod("()V")

    class AutoCloseInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/ParcelFileDescriptor$AutoCloseInputStream"
        __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;)V", False)]
        close = JavaMethod("()V")
        read = JavaMultipleMethod([("([B)I", False, False), ("([BII)I", False, False), ("()I", False, False)])