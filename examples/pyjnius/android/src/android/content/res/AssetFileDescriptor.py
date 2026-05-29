from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AssetFileDescriptor"]

class AssetFileDescriptor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/res/AssetFileDescriptor"
    __javaconstructor__ = [("(Landroid/os/ParcelFileDescriptor;JJ)V", False), ("(Landroid/os/ParcelFileDescriptor;JJLandroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    UNKNOWN_LENGTH = JavaStaticField("J")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    getLength = JavaMethod("()J")
    close = JavaMethod("()V")
    getStartOffset = JavaMethod("()J")
    createInputStream = JavaMethod("()Ljava/io/FileInputStream;")
    createOutputStream = JavaMethod("()Ljava/io/FileOutputStream;")
    getDeclaredLength = JavaMethod("()J")
    getParcelFileDescriptor = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    getExtras = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFileDescriptor = JavaMethod("()Ljava/io/FileDescriptor;")

    class AutoCloseOutputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetFileDescriptor$AutoCloseOutputStream"
        __javaconstructor__ = [("(Landroid/content/res/AssetFileDescriptor;)V", False)]
        write = JavaMultipleMethod([("(I)V", False, False), ("([BII)V", False, False), ("([B)V", False, False)])

    class AutoCloseInputStream(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/res/AssetFileDescriptor$AutoCloseInputStream"
        __javaconstructor__ = [("(Landroid/content/res/AssetFileDescriptor;)V", False)]
        reset = JavaMethod("()V")
        close = JavaMethod("()V")
        mark = JavaMethod("(I)V")
        read = JavaMultipleMethod([("([B)I", False, False), ("()I", False, False), ("([BII)I", False, False)])
        skip = JavaMethod("(J)J")
        available = JavaMethod("()I")
        markSupported = JavaMethod("()Z")
        getChannel = JavaMethod("()Ljava/nio/channels/FileChannel;")