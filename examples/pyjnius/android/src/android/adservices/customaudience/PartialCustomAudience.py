from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PartialCustomAudience"]

class PartialCustomAudience(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/adservices/customaudience/PartialCustomAudience"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getActivationTime = JavaMethod("()Ljava/time/Instant;")
    getExpirationTime = JavaMethod("()Ljava/time/Instant;")
    getUserBiddingSignals = JavaMethod("()Landroid/adservices/common/AdSelectionSignals;")
    getName = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/adservices/customaudience/PartialCustomAudience$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setUserBiddingSignals = JavaMethod("(Landroid/adservices/common/AdSelectionSignals;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setExpirationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        setActivationTime = JavaMethod("(Ljava/time/Instant;)Landroid/adservices/customaudience/PartialCustomAudience$Builder;")
        build = JavaMethod("()Landroid/adservices/customaudience/PartialCustomAudience;")