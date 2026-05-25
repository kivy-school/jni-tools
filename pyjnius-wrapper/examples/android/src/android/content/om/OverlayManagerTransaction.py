from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OverlayManagerTransaction"]

class OverlayManagerTransaction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/om/OverlayManagerTransaction"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    newInstance = JavaStaticMethod("()Landroid/content/om/OverlayManagerTransaction;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    registerFabricatedOverlay = JavaMethod("(Landroid/content/om/FabricatedOverlay;)V")
    unregisterFabricatedOverlay = JavaMethod("(Landroid/content/om/OverlayIdentifier;)V")