from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimelineRequest"]

class TimelineRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TimelineRequest"
    __javaconstructor__ = [("(III)V", False), ("(IIILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getIntervalMillis = JavaMethod("()I")
    getSelector = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")