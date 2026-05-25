from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayProperties"]

class OverlayProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/OverlayProperties"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    isCombinationSupported = JavaMethod("(II)Z")
    isMixedColorSpacesSupported = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")