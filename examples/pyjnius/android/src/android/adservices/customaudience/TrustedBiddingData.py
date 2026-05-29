from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustedBiddingData"]

class TrustedBiddingData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/TrustedBiddingData"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getTrustedBiddingKeys = JavaMethod("()Ljava/util/List;")
    getTrustedBiddingUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/TrustedBiddingData$Builder"
        __javaconstructor__ = [("()V", False)]
        setTrustedBiddingKeys = JavaMethod("(Ljava/util/List;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        setTrustedBiddingUri = JavaMethod("(Landroid/net/Uri;)Landroid/adservices/customaudience/TrustedBiddingData$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/TrustedBiddingData;")