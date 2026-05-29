from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TsResponse"]

class TsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TsResponse"
    __javaconstructor__ = [("(IIILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getSharedFilterToken = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")