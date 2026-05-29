from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FhirResource"]

class FhirResource(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/FhirResource"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FHIR_RESOURCE_TYPE_ALLERGY_INTOLERANCE = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_CONDITION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_ENCOUNTER = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_IMMUNIZATION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_LOCATION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_MEDICATION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_MEDICATION_REQUEST = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_MEDICATION_STATEMENT = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_OBSERVATION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_ORGANIZATION = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_PATIENT = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_PRACTITIONER = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_PRACTITIONER_ROLE = JavaStaticField("I")
    FHIR_RESOURCE_TYPE_PROCEDURE = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getId = JavaMethod("()Ljava/lang/String;")
    getType = JavaMethod("()I")
    getData = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/datatypes/FhirResource$Builder"
        __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False), ("(Landroid/health/connect/datatypes/FhirResource$Builder;)V", False), ("(Landroid/health/connect/datatypes/FhirResource;)V", False)]
        setId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/FhirResource$Builder;")
        setType = JavaMethod("(I)Landroid/health/connect/datatypes/FhirResource$Builder;")
        setData = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/FhirResource$Builder;")
        build = JavaMethod("()Landroid/health/connect/datatypes/FhirResource;")