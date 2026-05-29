from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DsmccResponse"]

class DsmccResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/DsmccResponse"
    __javaconstructor__ = [("(IIILandroid/os/ParcelFileDescriptor;)V", False), ("(IIIZLjava/util/List;)V", False), ("(III[I[Ljava/lang/String;)V", False)]
    BIOP_MESSAGE_TYPE_DIRECTORY = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_FILE = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_SERVICE_GATEWAY = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_STREAM = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getBiopMessageType = JavaMethod("()Ljava/lang/String;")
    getChildList = JavaMethod("()Ljava/util/List;")
    getStreamEventIds = JavaMethod("()[I")
    getStreamEventNames = JavaMethod("()[Ljava/lang/String;")
    getFile = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")