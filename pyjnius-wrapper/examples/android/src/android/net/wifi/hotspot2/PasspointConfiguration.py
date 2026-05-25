from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PasspointConfiguration"]

class PasspointConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/PasspointConfiguration"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/hotspot2/PasspointConfiguration;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    setHomeSp = JavaMethod("(Landroid/net/wifi/hotspot2/pps/HomeSp;)V")
    getHomeSp = JavaMethod("()Landroid/net/wifi/hotspot2/pps/HomeSp;")
    setCredential = JavaMethod("(Landroid/net/wifi/hotspot2/pps/Credential;)V")
    getCredential = JavaMethod("()Landroid/net/wifi/hotspot2/pps/Credential;")
    setSubscriptionExpirationTimeInMillis = JavaMethod("(J)V")
    getSubscriptionExpirationTimeMillis = JavaMethod("()J")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    isOsuProvisioned = JavaMethod("()Z")
    getUniqueId = JavaMethod("()Ljava/lang/String;")
    setDecoratedIdentityPrefix = JavaMethod("(Ljava/lang/String;)V")
    getDecoratedIdentityPrefix = JavaMethod("()Ljava/lang/String;")