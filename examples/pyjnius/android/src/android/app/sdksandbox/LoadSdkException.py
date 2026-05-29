from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LoadSdkException"]

class LoadSdkException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/sdksandbox/LoadSdkException"
    __javaconstructor__ = [("(Ljava/lang/Throwable;Landroid/os/Bundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLoadSdkErrorCode = JavaMethod("()I")
    getExtraInformation = JavaMethod("()Landroid/os/Bundle;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")