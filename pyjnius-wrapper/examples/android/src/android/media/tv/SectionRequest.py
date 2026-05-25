from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SectionRequest"]

class SectionRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/SectionRequest"
    __javaconstructor__ = [("(IIIII)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getTsPid = JavaMethod("()I")
    getTableId = JavaMethod("()I")
    getVersion = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")