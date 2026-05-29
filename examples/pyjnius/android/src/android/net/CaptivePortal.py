from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CaptivePortal"]

class CaptivePortal(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/CaptivePortal"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    ignoreNetwork = JavaMethod("()V")
    reportCaptivePortalDismissed = JavaMethod("()V")