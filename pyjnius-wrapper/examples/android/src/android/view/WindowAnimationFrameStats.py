from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WindowAnimationFrameStats"]

class WindowAnimationFrameStats(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/WindowAnimationFrameStats"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")