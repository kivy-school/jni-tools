from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaptivePortal"]

class CaptivePortal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/CaptivePortal"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    reportCaptivePortalDismissed = JavaMethod("()V")
    ignoreNetwork = JavaMethod("()V")