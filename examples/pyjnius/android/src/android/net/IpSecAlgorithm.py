from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["IpSecAlgorithm"]

class IpSecAlgorithm(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/IpSecAlgorithm"
    __javaconstructor__ = [("(Ljava/lang/String;[B)V", False), ("(Ljava/lang/String;[BI)V", False)]
    AUTH_AES_CMAC = JavaStaticField("Ljava/lang/String;")
    AUTH_AES_XCBC = JavaStaticField("Ljava/lang/String;")
    AUTH_CRYPT_AES_GCM = JavaStaticField("Ljava/lang/String;")
    AUTH_CRYPT_CHACHA20_POLY1305 = JavaStaticField("Ljava/lang/String;")
    AUTH_HMAC_MD5 = JavaStaticField("Ljava/lang/String;")
    AUTH_HMAC_SHA1 = JavaStaticField("Ljava/lang/String;")
    AUTH_HMAC_SHA256 = JavaStaticField("Ljava/lang/String;")
    AUTH_HMAC_SHA384 = JavaStaticField("Ljava/lang/String;")
    AUTH_HMAC_SHA512 = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CRYPT_AES_CBC = JavaStaticField("Ljava/lang/String;")
    CRYPT_AES_CTR = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSupportedAlgorithms = JavaStaticMethod("()Ljava/util/Set;")
    getTruncationLengthBits = JavaMethod("()I")
    getName = JavaMethod("()Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    getKey = JavaMethod("()[B")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")