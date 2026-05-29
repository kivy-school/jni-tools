from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BroadcastInfoRequest"]

class BroadcastInfoRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/BroadcastInfoRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_OPTION_AUTO_UPDATE = JavaStaticField("I")
    REQUEST_OPTION_ONESHOT = JavaStaticField("I")
    REQUEST_OPTION_ONEWAY = JavaStaticField("I")
    REQUEST_OPTION_REPEAT = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getRequestId = JavaMethod("()I")
    getType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getOption = JavaMethod("()I")