from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BatchResultCallback"]

class BatchResultCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/BatchResultCallback"
    onSystemError = JavaMethod("(Ljava/lang/Throwable;)V")
    onResult = JavaMethod("(Landroid/app/appsearch/AppSearchBatchResult;)V")