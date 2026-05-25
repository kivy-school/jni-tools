from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchBatchResult"]

class AppSearchBatchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchBatchResult"
    isSuccess = JavaMethod("()Z")
    getSuccesses = JavaMethod("()Ljava/util/Map;")
    getFailures = JavaMethod("()Ljava/util/Map;")
    getAll = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchBatchResult/Builder"
        __javaconstructor__ = [("()V", False)]
        setSuccess = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        setFailure = JavaMethod("(Ljava/lang/Object;ILjava/lang/String;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        setResult = JavaMethod("(Ljava/lang/Object;Landroid/app/appsearch/AppSearchResult;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/AppSearchBatchResult;")