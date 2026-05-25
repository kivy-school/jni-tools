from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TsResponse"]

class TsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TsResponse"
    __javaconstructor__ = [("(IIILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSharedFilterToken = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")