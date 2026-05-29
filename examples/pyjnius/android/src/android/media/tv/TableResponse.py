from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TableResponse"]

class TableResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TableResponse"
    __javaconstructor__ = [("(IIILandroid/net/Uri;II)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getTableByteArray = JavaMethod("()[B")
    getTableUri = JavaMethod("()Landroid/net/Uri;")
    getTableSharedMemory = JavaMethod("()Landroid/os/SharedMemory;")
    getSize = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getVersion = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/TableResponse$Builder"
        __javaconstructor__ = [("(IIIII)V", False)]
        setTableUri = JavaMethod("(Landroid/net/Uri;)Landroid/media/tv/TableResponse$Builder;")
        setTableByteArray = JavaMethod("([B)Landroid/media/tv/TableResponse$Builder;")
        setTableSharedMemory = JavaMethod("(Landroid/os/SharedMemory;)Landroid/media/tv/TableResponse$Builder;")
        build = JavaMethod("()Landroid/media/tv/TableResponse;")