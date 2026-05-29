from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FhirVersion"]

class FhirVersion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/datatypes/FhirVersion"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getMajor = JavaMethod("()I")
    parseFhirVersion = JavaStaticMethod("(Ljava/lang/String;)Landroid/health/connect/datatypes/FhirVersion;")
    getPatch = JavaMethod("()I")
    getMinor = JavaMethod("()I")
    isSupportedFhirVersion = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")