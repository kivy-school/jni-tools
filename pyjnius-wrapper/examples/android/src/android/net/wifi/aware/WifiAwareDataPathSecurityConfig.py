from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareDataPathSecurityConfig"]

class WifiAwareDataPathSecurityConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareDataPathSecurityConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    getCipherSuite = JavaMethod("()I")
    getPmk = JavaMethod("()[B")
    getPmkId = JavaMethod("()[B")
    getPskPassphrase = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/WifiAwareDataPathSecurityConfig/Builder"
        __javaconstructor__ = [("(I)V", False)]
        setPskPassphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        setPmk = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        setPmkId = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")