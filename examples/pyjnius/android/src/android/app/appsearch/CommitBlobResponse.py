from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommitBlobResponse"]

class CommitBlobResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/CommitBlobResponse"
    __javaconstructor__ = [("(Landroid/app/appsearch/AppSearchBatchResult;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getResult = JavaMethod("()Landroid/app/appsearch/AppSearchBatchResult;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")