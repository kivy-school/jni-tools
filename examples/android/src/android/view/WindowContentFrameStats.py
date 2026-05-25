from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowContentFrameStats"]

class WindowContentFrameStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowContentFrameStats"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getFramePostedTimeNano = JavaMethod("(I)J")
    getFrameReadyTimeNano = JavaMethod("(I)J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")