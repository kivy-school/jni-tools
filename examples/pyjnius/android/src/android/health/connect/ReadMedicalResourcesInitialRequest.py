from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadMedicalResourcesInitialRequest"]

class ReadMedicalResourcesInitialRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadMedicalResourcesInitialRequest"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getDataSourceIds = JavaMethod("()Ljava/util/Set;")
    getMedicalResourceType = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/ReadMedicalResourcesInitialRequest$Builder"
        __javaconstructor__ = [("(I)V", False), ("(Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;)V", False), ("(Landroid/health/connect/ReadMedicalResourcesInitialRequest;)V", False)]
        addDataSourceId = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;")
        clearDataSourceIds = JavaMethod("()Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;")
        addDataSourceIds = JavaMethod("(Ljava/util/Set;)Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;")
        setMedicalResourceType = JavaMethod("(I)Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;")
        setPageSize = JavaMethod("(I)Landroid/health/connect/ReadMedicalResourcesInitialRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/ReadMedicalResourcesInitialRequest;")