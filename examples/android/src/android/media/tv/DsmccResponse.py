from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DsmccResponse"]

class DsmccResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/DsmccResponse"
    __javaconstructor__ = [("(IIILandroid/os/ParcelFileDescriptor;)V", False), ("(IIIZLjava/util/List;)V", False), ("(III[I[Ljava/lang/String;)V", False)]
    BIOP_MESSAGE_TYPE_DIRECTORY = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_FILE = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_SERVICE_GATEWAY = JavaStaticField("Ljava/lang/String;")
    BIOP_MESSAGE_TYPE_STREAM = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getBiopMessageType = JavaMethod("()Ljava/lang/String;")
    getFile = JavaMethod("()Landroid/os/ParcelFileDescriptor;")
    getChildList = JavaMethod("()Ljava/util/List;")
    getStreamEventIds = JavaMethod("()[I")
    getStreamEventNames = JavaMethod("()[Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")