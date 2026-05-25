from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProxyInfo"]

class ProxyInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/ProxyInfo"
    __javaconstructor__ = [("(Landroid/net/ProxyInfo;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    buildDirectProxy = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/net/ProxyInfo;", True, False), ("(Ljava/lang/String;ILjava/util/List;)Landroid/net/ProxyInfo;", True, False)])
    buildPacProxy = JavaMultipleMethod([("(Landroid/net/Uri;)Landroid/net/ProxyInfo;", True, False), ("(Landroid/net/Uri;I)Landroid/net/ProxyInfo;", True, False)])
    getPacFileUrl = JavaMethod("()Landroid/net/Uri;")
    getHost = JavaMethod("()Ljava/lang/String;")
    getPort = JavaMethod("()I")
    getExclusionList = JavaMethod("()[Ljava/lang/String;")
    isValid = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")