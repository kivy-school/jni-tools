from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayInfo"]

class OverlayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getOverlayName = JavaMethod("()Ljava/lang/String;")
    getOverlayIdentifier = JavaMethod("()Landroid/content/om/OverlayIdentifier;")
    getTargetOverlayableName = JavaMethod("()Ljava/lang/String;")
    getTargetPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")