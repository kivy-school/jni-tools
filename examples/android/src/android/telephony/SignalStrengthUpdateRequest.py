from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalStrengthUpdateRequest"]

class SignalStrengthUpdateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SignalStrengthUpdateRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSignalThresholdInfos = JavaMethod("()Ljava/util/Collection;")
    isReportingRequestedWhileIdle = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/SignalStrengthUpdateRequest/Builder"
        __javaconstructor__ = [("()V", False)]
        setSignalThresholdInfos = JavaMethod("(Ljava/util/Collection;)Landroid/telephony/SignalStrengthUpdateRequest$Builder;")
        setReportingRequestedWhileIdle = JavaMethod("(Z)Landroid/telephony/SignalStrengthUpdateRequest$Builder;")
        build = JavaMethod("()Landroid/telephony/SignalStrengthUpdateRequest;")