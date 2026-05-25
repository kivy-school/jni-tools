from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoadSdkException"]

class LoadSdkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/LoadSdkException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getLoadSdkErrorCode = JavaMethod("()I")
    getExtraInformation = JavaMethod("()Landroid/os/Bundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")