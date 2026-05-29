from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GatewayInfo"]

class GatewayInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/GatewayInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/net/Uri;Landroid/net/Uri;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isEmpty = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getGatewayAddress = JavaMethod("()Landroid/net/Uri;")
    getGatewayProviderPackageName = JavaMethod("()Ljava/lang/String;")
    getOriginalAddress = JavaMethod("()Landroid/net/Uri;")