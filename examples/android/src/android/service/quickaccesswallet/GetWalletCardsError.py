from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetWalletCardsError"]

class GetWalletCardsError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/GetWalletCardsError"
    __javaconstructor__ = [("(Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getMessage = JavaMethod("()Ljava/lang/CharSequence;")