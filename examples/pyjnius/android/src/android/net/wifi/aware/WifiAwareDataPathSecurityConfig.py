from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WifiAwareDataPathSecurityConfig"]

class WifiAwareDataPathSecurityConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/wifi/aware/WifiAwareDataPathSecurityConfig"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getPmkId = JavaMethod("()[B")
    getPskPassphrase = JavaMethod("()Ljava/lang/String;")
    getCipherSuite = JavaMethod("()I")
    getPmk = JavaMethod("()[B")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder"
        __javaconstructor__ = [("(I)V", False)]
        setPmk = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        setPskPassphrase = JavaMethod("(Ljava/lang/String;)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        setPmkId = JavaMethod("([B)Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig$Builder;")
        build = JavaMethod("()Landroid/net/wifi/aware/WifiAwareDataPathSecurityConfig;")