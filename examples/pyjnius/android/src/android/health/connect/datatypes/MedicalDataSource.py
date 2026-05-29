from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MedicalDataSource"]

class MedicalDataSource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MedicalDataSource"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    getFhirBaseUri = JavaMethod("()Landroid/net/Uri;")
    getFhirVersion = JavaMethod("()Landroid/health/connect/datatypes/FhirVersion;")
    getLastDataUpdateTime = JavaMethod("()Ljava/time/Instant;")
    getDisplayName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MedicalDataSource$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;Landroid/health/connect/datatypes/FhirVersion;)V", False), ("(Landroid/health/connect/datatypes/MedicalDataSource$Builder;)V", False), ("(Landroid/health/connect/datatypes/MedicalDataSource;)V", False)]
        setId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        setPackageName = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        setFhirVersion = JavaMethod("(Landroid/health/connect/datatypes/FhirVersion;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        setFhirBaseUri = JavaMethod("(Landroid/net/Uri;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        setDisplayName = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        setLastDataUpdateTime = JavaMethod("(Ljava/time/Instant;)Landroid/health/connect/datatypes/MedicalDataSource$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/MedicalDataSource;")