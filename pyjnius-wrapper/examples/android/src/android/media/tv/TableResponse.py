from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TableResponse"]

class TableResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TableResponse"
    __javaconstructor__ = [("(IIILandroid/net/Uri;II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTableUri = JavaMethod("()Landroid/net/Uri;")
    getTableByteArray = JavaMethod("()[B")
    getTableSharedMemory = JavaMethod("()Landroid/os/SharedMemory;")
    getVersion = JavaMethod("()I")
    getSize = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/TableResponse/Builder"
        __javaconstructor__ = [("(IIIII)V", False)]
        setTableUri = JavaMethod("(Landroid/net/Uri;)Landroid/media/tv/TableResponse$Builder;")
        setTableByteArray = JavaMethod("([B)Landroid/media/tv/TableResponse$Builder;")
        setTableSharedMemory = JavaMethod("(Landroid/os/SharedMemory;)Landroid/media/tv/TableResponse$Builder;")
        build = JavaMethod("()Landroid/media/tv/TableResponse;")