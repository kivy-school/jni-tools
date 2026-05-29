from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasspointConfiguration"]

class PasspointConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/PasspointConfiguration"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/hotspot2/PasspointConfiguration;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredential = JavaMethod("()Landroid/net/wifi/hotspot2/pps/Credential;")
    isOsuProvisioned = JavaMethod("()Z")
    setCredential = JavaMethod("(Landroid/net/wifi/hotspot2/pps/Credential;)V")
    getHomeSp = JavaMethod("()Landroid/net/wifi/hotspot2/pps/HomeSp;")
    setSubscriptionExpirationTimeInMillis = JavaMethod("(J)V")
    getSubscriptionExpirationTimeMillis = JavaMethod("()J")
    setHomeSp = JavaMethod("(Landroid/net/wifi/hotspot2/pps/HomeSp;)V")
    getDecoratedIdentityPrefix = JavaMethod("()Ljava/lang/String;")
    setDecoratedIdentityPrefix = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getUniqueId = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")