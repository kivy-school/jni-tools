from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadMedicalResourcesPageRequest"]

class ReadMedicalResourcesPageRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadMedicalResourcesPageRequest"
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPageToken = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/health/connect/ReadMedicalResourcesPageRequest$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False), ("(Landroid/health/connect/ReadMedicalResourcesPageRequest$Builder;)V", False), ("(Landroid/health/connect/ReadMedicalResourcesPageRequest;)V", False)]
        setPageSize = JavaMethod("(I)Landroid/health/connect/ReadMedicalResourcesPageRequest$Builder;")
        build = JavaMethod("()Landroid/health/connect/ReadMedicalResourcesPageRequest;")
        setPageToken = JavaMethod("(Ljava/lang/String;)Landroid/health/connect/ReadMedicalResourcesPageRequest$Builder;")