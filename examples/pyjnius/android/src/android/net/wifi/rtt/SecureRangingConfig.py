from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRangingConfig"]

class SecureRangingConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/rtt/SecureRangingConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPasnConfig = JavaMethod("()Landroid/net/wifi/rtt/PasnConfig;")
    isRangingFrameProtectionEnabled = JavaMethod("()Z")
    isSecureHeLtfEnabled = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/rtt/SecureRangingConfig$Builder"
        __javaconstructor__ = [("(Landroid/net/wifi/rtt/PasnConfig;)V", False)]
        setRangingFrameProtectionEnabled = JavaMethod("(Z)Landroid/net/wifi/rtt/SecureRangingConfig$Builder;")
        setSecureHeLtfEnabled = JavaMethod("(Z)Landroid/net/wifi/rtt/SecureRangingConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/rtt/SecureRangingConfig;")