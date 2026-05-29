from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastInfoResponse"]

class BroadcastInfoResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/BroadcastInfoResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_RESULT_CANCEL = JavaStaticField("I")
    RESPONSE_RESULT_ERROR = JavaStaticField("I")
    RESPONSE_RESULT_OK = JavaStaticField("I")
    getType = JavaMethod("()I")
    getRequestId = JavaMethod("()I")
    getSequence = JavaMethod("()I")
    getResponseResult = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")