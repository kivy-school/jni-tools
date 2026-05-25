from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetWalletCardsRequest"]

class GetWalletCardsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/GetWalletCardsRequest"
    __javaconstructor__ = [("(IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCardWidthPx = JavaMethod("()I")
    getCardHeightPx = JavaMethod("()I")
    getIconSizePx = JavaMethod("()I")
    getMaxCards = JavaMethod("()I")