from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayManagerTransaction"]

class OverlayManagerTransaction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayManagerTransaction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    newInstance = JavaStaticMethod("()Landroid/content/om/OverlayManagerTransaction;")
    registerFabricatedOverlay = JavaMethod("(Landroid/content/om/FabricatedOverlay;)V")
    unregisterFabricatedOverlay = JavaMethod("(Landroid/content/om/OverlayIdentifier;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")