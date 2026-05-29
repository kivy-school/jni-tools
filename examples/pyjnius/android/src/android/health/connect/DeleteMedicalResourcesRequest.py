from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DeleteMedicalResourcesRequest"]

class DeleteMedicalResourcesRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/DeleteMedicalResourcesRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDataSourceIds = JavaMethod("()Ljava/util/Set;")
    getMedicalResourceTypes = JavaMethod("()Ljava/util/Set;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/DeleteMedicalResourcesRequest$Builder"
        __javaconstructor__ = [("(Landroid/health/connect/DeleteMedicalResourcesRequest$Builder;)V", False), ("(Landroid/health/connect/DeleteMedicalResourcesRequest;)V", False), ("()V", False)]
        addDataSourceId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/DeleteMedicalResourcesRequest$Builder;")
        clearDataSourceIds = JavaMethod("()Landroid/health/connect/DeleteMedicalResourcesRequest$Builder;")
        addMedicalResourceType = JavaMethod("(I)Landroid/health/connect/DeleteMedicalResourcesRequest$Builder;")
        clearMedicalResourceTypes = JavaMethod("()Landroid/health/connect/DeleteMedicalResourcesRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/DeleteMedicalResourcesRequest;")