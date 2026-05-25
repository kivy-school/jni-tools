from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WalletCard"]

class WalletCard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/WalletCard"
    CARD_TYPE_NON_PAYMENT = JavaStaticField("I")
    CARD_TYPE_PAYMENT = JavaStaticField("I")
    CARD_TYPE_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getCardId = JavaMethod("()Ljava/lang/String;")
    getCardType = JavaMethod("()I")
    getCardImage = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getPendingIntent = JavaMethod("()Landroid/app/PendingIntent;")
    getCardIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getCardLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getNonPaymentCardSecondaryImage = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getCardLocations = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/quickaccesswallet/WalletCard/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;ILandroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False), ("(Ljava/lang/String;Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
        setCardIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setCardLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setNonPaymentCardSecondaryImage = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setCardLocations = JavaMethod("(Ljava/util/List;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        build = JavaMethod("()Landroid/service/quickaccesswallet/WalletCard;")