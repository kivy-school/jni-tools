from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalStrengthUpdateRequest"]

class SignalStrengthUpdateRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/SignalStrengthUpdateRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isReportingRequestedWhileIdle = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getSignalThresholdInfos = JavaMethod("()Ljava/util/Collection;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/SignalStrengthUpdateRequest$Builder"
        __javaconstructor__ = [("()V", False)]
        setReportingRequestedWhileIdle = JavaMethod("(Z)Landroid/telephony/SignalStrengthUpdateRequest$Builder;")
        setSignalThresholdInfos = JavaMethod("(Ljava/util/Collection;)Landroid/telephony/SignalStrengthUpdateRequest$Builder;")
        build = JavaMethod("()Landroid/telephony/SignalStrengthUpdateRequest;")