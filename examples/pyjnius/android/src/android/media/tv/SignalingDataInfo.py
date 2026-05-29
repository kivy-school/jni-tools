from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SignalingDataInfo"]

class SignalingDataInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/SignalingDataInfo"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;II)V", False), ("(Ljava/lang/String;Ljava/lang/String;IILjava/lang/String;)V", False)]
    CONTENT_ENCODING_BASE64 = JavaStaticField("Ljava/lang/String;")
    CONTENT_ENCODING_UTF_8 = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    LLS_NO_GROUP_ID = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getSignalingDataType = JavaMethod("()Ljava/lang/String;")
    getGroup = JavaMethod("()I")
    getEncoding = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getVersion = JavaMethod("()I")
    getTable = JavaMethod("()Ljava/lang/String;")