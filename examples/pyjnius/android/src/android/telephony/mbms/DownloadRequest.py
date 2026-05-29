from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DownloadRequest"]

class DownloadRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/DownloadRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSubscriptionId = JavaMethod("()I")
    getFileServiceId = JavaMethod("()Ljava/lang/String;")
    getMaxDestinationUriSize = JavaStaticMethod("()I")
    getMaxAppIntentSize = JavaStaticMethod("()I")
    getDestinationUri = JavaMethod("()Landroid/net/Uri;")
    getSourceUri = JavaMethod("()Landroid/net/Uri;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    toByteArray = JavaMethod("()[B")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/telephony/mbms/DownloadRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Landroid/net/Uri;)V", False)]
        setAppIntent = JavaMethod("(Landroid/content/Intent;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        setSubscriptionId = JavaMethod("(I)Landroid/telephony/mbms/DownloadRequest$Builder;")
        fromSerializedRequest = JavaStaticMethod("([B)Landroid/telephony/mbms/DownloadRequest$Builder;")
        fromDownloadRequest = JavaStaticMethod("(Landroid/telephony/mbms/DownloadRequest;)Landroid/telephony/mbms/DownloadRequest$Builder;")
        build = JavaMethod("()Landroid/telephony/mbms/DownloadRequest;")
        setServiceInfo = JavaMethod("(Landroid/telephony/mbms/FileServiceInfo;)Landroid/telephony/mbms/DownloadRequest$Builder;")