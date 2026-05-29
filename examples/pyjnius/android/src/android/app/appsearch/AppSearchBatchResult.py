from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AppSearchBatchResult"]

class AppSearchBatchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/AppSearchBatchResult"
    getAll = JavaMethod("()Ljava/util/Map;")
    toString = JavaMethod("()Ljava/lang/String;")
    isSuccess = JavaMethod("()Z")
    getFailures = JavaMethod("()Ljava/util/Map;")
    getSuccesses = JavaMethod("()Ljava/util/Map;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/AppSearchBatchResult$Builder"
        __javaconstructor__ = [("()V", False), ("(Landroid/app/appsearch/AppSearchBatchResult;)V", False)]
        setFailure = JavaMethod("(Ljava/lang/Object;ILjava/lang/String;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        setSuccess = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        setResult = JavaMethod("(Ljava/lang/Object;Landroid/app/appsearch/AppSearchResult;)Landroid/app/appsearch/AppSearchBatchResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/AppSearchBatchResult;")