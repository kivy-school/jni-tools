from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WalletCard"]

class WalletCard(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/quickaccesswallet/WalletCard"
    CARD_TYPE_NON_PAYMENT = JavaStaticField("I")
    CARD_TYPE_PAYMENT = JavaStaticField("I")
    CARD_TYPE_UNKNOWN = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCardId = JavaMethod("()Ljava/lang/String;")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getCardImage = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getCardIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getCardLabel = JavaMethod("()Ljava/lang/CharSequence;")
    getCardLocations = JavaMethod("()Ljava/util/List;")
    getCardType = JavaMethod("()I")
    getNonPaymentCardSecondaryImage = JavaMethod("()Landroid/graphics/drawable/Icon;")
    getPendingIntent = JavaMethod("()Landroid/app/PendingIntent;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/quickaccesswallet/WalletCard$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;ILandroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False), ("(Ljava/lang/String;Landroid/graphics/drawable/Icon;Ljava/lang/CharSequence;Landroid/app/PendingIntent;)V", False)]
        setCardLocations = JavaMethod("(Ljava/util/List;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setCardLabel = JavaMethod("(Ljava/lang/CharSequence;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setCardIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        setNonPaymentCardSecondaryImage = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/service/quickaccesswallet/WalletCard$Builder;")
        build = JavaMethod("()Landroid/service/quickaccesswallet/WalletCard;")