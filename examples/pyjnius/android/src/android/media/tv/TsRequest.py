from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TsRequest"]

class TsRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TsRequest"
    __javaconstructor__ = [("(III)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTsPid = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")