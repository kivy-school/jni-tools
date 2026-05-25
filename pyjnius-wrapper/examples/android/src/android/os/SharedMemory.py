from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SharedMemory"]

class SharedMemory(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/SharedMemory"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    create = JavaStaticMethod("(Ljava/lang/String;I)Landroid/os/SharedMemory;")
    fromFileDescriptor = JavaStaticMethod("(Landroid/os/ParcelFileDescriptor;)Landroid/os/SharedMemory;")
    setProtect = JavaMethod("(I)Z")
    getSize = JavaMethod("()I")
    mapReadWrite = JavaMethod("()Ljava/nio/ByteBuffer;")
    mapReadOnly = JavaMethod("()Ljava/nio/ByteBuffer;")
    map = JavaMethod("(III)Ljava/nio/ByteBuffer;")
    unmap = JavaStaticMethod("(Ljava/nio/ByteBuffer;)V")
    close = JavaMethod("()V")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")