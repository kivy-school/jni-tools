from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdBuffer"]

class AdBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AdBuffer"
    __javaconstructor__ = [("(ILjava/lang/String;Landroid/os/SharedMemory;IIJI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()I")
    getMimeType = JavaMethod("()Ljava/lang/String;")
    getSharedMemory = JavaMethod("()Landroid/os/SharedMemory;")
    getOffset = JavaMethod("()I")
    getLength = JavaMethod("()I")
    getPresentationTimeUs = JavaMethod("()J")
    getFlags = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")