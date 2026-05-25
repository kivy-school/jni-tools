from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadRequest"]

class DownloadRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    getFileServiceId = JavaMethod("()Ljava/lang/String;")
    getSourceUri = JavaMethod("()Landroid/net/Uri;")
    getDestinationUri = JavaMethod("()Landroid/net/Uri;")
    getSubscriptionId = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")
    getMaxAppIntentSize = JavaStaticMethod("()I")
    getMaxDestinationUriSize = JavaStaticMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/DownloadRequest/Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Landroid/net/Uri;)V", False)]
        fromDownloadRequest = JavaStaticMethod("(Landroid/telephony/mbms/DownloadRequest;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        fromSerializedRequest = JavaStaticMethod("([B)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setServiceInfo = JavaMethod("(Landroid/telephony/mbms/FileServiceInfo;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setSubscriptionId = JavaMethod("(I)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setAppIntent = JavaMethod("(Landroid/content/Intent;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        build = JavaMethod("()Landroid/telephony/mbms/DownloadRequest;")