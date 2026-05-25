from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["QueryInfoGenerationCallback"]

class QueryInfoGenerationCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/query/QueryInfoGenerationCallback"
    __javaconstructor__ = [("()V", False)]
    onSuccess = JavaMethod("(Lcom/google/android/gms/ads/query/QueryInfo;)V")
    onFailure = JavaMethod("(Ljava/lang/String;)V")