from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ProcessedData"]

class ProcessedData(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/drm/ProcessedData"
    getAccountId = JavaMethod("()Ljava/lang/String;")
    getSubscriptionId = JavaMethod("()Ljava/lang/String;")
    getData = JavaMethod("()[B")