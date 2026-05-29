from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TimelineRequest"]

class TimelineRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TimelineRequest"
    __javaconstructor__ = [("(III)V", False), ("(IIILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    REQUEST_OPTION_AUTO_UPDATE = JavaStaticField("I")
    REQUEST_OPTION_ONESHOT = JavaStaticField("I")
    REQUEST_OPTION_ONEWAY = JavaStaticField("I")
    REQUEST_OPTION_REPEAT = JavaStaticField("I")
    getIntervalMillis = JavaMethod("()I")
    getSelector = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")