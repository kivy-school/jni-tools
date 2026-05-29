from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpenBlobForReadResponse"]

class OpenBlobForReadResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/OpenBlobForReadResponse"
    __javaconstructor__ = [("(Landroid/app/appsearch/AppSearchBatchResult;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    close = JavaMethod("()V")
    getResult = JavaMethod("()Landroid/app/appsearch/AppSearchBatchResult;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")