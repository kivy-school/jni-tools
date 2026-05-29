from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UpsertMedicalResourceRequest"]

class UpsertMedicalResourceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/UpsertMedicalResourceRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getFhirVersion = JavaMethod("()Landroid/health/connect/datatypes/FhirVersion;")
    getDataSourceId = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/UpsertMedicalResourceRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/health/connect/datatypes/FhirVersion;Ljava/lang/String;)V", False), ("(Landroid/health/connect/UpsertMedicalResourceRequest$Builder;)V", False), ("(Landroid/health/connect/UpsertMedicalResourceRequest;)V", False)]
        setDataSourceId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/UpsertMedicalResourceRequest$Builder;")
        setFhirVersion = JavaMethod("(Landroid/health/connect/datatypes/FhirVersion;)Landroid/health/connect/UpsertMedicalResourceRequest$Builder;")
        setData = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/UpsertMedicalResourceRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/UpsertMedicalResourceRequest;")