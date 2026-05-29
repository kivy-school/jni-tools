from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MedicalResourceId"]

class MedicalResourceId(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/MedicalResourceId"
    __javaconstructor__ = [("(Ljava/lang/String;ILjava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDataSourceId = JavaMethod("()Ljava/lang/String;")
    getFhirResourceId = JavaMethod("()Ljava/lang/String;")
    fromFhirReference = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Landroid/health/connect/MedicalResourceId;")
    getFhirResourceType = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")