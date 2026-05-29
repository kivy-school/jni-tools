from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AdBuffer"]

class AdBuffer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/AdBuffer"
    __javaconstructor__ = [("(ILjava/lang/String;Landroid/os/SharedMemory;IIJI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPresentationTimeUs = JavaMethod("()J")
    getSharedMemory = JavaMethod("()Landroid/os/SharedMemory;")
    getLength = JavaMethod("()I")
    getId = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    getOffset = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getMimeType = JavaMethod("()Ljava/lang/String;")