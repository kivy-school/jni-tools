from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ChangeLogTokenResponse"]

class ChangeLogTokenResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/changelog/ChangeLogTokenResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getToken = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")