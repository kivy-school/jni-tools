from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssetFileDescriptor"]

class AssetFileDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/AssetFileDescriptor"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;JJ)V", False), ("(Landroid/os/ParcelFileDescriptor;JJLandroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNKNOWN_LENGTH = JavaStaticField("J")
    getParcelFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")
    getStartOffset = JavaMethod("()J")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    getLength = JavaMethod("()J")
    getDeclaredLength = JavaMethod("()J")
    close = JavaMethod("()V")
    createInputStream = JavaMethod("()Ljava/io/FileInputStream;")
    createOutputStream = JavaMethod("()Ljava/io/FileOutputStream;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class AutoCloseInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetFileDescriptor/AutoCloseInputStream"
        __javaconstructor__ = [("(Landroid/content/res/AssetFileDescriptor;)V", False)]
        available = JavaMethod("()I")
        read = JavaMultipleMethod([("()I", False, False), ("([BII)I", False, False), ("([B)I", False, False)])
        skip = JavaMethod("(J)J")
        mark = JavaMethod("(I)V")
        markSupported = JavaMethod("()Z")
        reset = JavaMethod("()V")
        getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")
        close = JavaMethod("()V")

    class AutoCloseOutputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetFileDescriptor/AutoCloseOutputStream"
        __javaconstructor__ = [("(Landroid/content/res/AssetFileDescriptor;)V", False)]
        write = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False), ("(I)V", False, False)])