from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadableSubscription"]

class DownloadableSubscription(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/euicc/DownloadableSubscription"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getEncodedActivationCode = JavaMethod("()Ljava/lang/String;")
    forActivationCode = JavaStaticMethod("(Ljava/lang/String;)Landroid/telephony/euicc/DownloadableSubscription;")
    getConfirmationCode = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/euicc/DownloadableSubscription/Builder"
        __javaconstructor__ = [("(Landroid/telephony/euicc/DownloadableSubscription;)V", False), ("(Ljava/lang/String;)V", False)]
        build = JavaMethod("()Landroid/telephony/euicc/DownloadableSubscription;")
        setEncodedActivationCode = JavaMethod("(Ljava/lang/String;)Landroid/telephony/euicc/DownloadableSubscription$Builder;")
        setConfirmationCode = JavaMethod("(Ljava/lang/String;)Landroid/telephony/euicc/DownloadableSubscription$Builder;")