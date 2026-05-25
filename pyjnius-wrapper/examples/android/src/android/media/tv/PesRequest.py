from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PesRequest"]

class PesRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/PesRequest"
    __javaconstructor__ = [("(IIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTsPid = JavaMethod("()I")
    getStreamId = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")