from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustedBiddingData"]

class TrustedBiddingData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/TrustedBiddingData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getTrustedBiddingUri = JavaMethod("()Landroid/net/Uri;")
    getTrustedBiddingKeys = JavaMethod("()Ljava/util/List;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/TrustedBiddingData/Builder"
        __javaconstructor__ = [("()V", False)]
        setTrustedBiddingUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        setTrustedBiddingKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/TrustedBiddingData;")