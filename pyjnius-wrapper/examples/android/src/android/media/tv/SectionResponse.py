from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SectionResponse"]

class SectionResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/SectionResponse"
    __javaconstructor__ = [("(IIIIILandroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSessionId = JavaMethod("()I")
    getVersion = JavaMethod("()I")
    getSessionData = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")