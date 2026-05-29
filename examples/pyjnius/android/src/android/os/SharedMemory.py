from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedMemory"]

class SharedMemory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/SharedMemory"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    fromFileDescriptor = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;)Landroid/os/SharedMemory;")
    mapReadOnly = JavaMethod("()Ljava/nio/ByteBuffer;")
    mapReadWrite = JavaMethod("()Ljava/nio/ByteBuffer;")
    setProtect = JavaMethod("(I)Z")
    unmap = JavaStaticMethod("(Ljava/nio/ByteBuffer;)V")
    map = JavaMethod("(III)Ljava/nio/ByteBuffer;")
    close = JavaMethod("()V")
    getSize = JavaMethod("()I")
    create = JavaStaticMethod("(Ljava/lang/String;I)Landroid/os/SharedMemory;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")