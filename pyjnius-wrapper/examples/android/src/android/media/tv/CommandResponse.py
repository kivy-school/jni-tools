from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommandResponse"]

class CommandResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/CommandResponse"
    __javaconstructor__ = [("(IIILjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESPONSE_TYPE_JSON = JavaStaticField("Ljava/lang/String;")
    RESPONSE_TYPE_XML = JavaStaticField("Ljava/lang/String;")
    getResponse = JavaMethod("()Ljava/lang/String;")
    getResponseType = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")