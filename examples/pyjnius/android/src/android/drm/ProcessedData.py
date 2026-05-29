from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessedData"]

class ProcessedData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/ProcessedData"
    getData = JavaMethod("()[B")
    getAccountId = JavaMethod("()Ljava/lang/String;")
    getSubscriptionId = JavaMethod("()Ljava/lang/String;")