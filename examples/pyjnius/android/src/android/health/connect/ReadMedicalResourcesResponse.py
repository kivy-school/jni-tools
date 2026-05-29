from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadMedicalResourcesResponse"]

class ReadMedicalResourcesResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadMedicalResourcesResponse"
    __javaconstructor__ = [("(Ljava/util/List;Ljava/lang/String;I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getNextPageToken = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getRemainingCount = JavaMethod("()I")
    getMedicalResources = JavaMethod("()Ljava/util/List;")