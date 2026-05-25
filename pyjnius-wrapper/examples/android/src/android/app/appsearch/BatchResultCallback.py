from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatchResultCallback"]

class BatchResultCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/BatchResultCallback"
    onResult = JavaMethod("(Landroid/app/appsearch/AppSearchBatchResult;)V")
    onSystemError = JavaMethod("(Ljava/lang/Throwable;)V")