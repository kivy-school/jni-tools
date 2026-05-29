from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayProperties"]

class OverlayProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/OverlayProperties"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLutProperties = JavaMethod("()[Landroid/hardware/LutProperties;")
    isCombinationSupported = JavaMethod("(II)Z")
    isMixedColorSpacesSupported = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")