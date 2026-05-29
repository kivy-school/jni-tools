from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GetMedicalDataSourcesRequest"]

class GetMedicalDataSourcesRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/GetMedicalDataSourcesRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageNames = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/GetMedicalDataSourcesRequest$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/GetMedicalDataSourcesRequest$Builder;)V", False), ("(Landroid/health/connect/GetMedicalDataSourcesRequest;)V", False), ("()V", False)]
        clearPackageNames = JavaMethod("()Landroid/health/connect/GetMedicalDataSourcesRequest$Builder;")
        addPackageName = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/GetMedicalDataSourcesRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/GetMedicalDataSourcesRequest;")