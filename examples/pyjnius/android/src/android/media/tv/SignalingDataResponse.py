from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalingDataResponse"]

class SignalingDataResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/SignalingDataResponse"
    __javaconstructor__ = [("(IIILjava/util/List;Ljava/util/List;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getSignalingDataInfoList = JavaMethod("()Ljava/util/List;")
    getSignalingDataTypes = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")