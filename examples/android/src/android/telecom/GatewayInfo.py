from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GatewayInfo"]

class GatewayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/GatewayInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/net/Uri;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGatewayProviderPackageName = JavaMethod("()Ljava/lang/String;")
    getGatewayAddress = JavaMethod("()Landroid/net/Uri;")
    getOriginalAddress = JavaMethod("()Landroid/net/Uri;")
    isEmpty = JavaMethod("()Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")