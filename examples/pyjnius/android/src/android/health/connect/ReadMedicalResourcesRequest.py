from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ReadMedicalResourcesRequest"]

class ReadMedicalResourcesRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/health/connect/ReadMedicalResourcesRequest"
    getPageSize = JavaMethod("()I")