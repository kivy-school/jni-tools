from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastInfoRequest"]

class BroadcastInfoRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/BroadcastInfoRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_OPTION_AUTO_UPDATE = JavaStaticField("I")
    REQUEST_OPTION_REPEAT = JavaStaticField("I")
    getType = JavaMethod("()I")
    getRequestId = JavaMethod("()I")
    getOption = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")