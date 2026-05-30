from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class ConfigParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/ConfigParser"
    parsePasspointConfig = JavaStaticMethod("(Ljava/lang/String;[B)Landroid/net/wifi/hotspot2/PasspointConfiguration;")

class PasspointConfiguration(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/hotspot2/PasspointConfiguration"
    __javaconstructor__ = [("()V", False), ("(Landroid/net/wifi/hotspot2/PasspointConfiguration;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getCredential = JavaMethod("()Landroid/net/wifi/hotspot2/pps/Credential;")
    getHomeSp = JavaMethod("()Landroid/net/wifi/hotspot2/pps/HomeSp;")
    getSubscriptionExpirationTimeMillis = JavaMethod("()J")
    isOsuProvisioned = JavaMethod("()Z")
    setCredential = JavaMethod("(Landroid/net/wifi/hotspot2/pps/Credential;)V")
    setHomeSp = JavaMethod("(Landroid/net/wifi/hotspot2/pps/HomeSp;)V")
    setSubscriptionExpirationTimeInMillis = JavaMethod("(J)V")
    getDecoratedIdentityPrefix = JavaMethod("()Ljava/lang/String;")
    setDecoratedIdentityPrefix = JavaMethod("(Ljava/lang/String;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getUniqueId = JavaMethod("()Ljava/lang/String;")