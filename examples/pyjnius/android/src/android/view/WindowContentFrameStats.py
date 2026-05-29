from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowContentFrameStats"]

class WindowContentFrameStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowContentFrameStats"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    UNDEFINED_TIME_NANO = JavaStaticField("J")
    toString = JavaMethod("()Ljava/lang/String;")
    getFramePostedTimeNano = JavaMethod("(I)J")
    getFrameReadyTimeNano = JavaMethod("(I)J")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")