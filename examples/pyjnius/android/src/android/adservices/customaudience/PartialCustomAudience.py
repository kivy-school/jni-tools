from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PartialCustomAudience"]

class PartialCustomAudience(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/PartialCustomAudience"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getName = JavaMethod("()Ljava/lang/String;")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/PartialCustomAudience/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/PartialCustomAudience;")