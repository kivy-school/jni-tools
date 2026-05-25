from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayInfo"]

class OverlayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getOverlayName = JavaMethod("()Ljava/lang/String;")
    getTargetPackageName = JavaMethod("()Ljava/lang/String;")
    getTargetOverlayableName = JavaMethod("()Ljava/lang/String;")
    getOverlayIdentifier = JavaMethod("()Landroid/content/om/OverlayIdentifier;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")