from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxyInfo"]

class ProxyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ProxyInfo"
    __javaconstructor__ = [("(Landroid/net/ProxyInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    buildDirectProxy = JavaMultipleMethod([("(Ljava/lang/String;ILjava/util/List;)Landroid/net/ProxyInfo;", True, False), ("(Ljava/lang/String;I)Landroid/net/ProxyInfo;", True, False)])
    buildPacProxy = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/net/ProxyInfo;", True, False), ("(Landroid/net/Uri;I)Landroid/net/ProxyInfo;", True, False)])
    getExclusionList = JavaMethod("()[Ljava/lang/String;")
    getPacFileUrl = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    isValid = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")