from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CreateMedicalDataSourceRequest"]

class CreateMedicalDataSourceRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/CreateMedicalDataSourceRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getFhirBaseUri = JavaMethod("()Landroid/net/Uri;")
    getFhirVersion = JavaMethod("()Landroid/health/connect/datatypes/FhirVersion;")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/CreateMedicalDataSourceRequest$Builder"
        __javaconstructor__ = [("(Landroid/net/Uri;Ljava/lang/String;Landroid/health/connect/datatypes/FhirVersion;)V", False), ("(Landroid/health/connect/CreateMedicalDataSourceRequest$Builder;)V", False), ("(Landroid/health/connect/CreateMedicalDataSourceRequest;)V", False)]
        setFhirVersion = JavaMethod("(Landroid/health/connect/datatypes/FhirVersion;)Landroid/health/connect/CreateMedicalDataSourceRequest$Builder;")
        setFhirBaseUri = JavaMethod("(Landroid/net/Uri;)Landroid/health/connect/CreateMedicalDataSourceRequest$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/CreateMedicalDataSourceRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/CreateMedicalDataSourceRequest;")