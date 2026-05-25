from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StreamingServiceInfo"]

class StreamingServiceInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/StreamingServiceInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")