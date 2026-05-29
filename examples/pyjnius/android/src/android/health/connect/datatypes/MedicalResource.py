from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MedicalResource"]

class MedicalResource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/MedicalResource"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    MEDICAL_RESOURCE_TYPE_ALLERGIES_INTOLERANCES = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_CONDITIONS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_LABORATORY_RESULTS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_MEDICATIONS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_PERSONAL_DETAILS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_PRACTITIONER_DETAILS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_PREGNANCY = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_PROCEDURES = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_SOCIAL_HISTORY = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_VACCINES = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_VISITS = JavaStaticField("I")
    MEDICAL_RESOURCE_TYPE_VITAL_SIGNS = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Landroid/health/connect/MedicalResourceId;")
    getType = JavaMethod("()I")
    getFhirVersion = JavaMethod("()Landroid/health/connect/datatypes/FhirVersion;")
    getDataSourceId = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFhirResource = JavaMethod("()Landroid/health/connect/datatypes/FhirResource;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/MedicalResource$Builder"
        __javaconstructor__ = [("(ILjava/lang/String;Landroid/health/connect/datatypes/FhirVersion;Landroid/health/connect/datatypes/FhirResource;)V", False), ("(Landroid/health/connect/datatypes/MedicalResource$Builder;)V", False), ("(Landroid/health/connect/datatypes/MedicalResource;)V", False)]
        setFhirResource = JavaMethod("(Landroid/health/connect/datatypes/FhirResource;)Landroid/health/connect/datatypes/MedicalResource$Builder;")
        setDataSourceId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/MedicalResource$Builder;")
        setFhirVersion = JavaMethod("(Landroid/health/connect/datatypes/FhirVersion;)Landroid/health/connect/datatypes/MedicalResource$Builder;")
        setType = JavaMethod("(I)Landroid/health/connect/datatypes/MedicalResource$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/MedicalResource;")